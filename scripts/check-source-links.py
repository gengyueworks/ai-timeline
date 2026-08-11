#!/usr/bin/env python3
"""Check source URLs without turning network noise into false dead-link alerts."""

import argparse
import json
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "ai-timeline-public.json"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36"
NETWORK_MARKERS = (
    "timeout", "timed out", "ssl", "certificate", "eof", "reset", "refused",
    "unreachable", "temporary failure", "name or service not known", "nodename",
    "remote end closed", "connection aborted", "connection reset",
)


def classify_http_status(status):
    if 200 <= status < 400:
        return "healthy"
    if status in {401, 403, 406, 429}:
        return "blocked"
    if status in {404, 410}:
        return "candidate-dead"
    if status == 408 or 500 <= status < 600:
        return "transient"
    if 400 <= status < 500:
        return "review"
    return "review"


def classify_result(error_text):
    text = str(error_text).lower()
    if any(marker in text for marker in NETWORK_MARKERS):
        return "network-error"
    return "error"


def check_url(url, title, attempts=3, timeout=15, retry_delay=2):
    if not url or not url.startswith(("http://", "https://")):
        return {"title": title, "url": url, "classification": "invalid", "attempts": 0, "detail": "invalid URL"}

    history = []
    for attempt in range(1, attempts + 1):
        try:
            request = urllib.request.Request(
                url,
                headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml,*/*;q=0.8"},
                method="GET",
            )
            with urllib.request.urlopen(request, timeout=timeout) as response:
                result = {
                    "title": title,
                    "url": url,
                    "final_url": response.geturl(),
                    "classification": classify_http_status(response.status),
                    "http_status": response.status,
                    "attempt": attempt,
                }
                history.append(result)
                if result["classification"] == "healthy":
                    return result
        except HTTPError as exc:
            result = {
                "title": title,
                "url": url,
                "final_url": exc.geturl(),
                "classification": classify_http_status(exc.code),
                "http_status": exc.code,
                "attempt": attempt,
                "detail": str(exc.reason),
            }
            history.append(result)
        except (URLError, TimeoutError, OSError) as exc:
            result = {
                "title": title,
                "url": url,
                "classification": classify_result(exc),
                "attempt": attempt,
                "detail": str(exc),
            }
            history.append(result)

        if attempt < attempts:
            time.sleep(retry_delay)

    final = dict(history[-1])
    final["attempts"] = len(history)
    final["history"] = history
    return final


def add_persistence(result, previous):
    classification = result.get("classification")
    old_streak = int(previous.get("candidate_dead_streak", 0)) if previous else 0
    if classification == "candidate-dead":
        streak = old_streak + 1
    else:
        streak = 0
    result["candidate_dead_streak"] = streak
    result["confirmed_dead"] = streak >= 2
    return result


def load_previous(path):
    if not path or not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return {item.get("url"): item for item in data.get("results", []) if item.get("url")}


def write_report(path, results):
    path.parent.mkdir(parents=True, exist_ok=True)
    counts = {}
    for result in results:
        key = "confirmed-dead" if result.get("confirmed_dead") else result.get("classification", "unknown")
        counts[key] = counts.get(key, 0) + 1
    report = {
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "total_urls": len(results),
        "counts": counts,
        "results": sorted(results, key=lambda item: item.get("url", "")),
    }
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=DATA_PATH)
    parser.add_argument("--output", type=Path, help="Write a JSON report and use it as next run's history")
    parser.add_argument("--attempts", type=int, default=3)
    parser.add_argument("--timeout", type=int, default=15)
    parser.add_argument("--retry-delay", type=float, default=2)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--fail-on-confirmed-dead", action="store_true")
    args = parser.parse_args(argv)

    data = json.loads(args.data.read_text(encoding="utf-8"))
    url_titles = {}
    for event in data.get("events", []):
        url = event.get("source_url", "")
        if url:
            url_titles.setdefault(url, str(event.get("title_zh", ""))[:80])

    previous = load_previous(args.output)
    results = []
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = {
            executor.submit(check_url, url, title, args.attempts, args.timeout, args.retry_delay): url
            for url, title in url_titles.items()
        }
        for future in as_completed(futures):
            result = future.result()
            results.append(add_persistence(result, previous.get(result.get("url"))))

    if args.output:
        report = write_report(args.output, results)
    else:
        counts = {}
        for result in results:
            key = "confirmed-dead" if result.get("confirmed_dead") else result.get("classification", "unknown")
            counts[key] = counts.get(key, 0) + 1
        report = {"total_urls": len(results), "counts": counts}

    print(json.dumps(report, ensure_ascii=False, indent=2))
    if args.fail_on_confirmed_dead:
        return 1 if report.get("counts", {}).get("confirmed-dead", 0) else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())

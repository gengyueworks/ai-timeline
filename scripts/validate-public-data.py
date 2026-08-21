#!/usr/bin/env python3
"""Validate the public dataset and its derived metadata."""

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLIC_DATA = ROOT / "ai-timeline-public.json"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def derive_date_range(events):
    dates = [str(event.get("date", "")) for event in events if event.get("date")]
    if not dates:
        return ""
    return f"{min(dates)}–{max(dates)}"


def read_full_collection_count(path: Path):
    data = load_json(path)
    events = data.get("events", [])
    declared = data.get("total_events")
    if declared is not None and declared != len(events):
        raise ValueError(f"full collection total_events={declared} but events has {len(events)}")
    return len(events)


def validate_dataset(data, expected_public_count=118, full_data_path=None):
    events = data.get("events", [])
    errors = []

    if data.get("public_event_count") != len(events):
        errors.append("public_event_count does not match events length")
    if expected_public_count is not None and len(events) != expected_public_count:
        errors.append(f"public dataset must contain exactly {expected_public_count} events (got {len(events)})")

    derived_range = derive_date_range(events)
    if data.get("date_range") != derived_range:
        errors.append(f"date_range must be {derived_range!r} (got {data.get('date_range')!r})")

    if full_data_path is not None:
        try:
            full_count = read_full_collection_count(Path(full_data_path))
            if data.get("full_collection_size") != full_count:
                errors.append(
                    f"full_collection_size={data.get('full_collection_size')} "
                    f"does not match canonical full collection count {full_count}"
                )
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            errors.append(f"full collection could not be read: {exc}")

    seen = set()
    previous = ""
    required = [
        "id", "year", "date", "date_precision", "title_zh", "title_en", "type",
        "importance", "confidence", "summary_zh", "source_name", "source_url",
        "related_terms", "card_summary_zh",
    ]
    allowed_extra = {
        "behind_scenes_zh", "why_it_matters_zh", "tags", "type_legacy", "learning_path_hint",
        "missing_terms", "source_author", "card_summary_en", "summary_en", "context_en",
        "why_it_matters_en",
    }

    for i, event in enumerate(events):
        label = f"event[{i}]"
        for key in required:
            if key not in event or event[key] in (None, ""):
                errors.append(f"{label}: missing {key}")

        extra = set(event) - set(required) - allowed_extra
        if extra:
            errors.append(f"{label}: unknown fields present: {sorted(extra)}")

        date = str(event.get("date", ""))
        if not re.fullmatch(r"\d{4}(-\d{2})?(-\d{2})?", date):
            errors.append(f"{label}: invalid date {date}")
        key = date + ("-01-01" if len(date) == 4 else "-01" if len(date) == 7 else "")
        if previous and key < previous:
            errors.append(f"{label}: chronological order violation")
        previous = key

        signature = (date, event.get("title_zh"))
        if signature in seen:
            errors.append(f"{label}: duplicate event")
        seen.add(signature)

        card = str(event.get("card_summary_zh", ""))
        if not 20 <= len(card) <= 98:
            errors.append(f"{label}: card_summary_zh length must be 20–98")
        if card.endswith(("…", "，", "；", "：")):
            errors.append(f"{label}: card summary is truncated")
        if not isinstance(event.get("related_terms"), list) or len(event.get("related_terms", [])) > 8:
            errors.append(f"{label}: related_terms must be an array of at most 8 terms")
        if not str(event.get("source_url", "")).startswith(("http://", "https://")):
            errors.append(f"{label}: source_url must be public")
        if event.get("confidence") not in {"high", "medium", "low"}:
            errors.append(f"{label}: invalid confidence")
        if not isinstance(event.get("importance"), int) or not 1 <= event["importance"] <= 5:
            errors.append(f"{label}: invalid importance")
        summary_length = len(str(event.get("summary_zh", "")))
        if not 50 <= summary_length <= 600:
            errors.append(f"{label}: summary length {summary_length} outside 50–600")

    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=PUBLIC_DATA)
    parser.add_argument("--full-data", type=Path, help="Optional canonical full collection for count comparison")
    args = parser.parse_args(argv)

    try:
        data = load_json(args.data)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Validation failed: cannot read {args.data}: {exc}")
        return 1

    errors = validate_dataset(data, full_data_path=args.full_data)
    if errors:
        print("Validation failed:")
        print("\n".join("- " + error for error in errors))
        return 1

    print(
        f"PASS: {len(data['events'])} public events, date range {derive_date_range(data['events'])}, "
        "chronological order, required fields, sources, and content depth validated."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

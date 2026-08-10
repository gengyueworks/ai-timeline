#!/usr/bin/env python3
import json, re, sys
from pathlib import Path

p=Path(__file__).resolve().parents[1]/"ai-timeline-public.json"
d=json.loads(p.read_text(encoding="utf-8"))
events=d.get("events",[])
errors=[]
if d.get("public_event_count") != len(events): errors.append("public_event_count does not match events length")
if len(events) != 116: errors.append(f"public dataset must contain exactly 116 events (got {len(events)})")
seen=set(); previous=""
for i,e in enumerate(events):
    label=f"event[{i}]"
    required=["id","year","date","date_precision","title_zh","title_en","type","importance","confidence","summary_zh","source_name","source_url","related_terms","card_summary_zh"]
    for key in required:
        if key not in e or e[key] in (None,""): errors.append(f"{label}: missing {key}")
    # 允许深度字段（有内容版）：behind_scenes_zh / why_it_matters_zh / tags / type_legacy / learning_path_hint / missing_terms / source_author
    allowed_extra={"behind_scenes_zh","why_it_matters_zh","tags","type_legacy","learning_path_hint","missing_terms","source_author","card_summary_en","summary_en","context_en","why_it_matters_en"}
    extra=set(e)-set(required)-allowed_extra
    if extra: errors.append(f"{label}: unknown fields present: {sorted(extra)}")
    date=str(e.get("date",""))
    if not re.fullmatch(r"\d{4}(-\d{2})?(-\d{2})?",date): errors.append(f"{label}: invalid date {date}")
    key=date+('-01-01' if len(date)==4 else '-01' if len(date)==7 else '')
    if previous and key<previous: errors.append(f"{label}: chronological order violation")
    previous=key
    sig=(date,e.get("title_zh"))
    if sig in seen: errors.append(f"{label}: duplicate event")
    seen.add(sig)
    card=str(e.get("card_summary_zh",""))
    if not 20<=len(card)<=98: errors.append(f"{label}: card_summary_zh length must be 20–98")
    if card.endswith(("…","，","；","：")): errors.append(f"{label}: card summary is truncated")
    if not isinstance(e.get("related_terms"),list) or len(e.get("related_terms",[]))>8: errors.append(f"{label}: related_terms must be an array of at most 8 terms")
    if not str(e.get("source_url","")).startswith(("http://","https://")): errors.append(f"{label}: source_url must be public")
    if e.get("confidence") not in {"high","medium","low"}: errors.append(f"{label}: invalid confidence")
    if not isinstance(e.get("importance"),int) or not 1<=e["importance"]<=5: errors.append(f"{label}: invalid importance")
    n=len(e.get("summary_zh",""))
    if n<50 or n>600: errors.append(f"{label}: summary length {n} outside 50–600")
if errors:
    print("Validation failed:")
    print("\n".join("- "+x for x in errors))
    sys.exit(1)
print(f"PASS: {len(events)} public events, chronological order, required fields, sources, and content depth validated.")

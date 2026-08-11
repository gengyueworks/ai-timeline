# Release checklist

- [ ] Every new event has a working public source.
- [ ] `python3 scripts/test_maintenance.py` passes.
- [ ] Derived `date_range` and public event count pass validation.
- [ ] When the canonical full collection is available, `--full-data` comparison passes and the 272-event count is intentional.
- [ ] Event date matches the source and `date_precision`.
- [ ] Titles are factual rather than promotional.
- [ ] Summary is concise and contains no unsupported benchmark claims.
- [ ] No private fields or dictionary content are included.
- [ ] Events are chronologically sorted.
- [ ] `python3 scripts/validate-public-data.py` passes.
- [ ] Link report has been reviewed; network errors and anti-bot responses are not treated as confirmed dead links.
- [ ] Desktop and mobile pages have been visually checked.
- [ ] `updated_at` and counts are current.

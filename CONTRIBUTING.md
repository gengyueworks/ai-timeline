# Contributing

Thank you for helping improve AI Timeline. Contributions should make the chronology more accurate, verifiable, and useful—not merely larger.

## Corrections

Open an issue with the event title, disputed field, proposed correction, and a public source. For date corrections, state whether the source refers to an announcement, publication, release, or later report.

## New events

A proposal must include:

- `date` in `YYYY`, `YYYY-MM`, or `YYYY-MM-DD`;
- matching `date_precision`: `year`, `month`, or `day`;
- Chinese and English titles;
- a concise Chinese summary of approximately 100–200 characters;
- `type`, `importance` (1–5), and `confidence`;
- a descriptive source name and public source URL.

Prefer primary sources: papers, official release notes, institutional archives, standards bodies, or court/government records. Use reputable reporting when no primary source is available. Do not submit generated citations, inaccessible URLs, promotional claims presented as facts, or events whose significance is purely speculative.

## Pull requests

1. Edit `ai-timeline-public.json`.
2. Keep events in chronological order.
3. Run `python3 scripts/validate-public-data.py`.
4. Keep the pull request focused on one correction or a small related group.
5. Explain why the change belongs in the public timeline.

Editorial acceptance remains at the maintainer's discretion. The full private dataset and paid dictionary content are outside the contribution scope.

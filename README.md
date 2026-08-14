# The AI Timeline

**English** · [简体中文](./README.zh-CN.md)

[![Validate](https://github.com/gengyueworks/ai-timeline/actions/workflows/validate-data.yml/badge.svg)](https://github.com/gengyueworks/ai-timeline/actions/workflows/validate-data.yml)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-orange.svg)](./LICENSE)
[![Dataset: CC BY-NC 4.0](https://img.shields.io/badge/Dataset-CC%20BY--NC%204.0-orange.svg)](./LICENSE-DATA)

> **Not only a record of how human technology arrived here, but an act of imagination for the future we are about to meet.**

A source-backed, bilingual chronology of artificial intelligence, from the theoretical foundations of computation to modern models, agents, and the systems still taking shape around them.

**Live demo:** https://gengyueworks.github.io/ai-timeline/

## At a glance

- **272** events in the maintained full collection
- **116** representative events in this open dataset
- **1936–2026-08** historical coverage
- English and Chinese entries
- Sources across **55 domains**
- CI validation and GitHub Pages publishing

**Explore:** [Open the live timeline](https://gengyueworks.github.io/ai-timeline/) · [Browse the public dataset](./ai-timeline-public.json) · [Contribute](./CONTRIBUTING.md)

## Why this project exists

This timeline began as a by-product of learning.

I came to AI as a liberal-arts writer rather than a computer scientist. What drew me in was the feeling of following one idea into another, finding an old paper inside a new system, and watching a field that first looked impossibly large become a map that could be travelled.

AI is often narrated as a sequence of recent product launches. Its history runs through mathematics, cybernetics, cognitive science, neuroscience, philosophy, computer engineering, infrastructure, long periods of disappointment, and the stubborn work of people whose ideas arrived before the world was ready for them.

The timeline records more than dates. It connects papers, models, products, computing systems, institutions, debates, and cultural moments so that readers can ask what came before a breakthrough, what changed afterward, and where an idea went next.

Every map is drawn from somewhere. I live in China and read across Chinese- and English-language sources, so I sometimes notice open models, infrastructure projects, and developer communities that receive less attention in English-language summaries. When they are historically relevant, I include them alongside work from the rest of the world. This is not an argument for one country or company. It is an attempt to keep the view open, plural, and honest about where the map is being drawn from.

## The larger vision

The AI Timeline is being built as more than a longer list of events. Its long-term aim is to become a navigable public record of a field that is still inventing itself.

### A chronology that can be trusted

The foundation is a carefully sourced public chronology, maintained over time and corrected in public. Each entry should be concise enough to verify and rich enough to lead somewhere else. Dates matter, but so do the relationships between dates.

### A map of people, ideas, and systems

AI history is also a history of people and the questions they kept returning to. Future versions can let readers follow a person through papers, collaborations, laboratories, models, arguments, and consequences. They can trace how symbolic reasoning connects to modern agent systems, how perceptrons led toward deep neural networks, how statistical language methods opened a path to foundation models, and how research ideas become infrastructure and everyday tools.

The central questions are **What happened?** and **What did this become?**

### Historical scenes, not dates alone

Important history happens in laboratories, workshops, conference rooms, demonstrations, product launches, late-night experiments, and conversations that never appear in a formal paper. Over time, the archive can make room for photographs, oral histories, correspondence, talks, interface screenshots, contemporary reporting, and first-person recollections.

The goal is to preserve some sense of what the field felt like before its outcomes became obvious. A technical history is also a human history.

### An archive that grows with the field

Researchers, engineers, designers, founders, archivists, students, and curious readers often know parts of this history that no single editor can see alone. Contributions and corrections can help the archive become wider without turning it into a promotional directory.

The record should remain evidence-led. Interpretation, essays, visual stories, and learning paths can offer distinct points of view while leaving the underlying facts inspectable.

### A historical world for discovery

As the archive grows, it may support:

- people, model, institution, and concept maps;
- parallel timelines showing what was happening in different places at the same time;
- model family trees and intellectual lineages;
- filters across disciplines, countries, institutions, and themes;
- versioned datasets and a public API;
- reading paths for students, researchers, writers, and the curious;
- citations and exports for classrooms, articles, exhibitions, and research;
- editorial essays that interpret patterns without rewriting the record.

The ambition is simple to describe: something that can be read in five minutes, explored for five hours, and cited years later.

> **This is where memory becomes infrastructure.**

## What is here today

The maintained collection contains **272 bilingual events**. The open dataset contains **116 representative events**. Each public record includes:

- a year or exact date with an explicit precision level;
- a concise bilingual title and summary;
- an explanation of why the event matters;
- people, models, institutions, and themes;
- importance and confidence signals;
- at least one publicly accessible source.

The public dataset is the foundation. It can support educational tools, visualisations, research indexes, and new ways of learning the history of AI.

## Editorial principles

### Source before story

Every event should be traceable. Primary sources are preferred; strong secondary sources are used when they provide necessary context.

### Context without mythology

The timeline separates what happened, why it mattered, and what later narratives may have added to it.

### Specificity over hype

Revolutionary is not a historical description. Dates, people, systems, documents, demonstrations, and consequences are.

### Global by design

AI history did not happen in one laboratory, company, country, or language. The archive will continue expanding its coverage without treating any single ecosystem as the whole field.

### Correction is part of the record

A living archive must be able to change. Material corrections should remain visible through sources, version history, and public discussion.

## Quick start

```bash
git clone https://github.com/gengyueworks/ai-timeline.git
cd ai-timeline
python3 -m http.server 8000
```

Then open http://localhost:8000.

The public dataset is available at [`ai-timeline-public.json`](./ai-timeline-public.json), and its schema is documented in [`ai-timeline-schema.json`](./ai-timeline-schema.json).

## Contributing

Corrections and new-event proposals are welcome. A proposal should include:

1. the date and date precision;
2. a concise description of what happened;
3. why the event matters to the wider history of AI;
4. at least one reliable public source;
5. relevant people, models, institutions, or themes.

Please search the existing data for duplicates before opening an issue or pull request. See [`CONTRIBUTING.md`](./CONTRIBUTING.md) for the full editorial and validation rules.

## Repository structure

```text
ai-timeline/
├── .github/workflows/validate-data.yml
├── _meta/
├── scripts/
├── README.md
├── README.zh-CN.md
├── LICENSE
├── LICENSE-DATA
├── CONTRIBUTING.md
├── index.html
├── ai-timeline-public.json
└── ai-timeline-schema.json
```

## Scope and licensing

- Source code: CC BY-NC 4.0.
- Public dataset: CC BY-NC 4.0.
- Third-party photographs, quotations, logos, and archival materials remain subject to their original rights and licences.
- The maintained full collection, private research materials, learning paths, and companion projects remain outside the open dataset unless explicitly stated otherwise.

When reusing the archive, please credit **The AI Timeline by Yue Geng**, link back to the project, and preserve source attribution.

Suggested citation:

```text
Yue Geng. The AI Timeline. Version [date accessed]. [project URL]
```

## About

The AI Timeline is an independent editorial and archival project created by **Yue Geng**.

It began with a simple question: if artificial intelligence is changing how we imagine the future, where can we see, clearly and patiently, how that imagination was built?

The answer cannot be finished by one person or one version. It can be started carefully, kept open, and carried forward.

> **The history of AI is not only the road human technology has travelled. It is also part of the imagination with which we welcome the future.**

# AI Timeline

**English** · [简体中文](./README.zh-CN.md)

A source-backed, bilingual chronology of artificial intelligence—from the theoretical foundations of computation to modern models and agents.

**Live demo:** https://gengyueworks.github.io/ai-timeline/

## Why this project exists

This timeline began as a by-product of learning.

I love AI, but what draws me most is the feeling of exploration: following one idea into another, discovering how an old paper reappears inside a new product, and gradually seeing a vast field become a map. AI can feel like a sea of stars—brilliant, crowded, and almost impossible to hold in one view. A chronology gives me a way to travel through it without losing the connections between ideas.

The value of the project is therefore not simply that it collects dates. It turns a stream of papers, models, products, infrastructure shifts, debates, and cultural moments into a source-backed path that people can follow. It helps a curious reader see what came before a breakthrough, what changed after it, and where to continue learning. I maintain it both as an archive for others and as a record of my own attempt to understand the field more deeply.

I came to AI as a liberal-arts writer rather than a computer scientist. That background makes me attentive to language, context, forgotten branches, and the moment when a technical idea enters ordinary life. I do not expect this timeline to be the final or only map; it is one carefully maintained route through a much larger world.

Every map is drawn from somewhere. I live in China and read across Chinese- and English-language sources, so I sometimes notice open models, infrastructure projects, and developer communities that receive less attention in English-language summaries. When they are historically relevant, I include them alongside work from the rest of the world. This is not an argument for one country or company, only a natural part of keeping the view open, plural, and as complete as I can make it.

## At a glance

- **263** events in the maintained full collection
- **99** representative events in this open dataset
- **1936–2026-08** historical coverage
- Updated weekly
- Static HTML and JSON; no framework or build step required

The public edition is intentionally useful on its own. It provides a working timeline, a documented schema, verifiable sources, minimal dictionary links, and enough coverage to trace the major technical and cultural shifts in AI history.



## Repository structure

```text
ai-timeline/
├── .github/workflows/validate-data.yml
├── _meta/
│   ├── MAINTAINER.md
│   ├── RELEASE-CHECKLIST.md
│   └── SOURCES.md
├── scripts/
│   └── validate-public-data.py
├── README.md
├── README.zh-CN.md
├── LICENSE
├── LICENSE-DATA
├── CONTRIBUTING.md
├── index.html
├── ai-timeline-public.json
├── ai-timeline-schema.json
└── .gitignore
```

## Inclusion and sourcing

An event belongs in the timeline when it marks a meaningful change in at least one of these areas:

- foundational ideas, algorithms, or research methods;
- model capabilities and architectures;
- computing infrastructure and datasets;
- products and developer ecosystems;
- safety, governance, or cultural impact.

Every public event must include a date with an explicit precision level, a concise bilingual title, a 100–200 character Chinese summary, an importance score, a confidence level, and at least one publicly accessible source. Primary sources are preferred. See [`_meta/SOURCES.md`](./_meta/SOURCES.md).

## AI dictionary

The timeline records **what happened** in AI history. For readers who want to understand **what a concept means**, term links connect to [AI Demystified Dictionary](https://gengyueworks.github.io/ai-dictionary/), a companion paid project whose in-depth cards are under development. The timeline remains fully usable without purchasing the dictionary.

## Contributing

Corrections and new-event proposals are welcome. Please open an issue or pull request and include:

1. the proposed date and date precision;
2. a concise explanation of the event;
3. at least one reliable public source;
4. the reason the event matters to the broader AI timeline.

See [`CONTRIBUTING.md`](./CONTRIBUTING.md) for validation rules and editorial criteria.

## Scope and licensing

- **Source code:** MIT License.
- **Public dataset (`ai-timeline-public.json`):** CC BY-NC 4.0.
- **What this repository includes:** the timeline page, interactive code, data schema, validation rules, and 99 source-backed representative events — each with a curated card summary, an event overview, a behind-the-scenes narrative, and a "why it matters" note, so the timeline is fully readable on its own.
- **What this repository does not include:** the complete 263-event dataset, learning paths, relationship graphs, research drafts, and the full AI dictionary cards and paid content — these remain under full copyright unless otherwise stated.

The source code is licensed under MIT. The public dataset is CC BY-NC 4.0. The full timeline data, learning paths, and dictionary entries are not covered by these licenses and remain under full copyright unless otherwise stated.

For commercial use of the dataset, please open an issue describing the intended use.

---

## 中文说明

AI Timeline 是一份有来源依据的双语 AI 编年史，从计算理论起点记录到今天的模型、产品与 Agent。

- 完整维护库共 **263** 个事件
- 本仓库公开 **99** 个代表性事件
- 覆盖 **1936–2026 年 8 月**
- 每周更新
- 纯静态 HTML + JSON，可直接部署到 GitHub Pages

本仓库公开时间轴前端、数据结构、来源标准和代表性数据。完整数据、深度中文叙事、人物关联、学习路径与 AI 词典深度词卡不在本仓库的开放范围内。

时间轴回答 AI 历史上“发生了什么”；若想进一步理解某个概念“意味着什么”，可以访问配套的 [AI 祛魅词典](https://gengyueworks.github.io/ai-dictionary/)。词典是独立的付费项目，但时间轴本身可以免费完整使用。


### 为什么做这条时间轴？

这个项目最初只是我学习 AI 时自然长出来的副产品。AI 对我来说像一片星辰大海；时间轴让我能够沿着论文、模型、产品和社会影响继续探索，同时记住每条路线从哪里出发。它不只是日期集合，而是一条有来源、可追溯的学习路径。

我是文科写作者，也生活在中国，因此会同时阅读中英文资料，自然注意到一些不同的研究、开放模型和开发者社区。它们会在确实重要时与世界其他地方的节点一起出现。这不是替任何国家或公司争位置，而是我保持开放视野、诚实记录所见的一部分。

### 授权范围

- 代码：MIT
- 公开数据集：CC BY-NC 4.0
- 完整时间轴、深度叙事与词典内容：保留所有权利

欢迎通过 Issue 或 Pull Request 提交纠错与新增事件建议。

## Card copy standard

Every event uses an independently edited `card_summary_zh`; previews are never generated by truncating body text. See [`CARD-SUMMARY-SPEC.md`](./CARD-SUMMARY-SPEC.md).

## Selection balance

The 99-event public cut follows a company-neutral editorial standard. See [`_meta/SELECTION-STANDARD.md`](./_meta/SELECTION-STANDARD.md).

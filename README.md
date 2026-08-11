# AI Timeline

**English** · [简体中文](./README.zh-CN.md)

[![Validate](https://github.com/gengyueworks/ai-timeline/actions/workflows/validate-data.yml/badge.svg)](https://github.com/gengyueworks/ai-timeline/actions/workflows/validate-data.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Dataset: CC BY-NC 4.0](https://img.shields.io/badge/Dataset-CC%20BY--NC%204.0-orange.svg)](./LICENSE-DATA)

A source-backed, bilingual chronology of artificial intelligence—from the theoretical foundations of computation to modern models and agents.

**Live demo:** https://gengyueworks.github.io/ai-timeline/

## At a glance

- **272** events in the maintained full collection
- **116** representative events in this open dataset
- **1936–2026-08** historical coverage
- Bilingual (中文 + English)
- Sources across **55 domains**
- CI validation · MIT-licensed code · GitHub Pages site

**Get started:** [Open the live timeline](https://gengyueworks.github.io/ai-timeline/) · [Browse the public dataset](./ai-timeline-public.json) · [Contribute](./CONTRIBUTING.md)

## Quick start

Open the [live timeline](https://gengyueworks.github.io/ai-timeline/).

To run locally:

```bash
git clone https://github.com/gengyueworks/ai-timeline.git
cd ai-timeline
python3 -m http.server 8000
```

Then open http://localhost:8000.

## Use the public data

The public dataset is available at [`ai-timeline-public.json`](./ai-timeline-public.json). The schema is documented in [`ai-timeline-schema.json`](./ai-timeline-schema.json).

Developers can use the dataset to build educational tools, visualizations, research indexes, or timeline-based learning experiences.

## Why this project exists

This timeline began as a by-product of learning.

I love AI, but what draws me most is the feeling of exploration: following one idea into another, discovering how an old paper reappears inside a new product, and gradually seeing a vast field become a map. AI can feel like a sea of stars—brilliant, crowded, and almost impossible to hold in one view. A chronology gives me a way to travel through it without losing the connections between ideas.

The value of the project is therefore not simply that it collects dates. It turns a stream of papers, models, products, infrastructure shifts, debates, and cultural moments into a source-backed path that people can follow. It helps a curious reader see what came before a breakthrough, what changed after it, and where to continue learning. I maintain it both as an archive for others and as a record of my own attempt to understand the field more deeply.

The repository was made public on August 10, 2026, but the project itself has grown over months of private research and local development. The public release is a stable edition: research structure, editorial standards, data validation, and the publishing pipeline were all in place before the first public commit.

I came to AI as a liberal-arts writer rather than a computer scientist. That background makes me attentive to language, context, forgotten branches, and the moment when a technical idea enters ordinary life. I do not expect this timeline to be the final or only map; it is one carefully maintained route through a much larger world.

Every map is drawn from somewhere. I live in China and read across Chinese- and English-language sources, so I sometimes notice open models, infrastructure projects, and developer communities that receive less attention in English-language summaries. When they are historically relevant, I include them alongside work from the rest of the world. This is not an argument for one country or company, only a natural part of keeping the view open, plural, and as complete as I can make it.

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

## Maintainer resources

- [Maintainer notes](./_meta/MAINTAINER.md) — who maintains this and how
- [Source and inclusion standard](./_meta/SOURCES.md)
- [Selection standard](./_meta/SELECTION-STANDARD.md) — how events are chosen
- [Release checklist](./_meta/RELEASE-CHECKLIST.md)
- [Maintenance workflow](./_meta/MAINTENANCE.md) — how Codex participates in maintenance
- [Card copy standard](./CARD-SUMMARY-SPEC.md)

## Scope and licensing

- **Source code:** MIT License.
- **Public dataset (`ai-timeline-public.json`):** CC BY-NC 4.0.
- **What this repository includes:** the timeline page, interactive code, data schema, validation rules, and 116 source-backed representative events — each with a curated card summary, an event overview, a behind-the-scenes narrative, and a "why it matters" note, so the timeline is fully readable on its own.
- **What this repository does not include:** the complete 272-event dataset, learning paths, relationship graphs, research drafts, and the full AI dictionary cards and paid content — these remain under full copyright unless otherwise stated.

The source code is licensed under MIT. The public dataset is CC BY-NC 4.0. The full timeline data, learning paths, and dictionary entries are not covered by these licenses and remain under full copyright unless otherwise stated.

For commercial use of the dataset, please open an issue describing the intended use.

---

## 中文说明

AI Timeline 是一份有来源依据的双语 AI 编年史，从早期计算理论起点记录到今天的模型、产品与 Agent。

详细的中文长文介绍可参阅 [README.zh-CN.md](./README.zh-CN.md)。

---

### 项目概况

- 完整维护库共 272 个事件
- 本仓库公开 116 个代表性事件
- 覆盖跨度为 1936 至 2026 年 8 月
- 中英双语呈现（中文 + English）
- 来源覆盖 55 个顶级域名与文献库
- CI 数据校验 · 代码开源（MIT）· GitHub Pages 自动化部署

[打开在线时间轴](https://gengyueworks.github.io/ai-timeline/) · [浏览公开数据集](./ai-timeline-public.json) · [参与贡献](./CONTRIBUTING.md)

---

### 为什么做这条时间轴？

这个项目最初是我自己学习 AI 时记录下来的副产品。

我喜欢研究 AI，更喜欢那种顺藤摸瓜的感觉：沿着一个概念找到另一个概念，在今天的新产品里看到几十年前论文的影子，把散落的突破重新串成一张看得懂的地图。AI 领域跑得太快，每天信息铺天盖地，很容易让人迷失。做一条时间轴，能让我理清思想演进的来龙去脉，不至于迷路。

它不只是列出日期。它把论文、模型、产品、算力、行业讨论和文化事件连在一起，做成一条有来源、可追溯的路径。读者能看清一项突破的前因后果，知道变化怎么发生，也知道接下来可以去哪里深入研究。我维护它，既是给别人留一份方便查阅的档案，也是记录自己理解这个领域的过程。

这个仓库在 2026 年 8 月 10 日开源，但项目本身已经在本地跑了几个月。公开版是一个稳定版本：研究结构、编辑标准、数据校验机制和部署脚本，在第一次 commit 前就已经搭好了。

我是个文科写作者，没有计算机科班背景。这种视角让我对语言、语境、被遗忘的技术分支，以及技术怎么进入普通人生活更敏感。我没打算把它做成唯一或最终的 AI 全景图，它只是我认真打磨出来的一条路线。

地图总带着画图人的视角。我生活在中国，日常同时看中英文资料，自然会注意到一些在英文概述里较少提到的开源模型、基础设施和开发者社区。只要它们在技术演化里确实重要，我就把它们和世界其他地方的进展放在一起。这不是替谁说话，只是想保持开放和诚实，把我看到的真实世界放进来。

---

### 开放边界说明

公开版的 116 条事件可以完整浏览；完整维护库、全年时间轴和深度内容不在本仓库的开放范围内。

公开版仍然以开源、体验和可贡献为主，付费内容只做边界说明，不放大宣传。

---

### AI 词典关联

时间轴记录 AI 历史上“发生了什么”。如果想了解某个概念“意味着什么”，可以查看配套的 [AI 祛魅词典](https://gengyueworks.github.io/ai-dictionary/)。词典是独立的付费项目，里面的深度词卡还在撰写中。时间轴本身保持完整，不买词典也能正常使用全部功能。

---

### 授权与使用

- **代码：** MIT 许可证。
- **公开数据集（`ai-timeline-public.json`）：** CC BY-NC 4.0 许可证。
- **本仓库包含：** 时间轴页面、交互代码、数据 Schema、校验规则，以及 116 个有来源的代表性事件（每个事件包含卡片摘要、事件概览、背景故事与重要性解析，可独立完整浏览）。

如果需要商业使用数据集，请提交 Issue 说明使用场景。

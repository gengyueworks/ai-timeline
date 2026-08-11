# AI 时间轴

[English](./README.md) · **简体中文**

[![校验](https://github.com/gengyueworks/ai-timeline/actions/workflows/validate-data.yml/badge.svg)](https://github.com/gengyueworks/ai-timeline/actions/workflows/validate-data.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![数据: CC BY-NC 4.0](https://img.shields.io/badge/Dataset-CC%20BY--NC%204.0-orange.svg)](./LICENSE-DATA)

一份有来源依据的双语 AI 编年史，从计算理论起点记录到今天的模型、产品与 Agent。

[打开在线时间轴](https://gengyueworks.github.io/ai-timeline/) · [浏览公开数据集](./ai-timeline-public.json) · [参与贡献](./CONTRIBUTING.md)

---

## 项目概览

- **272** 个事件收录于完整维护库
- **116** 个代表性事件收录于公开数据集
- 覆盖 **1936–2026 年 8 月** 历史
- 中英双语（中文 + English）
- 来源覆盖 **55 个顶级域名** 与文献库
- CI 数据校验 · 代码开源（MIT）· GitHub Pages 自动化部署

---

## 快速开始

打开 [在线时间轴](https://gengyueworks.github.io/ai-timeline/) 即可直接体验。

如果在本地运行：

```bash
git clone https://github.com/gengyueworks/ai-timeline.git
cd ai-timeline
python3 -m http.server 8000
```

随后在浏览器打开 `http://localhost:8000`。

---

## 使用公开数据

公开数据集保存在 [`ai-timeline-public.json`](./ai-timeline-public.json) 中，数据结构规范详见 [`ai-timeline-schema.json`](./ai-timeline-schema.json)。

开发者可以使用这份数据集构建教育工具、可视化项目、研究索引或基于时间轴的学习体验。

---

## 为什么做这个项目？

这个项目最初是我学习 AI 时自然长出来的副产品。

我热爱 AI，但最吸引我的始终是那种探索感：顺着一个想法追下去，在最新的产品里看到几十年前论文的影子，看着原本庞杂无序的领域逐渐拼接成一张清晰的地图。AI 的发展速度快得像一片密集的星空，让人很难一眼看清全貌。而一条时间轴，正好能让我在这片星空中穿行时，不至于迷失思想之间的脉络。

因此，这个项目的价值不仅在于整理日期。它把看似零散的论文、模型、产品、算力基础设施、行业讨论与文化事件，串联成一条有据可查、可循线探索的路径。它帮助好奇的读者看清一项突破的前因后果，知道变化发生在哪里，也知道接下来可以去哪里深入研究。我维护它，既是为他人留一份方便查阅的档案，也是记录自己理解这个领域的过程。

本仓库于 2026 年 8 月 10 日正式开源，但项目本身已经在本地经过了数月的持续研究与迭代。这次公开的是一个稳定版本，研究结构、编辑标准、数据校验机制与自动化发布流程，在第一次提交之前就已经建立完毕。

我是以文科写作者的身份进入 AI 领域的，而不是计算机背景。这种视角让我对语言、语境、被忽略的技术分支，以及技术思想进入日常生活的方式更为敏感。我并不期待这条时间轴成为唯一的全景图，它只是通往这个庞大世界中，一条被认真打磨过的路径。

任何地图都带有绘制者的视野。我生活在中国，日常同时阅读中英文资料，因此也会注意到一些在英文汇总里较少被提及的开放模型、基础设施与开发者社区。只要它们在技术演进中确实具有历史意义，我就会把它们与世界其他地方的进展放在一起。这不是为了替某种立场发声，只是为了保持开放、真实和尽量完整的视角。

---

## 仓库目录结构

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

---

## 选条与来源标准

当一个事件在以下至少一个维度带来实质变化时，就会被收入时间轴：

1. 基础理论、算法或研究方法；
2. 模型能力与架构创新；
3. 计算基础设施与数据集；
4. 产品生态与开发者工具；
5. 安全、治理或社会文化影响。

公开版中的每个事件都包含明确精度的日期、简明双语标题、100 到 200 字的中文摘要、重要性评分、置信度以及至少一个公开可访问的来源（优先采用第一手来源）。详见 [`_meta/SOURCES.md`](./_meta/SOURCES.md)。

---

## AI 词典关联

时间轴记录 AI 历史上“发生了什么”。如果希望进一步理解某个概念“意味着什么”，可以参考配套的 [AI 祛魅词典](https://gengyueworks.github.io/ai-dictionary/)。词典是一个独立的付费项目，其中的深度词卡仍在持续撰写中。时间轴本身保持独立完整，不购买词典也可以正常使用全部功能。

---

## 参与贡献

欢迎提交纠错或新增事件建议。请提交 Issue 或 Pull Request，并包含以下内容：

1. 建议的日期与日期精度；
2. 事件的简要说明；
3. 至少一个可靠的公开来源；
4. 该事件对整个 AI 时间轴的重要性理由。

请参考 [`CONTRIBUTING.md`](./CONTRIBUTING.md) 了解校验规则与编辑规范。

---

## 维护者资源

- [维护者说明](./_meta/MAINTAINER.md) —— 本项目由谁维护以及如何维护
- [来源与入选标准](./_meta/SOURCES.md)
- [筛选标准](./_meta/SELECTION-STANDARD.md) —— 事件如何挑选
- [发布检查清单](./_meta/RELEASE-CHECKLIST.md)
- [维护流程](./_meta/MAINTENANCE.md) —— Codex 如何参与维护
- [卡片文案规范](./CARD-SUMMARY-SPEC.md)

---

## 授权范围与使用说明

- **代码：** MIT 许可证。
- **公开数据集（`ai-timeline-public.json`）：** CC BY-NC 4.0 许可证。
- **开放边界说明：** 公开版的 116 条事件可以完整浏览；完整维护库、全年时间轴和深度内容不在本仓库的开放范围内。
- **本仓库包含内容：** 时间轴前端页面、交互代码、数据 Schema、校验规则，以及 116 个有来源依据的代表性事件（每个事件均包含精修卡片摘要、事件概览、背景故事与重要性解析，可独立完整浏览）。

如需商业使用数据集，请提交 Issue 说明具体使用场景。

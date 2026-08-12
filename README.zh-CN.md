# AI Timeline（AI 时间轴）

[English](./README.md) · **简体中文**

[![校验](https://github.com/gengyueworks/ai-timeline/actions/workflows/validate-data.yml/badge.svg)](https://github.com/gengyueworks/ai-timeline/actions/workflows/validate-data.yml)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-orange.svg)](./LICENSE)
[![数据: CC BY-NC 4.0](https://img.shields.io/badge/Dataset-CC%20BY--NC%204.0-orange.svg)](./LICENSE-DATA)

一份有来源依据的双语 AI 编年史，从早期计算理论起点记录到今天的模型、产品与 Agent。

[打开在线时间轴](https://gengyueworks.github.io/ai-timeline/) · [浏览公开数据集](./ai-timeline-public.json) · [参与贡献](./CONTRIBUTING.md)

---

## 概况

- **272** 个事件收录于完整维护库
- **116** 个代表性事件收录于公开数据集
- 覆盖 **1936–2026 年 8 月** 历史
- 中英双语呈现（中文 + English）
- 来源覆盖 **55 个顶级域名** 与文献库
- CI 数据校验 · 代码 CC BY-NC 4.0（非商用）· GitHub Pages 自动化部署

---

## 快速开始

在线体验可以直接打开 [在线时间轴](https://gengyueworks.github.io/ai-timeline/)。

本地运行：

```bash
git clone https://github.com/gengyueworks/ai-timeline.git
cd ai-timeline
python3 -m http.server 8000
```

然后在浏览器访问 `http://localhost:8000`。

---

## 使用公开数据

公开数据集保存在 [`ai-timeline-public.json`](./ai-timeline-public.json)，数据结构规范写在 [`ai-timeline-schema.json`](./ai-timeline-schema.json)。

开发者可以用这份数据做可视化、研究索引、教学演示或时间轴学习工具。

---

## 为什么做这条时间轴？

这个项目最初是我自己学习 AI 时记录下来的副产品。

我喜欢研究 AI，更喜欢那种顺藤摸瓜的感觉：沿着一个概念找到另一个概念，在今天的新产品里看到几十年前论文的影子，把散落的突破重新串成一张看得懂的地图。AI 领域跑得太快，每天信息铺天盖地，很容易让人迷失。做一条时间轴，能让我理清思想演进的来龙去脉，不至于迷路。

它不只是列出日期。它把论文、模型、产品、算力、行业讨论和文化事件连在一起，做成一条有来源、可追溯的路径。读者能看清一项突破的前因后果，知道变化怎么发生，也知道接下来可以去哪里深入研究。我维护它，既是给别人留一份方便查阅的档案，也是记录自己理解这个领域的过程。

这个仓库在 2026 年 8 月 10 日开源，但项目本身已经在本地跑了几个月。公开版是一个稳定版本：研究结构、编辑标准、数据校验机制和部署脚本，在第一次 commit 前就已经搭好了。

我是个文科写作者，没有计算机科班背景。这种视角让我对语言、语境、被遗忘的技术分支，以及技术怎么进入普通人生活更敏感。我没打算把它做成唯一或最终的 AI 全景图，它只是我认真打磨出来的一条路线。

地图总带着画图人的视角。我生活在中国，日常同时看中英文资料，自然会注意到一些在英文概述里较少提到的开源模型、基础设施和开发者社区。只要它们在技术演化里确实重要，我就把它们和世界其他地方的进展放在一起。这不是替谁说话，只是想保持开放和诚实，把我看到的真实世界放进来。

---

## 仓库结构

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

一个事件只要在下面任意一个方面带来实质改变，就会被收录：

1. 基础理论、算法或研究方法；
2. 模型能力与架构创新；
3. 计算基础设施与数据集；
4. 产品生态与开发者工具；
5. 安全、治理或社会文化影响。

公开版里的每个事件都有明确精度的日期、简明双语标题、100 到 200 字的中文摘要、重要度评分、置信度和至少一个公开来源（优先用第一手来源）。详见 [`_meta/SOURCES.md`](./_meta/SOURCES.md)。

---

## AI 词典关联

时间轴记录 AI 历史上“发生了什么”。如果想了解某个概念“意味着什么”，可以查看配套的 [AI 祛魅词典](https://gengyueworks.github.io/ai-dictionary/)。词典是独立的付费项目，里面的深度词卡还在撰写中。时间轴本身保持完整，不买词典也能正常使用全部功能。

---

## 开放边界说明

公开版的 116 条事件可以完整浏览；完整维护库、全年时间轴和深度内容不在本仓库的开放范围内。

公开版仍然以开源、体验和可贡献为主，付费内容只做边界说明，不放大宣传。

---

## 参与贡献

欢迎提交纠错或新增事件建议。请提交 Issue 或 Pull Request，包含以下内容：

1. 建议的日期与精度；
2. 事件说明；
3. 至少一个可靠的公开来源；
4. 该事件对整个 AI 时间轴的重要性。

详细规则见 [`CONTRIBUTING.md`](./CONTRIBUTING.md)。

---

## 维护者资源

- [维护者说明](./_meta/MAINTAINER.md) —— 谁在维护、如何维护
- [来源与入选标准](./_meta/SOURCES.md)
- [筛选标准](./_meta/SELECTION-STANDARD.md) —— 事件挑选原则
- [发布检查清单](./_meta/RELEASE-CHECKLIST.md)
- [维护流程](./_meta/MAINTENANCE.md) —— Codex 参与维护的方式
- [卡片文案规范](./CARD-SUMMARY-SPEC.md)

---

## 授权与使用

- **代码：** CC BY-NC 4.0 许可证（非商用）。
- **公开数据集（`ai-timeline-public.json`）：** CC BY-NC 4.0 许可证（非商用）。
- **本仓库包含：** 时间轴页面、交互代码、数据 Schema、校验规则，以及 116 个有来源的代表性事件（每个事件包含卡片摘要、事件概览、背景故事与重要性解析，可独立完整浏览）。

如果需要商业使用数据集，请提交 Issue 说明使用场景。

# AI 时间轴

[English](./README.md) · **简体中文**

[![校验](https://github.com/gengyueworks/ai-timeline/actions/workflows/validate-data.yml/badge.svg)](https://github.com/gengyueworks/ai-timeline/actions/workflows/validate-data.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![数据: CC BY-NC 4.0](https://img.shields.io/badge/Dataset-CC%20BY--NC%204.0-orange.svg)](./LICENSE-DATA)

一份有来源依据的双语 AI 编年史，从计算理论起点记录到今天的模型、产品与 Agent。

**在线访问：** https://gengyueworks.github.io/ai-timeline/

## 为什么做这条时间轴？

这个项目最初只是我学习 AI 时自然长出来的副产品。

我喜欢 AI，但更吸引我的是探索本身：顺着一个概念找到另一个概念，看一篇几十年前的论文怎样在今天的产品里重新出现，再把散落的事件慢慢连成可以理解的路径。AI 对我来说很像一片星辰大海——明亮、浩瀚，也很容易让人迷失。时间轴是我航行其中、又不丢掉来路的一种方式。

所以，这个项目的价值不只是收集日期。它试着把论文、模型、产品、算力、争议和文化影响整理成一条有来源、可追溯的学习路径：一项突破之前发生了什么，它之后又改变了什么，一个刚进入 AI 的人还可以沿着哪些线索继续探索。它既是一份供别人使用的档案，也是我理解这个领域、记录自己学习过程的方法。

我是一个文科写作者，不是计算机科班出身。这反而让我格外在意语言、背景、被忽略的岔路，以及技术真正进入普通人生活的瞬间。我不认为这会是唯一正确或最终完整的 AI 地图；它只是我认真维护的一条路线，随着学习不断生长。

任何地图都会带着观察者所在的位置。我生活在中国，也会同时阅读中文和英文资料，因此自然会注意到一些在英文概述中不太显眼的开放模型、基础设施和开发者社区。它们如果确实具有历史意义，就应该和世界其他地方的重要工作一起出现。这不是要替某个国家或公司争位置，只是希望保持一种开放、多元的视野，把我真实看到的部分诚实地放进这张更大的地图里。

## 项目数据

- 完整维护库：272 个事件
- 本仓库公开：116 个代表性事件
- 时间范围：1936–2026 年 8 月
- 更新频率：每周
- 技术形式：纯静态 HTML + JSON



## 开放范围

本仓库公开：

- 时间轴页面与交互代码；
- 公开数据结构与校验规则；
- 116 个有公开来源的代表性事件（含卡片导语与深度叙述，便于直接阅读）；
- 来源收录标准与贡献流程。

本仓库不公开：

- 完整 272 条深度数据；
- 学习路径、人物关系与研究草稿；
- AI 祛魅词典的完整词卡与付费内容。

公开版不是工作进度表，而是稳定、可使用、可核验的发行版本。

## AI 词典

时间轴记录“发生了什么”。如果想理解一个概念“意味着什么”，右侧词卡会连接到 [AI 祛魅词典](https://gengyueworks.github.io/ai-dictionary/)。词典是独立的付费项目，时间轴无需购买即可使用。

## 贡献与纠错

提交 Issue 或 Pull Request 时请提供日期、日期精度、事件说明、公开来源和收录理由。详细规则见 [`CONTRIBUTING.md`](./CONTRIBUTING.md)。

## 授权

- 代码：MIT
- `ai-timeline-public.json`：CC BY-NC 4.0
- 完整时间轴、深度中文叙事和词典词卡：保留所有权利

## 卡片文案规范

每个事件都使用单独编辑的 `card_summary_zh`。卡片预览不会再从正文中机械截断，具体规则见 [`CARD-SUMMARY-SPEC.md`](./CARD-SUMMARY-SPEC.md)。

## 选取与平衡

公开版的 116 个事件遵循不偏向单一公司的编辑标准，具体见 [`_meta/SELECTION-STANDARD.md`](./_meta/SELECTION-STANDARD.md)。

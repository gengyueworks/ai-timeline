# AI Timeline · 维护工作流

> 这份文档说明项目如何被持续维护，以及 AI coding agents（Codex）如何参与真实的开源维护流程。
> 最后更新：2026-08-11

---

## 维护者

- **维护者**：Yue Geng（gengyueworks）
- **角色**：主要维护者（primary maintainer）
- **背景**：文科写作者，通过 AI coding agents 学习软件与开源维护

## 数据流

```
新事件提案 (Issue) → 事实核查 → 编辑审阅 → 双语写作 → 数据校验 → Release
```

## 完整库数量口径

公开版的 `full_collection_size` 当前统一记录为 **272**。维护者私有工作区中，2026-08-11 生成的英文完整数据是当前 272 条 canonical source；名为 `ai-timeline-data-263条-完整版.json` 的文件属于旧快照，不能继续作为完整库数量依据。

每周维护时，使用 `python3 scripts/validate-public-data.py --full-data <canonical-full-data.json>` 对照完整数据。校验脚本会以完整数据中的 `events` 数组长度为准，并检查 `total_events` 是否一致；文件名中的数字不参与判断。

公开数据的 `date_range` 由事件数组中的最小日期和最大日期计算。事件增删后，必须重新运行校验，不能手工保留过期日期范围。

### 1. 事件提案与事实核查

- 通过 Issue 模板收集新增事件/事实纠错/来源失效/翻译修正
- 所有日期与事实必须有一手来源（论文、官方公告、机构档案）
- 来源核查工具链：HN Algolia API → read4f → HuggingFace API → GitHub API → 官方博客

### 2. 编辑审阅

- 按 `_meta/SELECTION-STANDARD.md` 六维标准评估：技术意义、生态影响、历史独特性、来源可靠性、路线代表性、公司与地区平衡
- 同一家公司短期内原则上只保留一个相似模型更新

### 3. 双语写作

- 每条事件含：中文标题/英文标题/中文摘要/英文摘要/卡片导语/背后现场/为何重要
- 遵循 `CARD-SUMMARY-SPEC.md` 的导语规范
- 英文翻译遵循固定译法表（术语、分类、难度映射）

### 4. 数据校验

- 修改后运行 `python3 scripts/validate-public-data.py`
- 有 canonical 完整库时，追加 `--full-data <canonical-full-data.json>` 检查公开版与完整库数量口径
- GitHub Actions 自动校验：事件数、时间顺序、重复 ID、来源完整性、字段合法性
- 校验失败会阻止部署

### 5. 来源链接检查

`scripts/check-source-links.py` 只生成健康报告，不自动修改数据，也不因 403、429、超时、SSL、EOF 或连接重置创建 Issue。404/410 先标记为 `candidate-dead`；同一 URL 连续两次报告为候选失效后，才进入人工确认队列。

建议将报告写入 `reports/link-health/YYYY-MM-DD.json`，下一次使用同一个报告路径作为历史依据。只有人工确认来源确实失效后，才替换 URL 或关闭事件。

### 6. 发布

- 版本化 Release（v0.1.0 起）
- GitHub Pages 自动部署（push main 触发）
- 发布说明自动生成

## Codex 如何参与维护

Codex 在以下环节提供自动化帮助：

| 环节 | Codex 的作用 |
|---|---|
| 事件校验 | 验证新提案的日期/事实/来源格式 |
| 来源检查 | 检测失效链接、URL 完整性 |
| 数据完整性 | 检测时间顺序错误、重复 ID、缺失字段 |
| 双语审阅 | 辅助中英文编辑与事实核查 |
| Issue 分类 | 按类型分派 Issue（新增/纠错/失效/翻译）|
| 发布自动化 | 生成 Release notes、触发 Pages 部署 |

## 发布节奏

- **事件更新**：每周 2-5 条真正重要的事件（不灌水）
- **版本发布**：功能或数据集有明显进展时打 tag
- **来源复查**：定期批量检查 source_url 有效性

## 持续维护的证据

- 每日/每周 commit 记录
- GitHub Actions 校验历史
- Release 版本线
- 来源数据随版本更新

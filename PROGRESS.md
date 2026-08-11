# PROGRESS — AI Timeline 技术体验改造

> 交接指令：`~/Downloads/技术体验改造-交接指令-2026-08-11.md`
> 铁律：不改事件正文 / 不压缩 / 不删节点 / 不删词典连接 / 不删来源字段

## 基线（改造前，2026-08-11）

| 项 | 值 |
|---|---|
| 仓库 | `/tmp/ai-timeline/`（remote: gengyueworks/ai-timeline，分支 main） |
| 入口 | `index.html`（单文件，纯静态，无构建，41,272 字节） |
| 数据 | `ai-timeline-public.json` — **116 事件** |
| 词典连接 | `related_terms` 全量求和 **353**（展示逻辑需用求和，不能用去重 Set=159） |
| 校验脚本 | `scripts/validate-public-data.py` |

### 数据 type 分布（已核实，116 = 全量）
```
research: 78, model: 15, product: 6, infrastructure: 5, agent: 5, safety: 4, business: 3
```

### 最大风险
1. **分类错位**：筛选按钮 foundational/ecosystem/culture 在数据中不存在 → 点击空白；research(78) 主力无按钮
2. **词典连接统计错误**：现行代码用 `Set` 去重显示 159，真实连接求和应为 353
3. **英文状态不完整**：筛选/统计/提示语中文混杂；html lang 不切换；title/meta/og 不切换
4. **状态无持久化**：语言/筛选/搜索/展开刷新即丢
5. **首屏 DOM**：116 卡全渲染（详情默认 display:none 已确认，DOM 压力在卡片本体）
6. 校验脚本要求 `public_event_count == len(events) == 116`，改数据即失败 → 本次不动 JSON

## 修改记录

### [R1] 统一 locale + 分类修复 + 持久化 + 词典 missing 状态 + 可访问性（本次，2026-08-11）
- **locale 层**：新增 `LOCALES` 双语词典，覆盖 brand/筛选/搜索/统计/时间轴头/详情标签/收起/状态/aria-label；`applyLanguageMeta()` 同步 `html.lang`、`document.title`、meta description、og:title/og:description
- **分类**：canonical 类别 = 7 个真实 type（research/model/product/infrastructure/agent/safety/business），`CATEGORY_LABELS` 双语显示名；筛选按钮由 JS 生成（含「全部」），一键一类，全部有结果；`eventVisible` 改为 `type === filter` 直配；原始 `type` / `type_legacy` 字段不动
- **词典连接统计**：`term-count` 改为 `related_terms` 求和（=353），与验收一致
- **持久化**：URLSearchParams 保存 `lang/cat/q/e/open`；`pushState` 记录、`popstate` 恢复，后退/前进/刷新/复制 URL 均可还原；搜索输入防抖 350ms 写 URL
- **词典跳转**：跳转前状态已在 URL（history），返回后 popstate 自动恢复；missing 词条加 dashed 边框 + 「词典暂无此词条」badge + aria-label，不再伪装可点
- **首屏 DOM**：`.event` 加 `content-visibility: auto; contain-intrinsic-size: auto 140px;`
- **可访问性**：chip/search/term/collapse 等触控目标 ≥40-44px；`:focus-visible` 全局焦点环；chip 行可横向滚动防溢出

## 测试记录
- `python3 scripts/validate-public-data.py` → **PASS**（116 events, chronological, 校验通过）
- 浏览器验收（ego-browser，CDP emulation）：
  - 事件总数 116、词典连接 353（求和）→ ✅
  - 全部 116 个中文标题与 JSON 逐字比对 → ✅ 零改动
  - 8 个筛选按钮（全部+7类）全部有结果：research 78 / model 15 / product 6 / infrastructure 5 / agent 5 / safety 4 / business 3 → ✅ 无空白
  - 英文下 lang=en、title/meta/og、placeholder、筛选、统计、按钮全英文 → ✅ 无混杂
  - 搜索+分类+语言可组合（research+图灵+EN=1 条）→ ✅
  - URL 恢复：`?lang=en&cat=model&e=33` 打开即还原语言/筛选/展开 → ✅
  - 刷新/复制 URL/后退/前进 → ✅（`history.back()` 后 cat 重置为 all）
  - 默认详情收起（首屏 0 展开）→ ✅
  - 390/768/1055/1440 无横向溢出 → ✅
  - 触控目标：chip 42px、search 42px、term 44px、collapse 40px → ✅
  - 键盘：card focus + Enter/Space 展开、aria-expanded → ✅
  - 词典跳转 `ai-dictionary-lab.html?term=CNN&from=timeline` → ✅；返回后 lang/cat/展开状态完整恢复 → ✅
  - missing 词条：dashed 边框 +「词典暂无此词条」badge + disabled + aria-label → ✅
  - 搜索无结果：「没有匹配的历史节点。」→ ✅
- **修复的额外 bug**：搜索状态下点「收起」会被 auto-expand 覆盖（详情立即重新展开）→ 新增 `suppressAutoExpand` 标志修复

## 风险与后续
- 遗留：无
- 后续可选：subtimeline 数据当前为空（0 事件含 subtimeline），其渲染路径保留但未在浏览器实测
- 备注：词典 `ai-dictionary-expansion-review-draft.json` 返回 404（原代码 try/catch 静默处理，行为不变）

---
type:: Source
source-type:: x-thread
author:: Thariq Shihipar (@trq212)
date:: 2026-05-09
url:: https://x.com/trq212/status/2052809885763747935
raw-file:: _raw/thariq-html-effectiveness-x-thread.txt
created:: [[2026-05-08]]
---
- # Using Claude Code: The Unreasonable Effectiveness of HTML（Thariq Shihipar）
- ## 一句话总结
  > HTML 作为 LLM 输出格式的原始第一手论证：Thariq（Claude Code 团队）用 11M 次浏览证明，生成 HTML 比 Markdown 多花 2-4x token，却有更高概率被真正阅读和采纳。
- ## 背景
  - 作者 Thariq Shihipar (@trq212) 是 **Anthropic Claude Code 团队**成员
  - 发布于 2026-05-09，获得 **11M 浏览 · 937 回复 · 3.5K 转发 · 15K 点赞**
  - 这是 [[source/unreasonable-effectiveness-of-html]]（Simon Willison 的博文）的**原始来源**——Simon 是在看到此 X 帖后独立验证并放大传播的
- ## HTML > Markdown 的 5 个理由
  1. **信息密度（Information Density）**
     Markdown 是线性的（列表+层级），HTML 可以用表格、标签页、折叠区、颜色编码同时展示多维信息。一次代码审查的 HTML 输出 = diff + 标注 + 严重性颜色，Markdown 等价版需要 3x 篇幅且更难扫读。
  2. **视觉清晰度（Visual Clarity）**
     人类处理视觉信息远快于文本扫读。HTML 产出的输出人们会**真正阅读**，而不只是滚动浏览。颜色、布局、层次结构在一眼间传达意义。
  3. **易于分享（Ease of Sharing）**
     HTML 文件是自包含的完整 artifact，可在任何浏览器打开、邮件传阅、嵌入文档。Markdown 需要渲染器才可读。HTML 是通用文档格式。
  4. **双向交互（Two-way Interaction）**
     HTML + JavaScript 可以让输出变得可交互：可编辑字段、功能开关、滑块调参、点击确认/拒绝——这大幅压缩了人在环（human-in-the-loop）的反馈周期。
  5. **数据摄取（Data Ingestion）**
     HTML 可以内联渲染结构化数据（表格、图表、SVG）。本来需要 Excel 或 Grafana 的数据可以直接内嵌在输出中，无需外部依赖。
- ## 核心 Prompt 模式
  ```
  Output HTML, neatly styled and using capabilities of HTML and CSS and JavaScript
  to make the explanation rich and interactive and as clear as possible.
  ```
- ## 五大使用场景
  | 场景 | 具体示例 |
  |------|----------|
  | 规格/规划/探索 | 方案并排对比、SVG 架构图、实现时间线 |
  | 代码审查 | 带边栏标注的 diff、按严重性颜色标注、模块依赖图 |
  | 设计/原型 | 可调参数的动画沙盒、可点击用户流程原型、颜色 token 色板 |
  | 报告/学习 | 可折叠章节、多语言标签页代码、侧栏词汇表 |
  | 自定义编辑器 | 票据看板、功能开关编辑器、Prompt 调优界面 |
- ## Token 成本 vs. 实际价值
  - 生成 HTML 比 Markdown 多消耗 **2-4x token**
  - 但没人阅读的 Markdown 输出，实际价值为零
  - 被阅读、分享、采纳的 HTML 输出，具有复利价值
  - 结论：**对任何面向人类消费的输出，ROI 计算都有利于 HTML**
- ## 示例集合
  Thariq 发布了 20 个自包含 HTML 示例：[thariqs.github.io/html-effectiveness/](https://thariqs.github.io/html-effectiveness/)
- ## 历史背景
  GPT-4 时代（8K context），Markdown 在 token 预算紧张时占优。现代模型（100K-200K+ context）下，这一权衡已经翻转：HTML 的表达力优势现在值得花费更多 token。
- ## 与其他资料的关系
  - [[source/unreasonable-effectiveness-of-html]] — Simon Willison 的博文：覆盖/放大了本 X 帖，并新增了 copy.fail 案例作为独立验证
  - 两者共同构成 [[entity/html-as-llm-output-format]] 的核心来源
  - [[source/how-anthropic-teams-use-claude-code]] — Thariq 是 Claude Code 团队成员
- ## 引用此资料的页面
  - [[entity/html-as-llm-output-format]]

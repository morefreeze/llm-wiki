---
type:: Source
source-type:: article
author:: Simon Willison, Thariq Shihipar
date:: 2026-05-08
url:: https://simonwillison.net/2026/May/8/unreasonable-effectiveness-of-html/
raw-file:: _raw/unreasonable-effectiveness-of-html.txt
created:: [[2026-05-11]]
---
- # HTML 的不合理有效性（Simon Willison / Thariq Shihipar）
- ## 一句话总结
  > 用 HTML 而非 Markdown 作为 LLM 输出格式，能让 Agent 输出从「文字墙」升级为可交互、可导航、可操作的信息空间。
- ## 关键要点
  1. **HTML > Markdown 用于输出** — Markdown 是线性文本，HTML 可以包含 SVG 图表、交互组件、页内导航、标签页、可折叠区域
  2. **20 个自包含 .html 示例** — 涵盖 9 大场景：探索规划、代码审查、设计系统、原型、图表、演示、研究学习、报告、自定义编辑器
  3. **Token 效率的权衡** — GPT-4 时代 8K token 限制使 Markdown 更优；如今 token 窗口充裕，HTML 的富表达力更有价值
  4. **关键 Prompt 模式** — `"Output HTML, neatly styled and using capabilities of HTML and CSS and JavaScript to make the explanation rich and interactive"`
  5. **Simon 的验证** — 用 `curl | llm -m gpt-5.5` 解释 copy.fail 安全漏洞，生成暗色主题双栏布局的交互式代码解析
- ## 详细笔记
  ### 九大应用场景
  | 场景 | 示例 | 核心价值 |
  |------|------|----------|
  | 探索与规划 | 代码方案并排对比、视觉设计方向、实现计划 | 替代「三段文字墙在脑中比较」 |
  | 代码审查 | 带标注的 PR diff、模块地图、PR 描述 | diff 是空间信息，Markdown 压扁了它 |
  | 设计系统 | 颜色/字体 token 渲染为色板、组件变体清单 | 设计系统的原生介质就是 HTML |
  | 原型 | 动画沙盒（可调参数）、可点击流程 | 交互只能感受，无法描述 |
  | 图表 | 内联 SVG 插图、可点击流程图 | Agent 拥有真正的画笔 |
  | 演示 | 方向键翻页的单文件 PPT | `<section>` + 20 行 JS 即可 |
  | 研究学习 | 可折叠章节、标签页代码、侧栏词汇表 | 把新主题变得可导航 |
  | 报告 | 带图表的周报、分钟级事件时间线 | 加点结构+颜色，从「扫一眼」到「真的读」 |
  | 自定义编辑器 | 票据看板、Feature Flag 编辑器、Prompt 调优器 | 难以用文字描述的需求，用 UI 表达 |
  ### 核心洞察
  - **Diff 和调用图是空间信息**，Markdown 把它们压扁了
  - **交互只能感受，无法描述** — 抛弃式页面 5 秒传达的比一段文字更多
  - **编辑器模式** — 「最后总有一个导出按钮」，人始终在环中，环变得更紧
- ## 与其他资料的关系
  - 与 [[source/karpathy-vibe-coding-to-agentic-engineering]] 互补：Vibe Coding 的输出也可以是富 HTML
  - 补充了 [[entity/agentic-coding]]：Agent 输出格式选择是实践中的重要决策
  - 与 [[source/how-anthropic-teams-use-claude-code]] 相关：Thariq 是 Claude Code 团队成员
- ## 引用此资料的页面
  - [[entity/html-as-llm-output-format]]
  - [[entity/agentic-coding]]

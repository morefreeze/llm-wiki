---
type:: Entity
tags:: #prompt-engineering #html #agent #output-format
created:: [[2026-05-11]]
sources:: [[source/unreasonable-effectiveness-of-html]]
---
- # HTML as LLM Output Format（HTML 作为 LLM 输出格式）
- ## 概述
  用 HTML 替代 Markdown 作为 LLM 的输出格式请求，利用 HTML/CSS/JS 的富表达能力（SVG 图表、交互组件、页内导航、可折叠区域）将 Agent 输出从线性文字墙升级为可交互信息空间。
- ## 核心论点
  - **Markdown 适合输入/token 节约**，HTML 适合**输出/信息密度**
  - GPT-4 时代 8K token 限制使 Markdown 在 token 效率上占优，如今窗口充裕，HTML 的表达力更有价值
  - Diff、调用图、流程图是**空间信息**，Markdown 把它们压扁了；HTML 能还原空间感
  - 交互和动画**只能感受，无法描述**——HTML 让 Agent 拥有真正的画笔
- ## 九大应用场景
  1. **探索与规划** — 方案并排对比、视觉方向、实现时间线
  2. **代码审查** — 带边栏标注的 diff、模块地图、PR 描述
  3. **设计系统** — 颜色 token 色板、组件变体清单
  4. **原型** — 动画参数沙盒、可点击流程原型
  5. **图表** — 内联 SVG 插图、可点击部署流程图
  6. **演示** — 单文件 HTML 幻灯片
  7. **研究学习** — 可折叠章节、标签页代码、侧栏词汇表
  8. **报告** — 带图表的周报、事件时间线
  9. **自定义编辑器** — 票据看板、Feature Flag 编辑器、Prompt 调优器
- ## 关键 Prompt 模式
  `Output HTML, neatly styled and using capabilities of HTML and CSS and JavaScript to make the explanation rich and interactive and as clear as possible.`
  `Help me review this PR by creating an HTML artifact that describes it. Render the actual diff with inline margin annotations, color-code findings by severity.`
- ## 经典案例
  - **copy.fail 安全漏洞解析** — `curl | llm -m gpt-5.5` 生成暗色主题双栏布局、高亮步骤、安全警告 callout
  - **20 个自包含 .html 示例** — Thariq Shihipar 收集在 thariqs.github.io/html-effectiveness/
- ## 与 Markdown 的对比
  | 维度 | Markdown | HTML |
  |------|----------|------|
  | Token 效率 | ✅ 更高 | ❌ 标签开销 |
  | 交互性 | ❌ 纯文本 | ✅ JS 组件 |
  | 图表/视觉 | ❌ 需外部工具 | ✅ 内联 SVG |
  | 导航结构 | ❌ 线性 | ✅ 标签页/折叠/锚点 |
  | 适用场景 | 输入/快速草稿 | 输出/深度理解 |
- ## 关联
  - [[entity/agentic-coding]] — 输出格式选择是 Agent 实践中的关键决策
  - [[entity/claude-md-files]] — Claude Code 团队成员 Thariq 的实践
  - [[entity/living-specs]] — 富 HTML 输出可被视为活的文档
  - [[entity/harness]] — HTML 编辑器模式可作为 harness 的可视化层
- ## 来源
  - [[source/unreasonable-effectiveness-of-html]] — Simon Willison 引介 + Thariq Shihipar 原始示例

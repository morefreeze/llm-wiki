# LLM Wiki 操作日志

---

## [2026-05-07] ingest | 编程智能体的核心组件（Sebastian Raschka / 宝玉译）
- 从本地 RSS Pal 数据库提取文章内容（article ID 1561）
- 添加原始资料到 `_raw/coding-agent-components.txt`
- 创建资料摘要页 `wiki/sources/coding-agent-components.md`
- 创建实体页：
  - `wiki/entities/coding-harness.md` — 编程 Agent 六大组件架构 + LLM→推理模型→Agent→Agent harness→Coding harness 层次分类
- 更新实体页：
  - `wiki/entities/harness.md` — 补充 Raschka 的 Harness 层次分类和 Coding harness 特化视角
- 更新主题页：
  - `wiki/topics/agent-efficiency.md` — 补充 Context Bloat 管理三策略（截断/摘要/去重）
- 更新 `index.md`（36 页面，12 资料，18 实体，4 主题）

## [2026-05-06] init | 创建 LLM Wiki
- 初始化仓库结构：`raw/`、`wiki/`（entities/topics/sources/synthesis/）
- 创建 `AGENTS.md`（Schema）、`index.md`、`log.md`
- 创建目录占位文件

## [2026-05-06] ingest | LLM Wiki Pattern (Karpathy)
- 添加原始资料到 `raw/442a6bf555914893e9891c11519de94f.md`
- 创建资料摘要页 `wiki/sources/llm-wiki-pattern.md`
- 待建实体：Karpathy、Memex、RAG、Obsidian
- 待建主题：持久知识管理、增量知识编译

## [2026-05-06] ingest | Code Execution with MCP (Anthropic)
- 添加原始资料到 `raw/anthropic-code-execution-with-mcp.md`
- 创建资料摘要页 `wiki/sources/anthropic-code-execution-with-mcp.md`
- 创建实体页：
  - `wiki/entities/mcp.md` — Model Context Protocol
  - `wiki/entities/code-mode.md` — Cloudflare 的代码执行模式
  - `wiki/entities/skills.md` — 可复用 Agent 能力单元
  - `wiki/entities/progressive-disclosure.md` — 渐进式发现设计模式
- 创建主题页：
  - `wiki/topics/agent-efficiency.md` — Agent 效率优化（综合两篇资料）
- 更新 `index.md`（9 页面，2 资料，4 实体，1 主题）

## [2026-05-06] ingest | LLM Wiki Pattern by Karpathy

## [2026-05-06] ingest | Building agents that reach production systems with MCP

## [2026-05-06] ingest | 从玩具到生产力：用真实项目讲透 AI Agent 的 Harness Engineering

## [2026-05-06] ingest | 当我们在讨论 Harness 的时候，我们在讨论什么

## [2026-05-07] ingest | BestBlogs 2.0 内测开启（BestBlogs 创始人）
- 从本地 RSS Pal 数据库提取文章内容（article ID 1572）
- 添加原始资料到 `_raw/bestblogs-2.0-reading-workflow.md`
- 创建资料摘要页 `wiki/sources/bestblogs-2.0-reading-workflow.md`
- 创建实体页：
  - `wiki/entities/information-filtering.md` — 内容判断能力，信息过载时代的真正稀缺资源
- 创建主题页：
  - `wiki/topics/information-workflow.md` — 从发现到复用的完整知识输入路径
- 更新 `index.md`（27 页面，8 资料，13 实体，4 主题）

## [2026-05-07] ingest | 深度拆解 Hermes Agent 的记忆系统（Manthan Gupta / 宝玉整理）
- 从本地 RSS Pal 数据库提取文章内容（article ID 1119）
- 添加原始资料到 `_raw/hermes-agent-memory-system.txt`
- 创建资料摘要页 `wiki/sources/hermes-agent-memory-system.md`
- 创建实体页：
  - `wiki/entities/agent-memory-system.md` — Agent 四层记忆架构（语义/情景/程序/用户建模）+ Prompt Cache 优化原则
- 更新实体页：
  - `wiki/entities/skills.md` — 补充 Skills 作为程序记忆（Procedural Memory）的角色
- 更新主题页：
  - `wiki/topics/agent-efficiency.md` — 补充记忆分层与 Prompt Cache 命中率作为 Agent 效率的维度
- 更新 `index.md`（34 页面，11 资料，17 实体，4 主题）

## [2026-05-07] ingest | Karpathy 最新访谈：Vibe Coding 只是开始，真正重要的是 Agentic Engineering（宝玉整理）
- 从本地 RSS Pal 数据库提取文章内容（article ID 1108）
- 添加原始资料到 `_raw/karpathy-vibe-coding-to-agentic-engineering.txt`
- 创建资料摘要页 `wiki/sources/karpathy-vibe-coding-to-agentic-engineering.md`
- 创建实体页：
  - `wiki/entities/software-3-0.md` — Software 1.0/2.0/3.0 范式框架，context window 即程序
  - `wiki/entities/vibe-coding.md` — Vibe Coding vs Agentic Engineering：下限/上限区分，规格是人的工作
- 更新实体页：
  - `wiki/entities/agentic-coding.md` — 补充 Karpathy 的锯齿状智能、Vibe Coding/Agentic Engineering 分层、规格所有权
- 更新主题页：
  - `wiki/topics/agentic-developer-practices.md` — 补充 Karpathy 框架（规格所有权、锯齿状智能、AI-native 面试标准）
- 更新 `index.md`（32 页面，10 资料，16 实体，4 主题）

## [2026-05-06] ingest | Harness 不是目的，知识才是护城河（stevenpxiao）
- 从本地 RSS Pal 数据库提取文章内容（article ID 1597）
- 添加原始资料到 `_raw/harness-knowledge-moat.txt`
- 创建资料摘要页 `wiki/sources/harness-knowledge-moat.md`
- 创建实体页：
  - `wiki/entities/knowledge-lifecycle.md` — 五层存储 × 五种类型 × 三级成熟度 + 自动衰减的团队知识架构
- 更新实体页：
  - `wiki/entities/harness.md` — 补充"知识作为 Harness 核心组成"视角，Harness 三支柱与知识管理的关系
- 更新主题页：
  - `wiki/topics/agent-production.md` — 补充知识层作为 Agent 生产化完整路径的第三层
- 更新 `index.md`（29 页面，9 资料，14 实体，4 主题）

## [2026-05-06] ingest | How Anthropic Teams Use Claude Code (Anthropic PDF)
- 添加原始资料到 `_raw/how-anthropic-teams-use-claude-code.md`（从 PDF 提取）
- 创建资料摘要页 `wiki/sources/how-anthropic-teams-use-claude-code.md`
- 创建实体页：
  - `wiki/entities/claude-md-files.md` — 持久化 Agent 上下文的 Markdown 文件
  - `wiki/entities/checkpoint-workflow.md` — 频繁提交检查点的 Agent 协作安全网
- 更新主题页：
  - `wiki/topics/agentic-developer-practices.md` — 补充 Anthropic 内部案例和量化数据
- 更新 `index.md`（23 页面，7 资料，12 实体，3 主题）

## [2026-05-06] ingest | 10 Lessons for Agentic Coding (D. Breunig)
- 添加原始资料到 `_raw/10-lessons-for-agentic-coding.md`
- 创建资料摘要页 `wiki/sources/10-lessons-for-agentic-coding.md`
- 创建实体页：
  - `wiki/entities/agentic-coding.md` — Agentic coding 开发范式
  - `wiki/entities/living-specs.md` — 活规格文档实践
- 创建主题页：
  - `wiki/topics/agentic-developer-practices.md` — 代码廉价时代开发者工作方式
- 更新 `index.md`（19 页面，6 资料，10 实体，3 主题）

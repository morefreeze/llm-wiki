# LLM Wiki 操作日志

---

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

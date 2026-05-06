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

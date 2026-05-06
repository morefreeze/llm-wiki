---
type:: Index
updated:: [[2026-05-06]]
---

# LLM Wiki Index

> 📊 **15 pages** | 5 sources · 8 entities · 2 topics

---

## 📚 Sources（资料）

| 页面 | 一句话 | 来源 |
|------|--------|------|
| [[llm-wiki-pattern]] | 用 LLM 增量构建持久知识库的模式 | Karpathy Gist |
| [[anthropic-code-execution-with-mcp]] | 通过代码执行调用 MCP，token 消耗降 98.7% | Anthropic Blog |
| [[building-agents-that-reach-production-systems-with-mcp]] | 三种 Agent 连接方式对比，MCP 成为生产标准 | Anthropic Blog |
| [[从玩具到生产力用真实项目讲透-ai-agent-的-harness-engineering]] | Harness 层将 Agent 从玩具提升到生产力 | BestBlogs |
| [[当我们在讨论-harness-的时候我们在讨论什么]] | MiniMax × Hermes Agent 关于 Harness 的深度对谈 | BestBlogs |

## 🧩 Entities（实体）

| 页面 | 类型 | 核心定义 |
|------|------|----------|
| [[mcp]] | Protocol | Model Context Protocol，Agent 连接外部系统的开放标准 |
| [[code-mode]] | Pattern | Agent 通过编写代码（非直接调用）与 MCP 交互 |
| [[skills]] | Concept | 可复用的 Agent 能力单元（指令 + 脚本 + 资源） |
| [[progressive-disclosure]] | Pattern | 按需发现和加载工具定义的设计模式 |
| [[harness]] | Concept | Agent 驾驭层——安全带 + 方向盘 |
| [[tool-search]] | Pattern | 运行时按需搜索工具目录，token 减少 85%+ |
| [[mcp-apps]] | Extension | MCP 首个官方扩展，返回交互式界面 |
| [[elicitation]] | Feature | MCP server 中途暂停请求用户输入 |

## 🌐 Topics（主题）

| 页面 | 核心问题 | 涉及实体 |
|------|---------|----------|
| [[agent-efficiency]] | Agent 规模化后 token 和效率挑战 | [[code-mode]] [[progressive-disclosure]] [[tool-search]] |
| [[agent-production]] | Agent 从玩具到生产化的路径 | [[mcp]] [[harness]] [[skills]] [[plugin]] |

## 📊 Stats

- Sources: 5
- Entities: 8
- Topics: 2
- Synthesis: 0

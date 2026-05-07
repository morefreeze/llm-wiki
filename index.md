---
type:: Index
updated:: [[2026-05-06]]
---

# LLM Wiki Index

> 📊 **29 pages** | 9 sources · 14 entities · 4 topics

---

## 📚 Sources（资料）

| 页面 | 一句话 | 来源 |
|------|--------|------|
| [[llm-wiki-pattern]] | 用 LLM 增量构建持久知识库的模式 | Karpathy Gist |
| [[anthropic-code-execution-with-mcp]] | 通过代码执行调用 MCP，token 消耗降 98.7% | Anthropic Blog |
| [[building-agents-that-reach-production-systems-with-mcp]] | 三种 Agent 连接方式对比，MCP 成为生产标准 | Anthropic Blog |
| [[从玩具到生产力用真实项目讲透-ai-agent-的-harness-engineering]] | Harness 层将 Agent 从玩具提升到生产力 | BestBlogs |
| [[当我们在讨论-harness-的时候我们在讨论什么]] | MiniMax × Hermes Agent 关于 Harness 的深度对谈 | BestBlogs |
| [[10-lessons-for-agentic-coding]] | 代码廉价时代开发者的 10 条实践原则 | dbreunig.com |
| [[how-anthropic-teams-use-claude-code]] | Anthropic 10 个内部团队的 Claude Code 实战报告 | Anthropic PDF |
| [[bestblogs-2.0-reading-workflow]] | 内容判断才是稀缺资源，BestBlogs 转型为阅读工作流工具 | BestBlogs |
| [[harness-knowledge-moat]] | Harness 不是目的，知识才是护城河——AI 工程团队的知识沉淀实践 | BestBlogs |

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
| [[agentic-coding]] | Concept | 使用 AI Agent 辅助编码的开发范式，经验被放大 |
| [[living-specs]] | Practice | 随实现持续演进的活规格文档 |
| [[claude-md-files]] | Practice | 持久化 Agent 上下文的 Markdown 文件，持续改进飞轮 |
| [[checkpoint-workflow]] | Practice | 频繁提交 Git 检查点、失败时回滚的 Agent 协作安全网 |
| [[information-filtering]] | Concept | 内容判断能力——信息过载时代真正稀缺的资源 |
| [[knowledge-lifecycle]] | Concept | 五层存储 × 五种类型 × 三级成熟度 + 自动衰减的团队知识架构 |

## 🌐 Topics（主题）

| 页面 | 核心问题 | 涉及实体 |
|------|---------|----------|
| [[agent-efficiency]] | Agent 规模化后 token 和效率挑战 | [[code-mode]] [[progressive-disclosure]] [[tool-search]] |
| [[agent-production]] | Agent 从玩具到生产化的路径 | [[mcp]] [[harness]] [[skills]] |
| [[agentic-developer-practices]] | 代码廉价时代开发者如何调整工作方式 | [[agentic-coding]] [[living-specs]] [[claude-md-files]] [[checkpoint-workflow]] |
| [[information-workflow]] | 从发现到复用的完整知识输入路径 | [[information-filtering]] [[llm-wiki-pattern]] |

## 📊 Stats

- Sources: 9
- Entities: 14
- Topics: 4
- Synthesis: 0

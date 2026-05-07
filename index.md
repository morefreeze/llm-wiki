---
type:: Index
updated:: [[2026-05-07]]
---

# LLM Wiki Index

> 📊 **56 pages** | 23 sources · 27 entities · 4 topics

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
| [[karpathy-vibe-coding-to-agentic-engineering]] | Vibe Coding 只是开始，真正重要的是 Agentic Engineering | baoyu.io |
| [[hermes-agent-memory-system]] | Hermes Agent 四层记忆架构：冷热分离 + 缓存优先 + 程序记忆 | baoyu.io |
| [[coding-agent-components]] | 编程 Agent 六大核心组件：Harness 比模型更重要 | baoyu.io |
| [[harness-what-it-actually-is]] | 五子系统模型（厨房类比）+ 4 阶段实验，成功率 20%→100% | walkinglabs.github.io |
| [[repo-as-system-of-record]] | 仓库即规范：知识可见性缺口 + 冷启动测试 + 知识衰减率 20%/月 | walkinglabs.github.io |
| [[instruction-file-architecture]] | 路由文件 + 渐进式披露：600 行 AGENTS.md → 80 行路由文件，成功率 45%→72% | walkinglabs.github.io |
| [[session-continuity-across-sessions]] | PROGRESS.md + DECISIONS.md：重建时间从 15 分钟降到 3 分钟（78%降低） | walkinglabs.github.io |
| [[initialization-independent-phase]] | 自举契约四条件：独立初始化让多会话功能完成率高 31% | walkinglabs.github.io |
| [[wip-limit-task-boundaries]] | WIP=1：少做但做完，完成率 87.5% vs 37.5%，代码行数与功能呈负相关 | walkinglabs.github.io |
| [[feature-list-as-harness-primitive]] | 功能清单三元组是 harness 脊梁骨，完成率高 45%，诊断时间降 60-80% | walkinglabs.github.io |
| [[prevent-premature-completion]] | 置信度校准偏差（Guo 2017）+ 三层终止校验 + 三 agent 架构（$9 不可用 vs $200 可用） | walkinglabs.github.io |
| [[e2e-testing-changes-results]] | E2E 测试不仅改变结果还改变 agent 编码行为 + 架构边界执行规则 | walkinglabs.github.io |
| [[harness-observability]] | 双层可观测性 + 冲刺合同 + Anthropic 三 agent 实验（3h50m，$124.70） | walkinglabs.github.io |
| [[clean-session-state]] | 清洁状态五维度 + 12 周熵增数据 + harness 简化原则（Lehman 定律） | walkinglabs.github.io |

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
| [[software-3-0]] | Paradigm | LLM 作为新的可编程计算机，context window 作为程序 |
| [[vibe-coding]] | Practice | 凭感觉编程（Karpathy 提出）vs Agentic Engineering 的下限/上限区分 |
| [[agent-memory-system]] | Architecture | Agent 四层记忆架构：语义/情景/程序/用户建模 + Prompt Cache 优化 |
| [[coding-harness]] | Architecture | 编程运行框架六大组件：仓库上下文/缓存复用/工具/瘦身/记忆/子 Agent |
| [[harness-5-subsystems]] | Model | 五子系统（指令/工具/环境/状态/反馈）+ 厨房类比 + 成功率 20%→100% |
| [[repo-as-system-of-record]] | Principle | 仓库即规范：知识可见性缺口 + 冷启动测试 + ACID 状态管理 |
| [[instruction-architecture]] | Pattern | 路由文件 + 渐进式披露：防止指令膨胀，中间迷失效应（Liu 2023） |
| [[session-continuity]] | Practice | 跨会话连续性工件 + 自举契约 + 上下文焦虑 + 漂移 |
| [[wip-limit]] | Practice | WIP=1 + Overreach/Under-finish + VCR + 完成证据 |
| [[feature-list-primitive]] | Pattern | 功能清单三元组（行为/验证/状态）+ 通过状态门控 + 状态机模型 |
| [[completion-validation]] | Practice | 三层终止校验 + E2E 测试 + Planner/Generator/Evaluator 架构 |
| [[harness-observability]] | Pattern | 双层可观测性（运行时+过程）+ 冲刺合同 + 任务轨迹 |
| [[clean-session-state]] | Practice | 清洁状态五维度 + 会话完整性 + 质量文档 + 幂等清理 |

## 🌐 Topics（主题）

| 页面 | 核心问题 | 涉及实体 |
|------|---------|----------|
| [[agent-efficiency]] | Agent 规模化后 token 和效率挑战 | [[code-mode]] [[progressive-disclosure]] [[tool-search]] |
| [[agent-production]] | Agent 从玩具到生产化的路径 | [[mcp]] [[harness]] [[harness-5-subsystems]] [[session-continuity]] [[clean-session-state]] |
| [[agentic-developer-practices]] | 代码廉价时代开发者如何调整工作方式 | [[agentic-coding]] [[wip-limit]] [[completion-validation]] [[feature-list-primitive]] [[session-continuity]] |
| [[information-workflow]] | 从发现到复用的完整知识输入路径 | [[information-filtering]] [[llm-wiki-pattern]] |

## 📊 Stats

- Sources: 23
- Entities: 27
- Topics: 4
- Synthesis: 0

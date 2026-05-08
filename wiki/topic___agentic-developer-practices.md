---
type:: Topic
tags:: #agent #developer-workflow #coding #practices
created:: [[2026-05-06]]
sources:: [[source/10-lessons-for-agentic-coding]] [[source/how-anthropic-teams-use-claude-code]] [[source/karpathy-vibe-coding-to-agentic-engineering]] [[source/wip-limit-task-boundaries]] [[source/feature-list-as-harness-primitive]] [[source/prevent-premature-completion]] [[source/e2e-testing-changes-results]] [[source/session-continuity-across-sessions]] [[source/initialization-independent-phase]]
---

# Agentic 开发者实践

## 核心问题
当 AI Agent 让代码生成变得廉价，开发者应如何调整工作方式以最大化价值？

## 核心观点

> "代码廉价，但维护、支持和安全不廉价。"

Agent 时代的开发者不再是代码生产者，而是**判断者、引导者、架构师**。经验和品味的价值被放大，而非降低。

## 实践框架

### 🔄 开发节奏
| 实践 | 传统做法 | Agent 时代 |
|------|---------|-----------|
| 实现 | 谨慎，成本高 | 大胆实验，频繁重建 |
| 测试 | 单元测试为主 | 端到端测试优先 |
| 规格 | 项目前固定 | 随实现持续更新（[[entity/living-specs]]） |
| 文档 | 意图记在脑子里 | [[entity/claude-md-files]] 持久化 |
| 版本控制 | 里程碑提交 | [[entity/checkpoint-workflow]]：频繁提交、失败回滚 |

### 🎯 精力分配
- **自动化**：所有简单、重复的任务（批量广告创意、测试生成、重构）
- **聚焦**：设计决策、性能优化、安全架构——真正难的问题
- **培养**：领域专业知识和用户理解（"品味"）

### 🧠 与 Agent 协作模式

**任务分类（来自 Anthropic 内部实践）：**
| 任务类型 | 策略 |
|---------|------|
| 外围功能/原型 | auto-accept 模式，失败就 rollback |
| 核心业务逻辑 | 同步监督，给详细 prompt，实时检查 |
| 陌生代码库 | 让 Claude 先说，再提问 |
| 复杂重构 | Slot machine：commit → 30分钟 → 接受/重来 |

**经验放大效应：**
- 技术深度越高，Agent 使用效率越高（Anthropic 工程师的普遍观察）
- 能更精准提示、更快识别错误、更有效引导方向
- 但非技术人员同样受益——法务、市场、设计师都能构建生产级工具

### 📋 工作流建议
1. **在 Claude.ai 规划，在 Claude Code 实现** — 先用对话界面思考清楚
2. **写好 [[entity/claude-md-files]]** — 记录工作流、工具、约定、注意事项
3. **Treat as iterative partner** — 不要期望一次性完美解决，迭代协作
4. **从最少信息开始** — 让 Claude 引导你，而非前置大量解释

## 跨职能扩展（非技术团队的 Agentic Coding）
Anthropic 内部的显著发现：**非开发者也能受益**
- 法务团队：1小时构建无障碍辅助应用
- 市场团队：构建 Figma 插件和 MCP server
- 产品设计师：直接实现 state management 修改

关键：让非技术用户在 Claude.md 中说明自己的背景（"我是设计师，需要详细解释"），Agent 会调整响应风格。

## 量化参考数据（来自 Anthropic）
| 场景 | 提升 |
|------|------|
| 基础设施调试 | 15分钟 → 5分钟 |
| 广告文案制作 | 2小时 → 15分钟 |
| 数据科学重构 | 2-4x 提速 |
| ML 概念研究 | 80% 时间节省 |
| 复杂产品上线 | 一周协调 → 两次30分钟通话 |

## 与其他主题的关系
| 主题 | 关联 |
|------|------|
| [[topic/agent-efficiency]] | token/工具层面的效率 vs 开发者工作流效率，互补视角 |
| [[topic/agent-production]] | 生产化基础设施（[[entity/harness]]、[[entity/mcp]]）是开发者实践的运行环境 |

## Karpathy 的关键补充（2026 年 4 月）

[[source/karpathy-vibe-coding-to-agentic-engineering]] 对这个主题做了几个重要补充：

**Vibe Coding vs Agentic Engineering 的清晰区分：**
- Vibe Coding：抬高所有人做软件的下限（入口变宽）
- Agentic Engineering：保住专业软件的质量上限（不妥协）

**规格是人最重要的工作：**
> "细节可以外包，理解不能外包。"

Agent 可以记 API 细节，但人必须理解系统结构（身份归属、内存布局、架构边界）。否则 Agent 会写出"能跑但设计错误"的代码（如用 Stripe 邮箱关联 Google 用户的支付记录）。

**锯齿状智能（Jagged Intelligence）的实践含义：**
不能因为 Agent 在代码上很强就假设它在所有工程判断上都强。更准确的做法：探索 Agent 的能力边界，知道哪些任务在训练覆盖的"能力高峰"里，哪些在"断崖"旁边。

**AI-native 工程师的面试标准（新视角）：**
- 旧标准：算法题（测不出 Agentic Engineering 能力）
- 新标准：大项目（如做一个完整的 Twitter clone）+ 红队攻击（用多个 Agent 去攻击候选人做的系统）

## Harness Engineering 课程的补充实践

Learn Harness Engineering 课程对几个关键实践进行了系统化和数据化：

**任务边界控制（[[entity/wip-limit]]）：** WIP=1 是 agent harness 的默认安全设置。Anthropic 数据：使用"小下一步"策略的 agent，任务完成率比宽泛提示高 37%。代码行数和功能完成率呈弱负相关——写得越多，完成得越少。

**完成校验（[[entity/completion-validation]]）：** Agent 系统性地过度自信（Guo et al. 2017）。三层终止校验（静态分析→运行时行为→系统级 E2E）缺一不可。E2E 测试不仅改变检测结果，还改变 agent 的编码行为。Planner+Generator+Evaluator 三 agent 架构（$200/6h）vs 单 agent 裸跑（$9/20min）——功能是否可用天壤之别。

**功能清单原语（[[entity/feature-list-primitive]]）：** 功能清单是 harness 的脊梁骨（行为描述/验证命令/当前状态三元组），减少 60-80% 的会话启动诊断时间，功能完成率比自由形式高 45%。

**跨会话连续性（[[entity/session-continuity]]）：** 独立初始化阶段（自举契约四条件）+ 连续性工件（PROGRESS.md + DECISIONS.md）把重建成本从 15 分钟降到 3 分钟。

## 开放问题
- 随着 Agent 能力提升，"品味"和"经验"的优势会持续多久？（Karpathy 承认：这取决于实验室是否把审美纳入 RL 训练目标）
- 端到端测试能否完全替代单元测试，还是两者需要平衡？
- 非技术人员的 agentic coding 采用会改变软件团队的组织结构吗？
- Agent-first 基础设施何时出现第一波收敛？（文档、部署、auth、payments 为 Agent 重写）

## 参见
- [[entity/agentic-coding]] — 核心概念
- [[entity/living-specs]] — 活规格文档实践
- [[entity/claude-md-files]] — 持久化上下文文件
- [[entity/checkpoint-workflow]] — Agent 安全网
- [[entity/harness]] — 生产化约束层
- [[topic/agent-efficiency]] — 效率优化主题

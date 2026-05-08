---
type:: Topic
tags:: #agent #production #mcp #safety #knowledge
created:: [[2026-05-06]]
sources:: [[source/building-agents-that-reach-production-systems-with-mcp]] [[source/从玩具到生产力用真实项目讲透-ai-agent-的-harness-engineering]] [[source/当我们在讨论-harness-的时候我们在讨论什么]] [[source/harness-knowledge-moat]] [[source/harness-what-it-actually-is]] [[source/why-repo-is-system-of-record]] [[source/why-sessions-must-leave-clean-state]]
---

# Agent 生产化

## 核心问题
Agent 从「玩具」到「生产」需要解决三个关键问题：
- **连接性**：Agent 如何可靠地连接外部系统
- **安全性**：Agent 如何安全地使用能力而不失控
- **可扩展性**：集成如何从 1 对 1 扩展到 M 对 N

## 连接方式演进

| 方式 | 适用场景 | 局限 | 规模化 |
|------|---------|------|--------|
| 直接 API 调用 | 小规模、一次性集成 | M×N 问题 | ❌ |
| CLI | 本地环境、沙箱容器 | 无法覆盖 Web/移动/云 | ⚠️ |
| [[entity/mcp]] | 云端 Agent、跨平台 | 前期投入稍大 | ✅ |

## 生产级 MCP Server 设计模式
1. **构建远程 Server** — 获得最大分发覆盖
2. **按意图分组工具** — 而非按端点 1:1 镜像 API
3. **代码编排** — 大 API 表面用代码沙箱（如 Cloudflare 2 工具覆盖 2500 端点）
4. **富语义交付** — [[entity/mcp-apps]]（交互界面）、[[entity/elicitation]]（用户输入）
5. **标准化认证** — OAuth + CIMD + Vaults

## Harness：从玩具到生产力的关键
- [[entity/harness]] 是 Agent 的安全约束与引导层
- 不是框架，而是「安全带 + 方向盘」
- 五大组件：输入验证、输出过滤、权限控制、错误处理、日志记录
- 与 [[entity/mcp]] 的认证和权限机制互补

## 生态规模
- MCP SDK 下载量：3 亿次/月（2026 年 4 月）
- Claude MCP 目录：200+ 个 server
- 兼容客户端：Claude、ChatGPT、Cursor、VS Code 等

## 知识作为生产化的真正护城河

[[source/harness-knowledge-moat]] 补充了生产化路径上被低估的一层：

> **Harness 不是目的，知识才是护城河。**

工作流是可替换的（今天 16 阶段状态机，明天图结构 DAG），但团队积累的领域知识是永恒有价值的。没有知识闭环的 Agent 工作流是"一次性"的——每次都从零开始，每次都踩同样的坑。

生产化 Agent 系统的完整路径：
1. **连接层**（[[entity/mcp]] / MCP Server）— Agent 如何可靠连接外部系统
2. **驾驭层**（[[entity/harness]]）— Agent 如何安全、可控地使用能力
3. **知识层**（[[entity/knowledge-lifecycle]]）— 每次交付如何自动沉淀知识，让系统越用越聪明

Big Model vs Big Harness 的务实立场：知识工程的投入是**确定性回报**（每条 proven 知识让所有后续工作流受益），模型提升是概率性回报（不知道下一代模型在你的特定场景上是否更好）。

## Harness Engineering 课程：生产化的系统化路径

[[entity/harness-5-subsystems]] 把 Harness 拆解为五个可检查的子系统，并给出了量化数据（成功率 20%→100%）。生产化路径上的关键实践：

- **[[entity/repo-as-system-of-record]]**：仓库即规范——知识可见性缺口 + 冷启动测试（5问判断仓库质量）+ 知识衰减率（20%/月），人工介入降低 60%
- **[[entity/session-continuity]]**：跨会话连续性——PROGRESS.md + DECISIONS.md + 上下文焦虑 + 漂移，重建时间从 15 分钟降到 3 分钟（78%降低）
- **[[entity/clean-session-state]]**：清洁状态五维度——12 周熵增数据（构建从 100% 降到 68%）+ 双模式清理策略 + harness 简化原则
- **[[entity/harness-observability]]**：可观测性——双层（运行时+过程）+ 冲刺合同 + Anthropic 三 agent 实验（3h50m，$124.70）

## 参见
- [[entity/mcp]] — Model Context Protocol
- [[entity/harness]] — Agent 驾驭层
- [[entity/harness-5-subsystems]] — 五子系统模型（指令/工具/环境/状态/反馈）
- [[entity/knowledge-lifecycle]] — 五层 × 五型 × 三级成熟度知识架构
- [[entity/skills]] — 可复用能力
- [[plugin]] — Skills + MCP 打包
- [[topic/agent-efficiency]] — Agent 效率优化
- [[entity/tool-search]] — 按需工具发现

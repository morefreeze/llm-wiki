---
type:: Entity
tags:: #agent #coding #developer-workflow
created:: [[2026-05-06]]
sources:: [[10-lessons-for-agentic-coding]], [[karpathy-vibe-coding-to-agentic-engineering]]
---

# Agentic Coding（智能体编码）

## 概述
使用 AI Agent（如 Claude Code、Codex）辅助或主导代码生成的开发范式。代码生成成本趋近于零，开发者角色从"写代码"转变为"引导、判断、维护"。

## 核心特征
- **代码廉价** — Agent 可以快速生成大量代码，实验成本极低
- **经验放大** — 有经验的开发者能更好地提示 Agent、识别错误、做出判断，效率被成倍放大
- **重建友好** — 低成本使频繁重构和推倒重来成为合理策略

## 关键实践
- **端到端测试** — 测试行为结果而非实现细节，为 Agent 重构保留空间
- **[[living-specs]]** — 规格文档随实现持续同步更新
- **意图文档** — 记录决策背后的原因，维持 Agent 和开发者的方向一致
- **寻找难题** — 把精力集中在设计、性能、安全等真正创造价值的挑战上

## 隐性成本
> "代码廉价，但维护、支持和安全不廉价。"

快速生成的代码积累的隐患：
- 技术债和维护负担
- 安全漏洞风险
- 超出支持能力的产品规模

## 关联
- [[harness]] — Agent 的生产化约束层，与 agentic coding 的工程基础互补
- [[skills]] — 可复用的 Agent 能力单元，提升编码效率
- [[living-specs]] — Agentic coding 的核心文档实践
- [[agent-efficiency]] — Token 和工具层面的效率优化

## Karpathy 的补充框架

[[karpathy-vibe-coding-to-agentic-engineering]] 对 agentic coding 做了重要分层：

- **[[vibe-coding]]**（Karpathy 2025 年提出）：完全放手让模型主导，适合探索性开发和 side project，抬高创作下限
- **Agentic Engineering**：在使用 Agent 加速的同时，保住专业软件的质量、安全、责任上限

两者的核心区别：是否坚守**规格（spec）是人的工作**这一原则。Agent 填补实现细节，人负责系统边界、数据归属、质量标准。

**锯齿状智能（Jagged Intelligence）** 是 agentic coding 的重要背景：LLM 能力曲线不是平滑上升，而是有高峰（RL 覆盖的可验证领域）和断崖（训练分布外）。开发者需要探索 Agent 的能力边界，知道哪些任务在高峰里，哪些在断崖旁边。

## 关联
- [[harness]] — Agent 的生产化约束层，与 agentic coding 的工程基础互补
- [[skills]] — 可复用的 Agent 能力单元，提升编码效率
- [[living-specs]] — Agentic coding 的核心文档实践
- [[agent-efficiency]] — Token 和工具层面的效率优化
- [[vibe-coding]] — Agentic coding 的两种形态：探索性的 Vibe Coding 与专业的 Agentic Engineering
- [[software-3-0]] — Agentic coding 的范式背景

## 来源
- [[10-lessons-for-agentic-coding]] — 10 条开发者实践原则
- [[karpathy-vibe-coding-to-agentic-engineering]] — Karpathy 的 Vibe Coding vs Agentic Engineering 框架、锯齿状智能、规格所有权

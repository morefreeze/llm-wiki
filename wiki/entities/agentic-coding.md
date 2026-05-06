---
type:: Entity
tags:: #agent #coding #developer-workflow
created:: [[2026-05-06]]
sources:: [[10-lessons-for-agentic-coding]]
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

## 来源
- [[10-lessons-for-agentic-coding]] — 10 条开发者实践原则

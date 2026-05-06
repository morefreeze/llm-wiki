---
type:: Entity
tags:: #agent #developer-workflow #git #safety
created:: [[2026-05-06]]
sources:: [[how-anthropic-teams-use-claude-code]] [[10-lessons-for-agentic-coding]]
---

# Checkpoint Workflow（检查点工作流）

## 概述
与 AI Agent 协作时，**频繁提交 Git checkpoint**，Agent 实验失败时直接回滚，而不是试图修复错误。是 [[agentic-coding]] 中管理 Agent 自主工作风险的核心实践。

## 核心思路
> "commit your work as you go" — Security Engineering team

Agent 工作时可能走偏。与其在错误上反复修补，不如：
1. **提交当前状态** → 让 Agent 自主工作
2. **验证结果** → 接受（约1/3成功率）或直接回滚
3. **失败则重来** — 重新开始通常比修复更高效

## "Slot Machine" 策略
Data Science & ML Engineering 团队的比喻：
- 保存状态 → 让 Claude 工作 30 分钟 → 接受结果 or 重新开始
- "Starting over often has a higher success rate than trying to fix Claude's mistakes"

## 适用场景
| 场景 | 策略 |
|------|------|
| 外围功能/原型 | auto-accept + checkpoint，失败就 reset |
| 核心业务逻辑 | 同步监督 + 小步 checkpoint |
| 复杂重构 | commit 初始状态 → 实验 → 接受 or 回滚 |
| 陌生代码库任务 | 完全委托 + checkpoint 兜底 |

## 与 RL Engineering 的实践
- 使用 "try and rollback" 方法论
- 频繁提交使实验性开发成为可能，无需担心破坏稳定代码

## 关联
- [[agentic-coding]] — Checkpoint 工作流是 agentic coding 的安全网
- [[claude-md-files]] — Claude.md 中写入 checkpoint 指令（"commit as you go"）
- [[living-specs]] — 每次 session 结束时更新规格，形成闭环

## 来源
- [[how-anthropic-teams-use-claude-code]] — RL Engineering、Data Science、Security Engineering 三个团队的共同实践
- [[10-lessons-for-agentic-coding]] — "Rebuild Often" 原则的底层支撑

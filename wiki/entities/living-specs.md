---
type:: Entity
tags:: #developer-workflow #documentation #specs
created:: [[2026-05-06]]
sources:: [[10-lessons-for-agentic-coding]]
---

# Living Specs（活规格文档）

## 概述
在 [[agentic-coding]] 范式下，将规格说明文档作为**随实现持续演进的活文档**，而非项目开始前固定的需求文档。

## 核心理念
- 传统规格文档：项目开始前写好，之后基本不变
- 活规格文档：实现过程中不断更新，捕获新的学习和决策

## 为什么重要
1. **实现会暴露遗漏** — 写代码时会发现规格中未考虑的决策
2. **给 Agent 的指令** — Agent 每次任务都需要上下文，活文档是最好的 prompt 素材
3. **团队共同记忆** — 记录"为什么这样做"，不只是"做了什么"
4. **持续对齐** — 开发者和 Agent 始终基于最新规格工作

## 实践方式
- 每次重要实现决策后更新规格
- 在规格旁记录意图（Document Intent）：不只记录 what，还记录 why
- 把规格和代码一起提交到版本控制

## 关联
- [[agentic-coding]] — 活规格文档是 agentic coding 的核心实践
- [[harness]] — Harness 工程中同样需要文档驱动的上下文管理

## 来源
- [[10-lessons-for-agentic-coding]] — Lesson 4 (Document Intent) + Lesson 5 (Keep Specs Synchronized)

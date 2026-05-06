---
type:: Entity
tags:: #agent #developer-workflow #documentation #context
created:: [[2026-05-06]]
sources:: [[how-anthropic-teams-use-claude-code]] [[10-lessons-for-agentic-coding]]
---

# Claude.md Files（上下文记忆文件）

## 概述
放在代码库根目录（或子目录）的 Markdown 文件，用于向 AI Agent 提供持久化上下文：工作流程、工具约定、代码风格、注意事项等。Agent 每次启动或执行任务时读取，是 [[living-specs]] 最具体的实现形式。

## 作用
- **持久化上下文** — Agent 无需每次从零开始，直接继承团队约定
- **约束行为** — 防止重复错误（如"不要 cd，直接用绝对路径"）
- **跨人员共享** — 团队最佳实践的共同载体
- **持续改进飞轮** — 每次 session 结束后让 Agent 建议改进点，写回文件

## Anthropic 内部实践
- **Data Infrastructure**：记录 workflows、tools、expectations；详细程度决定 Claude Code 表现质量
- **RL Engineering**：添加 "run pytest not run; don't cd unnecessarily" 等具体指令，显著提升一致性
- **Product Design**：写入"我是设计师、需要详细解释和小步修改"，让 Agent 调整响应风格

## 最佳内容
```markdown
# 项目名称

## 工作流
- 如何运行测试：pytest not python -m pytest
- 如何构建：make build

## 约定
- 路径：使用绝对路径，不要 cd
- 提交：每个小功能提交一次 checkpoint

## 上下文
- 代码库结构说明
- 重要模式和反模式
```

## 与相关概念的关系
- [[living-specs]] — Claude.md 文件是 living specs 的核心载体
- [[agentic-coding]] — Claude.md 是 agentic coding 的基础设施
- [[harness]] — Harness 工程中的 CLAUDE.md/AGENTS.md 是 harness 约束层的文档部分
- [[checkpoint-workflow]] — 常在 Claude.md 中写入 checkpoint 指令

## 来源
- [[how-anthropic-teams-use-claude-code]] — Anthropic 10 个团队的实践
- [[10-lessons-for-agentic-coding]] — "Document Intent" + "Keep Specs Synchronized" 两条原则

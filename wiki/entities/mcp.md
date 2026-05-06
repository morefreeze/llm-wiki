---
type:: Entity
tags:: #protocol #agent #tools
created:: [[2026-05-06]]
sources:: [[anthropic-code-execution-with-mcp]]
---

- # MCP (Model Context Protocol)
- ## 概述
  MCP 是一个开放标准，用于将 AI Agent 连接到外部系统（工具、数据源）。开发者只需实现一次 MCP，即可接入整个集成生态。
- ## 关键信息
- **发布时间**：2024 年 11 月（由 Anthropic 发布）
- **核心价值**：统一协议替代碎片化的定制集成
- **生态系统**：数千个 MCP server、所有主要语言的 SDK
- **行业地位**：已成为 Agent 连接工具/数据的事实标准
- ## 当前挑战
- 工具数量增长后，定义加载消耗大量 token
- 中间结果反复经过模型上下文
- → 参见 [[code-mode]] 的解决方案
- ## 扩展模式
  1. **直接工具调用**（传统）：所有定义加载到 context，结果经过模型
  2. **代码执行**（Code Mode）：工具作为代码 API，Agent 写代码调用，参见 [[anthropic-code-execution-with-mcp]]
- ## 关联
- [[code-mode]] — 高效使用 MCP 的方式
- [[skills]] — 基于代码执行的能力积累
- [[anthropic-code-execution-with-mcp]] — Anthropic 工程博客
- [[llm-wiki-pattern]] — Karpathy 的 LLM 知识管理模式（MCP 可作为工具层）
- ## 来源
- [[anthropic-code-execution-with-mcp]] — Anthropic 工程博客
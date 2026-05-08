---
type:: Entity
tags:: #protocol #agent #tools
created:: [[2026-05-06]]
sources:: [[source/anthropic-code-execution-with-mcp]] [[source/mcp-introduction-stytch]] [[source/apis-dont-make-good-mcp-tools]] [[source/writing-tools-for-agents]]
---

- # MCP (Model Context Protocol)
- ## 概述
  MCP 是一个开放标准，用于将 AI Agent 连接到外部系统（工具、数据源）。开发者只需实现一次 MCP，即可接入整个集成生态。

  > **USB-C 类比**：就像 USB-C 统一了设备连接，MCP 统一了 AI 与工具的连接。

- ## 关键信息
- **发布时间**：2024 年 11 月（由 Anthropic 发布）
- **核心价值**：统一协议替代碎片化的定制集成
- **生态系统**：数千个 MCP server、所有主要语言的 SDK
- **行业地位**：已成为 Agent 连接工具/数据的事实标准
- **传输协议**：JSON-RPC 2.0（支持 stdio、HTTP/SSE、Cloudflare Workers）
- **认证机制**：OAuth 2.0（Dynamic Client Registration + 作用域 token + 多用户云支持）

- ## 三类交互原语
  1. **Tools**：模型可执行的动作（函数调用）
  2. **Resources**：模型可读取的数据（文件、数据库记录）
  3. **Prompts**：预定义的提示模板，可参数化

- ## 当前挑战
- 工具数量增长后，定义加载消耗大量 token
- 中间结果反复经过模型上下文
- → 参见 [[entity/code-mode]] 的解决方案

- ## 扩展模式
  1. **直接工具调用**（传统）：所有定义加载到 context，结果经过模型
  2. **代码执行**（Code Mode）：工具作为代码 API，Agent 写代码调用，参见 [[source/anthropic-code-execution-with-mcp]]

- ## MCP vs 其他集成方案
  | 方案 | 特点 | 问题 |
  |------|------|------|
  | ChatGPT Plugins | 平台锁定，单一供应商 | 只限 OpenAI |
  | LangChain Tools | Python 代码耦合 | 非通用协议 |
  | OpenAI Function Calling | 强类型，文档好 | 无标准生态 |
  | **MCP** | 开放标准，跨语言跨平台 | 工具过多时 token 膨胀 |

- ## MCP 工具设计陷阱
  直接将 REST API 转化为 MCP 工具效果很差（[[source/apis-dont-make-good-mcp-tools]]）：
- **Tool Count 爆炸**：VS Code 限制 128 个工具，认知负载远在此之前崩溃
- **Context 宽度问题**：100 条记录 × 50 个字段 = 大量 token 浪费
- **缺乏 Agent 能力**：原始 API 缺少分页感知、流式控制、批量操作等 Agent 需要的能力
- **Token 格式低效**：JSON 比 CSV 消耗约 2x token

  → 正确做法参见 [[source/writing-tools-for-agents]]（五原则）

- ## MCP 注册表（Registry）
  2025 年 9 月：MCP 官方 Registry 预览版发布，解决了工具发现和版本管理问题，推动 MCP 生态标准化。

- ## 关联
- [[entity/code-mode]] — 高效使用 MCP 的方式
- [[entity/skills]] — 基于代码执行的能力积累
- [[entity/progressive-disclosure]] — 动态按需加载工具定义，解决 Token 膨胀
- [[entity/context-engineering]] — MCP 工具设计直接影响 Context 质量
- [[entity/ai-native-development]] — AI-Native 团队用 MCP 整合所有工具（Notion/Linear/AWS/Git）
- [[topic/cs146s-modern-software-developer]] — CS146S Week 2 核心主题

- ## 来源
- [[source/anthropic-code-execution-with-mcp]] — 通过代码执行调用 MCP，token 消耗降 98.7%
- [[source/mcp-introduction-stytch]] — MCP 综合介绍：USB-C 类比，JSON-RPC 架构，OAuth 认证
- [[source/apis-dont-make-good-mcp-tools]] — 为何直接把 API 转成 MCP 工具效果差
- [[source/writing-tools-for-agents]] — 为 Agent 设计高效工具的五大原则（Anthropic）
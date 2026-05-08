---
type:: Source
source-type:: article
author:: Stytch Team
date:: 2024-01-01
url:: https://stytch.com/blog/model-context-protocol-introduction/
raw-file:: _raw/mcp-introduction-stytch.txt
created:: [[2026-05-08]]
---
# Model Context Protocol (MCP): An Introduction

## 一句话总结
> MCP 是 AI 领域的"USB-C 接口"——一个基于 JSON-RPC 2.0 的开放标准，让 LLM 通过统一的 client-server 协议安全、结构化地访问外部工具和数据，彻底替代碎片化的一次性集成方案。

## 关键要点
1. **USB-C 类比**：MCP 为 AI 提供通用标准接口，正如 USB-C 统一了硬件连接；不同 AI 客户端和服务端只需实现一次协议即可互通
2. **JSON-RPC 2.0**：所有通信使用标准化 JSON-RPC 2.0 消息格式，包括工具发现（`tools/list`）和工具调用（`tools/call`）两类核心操作
3. **三类交互原语**：Tools（函数调用）、Resources（文档等数据上下文）、Prompts（预定义模板），支持复杂的多轮交互
4. **OAuth 2.0 认证**：引入 Dynamic Client Registration（DCR）和自动端点发现，解决早期版本必须本地部署的认证缺陷，支持多用户云端部署
5. **对比 ChatGPT Plugins**：OpenAI 插件系统基于 OpenAPI、仅限单轮交互且平台私有；MCP 是开放标准，支持持久连接和跨平台使用
6. **对比 LangChain Tools**：LangChain 在开发时静态绑定工具；MCP 在运行时动态发现工具，将标准化层从框架层下移至协议层
7. **Agent 核心基础设施**：MCP 让 Agent 从"孤立的大脑"变成"能干事的执行者"，支持跨系统多步工作流

## 详细笔记

### 核心定位：什么是 MCP

MCP（Model Context Protocol）是 Anthropic 提出的开放标准，将 AI 模型与外部数据和服务之间的连接标准化。其核心价值在于提供统一接口，让 LLM 能以结构化、安全的方式调用 API、读取数据库、执行函数。

**USB-C 类比的含义**：正如 USB-C 出现前，每个设备厂商有自己的充电接口，AI 集成在 MCP 之前也是各系统各自为政——每接入一个新服务就要写一套定制化代码。MCP 提供的"通用接口"意味着：只要服务端实现了 MCP Server，任何兼容 MCP 的 AI 客户端都能直接使用，无需额外适配。

### Client-Server 架构

MCP 采用清晰的双层架构：

- **MCP Client**：嵌入在 AI 应用侧（聊天机器人、IDE 助手、自动化工具），负责发起请求、处理响应、将结果注入 LLM 上下文
- **MCP Server**：暴露外部能力，包括可调用函数、数据资源和提示词模板

双方之间的所有交互均通过标准化的 **JSON-RPC 2.0** 消息完成，确保安全性和结构一致性。

### JSON-RPC 2.0 消息格式

**工具发现请求**（Client → Server）：
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list",
  "params": {}
}
```
Server 返回可用工具的定义列表，包含名称、描述和输入 Schema，供 LLM 理解有哪些能力可用。

**工具调用请求**：
```json
{
  "method": "tools/call",
  "params": {
    "name": "toolName",
    "arguments": { "key": "value" }
  }
}
```

### 三类交互原语

| 原语类型 | 作用 |
|----------|------|
| **Tools** | 可执行函数调用，如查询数据库、发送邮件 |
| **Resources** | 数据上下文注入，如文档、文件、实时数据流 |
| **Prompts** | 预定义提示词模板，支持参数化复用 |

这三类原语共同支持复杂的多轮交互，而不仅仅是简单的单次 API 查询。

### 典型工作流程

1. **连接初始化**：Host 应用建立 MCP Client 连接（stdio 或 HTTP/SSE）
2. **能力发现**：Client 通过 JSON-RPC 查询可用工具列表
3. **LLM 工具选择**：模型根据用户 query 决定调用哪个工具
4. **工具执行**：Client 发送调用请求，Server 处理后返回结果
5. **上下文集成**：结果注入模型对话上下文，生成最终响应

### OAuth 2.0 认证演进

**早期问题**：MCP 初期没有标准化认证机制，只能本地部署或手动共享凭据，严重限制了多用户和云端使用场景。

**当前方案**：集成 OAuth 2.0，具体特性包括：
- **Dynamic Client Registration（DCR）**：自动注册客户端，无需手动配置
- **自动端点发现**：标准化元数据 URL，减少配置开销
- **Scoped Token 管理**：Token 权限范围与用户实际权限对齐
- **多用户并发支持**：使云端部署和大规模商用成为可能

### 与同类方案的对比

#### vs. 定制化集成（传统做法）
传统方式需要为每个服务编写独立集成代码，手动管理 API Key，形成脆弱、不可扩展的系统。MCP 通过统一协议层一次性解决这些问题。

#### vs. ChatGPT Plugins（2023）
| 维度 | ChatGPT Plugins | MCP |
|------|-----------------|-----|
| 标准基础 | OpenAPI | JSON-RPC 2.0 |
| 开放性 | 平台私有 | 开放标准 |
| 交互模式 | 单轮 | 支持持久连接、多轮 |
| 跨平台 | 仅 ChatGPT | 任何兼容客户端 |

#### vs. LangChain Tools
| 维度 | LangChain | MCP |
|------|-----------|-----|
| 工具绑定时机 | 开发时静态包含 | 运行时动态发现 |
| 标准化层级 | 框架层（Python API） | 协议层（跨语言） |
| 工具更新 | 需重新部署应用 | Server 更新自动生效 |

LangChain 后来新增了 MCP 支持，Agent 可通过 LangChain 访问 MCP Server 作为动态工具源——两者并非替代而是互补。

#### vs. OpenAI Function Calling
Function Calling 解决的是"模型如何格式化输出函数调用（JSON 结构）"，MCP 解决的是"如何标准化执行和处理结果"。两者定位互补，可同时使用。

### 部署灵活性

MCP Server 支持多种语言和部署方式：
- **本地 stdio**：进程间通信，适合开发调试
- **远程 HTTP/SSE**：云端部署，支持多客户端并发
- **Cloudflare 等平台**：Serverless 托管
- **MCP Inspector**：官方调试工具，提供交互式调试界面

### 实际应用场景

- 带实时数据访问的 AI 聊天机器人（对接 CRM、数据库）
- 自动化工作流（检索数据 → 发送通知 → 写入数据库的多步 Agent）
- 金融、医疗、制造业的 AI 流程自动化
- IDE 中的 AI 编程助手（对接代码库、文档、CI 系统）

## 与其他资料的关系
- 与 [[source/building-agents-that-reach-production-systems-with-mcp]] 互补：Stytch 文章是 MCP 入门概览，Anthropic 文章是生产级最佳实践深度指南
- 与 [[source/anthropic-code-execution-with-mcp]] 对比：本文介绍 MCP 协议本身，后者探讨如何用代码执行优化 MCP 工具调用的 token 效率
- 与 [[source/apis-dont-make-good-mcp-tools]] 形成递进关系：本文讲清楚 MCP 是什么，后者进一步指出"直接把 API 转成 MCP 工具"的陷阱
- 补充了 [[entity/mcp]] 的基础概念：JSON-RPC 2.0、三类原语、OAuth 2.0 认证机制

## 引用此资料的页面
- [[entity/mcp]]
- [[topic/cs146s-modern-software-developer]]

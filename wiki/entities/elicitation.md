---
type:: Entity
created:: [[2026-05-06]]
---

# MCP Elicitation

**MCP Elicitation** 是 [[mcp]]（Model Context Protocol）的一项能力，允许 server 在工具调用中途暂停执行，主动向用户请求输入后再继续。

## 两种模式

### Form Mode

Server 发送一个 JSON Schema，由客户端渲染为**原生表单**。典型用途包括：

- 请求缺失的工具参数
- 在执行破坏性操作前要求用户确认

### URL Mode

Server 将用户引导到**浏览器**中完成交互。典型用途包括：

- 完成 OAuth 授权流程
- 处理支付操作
- 收集用户凭证

## 相关概念

- [[mcp]] — Elicitation 所依赖的基础协议
- [[harness]] — 安全控制机制，与 Elicitation 的用户确认流程密切相关

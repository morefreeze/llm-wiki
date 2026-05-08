---
type:: Source
source-type:: article
author:: Anthropic
date:: 2026-04-22
url:: https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp
raw-file:: _raw/building-agents-that-reach-production-systems-with-mcp.txt
created:: [[2026-05-06]]
---
# Building agents that reach production systems with MCP

## 一句话总结
> Anthropic 系统阐述 Agent 连接生产系统的三种路径（直接 API、CLI、MCP），论证 MCP 作为通用协议层的规模化优势，并给出构建高效 MCP Server 的五大模式及客户端上下文优化策略。

## 关键要点
1. Agent 连接外部系统有三种方式：直接 API 调用（M×N 问题）、CLI（无法覆盖 Web/移动端/云托管）、MCP（通用协议层，一次构建可达所有兼容客户端）
2. MCP SDK 月下载量已超 3 亿次，生态覆盖 Claude、ChatGPT、Cursor、VS Code 等主流客户端
3. 构建高效 MCP Server 的五大模式：远程部署、按意图分组工具、代码编排大 API 表面、交付富语义、标准化认证
4. 客户端侧通过 Tool Search（按需加载，token 减少 85%+）和 Programmatic Tool Calling（代码沙箱处理，token 减少 37%）大幅提升上下文效率
5. Skills 与 MCP 互补：Plugin 模式打包 skills + MCP servers，分发模式从 MCP server 发布 skills

## 详细笔记

### Agent 连接外部系统的三种方式

**直接 API 调用**
- 适合一对一小规模集成场景
- 规模化后遇到 M×N 问题：M 个 agent 各自对接 N 个服务，集成工作量指数级增长

**CLI（命令行接口）**
- 轻量快速，适合本地开发
- 致命局限：无法覆盖移动端、Web 应用和云托管平台

**MCP（Model Context Protocol）**
- 提供通用协议层，解决 M×N 问题——一个远程 server 可达任何兼容客户端
- 已兼容客户端：Claude、ChatGPT、Cursor、VS Code 等
- 支持标准化认证（OAuth）、服务发现和富语义交互
- MCP SDK 下载量已超过 3 亿次/月，生态规模显著

### 构建有效 MCP Server 的五大模式

1. **构建远程 server 以获得最大覆盖** — 本地 server 受限于运行环境，远程 server 可被任何客户端随时调用
2. **按意图分组工具，不按端点镜像** — 工具应按用户意图组织，而非机械映射 REST 端点，减少 agent 的选择负担
3. **大 API 表面时设计为代码编排** — 典型案例：Cloudflare 仅用 2 个工具覆盖 2500 个 API 端点，通过让 agent 编写和执行编排代码实现
4. **交付富语义** — 利用 MCP Apps 交互界面和 Elicitation 机制获取用户输入，超越纯文本交互
5. **使用标准化认证** — OAuth + CIMD + Vaults 组合，实现安全且可互操作的认证流程

### 客户端上下文效率优化

- **Tool Search**：按需加载工具定义，而非一次性注入所有工具描述，token 消耗减少 85% 以上
- **Programmatic Tool Calling**：在代码沙箱中处理工具返回结果，避免将大量原始数据注入对话上下文，token 减少 37%

### Skills 与 MCP 的互补关系

- **Plugin 模式**：将 skills 与 MCP servers 打包在一起，作为完整功能单元分发
- **分发模式**：从 MCP server 直接发布 skills，实现 skills 的动态发现和安装

## 与其他资料的关系
- 与 [[MCP]] 协议规范直接相关，是 Anthropic 官方对 MCP 最佳实践的权威指南
- 补充了 [[Agent 架构]] 中关于工具调用和生产系统集成的实践模式
- 涉及 [[Tool Use]] 的优化策略（Tool Search、Programmatic Tool Calling）

## 引用此资料的页面
- （待其他页面引用时更新）

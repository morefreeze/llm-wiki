---
type:: Topic
tags:: #agent #production #mcp #safety
created:: [[2026-05-06]]
sources:: [[building-agents-that-reach-production-systems-with-mcp]] [[从玩具到生产力用真实项目讲透-ai-agent-的-harness-engineering]] [[当我们在讨论-harness-的时候我们在讨论什么]]
---

# Agent 生产化

## 核心问题
Agent 从「玩具」到「生产」需要解决三个关键问题：
- **连接性**：Agent 如何可靠地连接外部系统
- **安全性**：Agent 如何安全地使用能力而不失控
- **可扩展性**：集成如何从 1 对 1 扩展到 M 对 N

## 连接方式演进

| 方式 | 适用场景 | 局限 | 规模化 |
|------|---------|------|--------|
| 直接 API 调用 | 小规模、一次性集成 | M×N 问题 | ❌ |
| CLI | 本地环境、沙箱容器 | 无法覆盖 Web/移动/云 | ⚠️ |
| [[mcp]] | 云端 Agent、跨平台 | 前期投入稍大 | ✅ |

## 生产级 MCP Server 设计模式
1. **构建远程 Server** — 获得最大分发覆盖
2. **按意图分组工具** — 而非按端点 1:1 镜像 API
3. **代码编排** — 大 API 表面用代码沙箱（如 Cloudflare 2 工具覆盖 2500 端点）
4. **富语义交付** — [[mcp-apps]]（交互界面）、[[elicitation]]（用户输入）
5. **标准化认证** — OAuth + CIMD + Vaults

## Harness：从玩具到生产力的关键
- [[harness]] 是 Agent 的安全约束与引导层
- 不是框架，而是「安全带 + 方向盘」
- 五大组件：输入验证、输出过滤、权限控制、错误处理、日志记录
- 与 [[mcp]] 的认证和权限机制互补

## 生态规模
- MCP SDK 下载量：3 亿次/月（2026 年 4 月）
- Claude MCP 目录：200+ 个 server
- 兼容客户端：Claude、ChatGPT、Cursor、VS Code 等

## 参见
- [[mcp]] — Model Context Protocol
- [[harness]] — Agent 驾驭层
- [[skills]] — 可复用能力
- [[plugin]] — Skills + MCP 打包
- [[agent-efficiency]] — Agent 效率优化
- [[tool-search]] — 按需工具发现

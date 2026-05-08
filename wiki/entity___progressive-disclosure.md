---
type:: Entity
tags:: #pattern #design #ux
created:: [[2026-05-06]]
sources:: [[source/anthropic-code-execution-with-mcp]]
---

- # Progressive Disclosure（渐进式发现）
- ## 概述
  一种设计模式：模型通过浏览文件系统按需发现和加载工具定义，而非一次性全部加载。
- ## 在 MCP 代码执行中的应用
  1. Agent 列出 `./servers/` 目录发现可用的 MCP server
  2. 读取具体工具文件了解接口
  3. 只加载当前任务需要的定义
  4. 可通过 `search_tools` 工具搜索相关定义
  5. 支持不同详细级别：仅名称 / 名称+描述 / 完整定义+Schema
- ## 价值
- 从 150,000 token（全量加载）→ 2,000 token（按需加载）
- 模型天然擅长浏览文件系统
- ## 关联
- [[entity/mcp]] — Progressive Disclosure 在 MCP 中的具体应用
- [[entity/code-mode]] — Code Mode 的核心设计原则
- [[topic/agent-efficiency]] — 相关主题
- ## 来源
- [[source/anthropic-code-execution-with-mcp]] — Anthropic 工程博客
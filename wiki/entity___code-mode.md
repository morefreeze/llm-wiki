---
type:: Entity
tags:: #pattern #efficiency #cloudflare
created:: [[2026-05-06]]
sources:: [[source/anthropic-code-execution-with-mcp]]
---

- # Code Mode
- ## 概述
  Cloudflare 提出的概念，指 Agent 通过编写代码（而非直接工具调用）来与 MCP server 交互。Anthropic 独立发现了相同的洞察。
- ## 核心洞察
  LLM 擅长写代码，应该利用这一优势让 Agent 以代码方式高效调用工具。
- ## 关键数据
- Token 消耗：150,000 → 2,000（节省 98.7%）
- 来源：Anthropic 工程博客实测数据
- Cloudflare 独立验证了类似结论
- ## 关联
- [[entity/mcp]] — Code Mode 是 MCP 的高效使用方式
- [[entity/progressive-disclosure]] — Code Mode 的关键设计模式
- [[topic/agent-efficiency]] — 相关主题
- ## 来源
- [[source/anthropic-code-execution-with-mcp]] — Anthropic 工程博客
- Cloudflare 博客（引用于 Anthropic 文章中）
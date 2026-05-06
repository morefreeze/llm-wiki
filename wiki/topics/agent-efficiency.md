---
type:: Topic
tags:: #agent #efficiency #token-optimization #mcp
created:: [[2026-05-06]]
sources:: [[anthropic-code-execution-with-mcp]] [[llm-wiki-pattern]]
---
# Agent 效率优化

## 核心问题
随着 Agent 连接的工具/知识源增长，效率和成本面临严峻挑战：
- 工具定义膨胀 → 上下文窗口被工具描述占满
- 中间结果反复经过模型 → Token 翻倍消耗
- RAG 模式无积累 → 每次查询重新检索拼凑

## 解决方案对比

| 方案 | 解决的问题 | 原理 | 来源 |
|------|-----------|------|------|
| [[code-mode]] | 工具定义膨胀 | 代码 API + 文件系统按需发现 | [[anthropic-code-execution-with-mcp]] |
| [[code-mode]] | 中间结果膨胀 | 执行环境过滤，只返回必要数据 | [[anthropic-code-execution-with-mcp]] |
| [[llm-wiki-pattern]] | 知识无积累 | 增量编译 Wiki，知识只编译一次 | [[llm-wiki-pattern]] |
| [[progressive-disclosure]] | 定义过载 | 按需加载，支持不同详细级别 | [[anthropic-code-execution-with-mcp]] |

## 核心原则

1. **编译一次，复用多次**：无论是工具接口还是知识，都应该预编译而非实时检索
2. **按需加载**：只加载当前任务需要的定义和数据
3. **数据在执行环境处理**：过滤/聚合/转换在模型外部完成
4. **持久化和积累**：保存中间状态和可复用代码（[[skills]]）

## 量化效果
- Token 节省：98.7%（150K → 2K）
- 知识复用：Wiki 模式消除了 RAG 的重复检索开销

## 开放问题
- 代码执行环境的沙箱安全如何平衡效率？
- 大规模 Agent 系统中如何管理 Skills 的版本和依赖？
- Wiki 增长到数千页后，index.md 是否需要升级为搜索引擎（如 qmd）？

## 参见
- [[mcp]] — 工具连接协议
- [[skills]] — 可复用能力积累
- [[pii-tokenization]] — 隐私保护的数据流管理

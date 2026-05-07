---
type:: Topic
tags:: #agent #efficiency #token-optimization #mcp #memory
created:: [[2026-05-06]]
updated:: [[2026-05-07]]
sources:: [[anthropic-code-execution-with-mcp]] [[llm-wiki-pattern]] [[building-agents-that-reach-production-systems-with-mcp]] [[hermes-agent-memory-system]]
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
| [[tool-search]] | 工具定义过载 | 运行时搜索工具目录，按需加载 | [[building-agents-that-reach-production-systems-with-mcp]] |

## 核心原则
  
1. **编译一次，复用多次**：无论是工具接口还是知识，都应该预编译而非实时检索
2. **按需加载**：只加载当前任务需要的定义和数据
3. **数据在执行环境处理**：过滤/聚合/转换在模型外部完成
4. **持久化和积累**：保存中间状态和可复用代码（[[skills]]）

## 量化效果
- Token 节省：98.7%（150K → 2K）
- [[tool-search]]：工具定义 token 减少 85%+
- Programmatic Tool Calling：多步骤工作流 token 减少 37%
- 知识复用：Wiki 模式消除了 RAG 的重复检索开销

## 记忆分层与 Prompt Cache（Hermes 的补充视角）

[[hermes-agent-memory-system]] 提供了另一个效率维度：**Prompt Cache 命中率**。

Hermes Agent 的核心优化目标：让系统提示词的稳定前缀尽可能长时间不变 = 高 Cache 命中率 = 低延迟低成本。

由此衍生的[[agent-memory-system]]四层架构：

| 层级 | 大小 | 放在哪里 | 触发方式 |
|------|------|---------|---------|
| 提示词记忆（MEMORY.md + USER.md） | ~1300 Token | 系统提示词（固化） | 会话开始自动注入 |
| 技能索引 | 轻量 | 系统提示词（固化） | 会话开始自动注入 |
| 完整技能内容 | 按需 | 工具调用返回 | 模型主动请求 |
| SQLite 历史会话 | 大 | 数据库（冷存储） | session_search 工具触发 |

原则：**把常驻信息做小做稳（缓存友好），把偶发信息做成工具调用（按需检索）。**

这与本主题的核心原则完全一致：按需加载、数据在执行环境处理，只有真正需要的信息才进入上下文窗口。

## 开放问题
- 代码执行环境的沙箱安全如何平衡效率？
- 大规模 Agent 系统中如何管理 Skills 的版本和依赖？
- Wiki 增长到数千页后，index.md 是否需要升级为搜索引擎（如 qmd）？
- Prompt Cache 对不同模型供应商的命中率差异有多大？记忆架构设计需要为此做调整吗？

## 参见
- [[mcp]] — 工具连接协议
- [[skills]] — 可复用能力积累
- [[harness]] — Agent 安全驾驭层
- [[plugin]] — Skills + MCP 打包分发

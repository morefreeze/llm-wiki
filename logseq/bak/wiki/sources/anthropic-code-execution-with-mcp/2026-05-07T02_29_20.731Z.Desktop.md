---
type:: Source
source-type:: article
author:: [[Adam Jones]] [[Conor Kelly]]
date:: 2025-11-04
url:: https://www.anthropic.com/engineering/code-execution-with-mcp
raw-file:: raw/anthropic-code-execution-with-mcp.md
created:: [[2026-05-06]]
---
# Code Execution with MCP: Building More Efficient AI Agents

## 一句话总结
> 让 Agent 通过编写代码调用 MCP 工具（而非直接工具调用），可将 token 消耗从 150K 降至 2K，节省 98.7%，同时带来隐私保护和技能积累。

## 关键要点

1. **问题**：MCP 工具扩展后，工具定义 + 中间结果 占满上下文窗口，Agent 效率急剧下降
2. **方案**：将 MCP 工具呈现为文件系统上的代码 API，Agent 按需发现和调用
3. **数据**：Token 从 150,000 → 2,000（98.7% 节省），Cloudflare 独立验证
4. **渐进式发现**：模型浏览文件系统按需加载工具定义，支持搜索和不同详细级别
5. **上下文高效**：在执行环境中过滤数据（万行表格→5行），支持聚合和 join
6. **控制流优化**：循环/条件/错误处理用标准代码，减少模型介入
7. **隐私保护**：中间结果留在执行环境，PII 自动 tokenization
8. **技能积累**：Agent 可保存可复用代码为 Skills，结合 SKILL.md 形成知识库

## 核心架构

```
传统方式：工具定义 → 全部加载到 context → 模型直接调用 → 中间结果经过模型
代码执行：文件系统 → Agent 按需发现 → 写代码调用 → 数据在执行环境处理
```

## 与其他资料的关系

| 资料 | 关系 |
|------|------|
| [[llm-wiki-pattern]] | 互补——Wiki 是知识持久化，代码执行是工具交互高效化 |
| Cloudflare "Code Mode" | 独立验证了同一洞察 |

## 提取的实体
- [[MCP]] — Model Context Protocol，开放标准
- [[Code Mode]] — Cloudflare 的概念
- [[Skills]] — 可复用的 Agent 能力，含 SKILL.md
- [[Progressive Disclosure]] — 按需加载的设计模式
- [[PII Tokenization]] — 敏感数据自动替换

## 引用此资料的页面
- [[entities/mcp]]
- [[entities/code-mode]]
- [[entities/skills]]
- [[topics/agent-efficiency]]

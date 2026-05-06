---
type:: Source
source-type:: article
author:: [[Andrej Karpathy]]
date:: 2026
url:: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
raw-file:: raw/442a6bf555914893e9891c11519de94f.md
created:: [[2026-05-06]]
---
# LLM Wiki Pattern

## 一句话总结
> 与其每次查询都从原始文档重新检索（RAG），不如让 LLM 增量构建一个持久的、互联的 wiki——知识编译一次，持续复利。

## 关键要点

1. **传统 RAG 的问题**：无积累，每次重新发现知识，无法综合多文档
2. **LLM Wiki 模式**：LLM 维护结构化 wiki，新源触发多页面更新（10-15页/源）
3. **三层架构**：Raw Sources（只读）→ Wiki（LLM 拥有）→ Schema（配置文件）
4. **三个操作**：Ingest（摄入）、Query（查询+回存）、Lint（健康检查）
5. **两个导航文件**：index.md（内容目录）+ log.md（时间日志）
6. **人类角色**：筛选资料、引导分析、提出好问题
7. **LLM 角色**：总结、交叉引用、归档、维护一致性
8. **灵感来源**：Vannevar Bush 的 Memex (1945)

## 与其他概念的关系

| 概念 | 关系 |
|------|------|
| [[RAG]] | 替代方案——RAG 是实时检索，Wiki 是预编译 |
| [[Memex]] | 精神先驱——个人知识存储 + 关联路径 |
| [[Obsidian]] / [[Logseq]] | 浏览层——人类阅读 wiki 的工具 |
| [[qmd]] | 可选工具——Markdown 搜索引擎（BM25+向量） |

## 引用此资料的页面
- （待建：增量知识编译、持久知识管理主题页）

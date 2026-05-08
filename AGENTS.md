# LLM Wiki — 持久化知识库

> 基于 Karpathy 的 LLM Wiki 模式构建。LLM 增量构建并维护一个结构化、互联的 Markdown 知识库，位于你和原始资料之间。

## 核心理念

不是 RAG（每次重新检索），而是 **增量编译**：
- 添加新源 → LLM 阅读、提取、整合到现有 wiki
- 更新实体页、修正过时信息、建立交叉引用
- 知识只编译一次，持续保持最新

## 三层架构

```
llm-wiki/
├── AGENTS.md              ← Schema（本文件）：告诉 LLM 如何维护 wiki
├── index.md               ← 内容目录：所有页面的链接和摘要
├── log.md                 ← 时间日志：append-only 操作记录
├── _raw/                  ← 原始资料（不可变，只读）
│   └── <source>.txt       ← 使用 .txt 扩展名（避免 Logseq 索引冲突）
└── wiki/                  ← LLM 生成的 wiki 页面（LLM 拥有此层）
    ├── entity___<name>.md ← 实体页（概念词条），Logseq 引用：[[entity/<name>]]
    ├── source___<name>.md ← 资料摘要页，Logseq 引用：[[source/<name>]]
    ├── topic___<name>.md  ← 主题综述页，Logseq 引用：[[topic/<name>]]
    └── synthesis___<name>.md ← 综合分析页，Logseq 引用：[[synthesis/<name>]]
```

**Logseq 命名规范**：wiki/ 目录下使用平铺结构，以 `___`（三下划线）代替路径分隔符：
- 文件：`entity___harness.md`  →  Logseq 链接：`[[entity/harness]]`
- 文件：`source___llm-wiki-pattern.md`  →  Logseq 链接：`[[source/llm-wiki-pattern]]`
- 文件：`topic___agent-production.md`  →  Logseq 链接：`[[topic/agent-production]]`

## Logseq 集成

本 wiki 同时映射到 Logseq 知识库 `~/git/mylogseq/`：
- wiki 页面对应 Logseq 的 `R/`（资源）和 `P/`（项目）页面
- 文件系统命名：`R___xxx.md`，Logseq 引用：`[[R/xxx]]`
- 使用 Logseq 的 `type::`、`tags::`、`created::` 属性
- LLM 维护 wiki 目录，用户在 Logseq 中浏览和链接

## 操作流程

### Ingest（摄入）
1. 用户将原始资料放入 `_raw/`
2. LLM 阅读资料，讨论关键要点
3. 写入摘要页 `wiki/source___<title>.md`（Logseq 链接：`[[source/<title>]]`）
4. 更新/新建 `wiki/entity___<name>.md` 和 `wiki/topic___<name>.md`
5. 更新 `index.md`
6. 追加记录到 `log.md`

### Query（查询）
1. LLM 搜索 `index.md` 找到相关页面
2. 阅读相关页面，综合回答
3. 有价值的回答可以存为新的 wiki 页面

### Lint（检查）
1. 查找矛盾、过时信息
2. 孤立页面（无入链）
3. 缺失的交叉引用
4. 建议新的调查方向

## 页面格式

### 实体页 (entities/)
```markdown
---
type:: Entity
tags:: #标签
created:: [[YYYY-MM-DD]]
sources:: [[来源页]]
---
# 实体名称

## 概述
简短定义

## 关键信息
- 要点1
- 要点2

## 关联
- [[相关实体1]]
- [[相关实体2]]

## 来源
- [[来源页1]] — 相关要点
```

### 主题页 (topics/)
```markdown
---
type:: Topic
tags:: #标签
created:: [[YYYY-MM-DD]]
sources:: [[来源页1]] [[来源页2]]
---
# 主题名称

## 核心观点
综合摘要

## 不同视角
| 观点 | 来源 | 说明 |
|------|------|------|

## 开放问题
- 待探索的问题

## 参见
- [[相关主题]]
```

### 资料摘要页 (sources/)
```markdown
---
type:: Source
source-type:: article|paper|video|book
author:: 作者
date:: YYYY-MM-DD
url:: 原始链接
raw-file:: _raw/<filename>.txt
created:: [[YYYY-MM-DD]]
---
# 资料标题

## 一句话总结
> 核心观点

## 关键要点
1. 要点1
2. 要点2

## 详细笔记
...

## 与其他资料的关系
- 与 [[来源B]] 对比：...
- 补充了 [[概念X]]：...

## 引用此资料的页面
- [[实体页A]]
- [[主题页B]]
```

## 日志格式 (log.md)

```
## [YYYY-MM-DD] ingest | 资料标题
- 添加了来源页 [[sources/title]]
- 更新了 [[entities/X]]，[[topics/Y]]
- 新增 [[entities/Z]] 页面

## [YYYY-MM-DD] query | 问题摘要
- 生成了分析页 [[synthesis/title]]

## [YYYY-MM-DD] lint
- 修复了 [[entities/X]] 中的过时信息
- 为 [[topics/Y]] 添加了缺失的交叉引用
```

## 约定

- 所有 wiki 页面使用 Markdown 格式
- 页面间用 `[[wikilink]]` 互相链接
- 每次操作必须更新 `index.md` 和 `log.md`
- 原始资料放在 `_raw/` 下（.txt 扩展名），LLM 只读不写
- 优先中文撰写，技术术语保留英文
- 新页面创建时必须包含 frontmatter 属性

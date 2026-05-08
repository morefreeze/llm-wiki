---
type:: Entity
tags:: #information #reading #knowledge-management #product
created:: [[2026-05-07]]
sources:: [[source/bestblogs-2.0-reading-workflow]] [[source/llm-wiki-pattern]]
---

- # Information Filtering（信息过滤/判断）
- ## 概述
  在内容过载时代，真正稀缺的不是内容本身，而是**高质量信息的发现、判断、压缩和持续跟踪**能力。信息过滤是知识工作者最核心的认知瓶颈。
- ## 核心问题
  > "获取内容早就不是门槛，判断内容才是。"
  
  每天重复的判断消耗大量注意力：
- 这篇要不要点开？
- 这篇是不是只是标题写得好？
- 这个播客值不值得花 1 小时？
- 今天事情很多，到底先看哪几篇？
- ## 三个层次
  
  | 层次 | 问题 | 工具/方法 |
  |------|------|---------|
  | **发现** | 哪里有好内容？ | RSS、Newsletter、社群、推荐算法 |
  | **判断** | 这个值不值得读？ | AI 摘要、个性化推荐、公共质量池 |
  | **提炼** | 读完留下什么？ | [[source/llm-wiki-pattern]]、笔记系统、知识编译 |
- ## 解决方案方向
  
  **平台层（BestBlogs 模式）**
- 建立公共质量池：由人工/AI 认真筛选，降低个人判断起点
- 个性化层：根据行为慢慢适配，让推荐"越来越适合我"
- 工作流化：把发现→判断→阅读→沉淀串成一条完整路径
  
  **个人层（Karpathy LLM Wiki 模式）**
- 把值得看的内容 ingest 到个人知识库
- LLM 增量编译：知识只处理一次，持续保持最新
- 不是 RAG（每次检索），而是持久化知识图谱
- ## 关联
- [[source/llm-wiki-pattern]] — 个人知识编译，解决"读完留下什么"
- [[topic/information-workflow]] — 信息过滤是工作流的核心环节
- [[entity/agentic-coding]] — Agent 也面临"工具判断"问题，与信息判断同构
- ## 来源
- [[source/bestblogs-2.0-reading-workflow]] — BestBlogs 2.0 的核心产品洞察
- [[source/llm-wiki-pattern]] — Karpathy 从个人角度解决同类问题
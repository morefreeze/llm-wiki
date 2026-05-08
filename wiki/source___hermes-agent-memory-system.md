---
type:: Source
source-type:: article
author:: Manthan Gupta（宝玉翻译整理）
date:: 2026-04-29
url:: https://baoyu.io/blog/2026-04-29/manthanguptaa-2034849672985288957
raw-file:: _raw/hermes-agent-memory-system.txt
created:: [[2026-05-07]]
---

- # 深度拆解 Hermes Agent 的记忆系统：它如何修正 OpenClaw 的误区
- ## 一句话总结
  > 真正的诀窍不是记住更多，而是在正确的层级、以正确的成本，记住正确的事情——Hermes 用"冷热分离+缓存优先"修正了 OpenClaw 的记忆模式。
- ## 关键要点
  
  1. **四层记忆架构** — 提示词记忆（热/固定）+ SQLite 历史搜索（冷/按需）+ Skills（程序记忆）+ Honcho（深层用户建模，可选）
  2. **缓存优先设计** — 核心原则是让系统提示词的稳定前缀尽可能长时间不变，频繁改动提示词 = 延迟增加 + 成本上升
  3. **"精选状态"非"日记"** — MEMORY.md（2200字符）+ USER.md（1375字符），严格存用户偏好/环境事实/错误修正/稳定规范；不存任务进度/会话结果/临时 TODO
  4. **记忆冲刷（Memory Flush）** — 长对话压缩前，先让模型把值得保留的内容写入 MEMORY.md，防止摘要有损丢失重要事实
  5. **Skills = 程序记忆** — 如何做事（procedural）不同于记住什么（semantic）；技能索引在提示词中，完整技能按需加载
  6. **Honcho 集成的智慧** — 第一轮织入系统提示词，之后追加在用户消息后面（不修改系统提示词）——保持缓存有效的同时读到最新信息
- ## 详细笔记
- ### 上下文结构（提示词组装顺序）
  
  ```
  [0] 默认智能体身份
  [1] 工具使用行为指南
  [2] Honcho 集成（可选）
  [3] 可选系统消息
  [4] MEMORY.md 快照（固化）
  [5] USER.md 快照（固化）
  [6] 技能索引
  [7] 上下文文件（AGENTS.md, SOUL.md 等）
  [8] 日期/时间 + 平台信息
  [9] 对话历史
  [10] 当前用户消息
  ```
- ### 记忆的三类存储 vs 认知科学映射
  
  | Hermes 设计 | 认知科学类比 |
  |------------|------------|
  | MEMORY.md + USER.md（提示词，固定） | 语义记忆（Semantic Memory） |
  | session_search（SQLite，按需） | 情景记忆（Episodic Memory） |
  | Skills（按需加载） | 程序记忆（Procedural Memory） |
  | Honcho（跨平台） | 长期记忆 + 用户模型 |
- ### Hermes vs OpenClaw
- **OpenClaw**：记忆更接近"以 Markdown 为中心的存储"，日志和长效文件是主要事实来源，提示词缓存优化较弱
- **Hermes**：提示词记忆严格限制（1300 Token）；历史记录存在 SQLite 里，只在需要时搜索；缓存友好是核心设计目标
  
  **Hermes 更关注缓存效率：** 不是所有东西都配住在"系统提示词"这个黄金地段。
- ### 记忆冲刷机制
  
  长对话压缩前的流程：
  1. 发送指令："优先保存用户偏好、修正建议和重复模式，而非具体的任务细节"
  2. 运行一次额外的模型调用，只开启 `memory` 工具
  3. 模型主动写入 MEMORY.md
  4. 然后进行对话压缩
- ### 技能索引的渐进式设计
  
  提示词中只有技能索引（轻量），完整技能内容按需加载——与 [[entity/progressive-disclosure]] 和 [[entity/tool-search]] 的设计理念完全一致。
- ## 与其他资料的关系
- 与 [[source/anthropic-code-execution-with-mcp]] 高度呼应：Anthropic 文章中的 Skills 概念（可复用代码单元）在 Hermes 中以"程序记忆层"的形式落地；技能索引+按需加载与 progressive-disclosure 同构
- 与 [[source/当我们在讨论-harness-的时候我们在讨论什么]] 直接相关：Hermes Agent 正是这篇文章讨论的 Harness 实践主体
- 与 [[source/harness-knowledge-moat]] 呼应：Hermes 的 MEMORY.md 系统和 Layer 0-T 团队约定类似，都是把稳定的高价值知识固化到 Agent 的常驻上下文中
- 与 [[source/llm-wiki-pattern]] 呼应：Karpathy 的 LLM Wiki 模式（知识编译一次，持续复用）与 Hermes 的 session_search（历史按需搜索，辅助模型摘要）是同一思路在不同层次的应用
- ## 引用此资料的页面
- [[entities/agent-memory-system]]
- [[entities/skills]]
- [[topics/agent-efficiency]]
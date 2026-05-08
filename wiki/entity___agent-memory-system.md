---
type:: Entity
tags:: #agent #memory #context-engineering #harness
created:: [[2026-05-07]]
sources:: [[source/hermes-agent-memory-system]]
related:: [[entity/harness]], [[entity/skills]], [[entity/progressive-disclosure]], [[topic/agent-efficiency]], [[entity/knowledge-lifecycle]]
---

- # Agent 记忆系统（Agent Memory System）
  
  Agent 在长对话、跨会话场景下如何分层管理记忆的架构设计。核心原则：**在正确的层级、以正确的成本，记住正确的事情。**
- ## 核心设计挑战
  
  Agent 记忆面临两个相反的压力：
- **系统提示词稳定性**：提示词越稳定，Prompt Cache 命中率越高，延迟越低，成本越小
- **记忆的完整性**：对话历史、用户偏好、学到的技能都需要某种形式的持久化
  
  解法：**冷热分离 + 按需加载**。
- ## Hermes Agent 的四层记忆架构
- ### 第一层：提示词记忆（热记忆 / Semantic Memory）
  
  | 文件 | 用途 | 限制 |
  |------|------|------|
  | `MEMORY.md` | 智能体笔记：环境、规范、工具怪癖、教训 | 2,200 字符 |
  | `USER.md` | 用户画像：偏好、沟通风格、身份信息 | 1,375 字符 |
  
  **设计原则：**
- 会话开始时固化快照，整个会话期间不变（缓存友好）
- 使用字符限制（非 Token 限制），与模型无关
- 纯文本 + 简单分隔符（`§`），无向量数据库
  
  **存什么 vs 不存什么：**
  
  | ✅ 存储 | ❌ 不存储 |
  |--------|---------|
  | 用户偏好和沟通风格 | 任务进度和 TODO |
  | 环境事实（OS、项目路径） | 会话结果和临时状态 |
  | 反复出现的错误修正 | 一次性的具体任务细节 |
  | 稳定的规范和约定 | |
  
  > 记忆是"精选状态"，不是"日记"。
- ### 第二层：历史会话搜索（冷存储 / Episodic Memory）
  
  所有过去的会话存储在 SQLite 数据库中。当模型需要回溯历史时，触发 `session_search` 工具：
  
  1. 全文搜索过去的消息
  2. 按会话分组结果
  3. 加载匹配度最高的会话
  4. **用便宜的辅助模型摘要**（小模型 + 大模型架构）
  5. 将精炼后的回顾内容返回主模型
  
  比把完整历史塞进每个提示词便宜且高效。
- ### 第三层：技能（Skills / Procedural Memory）
  
  存储在 `~/.hermes/skills/`：Agent 发现复杂流程、修复棘手问题或学会更好方法时保存的"可复用操作序列"。
  
  大多数记忆系统只关注"知道什么"（语义/情景记忆），但 Agent 还需要记住"怎么做事"（程序记忆）。
  
  实现方式：提示词中只放**技能索引**（轻量），完整技能内容按需加载——与 [[entity/progressive-disclosure]] 和 [[entity/tool-search]] 的设计理念一致。
- ### 第四层：Honcho（用户建模 / 可选）
  
  跨设备、跨平台的记忆连续性。集成时不破坏提示词缓存的巧妙设计：
- **第一轮对话**：Honcho 上下文织入系统提示词
- **之后对话**：Honcho 回溯内容追加在用户消息后面（不修改系统提示词）
  
  缓存继续有效，同时 Agent 能读到最新背景信息。
- ## 记忆冲刷（Memory Flush）
  
  长对话压缩（摘要有损）之前，Hermes 会先进行"记忆冲刷"：
  
  1. 向模型发送指令："优先保存用户偏好、修正建议和重复模式，而非具体的任务细节"
  2. 运行额外的模型调用，只开启 `memory` 工具
  3. 模型主动写入 MEMORY.md，防止摘要时丢失重要事实
  4. 然后进行对话压缩
- ## 设计原则总结
  
  | 原则 | 实现 |
  |------|------|
  | **缓存优先** | 让稳定的系统提示词前缀尽可能保持不变 |
  | **冷热分离** | 高频用到的信息进热记忆，低频/大量的信息进冷存储 |
  | **按需加载** | 技能索引在提示词中，完整技能内容按需读取 |
  | **记忆多样性** | semantic + episodic + procedural + user model，覆盖不同记忆需求 |
  | **模型无关性** | 字符限制而非 Token 限制，纯文本格式 |
- ## Prompt Cache 的重要性
  
  提示词缓存（Prompt Caching）是 Agent 效率的关键机制：
- **稳定的提示词前缀** = 高命中率 = 低延迟低成本
- **频繁变更提示词** = 缓存失效 = 成本翻倍
  
  Hermes 的整个记忆架构都在服务这一原则：注入提示词的内容（MEMORY.md、USER.md、技能索引）尽量小而稳定，其他内容（历史会话、完整技能、Honcho 实时上下文）通过工具按需获取。
- ## 与认知科学的映射
  
  | Hermes 设计 | 认知科学类比 |
  |------------|------------|
  | MEMORY.md + USER.md | 语义记忆（Semantic Memory） |
  | session_search（SQLite） | 情景记忆（Episodic Memory） |
  | Skills（程序记忆） | 程序记忆（Procedural Memory） |
  | Honcho（跨平台用户建模） | 长期记忆 + 自我模型 |
- ## 关联
- [[entity/skills]] — Hermes Skills 层的程序记忆实现
- [[entity/progressive-disclosure]] — 技能索引 + 按需加载 = 渐进式发现模式
- [[topic/agent-efficiency]] — Prompt Cache 命中率是 Agent 效率的核心指标之一
- [[entity/knowledge-lifecycle]] — 知识成熟度管理与记忆冲刷/衰减机制的相似性
- [[entity/harness]] — 记忆系统是 Context Engineering（上下文工程）支柱的核心组成
- ## 来源
- [[source/hermes-agent-memory-system]] — Manthan Gupta 对 Hermes 开源代码的深度拆解
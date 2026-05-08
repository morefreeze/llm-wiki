---
type:: Source
source-type:: article
author:: Drew Breunig
date:: 2025-06-22
url:: https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html
raw-file:: _raw/how-long-contexts-fail.txt
created:: [[2026-05-08]]
---

- # How Long Contexts Fail (and How to Fix Them)
- ## 一句话总结
  > context window 越大并不意味着越好——过载的 context 会通过中毒、分心、混淆、冲突四种模式让 agent 以令人意外的方式失败。
- ## 关键要点
  
  1. **Context Poisoning（上下文中毒）** — 幻觉或错误信息一旦进入 context 就会被反复引用，像毒素一样扩散并腐化后续输出
  2. **Context Distraction（上下文分心）** — context 超过临界长度后，模型过度依赖历史信息而不是运用训练知识，开始重复已有动作而非合成新策略
  3. **Context Confusion（上下文混淆）** — 无关内容迫使模型注意不必要的信息，tool 数量过多会显著降低性能，即使总量仍在 context window 内
  4. **Context Clash（上下文冲突）** — 同一 context 内来自不同来源的信息相互矛盾，导致推理失效；"sharded prompt"（分批次提供信息）比一次性提供性能低 39%
  5. **Agent 特别脆弱** — agent 同时从多个来源收集信息、进行连续工具调用、维护对话历史，天然容易触发所有四种失败模式
- ## 详细笔记
- ### 核心前提：更大的 context 不等于更好的结果
  
  LLM 的 context window 已经扩展到百万 token 量级（如 Gemini 的 1M token context），但这并不意味着模型能有效利用所有内容。
  
  当 context 过载时，模型会以四种可预测的模式失败。这对 agent 系统尤其危险，因为 agent 会在多个推理步骤中持续累积 context。
- ### 失败模式 1：Context Poisoning（上下文中毒）
  
  **定义**：幻觉或错误信息进入 context 后，被模型反复引用，导致错误不断被强化和扩大。
  
  **典型案例**：Gemini 2.5 玩 Pokémon 的 agent
  - agent 偶发性地产生了对游戏状态的幻觉
  - 这些错误的游戏状态信息被写入 context 的"目标"部分
  - 模型随后"fixated on achieving impossible or irrelevant goals"（执着于追求不可能或无关的目标）
  - 结果：agent 制定了"荒谬的策略"（nonsensical strategies），整体表现崩溃
  
  **本质**：模型信任 context 胜过自己的推理。一旦错误信息获得 context 的权威性，它就像毒素一样污染后续的每一步输出。
- ### 失败模式 2：Context Distraction（上下文分心）
  
  **定义**：随着 context 增长，模型越来越依赖已有信息，而不是运用训练知识生成新方案。
  
  **Gemini agent 的观察**：
  - 当 context 显著超过 100k token 后，agent 表现出"favoring repeating actions from its vast history rather than synthesizing novel plans"（倾向于重复历史动作而非合成新计划）
  - agent 陷入循环，无法跳出已有的行为模式
  
  **Databricks 研究数据**：
  - 对 Llama 3.1 405B 的测试显示，正确率在约 **32k token** 处开始下降
  - 更小的模型下降更早
  
  **本质**：context 本身变成了认知负担。过长的历史让模型"近视"——只能看到已经发生的事情，失去了从训练知识中提取新策略的能力。
- ### 失败模式 3：Context Confusion（上下文混淆）
  
  **定义**：无关或多余的内容迫使模型处理不必要的信息，稀释注意力，降低输出质量。
  
  **核心原理**：
  > "If you put something in the context, the model has to pay attention to it."（只要你把某些东西放进 context，模型就必须关注它。）
  
  **工具数量的影响**（Berkeley Function-Calling Leaderboard 数据）：
  - 所有模型在工具数量增加时性能都会下降
  - GeoEngine benchmark 测试：一个 quantized Llama 3.1 8B 模型
    - 使用 **46 个工具**时：失败
    - 使用 **19 个工具**时：成功
    - 注意：两种情况下总 token 量都在该模型 16k context window 之内
    - 结论：问题不是 context 长度，而是**无关工具的干扰**
  
  **本质**：context 中的每个元素都要抢占有限的注意力资源。多余的工具、无关的文档、过时的对话历史——都在稀释模型对真正重要信息的关注度。
- ### 失败模式 4：Context Clash（上下文冲突）
  
  **定义**：同一 context 内来自不同来源（或不同对话轮次）的信息相互矛盾，导致模型推理失轨。
  
  **Microsoft & Salesforce 研究**：
  - 实验设计：将相同的 prompt 信息**分批次**提供（sharded prompts）vs 一次性提供
  - 结果：分批提供方式导致平均性能**下降 39%**
  - 具体数据：OpenAI o3 的得分从 **98.1 降至 64.1**
  
  **研究者的解释**：
  > "LLMs often make assumptions in early turns...when LLMs take a wrong turn in a conversation, they get lost."（LLM 在早期轮次中常常做出假设……一旦在对话中走错方向，就会迷失。）
  
  **本质**：模型在处理多轮对话时，早期的假设和中间结论会被"锁定"在 context 中，后续的矛盾信息无法有效纠正已有的错误路径。这与人类思维的"首因效应"类似。
- ### 为什么 Agent 特别脆弱
  
  Agent 天然地在以下几个维度上累积 context 风险：
  - **多源信息收集**：同时从 web、文件、数据库、API 获取信息，来源多样性增加冲突风险
  - **连续工具调用**：每次工具调用的输出都追加到 context，context 持续增长
  - **对话历史维护**：系统 prompt + 用户消息 + 每一步的 reasoning 都保留在 context 中
  - **多步推理**：在多个推理步骤中，每一步的错误都可能被下一步引用和放大
  
  结果：一个长时间运行的 agent 几乎必然会遇到上述四种失败模式中的一种或多种。
- ### 缓解措施（文章提及的方向）
  
  文章提到将在后续文章中详细介绍具体修复方法，方向包括：
  
  - **Context Hygiene（上下文卫生）** — 主动清理过时信息，避免无关内容积累
  - **Summarization（摘要化）** — 将冗长的历史压缩为关键信息，减少 distraction
  - **RAG（检索增强生成）** — 动态加载所需信息而非预先塞满 context，避免 confusion
  - **动态工具加载** — 只在需要时加载相关工具，而非将所有工具常驻 context
  - **Context 隔离（quarantine）** — 将可能有毒的信息来源与核心推理隔离
- ## 与其他资料的关系
- 与 [[entity/context-engineering]] 直接相关：本文系统描述了 context 管理失败的四种模式，是 context engineering 实践的重要理论基础
- 与 [[source/10-lessons-for-agentic-coding]] 互补：Breunig 的另一篇文章讲 agentic coding 的实践教训；本文讲 context 层面的底层失败机制
- 与 [[entity/agent-memory-system]] 相关：agent memory 系统的设计需要考虑所有四种失败模式，尤其是 poisoning 和 distraction
- 与 [[entity/information-filtering]] 相关：context confusion 和 context clash 的根本原因都是信息过载，信息过滤是核心对策
- ## 引用此资料的页面
- [[topic/cs146s-modern-software-developer]]

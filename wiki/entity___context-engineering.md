---
type:: Entity
tags:: #context #prompt-engineering #agent #llm
created:: [[2026-05-08]]
sources:: [[source/specs-are-the-new-source-code]] [[source/how-long-contexts-fail]] [[source/context-rot]] [[source/writing-tools-for-agents]] [[source/coding-agents-101-devin]]
---

- # Context Engineering（上下文工程）
- ## 概述
  Context Engineering 是继 Prompt Engineering 之后的新范式：不再只关注单个 prompt 的措辞，而是系统性地设计和管理 LLM 接收到的完整上下文——包括系统提示、工具定义、历史记录、检索内容、用户输入等所有输入。

  > "真正的问题不是怎么写 prompt，而是怎么管理 context。" — Stanford CS146S Week 3 核心主题

- ## 为什么 Context Engineering 取代 Prompt Engineering
- **模型能力跃升**：当前模型足够聪明，单次 prompt 技巧已非瓶颈
- **输入规模膨胀**：Agent 场景下上下文可达数万乃至数十万 token，单次 prompt 的概念已不够描述问题
- **多源信息整合**：Agent 从工具、检索系统、历史对话、文档等多个来源累积上下文，需要系统化管理
- **失效模式复杂化**：长上下文下出现四种系统性失效（见下），超出了 prompt 技巧的修复范围

- ## 四种失效模式（Context Failure Modes）
  来源：[[source/how-long-contexts-fail]] + [[source/context-rot]]
  
  | 失效类型 | 描述 | 典型案例 |
  |--------|------|---------|
  | **Context Poisoning** | 上下文中包含错误信息，模型被"污染" | Gemini 2.5 Pokemon Agent 幻觉游戏状态 |
  | **Context Distraction** | 上下文过长，模型在噪声中"分心" | 超过 32k token 后正确率骤降 |
  | **Context Confusion** | 上下文中存在矛盾信息，模型无法判断 | 46 工具失败，19 工具成功（同等 token 长度） |
  | **Context Clash** | System prompt 与 user content 冲突 | 分片 prompt 导致 39% 性能下降 |

- ## Context Rot（上下文腐化）
  上下文腐化是 Distraction/Confusion 的长期演化形式：随着上下文累积，模型性能**非均匀**地退化：
- 位置效应：靠近开头和结尾的内容比中间更容易被"记住"
- 跨模型一致性：所有主流模型（Claude 4、GPT-4.1、Gemini 2.5）都存在此现象，程度各异
- → 参见 [[source/context-rot]]

- ## 核心实践
  
  **Spec 作为上下文锚点**（[[source/specs-are-the-new-source-code]]）：
- 将 Spec（设计规格）作为与 AI 协作的核心文档
- 代码是 Spec 的有损投影——AI 生成代码可以重建，但 Spec 蕴含的意图不可重建
- 工作流：prototype → 提炼 Spec → AI 实现

  **工具设计减少干扰**（[[source/writing-tools-for-agents]]）：
- 每个工具职责单一、命名清晰（按意图而非 API 结构分组）
- 返回语义化上下文而非原始数据
- Token 效率优先：分页、截断、格式优化（CSV 优于 JSON，节省约 50%）

  **Agent 任务管理**（[[source/coding-agents-101-devin]]）：
- 明确任务边界，避免单次 session 累积过多无关上下文
- 使用检查点（checkpoints）定期"清零"历史
- 提供结构化的计划文档作为持久上下文

- ## 上下文修复策略
- **上下文卫生（Context Hygiene）**：主动清除过时/错误信息
- **摘要压缩**：将历史长对话压缩为摘要，减少干扰
- **RAG 替代预加载**：按需检索而非一次性加载所有文档
- **动态工具加载**：只在需要时加载工具定义（[[entity/progressive-disclosure]]）
- **上下文隔离（Context Quarantine）**：将不可信外部内容隔离处理，防止 Poisoning

- ## 与 Secure Vibe Coding 的关系
  Context Engineering 的 Poisoning 失效模式与 Prompt Injection 攻击直接相关：
  恶意内容嵌入上下文（如仓库代码、用户消息），可能"污染"模型决策，导致 RCE（参见 [[source/copilot-rce-via-prompt-injection]]）。
  → 参见 [[entity/secure-vibe-coding]]

- ## 关联
- [[entity/agentic-coding]] — Context Engineering 是 Agentic Coding 的核心基础设施
- [[entity/living-specs]] — Spec 是主要的长期上下文锚点
- [[entity/mcp]] — MCP 工具设计直接影响上下文质量
- [[entity/progressive-disclosure]] — 动态加载工具定义，控制上下文膨胀
- [[entity/secure-vibe-coding]] — Context Poisoning = Prompt Injection 的语义等价
- [[topic/cs146s-modern-software-developer]] — CS146S Week 3 核心主题
- [[topic/agentic-developer-practices]] — 开发者实践层面的上下文管理

- ## 来源
- [[source/specs-are-the-new-source-code]] — Spec 是新的源代码，代码是有损投影
- [[source/how-long-contexts-fail]] — 四种 Context 失效模式详解（Breunig）
- [[source/context-rot]] — 上下文腐化：位置效应和非均匀退化（Chroma Research）
- [[source/writing-tools-for-agents]] — 工具设计五原则（Anthropic）
- [[source/coding-agents-101-devin]] — Agent 任务管理与检查点（Devin/Cognition）

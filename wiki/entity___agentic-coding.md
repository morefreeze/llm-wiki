---
type:: Entity
tags:: #agent #coding #developer-workflow
created:: [[2026-05-06]]
sources:: [[source/10-lessons-for-agentic-coding]], [[source/karpathy-vibe-coding-to-agentic-engineering]], [[source/coding-agents-101-devin]], [[source/good-context-good-code]], [[source/how-anthropic-teams-use-claude-code]], [[source/agentic-coding-is-a-trap]]
---

- # Agentic Coding（智能体编码）
- ## 概述
  使用 AI Agent（如 Claude Code、Codex）辅助或主导代码生成的开发范式。代码生成成本趋近于零，开发者角色从"写代码"转变为"引导、判断、维护"。
- ## 核心特征
- **代码廉价** — Agent 可以快速生成大量代码，实验成本极低
- **经验放大** — 有经验的开发者能更好地提示 Agent、识别错误、做出判断，效率被成倍放大
- **重建友好** — 低成本使频繁重构和推倒重来成为合理策略
- ## 关键实践
- **端到端测试** — 测试行为结果而非实现细节，为 Agent 重构保留空间
- **[[entity/living-specs]]** — 规格文档随实现持续同步更新
- **意图文档** — 记录决策背后的原因，维持 Agent 和开发者的方向一致
- **寻找难题** — 把精力集中在设计、性能、安全等真正创造价值的挑战上
- ## 隐性成本
  > "代码廉价，但维护、支持和安全不廉价。"
  
  快速生成的代码积累的隐患：
- 技术债和维护负担
- 安全漏洞风险
- 超出支持能力的产品规模
- ## Devin/Cognition 的补充：有效管理 Coding Agent
  来源：[[source/coding-agents-101-devin]]
  
  **四条基本规则**：
  1. 任务需有明确的验收标准（可测试、可验证）
  2. 在计划阶段让 Agent 生成详细执行计划，先确认后执行
  3. 在实现阶段分块推进，每块完成后做检查点
  4. 高风险操作（部署、数据库写入）始终保留人工确认

  **最佳任务规模**：1-6 小时范围内产出 ROI 最高；过小则 overhead 浪费大，过大则容易失控。

- ## 关联
- [[entity/harness]] — Agent 的生产化约束层，与 agentic coding 的工程基础互补
- [[entity/skills]] — 可复用的 Agent 能力单元，提升编码效率
- [[entity/living-specs]] — Agentic coding 的核心文档实践
- [[entity/context-engineering]] — Context Engineering 是 Agentic Coding 的基础设施
- [[entity/ai-native-development]] — Agentic Coding 的团队扩展形式：AI-Native Development
- [[entity/secure-vibe-coding]] — Agentic Coding 的安全约束层
- [[topic/agent-efficiency]] — Token 和工具层面的效率优化
- [[topic/cs146s-modern-software-developer]] — CS146S 贯穿全课程的核心主题

- ## Karpathy 的补充框架
  
  [[source/karpathy-vibe-coding-to-agentic-engineering]] 对 agentic coding 做了重要分层：
- **[[entity/vibe-coding]]**（Karpathy 2025 年提出）：完全放手让模型主导，适合探索性开发和 side project，抬高创作下限
- **Agentic Engineering**：在使用 Agent 加速的同时，保住专业软件的质量、安全、责任上限
  
  两者的核心区别：是否坚守**规格（spec）是人的工作**这一原则。Agent 填补实现细节，人负责系统边界、数据归属、质量标准。
  
  **锯齿状智能（Jagged Intelligence）** 是 agentic coding 的重要背景：LLM 能力曲线不是平滑上升，而是有高峰（RL 覆盖的可验证领域）和断崖（训练分布外）。开发者需要探索 Agent 的能力边界，知道哪些任务在高峰里，哪些在断崖旁边。
- ## 关联
- [[entity/harness]] — Agent 的生产化约束层，与 agentic coding 的工程基础互补
- [[entity/skills]] — 可复用的 Agent 能力单元，提升编码效率
- [[entity/living-specs]] — Agentic coding 的核心文档实践
- [[entity/context-engineering]] — Context Engineering 是 Agentic Coding 的基础设施
- [[entity/ai-native-development]] — Agentic Coding 的团队扩展形式：AI-Native Development
- [[entity/secure-vibe-coding]] — Agentic Coding 的安全约束层
- [[topic/agent-efficiency]] — Token 和工具层面的效率优化
- [[entity/vibe-coding]] — Agentic coding 的两种形态：探索性的 Vibe Coding 与专业的 Agentic Engineering
- [[entity/software-3-0]] — Agentic coding 的范式背景
- [[entity/html-as-llm-output-format]] — Agent 输出格式选择：HTML 替代 Markdown 提升信息密度
- [[topic/cs146s-modern-software-developer]] — CS146S 贯穿全课程的核心主题

- ## Lars Faye 的反驳：Agentic Coding Is a Trap
  来源：[[source/agentic-coding-is-a-trap]]

  Agentic coding 在短期提升产出，却在中长期侵蚀**监督 AI 所必须具备的能力**——这是"监督的悖论"。

  **核心数据**：
  - Anthropic 内部研究：重度使用 AI 的开发者调试技能下降 **47%**，数月内即可观测
  - LinkedIn 总监已禁止团队在批判性思维任务中使用 AI

  **陷阱机制**：
  | 阶段 | 现象 |
  |------|------|
  | 短期 | 产出↑，感觉很好 |
  | 中期 | 技能停滞，继而下降 |
  | 长期 | 无法有效监督 AI，也无法脱离 AI 工作 |

  **作者原则**（"像 Ship's Computer 那样用，而不是像 Data"）：
  1. AI 永远是辅助进程，不是主进程
  2. 不生成超过自己能逐行审查的代码
  3. 只要求 AI 做你自己也能做的事

  **优先级倒置**：传统学习是"速度→理解"，AI 辅助要求先"理解→才能引导 AI"——大多数开发者没有意识到这一根本逆转。

- ## 来源
- [[source/10-lessons-for-agentic-coding]] — 10 条开发者实践原则
- [[source/karpathy-vibe-coding-to-agentic-engineering]] — Karpathy 的 Vibe Coding vs Agentic Engineering 框架、锯齿状智能、规格所有权
- [[source/coding-agents-101-devin]] — Devin/Cognition：有效管理 Coding Agent 的四条规则与检查点架构
- [[source/good-context-good-code]] — StockApp：AI 原生团队 2.5x 生产力实践
- [[source/how-anthropic-teams-use-claude-code]] — Anthropic 10 个内部团队的 Claude Code 实战报告
- [[source/agentic-coding-is-a-trap]] — Lars Faye：监督的悖论、47% 调试技能下降、Ship's Computer 原则
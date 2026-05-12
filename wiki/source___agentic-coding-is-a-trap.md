---
type:: Source
source-type:: article
author:: Lars Faye
date:: 2026-05
url:: https://larsfaye.com/articles/agentic-coding-is-a-trap
raw-file:: _raw/agentic-coding-is-a-trap.txt
created:: [[2026-05-08]]
---
- # Agentic Coding Is a Trap（Lars Faye）
- ## 一句话总结
  > Agentic coding 是一个陷阱：它在短期内提升了产出，却在中长期侵蚀了监督 AI 所必须具备的那些能力——这就是"监督的悖论"。
- ## 核心论点
  - **认知债务（Cognitive Debt）**：把思考外包给 AI，代价是理解力的逐步丧失
  - **监督的悖论（Paradox of Supervision）**：有效监督 AI 需要深厚的领域知识；但依赖 AI 恰好侵蚀这些知识
  - **优先级倒置**：传统学习路径是"速度→理解"，AI 辅助要求先有"理解→才能引导 AI"，绝大多数开发者没有意识到这一根本逆转
  - **编程 = 规划**：很多开发者是在"写代码"的过程中完成规划的，规格驱动开发（Spec-Driven）假设规划可以从实现中分离，这本身就是一个错误假设
- ## 关键数据
  - **Anthropic 内部研究**：重度依赖 AI 的开发者调试技能下降 **47%**
  - 技能衰减在**数月内**即可显著观测到
  - LinkedIn 一位总监已**禁止团队使用 AI 辅助完成需要批判性思维的任务**
  - 参考：Simon Willison 关于认知债务的系列文章；Margaret Storey 的认知负荷研究
- ## 陷阱的完整机制
  | 阶段 | 现象 |
  |------|------|
  | 短期 | 产出↑，感觉很好 |
  | 中期 | 技能停滞，继而下降 |
  | 长期 | 无法有效监督 AI，也无法脱离 AI 工作 |
  | 净结果 | 结果比以前更差，还多了依赖 |
- ## 对规格驱动开发的反驳
  规格驱动开发的前提假设（先写规格再交给 AI 实现）存在根本缺陷：
  - 规格永远是不完整的
  - 模糊性导致幻觉
  - 迭代消耗比直接写代码更多的 token 和时间
  核心问题：**很多开发者是在写代码的过程中完成规划的，而不是规划之后再写代码**
- ## 供应商锁定风险
  重度依赖 Claude 的开发者在 Claude 宕机时会陷入完全停工状态。这是一种组织尚未量化的新型生产力风险。
- ## 作者的实践原则
  Lars Faye 本人的规则集（"像 Ship's Computer 那样用，而不是像 Data 那样用"）：
  1. AI 永远是**辅助进程**，不是主进程
  2. **不生成超过自己能逐行审查的代码**
  3. 只要求 AI 做**你自己也能做的事**
  4. 永远不用 AI 来**第一次理解**一个代码库
  5. 类比：Ship's Computer（给你数据，你决策）vs Data（它替你决策）——只有前者能增强能力
- ## 与其他资料的关系
  - 与 [[source/10-lessons-for-agentic-coding]] 对立/互补：10 条原则倡导拥抱 Agent，本文警告代价
  - 与 [[source/karpathy-vibe-coding-to-agentic-engineering]] 有共鸣：Karpathy 同样强调规格所有权是人的工作
  - 与 [[source/coding-agents-101-devin]] 的检查点架构形成呼应：监督机制是共同关注点
  - 与 [[source/good-context-good-code]] 的 StockApp 数据形成张力：生产力↑ vs 技能↓ 哪个是真相？
- ## 引用此资料的页面
  - [[entity/agentic-coding]]

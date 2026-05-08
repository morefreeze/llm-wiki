---
type:: Source
source-type:: article
author:: stevenpxiao
date:: 2026-04
url:: https://www.bestblogs.dev/article/93462cd7
raw-file:: _raw/harness-knowledge-moat.txt
created:: [[2026-05-06]]
---

- # Harness 不是目的，知识才是护城河
- ## 一句话总结
  > 工作流只是管道，知识才是流过管道的活水——AI 工程团队的真正护城河是领域知识的持续沉淀，而非工作流的复杂程度。
- ## 关键要点
  
  1. **核心论点** — "Harness 不是目的，知识才是护城河"；工作流可替换，知识可累积；知识是团队的复利资产
  2. **Harness 三支柱** — 上下文工程（知识检索注入）× 架构约束（状态机设计）× 持续治理（知识生命周期 + 自动衰减）；知识管理本就是 Harness 核心
  3. **五层 × 五型 × 三级** — Layer 0-P/0-T/1/2/3 × model/decision/guideline/pitfall/process × draft/verified/proven + 自动衰减机制
  4. **独立 Git 仓库** — 团队知识库独立于业务项目，跨项目共享，三角色协作（maintainer/contributor/reader），区块链式贡献记录
  5. **三级渐进式索引** — 借鉴 Karpathy LLM Wiki，knowledge-catalog.md（~50 行）→ catalog.md（~300 行）→ 完整条目，上下文效率提升一个数量级
  6. **人机交互瓶颈** — 工作流依赖人的在场；解法：远程操控 + 跨设备接管（文件系统即状态机 + 异步审批 + 通知触达）
- ## 详细笔记
- ### 三大标志性 Harness 实践对比
  
  | 实践方 | 核心关注 | 关键动作 |
  |--------|---------|---------|
  | OpenAI — Codex | 人机交互协议 | 零手写代码，通过精确指令协议驾驭 Agent |
  | Cursor — Self-Driving | 多 Agent 协同 | 背景 Agent 自动检测冲突并运行测试 |
  | Anthropic — Claude Code | 长时运行稳定性 | 多层记忆 + CLAUDE.md 约束 |
- ### 知识分层架构（三个维度正交）
  
  **存储层（在哪）**：
- Layer 0-P：个人偏好，纯本地不共享
- Layer 0-T：团队约定，团队级 Git 共享
- Layer 1：技术知识，跨项目通用
- Layer 2：业务知识，按业务领域组织
- Layer 3：项目知识，随项目走
  
  知识可"向上提升"：Layer 3 的项目知识若被判定跨项目通用，自动提升到 Layer 1/2。
  
  **知识类型（是什么，MECE）**：model / decision / guideline / pitfall / process
  
  **成熟度（多可信）**：
- draft → verified（在 1 个工作流中被成功引用）→ proven（在 ≥2 个不同项目中被验证）
- 自动衰减：proven 12 月未引用→降级 verified，verified 6 月未引用→降级 draft，draft 长期未引用→归档
- ### 工作流的三个知识关键时刻
  
  1. **INIT（知识注入）**：git pull 知识仓库，注入全景目录到 Agent
  2. **各阶段执行（知识消费）**：Agent 在决策点按需查询，每个阶段有独立查询预算
  3. **ARCHIVE（知识提取）**：@archiver 自动从产物提取知识条目，执行层级提升判定
- ### 三级渐进式索引（借鉴 Karpathy）
  
  ```
  Step 1: knowledge-catalog.md（~50 行）→ 了解全貌，定位分类
  Step 2: catalog.md（~100-300 行）→ 定位相关条目
  Step 3: TK-*.md / BK-*.md（~50-200 行）→ 读完整内容
  Step 4: 原始产物（可选）→ 追溯推导过程
  ```
- ### Big Model vs Big Harness
  
  立场：知识工程的投入是**确定性回报**，模型提升是概率性回报。再强的模型也不知道你业务系统里的隐藏坑。
- ## 与其他资料的关系
- 与 [[source/从玩具到生产力用真实项目讲透-ai-agent-的-harness-engineering]] 互补：前者是 Harness 系统的工程架构，本文聚焦 Harness 之上的知识管理层
- 与 [[source/当我们在讨论-harness-的时候我们在讨论什么]] 呼应：本文给出了"技术护城河在垂直领域知识"这一论断的具体落地方案
- 与 [[source/llm-wiki-pattern]] 深度呼应：本文明确引用 Karpathy LLM Wiki 的三级索引 + Lint 机制，并在工程系统中实现了类似模式
- 补充 [[source/10-lessons-for-agentic-coding]]：Breunig 的"记录意图"和"保持规格同步"原则，与本文的 decision/guideline 知识类型高度一致
- 与 [[source/how-anthropic-teams-use-claude-code]] 呼应：Claude.md 作为持续改进飞轮，正是本文 Layer 0-T/Layer 3 知识层在 Claude Code 生态中的具体形态
- ## 引用此资料的页面
- [[entities/harness]]
- [[entities/knowledge-lifecycle]]
- [[topics/agent-production]]
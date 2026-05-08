---
type:: Entity
created:: [[2026-05-07]]
updated:: [[2026-05-07]]
sources:: [[source/session-continuity-across-sessions]], [[source/initialization-independent-phase]]
related:: [[entity/harness]], [[entity/harness-5-subsystems]], [[entity/repo-as-system-of-record]], [[entity/clean-session-state]], [[entity/feature-list-primitive]]
---

- # 跨会话连续性（Session Continuity）
  
  Agent 每次新会话都会"失忆"——连续性工件（PROGRESS.md + DECISIONS.md）是给失忆工匠的日记本，把重建成本从 15 分钟压到 3 分钟。
- ## 为什么跨会话必然丢信息
  
  不管窗口多大（128K、200K、1M），长任务总会用完。压缩保留"是什么"但丢了"为什么"；重置开新会话但依赖工件完备性。
  
  更深层的问题：中间推理步骤包含决策的"为什么"——为什么选了方案 A 而不是方案 B。压缩通常丢失这些信息，下一个会话可能"优化"掉一个有意为之的设计决策。
- ## 四种连续性工件
  
  | 工件 | 内容 | 解决的问题 |
  |------|------|----------|
  | PROGRESS.md | 已完成/进行中/下一步 + 当前 commit hash | 重复劳动、漂移 |
  | DECISIONS.md | 什么决策、为什么、什么时候 | 决策逆转 |
  | 验证记录 | 哪些测试通过/失败 | 重复诊断 |
  | git 检查点 | 原子工作单元的 commit | 状态快照 |
- ## 上下文焦虑（Context Anxiety）
  
  Anthropic 观察到的现象：当 agent 感觉上下文快满了，它会表现出"过早收敛"行为——匆忙结束当前工作，跳过验证步骤，或选择简单方案而非最优方案。就像考试时发现时间快到了，赶紧随便选选择题。
- ## 漂移（Drift）
  
  每次会话边界都会引入漂移：agent 的理解与代码仓库实际状态之间的偏差，不加控制会越漂越远。几个会话累积下来，实现方向可能悄悄偏离了原始需求。
- ## 压缩 vs 重置：模型相关的策略选择
  
  Anthropic 的实际数据：
- **Sonnet 4.5**：上下文焦虑严重，上下文重置成为 harness 的关键组件
- **Opus 4.5**：这种行为大幅减弱，压缩管理上下文就够了
  
  **结论**：harness 设计需要对目标模型有具体理解，而不是套用通用模板。
- ## 初始化独立阶段：连续性的前置条件
  
  跨会话连续性的前提是第一个会话打好地基。**自举契约（Bootstrap Contract）** 定义项目能被全新 agent 会话无歧义操作的充要条件：
  
  1. **能启动**：`make dev` 能成功
  2. **能测试**：`make test` 至少一个测试通过
  3. **能看进度**：任务分解文件存在且机器可读
  4. **能接手下一步**：新 agent 只看仓库能知道下一步做什么
  
  Anthropic 实验：独立初始化阶段的项目，多会话功能完成率比混合方式高 **31%**。
- ## 实战数据
  
  12 功能点博客系统，5 个会话对比：
  
  |  | 无日记本 | 有日记本 |
  |--|---------|---------|
  | 重建时间 | ~15 分钟/会话 | ~3 分钟/会话（减少 **78%**） |
  | 功能完成率 | 58%（7/12 完成） | 100%（12/12 完成） |
  | 隐含缺陷率 | 43% | 8% |
- ## 参考来源
- [[source/session-continuity-across-sessions]] — 四种连续性工件 + 上下文焦虑 + 漂移 + 实战数据
- [[source/initialization-independent-phase]] — 自举契约 + 独立初始化阶段
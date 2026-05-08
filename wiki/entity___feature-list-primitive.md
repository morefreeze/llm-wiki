---
type:: Entity
created:: [[2026-05-07]]
updated:: [[2026-05-07]]
sources:: [[source/feature-list-as-harness-primitive]]
related:: [[entity/harness]], [[entity/harness-5-subsystems]], [[entity/wip-limit]], [[entity/session-continuity]], [[entity/completion-validation]]
---

- # 功能清单原语（Feature List as Harness Primitive）
  
  功能清单不是给人看的备忘录，是整个 harness 的脊梁骨。调度器、验证器、交接器、进度追踪器都从它派生——脊梁骨断了，全身都瘫。
- ## 核心数据模型：三元组结构
  
  每个功能项是 `(行为描述, 验证命令, 当前状态)` 的三元组，缺一不完整：
  
  ```json
  {
  "id": "F03",
  "behavior": "POST /cart/items with {product_id, quantity} returns 201",
  "verification": "curl -X POST http://localhost:3000/api/cart/items ... | jq .status == 201",
  "state": "passing",
  "evidence": "commit abc123, test output log"
  }
  ```
- **行为描述**：告诉 agent 做什么（可验证的行为规范）
- **验证命令**：告诉 agent 怎么算做完（可执行的完成证据）
- **当前状态**：告诉 agent 现在到哪了（状态机）
- ## 状态机模型
  
  四种状态：`not_started` → `active` → `passing`（或 `blocked`）。
  
  **通过状态门控**：功能从 `active` 变成 `passing` 的唯一方式是验证命令执行成功，由 harness 控制，agent 不能直接改状态。`passing` 状态不可逆。
- ## 功能清单服务的四个 Harness 组件
  
  | 组件 | 功能清单的角色 |
  |------|--------------|
  | **调度器** | 读状态，选下一个 not_started 功能（工厂排产系统） |
  | **验证器** | 执行验证命令，判断是否允许状态转移（质检） |
  | **交接报告器** | 自动生成会话交接摘要（换班交接表） |
  | **进度追踪器** | 统计状态分布，提供健康度指标（仪表盘） |
- ## 粒度控制
  
  每个功能项应该是"一次会话能完成"的范围：
- ✅ "用户可以添加商品到购物车" — 好粒度
- ❌ "实现购物车" — 太粗，做不完
- ❌ "创建 Cart 模型的 name 字段" — 太细，管理开销大
- ## 实战数据
  
  10 个功能点电商平台，对比非结构化笔记和结构化功能清单：
  
  |  | 备忘录模式 | 功能清单原语 |
  |--|--------|--------|
  | 新会话推断状态时间 | 20 分钟 | 3 分钟 |
  | 重复实现 | 有 | 零 |
  | 功能完成率 | 基线 | 高 **45%** |
  
  Anthropic：好的进度记录可以减少 **60-80%** 的会话启动诊断时间。
- ## 参考来源
- [[source/feature-list-as-harness-primitive]] — 功能清单原语完整讲解 + 三元组结构 + 实战数据
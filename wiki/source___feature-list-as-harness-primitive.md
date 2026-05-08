---
type:: Source
tags:: #harness #feature-list #harness-primitive #state-machine #completion-evidence
created:: [[2026-05-07]]
url:: https://walkinglabs.github.io/learn-harness-engineering/zh/lectures/lecture-08-why-feature-lists-are-harness-primitives/
author:: walkinglabs.github.io
raw:: [[source/feature-list-as-harness-primitive]]
---

# 用功能清单约束 Agent 该做什么（Learn Harness Engineering L08）

> **一句话**：功能清单不是备忘录，是整个 harness 的脊梁骨——调度器、验证器、交接器都从它派生；缺了它，所有组件都散架。

## 关键观点

### 1. Agent 不知道"做完"是什么意思

没有功能清单，agent 用隐式标准判断完成——通常是"代码没有明显语法错误"。而实际需要的是端到端行为验证。非结构化的进度记录（"购物车基本完成了"）无法回答：基本完成是什么意思？通过了哪些测试？Anthropic 数据：好的进度记录可以减少 **60-80%** 的会话启动诊断时间。

### 2. 功能清单服务四个 Harness 组件

| 组件 | 功能清单的角色 |
|------|--------------|
| 调度器 | 读状态，选下一个 not_started 功能 |
| 验证器 | 执行验证命令，判断是否允许状态转移 |
| 交接报告器 | 自动生成会话交接摘要 |
| 进度追踪器 | 统计状态分布，提供健康度指标 |

### 3. 三元组结构（核心数据模型）

每个功能项是 `(行为描述, 验证命令, 当前状态)` 三元组，缺一不完整：

```json
{
  "id": "F03",
  "behavior": "POST /cart/items with {product_id, quantity} returns 201",
  "verification": "curl -X POST http://localhost:3000/api/cart/items ... | jq .status == 201",
  "state": "passing",
  "evidence": "commit abc123, test output log"
}
```

### 4. 状态机模型与通过状态门控

四种状态：`not_started` → `active` → `passing`（或 `blocked`）。功能从 `active` 变成 `passing` 的**唯一方式**是验证命令执行成功，由 harness 控制，agent 不能直接改状态。

### 5. 实战数据

10 个功能点电商平台，两种追踪方式：

|  | 备忘录模式 | 脊梁骨模式（三元组清单） |
|--|--------|--------|
| 新会话推断状态时间 | 20 分钟 | 3 分钟 |
| 重复实现 | 有 | 零 |
| 功能完成率 | 基线 | 高 **45%** |

## 相关实体

- [[entity/feature-list-primitive]] — 功能清单原语核心概念
- [[entity/wip-limit]] — WIP=1 与功能清单状态机结合使用
- [[entity/session-continuity]] — 功能清单是跨会话连续性的关键工件

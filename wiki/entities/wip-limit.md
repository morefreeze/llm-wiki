---
type:: Entity
created:: [[2026-05-07]]
updated:: [[2026-05-07]]
sources:: [[wip-limit-task-boundaries]]
related:: [[harness]], [[harness-5-subsystems]], [[feature-list-primitive]], [[completion-validation]]
---

# WIP 限制与任务边界（WIP Limit）

WIP=1 是 agent harness 的默认安全设置——"少做但做完"永远优于"多做但做半"。Agent 生成代码行数和实际完成功能数量呈弱负相关：写得越多，完成得越少。

## Overreach 与 Under-finish

**过度延伸（Overreach）**：agent 在一次会话中激活的任务数量超过最优值。可量化——同时做 5 个功能但 0 个跑通，就是 overreach。

**不足完成（Under-finish）**：已启动的任务中，通过端到端验证的比例低于阈值。写了代码但没跑通测试，就是 under-finish。

这两个问题不是独立的，而是互相加剧形成恶性循环：overreach → 注意力分散 → under-finish → 半成品代码增加复杂度 → 下一个任务更容易 overreach。

## 数学基础

注意力是有限资源：上下文容量 C，同时激活 k 个任务，每任务获得 C/k 推理资源。当 C/k 低于完成单个任务的最小阈值时，所有任务都做不完。

Kanban 的 Little 法则：L = λ × W（在制品数量 × 前置时间 = 吞吐量的倒数）。在制品 L 过大，前置时间 W 必然增加。

## 核心机制

| 机制 | 说明 |
|------|------|
| **WIP 限制** | 来自 Kanban，对 agent WIP=1 是最安全默认值 |
| **完成证据** | 任务变"完成"必须满足的可执行验证条件 |
| **范围表面（DAG）** | 工作单元节点 + 依赖边，状态：not_started/active/blocked/passing |
| **验证完成率（VCR）** | 已通过验证任务数 / 已启动任务数，VCR<1.0 时阻止新任务启动 |
| **完成压力** | WIP 限制 + 完成证据共同产生的约束力 |

## 实战数据

8 个功能点 REST API，两种策略：

|  | 自助餐模式（无约束） | 单盘模式（WIP=1） |
|--|--------|--------|
| 第一个会话同时启动 | 5 个功能 | 1 个功能 |
| 代码行数 | ~800 行 | ~200 行 |
| 端到端通过率 | 20% | 100% |
| 最终完成率 | 37.5%（3/8） | 87.5%（7/8） |

总代码量更少（800 行 vs 1200 行），但有效代码更多。一口一口吃，反而吃得最多。

Anthropic 实验数据：使用"小下一步"策略（等价于 WIP=1）的 agent，任务完成率比使用宽泛提示的 agent 高 **37%**。

## Harness 实施

在 CLAUDE.md 里显式写明：
- 任何时刻只允许一个任务处于"进行中"
- 端到端验证通过后才能开始下一个
- 完成证据必须是可执行的（不是"代码看起来没问题"，而是"curl 返回 201"）
- 范围表面外部化为机器可读文件
- VCR < 1.0 时阻止新任务启动

## 参考来源

- [[wip-limit-task-boundaries]] — WIP=1 + Overreach/Under-finish 完整讲解 + 实战数据

---
type:: Source
tags:: #harness #harness-engineering #five-subsystems #agent-infrastructure
created:: [[2026-05-07]]
url:: https://walkinglabs.github.io/learn-harness-engineering/zh/lectures/lecture-02-what-a-harness-actually-is/
author:: walkinglabs.github.io
raw:: [[harness-what-it-actually-is]]
---

# Harness 到底是什么（Learn Harness Engineering L02）

> **一句话**：Harness 由五个子系统组成——指令、工具、环境、状态、反馈——缺少任何一个都不是完整的 harness。

## 关键观点

### 1. Harness 不只是一个 prompt 文件

大部分人说的 harness 其实只是"一个 prompt 文件"。这不是 harness。就像你开了一家餐厅，只有食材——没有灶台、没有刀具、没有菜谱、没有出菜流程——那不叫餐厅，那叫冰箱。

### 2. 五子系统模型（厨房类比）

| 子系统 | 厨房类比 | 核心作用 |
|--------|---------|---------|
| **指令**（AGENTS.md 50-200行） | 菜谱架 | Agent 知道"该做什么" |
| **工具**（shell + 最小权限） | 刀具架 | Agent 有能力执行 |
| **环境**（锁定依赖 + 版本） | 灶台 | 稳定的运行基础 |
| **状态**（PROGRESS.md） | 备菜台 | 跨会话的工作记录 |
| **反馈**（验证命令） | 出菜检查口 | 判断是否做对了 |

### 3. 反馈子系统的高投入产出比

反馈子系统（验证命令）的投入产出比最高。一个简单的 `make test` 命令就能把 agent 的成功率从 20% 提升到 100%——因为 agent 现在知道自己做没做对，而不是凭感觉猜。

### 4. 真实数据：成功率从 20% → 100%

4 阶段实验对比：
- 阶段 1（空厨房）：agent 完全没有 harness，成功率约 20%
- 阶段 2（加菜谱架）：只有 AGENTS.md，成功率约 45%
- 阶段 3（加出菜检查口）：有指令+验证，成功率约 80%
- 阶段 4（加备菜台）：完整五子系统，成功率约 100%

### 5. Harness 和代码一样会腐化

> "Harness 和代码一样会腐化，要还 harness 债。"

如果 harness 不随项目一起更新，它描述的项目状态就和实际代码脱节了——就像菜谱上写的是上个月的食材和做法，而厨房里的食材已经全换了。

## 相关实体

- [[harness-5-subsystems]] — 五子系统模型详解
- [[harness]] — Harness 驾驭层核心概念

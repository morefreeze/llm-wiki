---
type:: Source
tags:: #harness #wip-limit #overreach #under-finish #task-boundaries #kanban
created:: [[2026-05-07]]
url:: https://walkinglabs.github.io/learn-harness-engineering/zh/lectures/lecture-07-why-agents-overreach-and-under-finish/
author:: walkinglabs.github.io
raw:: [[source/wip-limit-task-boundaries]]
---

# 给 Agent 划清每次任务的边界（Learn Harness Engineering L07）

> **一句话**：WIP=1 是 agent harness 的默认安全设置——"少做但做完"永远优于"多做但做半"，代码行数与功能完成率呈弱负相关。

## 关键观点

### 1. 注意力是有限的资源（数学）

上下文容量 C，同时激活 k 个任务，每任务平均 C/k 推理资源。当 C/k 低于完成单个任务的最小阈值时，所有任务都做不完。Anthropic 实验：使用"小下一步"策略（等价于 WIP=1）的 agent，任务完成率比宽泛提示高 **37%**。agent 生成代码行数和完成功能数量呈**弱负相关**。

### 2. Overreach 与 Under-finish 互相加剧

过度延伸（Overreach）→ 注意力分散 → 不足完成（Under-finish）→ 半成品代码增加系统复杂度 → 下一个任务更容易 overreach。Kanban 的 Little 法则：L = λ × W，在制品 L 过大，前置时间 W 必然增加。

### 3. 核心概念表

| 概念 | 定义 |
|------|------|
| Overreach | 一次会话激活任务数超过最优值（可量化） |
| Under-finish | 已启动任务中端到端通过率低于阈值 |
| WIP 限制 | 来自 Kanban，对 agent WIP=1 是最安全默认值 |
| 完成证据 | 任务变"完成"必须满足的可验证条件 |
| 范围表面 | DAG 结构，节点=工作单元，状态四种：not_started/active/blocked/passing |
| 验证完成率（VCR） | 已通过验证任务数 / 已启动任务数，VCR<1.0 时阻止新任务启动 |

### 4. 实战数据

8 个功能点 REST API，两种策略：

|  | 自助餐模式（无约束） | 单盘模式（WIP=1） |
|--|--------|--------|
| 第一个会话同时启动 | 5 个功能 | 1 个功能 |
| 代码行数 | ~800 行 | ~200 行 |
| 端到端通过率 | 20% | 100% |
| 3-4 个会话完成功能 | 37.5%（3/8） | 87.5%（7/8） |

### 5. Harness 实施要点

在 CLAUDE.md 里显式写明：
- 任何时刻只允许一个任务处于"进行中"
- 端到端验证通过后才能开始下一个
- 范围表面外部化为机器可读文件
- VCR < 1.0 时阻止新任务启动

## 相关实体

- [[entity/wip-limit]] — WIP 限制 + Overreach + Under-finish 核心概念
- [[entity/feature-list-primitive]] — 范围表面和功能清单是承载任务边界的数据结构
- [[entity/harness-5-subsystems]] — 任务边界控制是 harness 状态子系统的组成部分

---
type:: Source
tags:: #harness #observability #sprint-contract #task-trajectory #multi-agent #evaluator
created:: [[2026-05-07]]
url:: https://walkinglabs.github.io/learn-harness-engineering/zh/lectures/lecture-11-why-observability-belongs-inside-the-harness/
author:: walkinglabs.github.io
raw:: [[entity/harness-observability]]
---

# 让 Agent 的运行过程可观测（Learn Harness Engineering L11）

> **一句话**：没有可观测性，agent 在不确定状态中做决策——harness 必须内置双层可观测性（运行时 + 过程），缺失导致 30-50% 的会话时间浪费在重复诊断上。

## 关键观点

### 1. 可观测性缺失的四类系统性问题

| 问题 | 说明 |
|------|------|
| 无法区分"正确"和"看似正确" | 只有运行时追踪能揭示执行路径偏离 |
| 评估变成玄学 | 缺评分标准，同一输出不同评估者给出截然不同评价 |
| 重试变成盲猜 | 不知为何失败，随机重试方向，消耗 token 和时间 |
| 会话交接信息断崖 | 新会话从零诊断系统状态，占总时间 30-50% |

### 2. 双层可观测性

**运行时可观测性**：系统层信号（日志、追踪、进程事件、健康检查）。回答"系统做了什么"。类比：仪表盘（速度、油量、发动机温度）。

**过程可观测性**：harness 决策工件可见性（计划、评分标准、验收条件）。回答"为什么这个变更应该被接受"。类比：导航系统（知道在哪、为何走这条路）。

### 3. 核心概念

| 概念 | 定义 |
|------|------|
| 任务轨迹（Task Trajectory） | 任务完整决策路径记录，类似分布式系统请求追踪 |
| 冲刺合同（Sprint Contract） | 编码开始前协商的短期协议，约定范围、验证标准、排除项 |
| 评估评分标准 | 把质量评估变成结构化评分，使评估可复现 |

### 4. Anthropic 三 Agent 架构实验数据

"用 Web Audio API 做一个浏览器端 DAW"任务，三种角色 + 完整可观测性：

| Agent 和阶段 | 时长 | 成本 |
|-------------|------|------|
| Planner（规划者） | 4.7 分钟 | $0.46 |
| Build 第 1 轮 | 2 小时 7 分钟 | $71.08 |
| QA 第 1 轮 | 8.8 分钟 | $3.24 |
| Build 第 2 轮 | 1 小时 2 分钟 | $36.89 |
| QA 第 2 轮 | 6.8 分钟 | $3.09 |
| Build 第 3 轮 | 10.9 分钟 | $5.88 |
| QA 第 3 轮 | 9.6 分钟 | $4.06 |
| **总计** | **3 小时 50 分钟** | **$124.70** |

Evaluator 用 Playwright MCP 像用户一样点击运行中的应用，按四个维度评分（产品深度、功能性、视觉设计、代码质量），任一维度不达阈值则 sprint 失败。

### 5. OpenTelemetry 标准化

每个 harness 会话创建一个 trace，每个任务创建一个 span，每个验证步骤创建子 span，可接入 Jaeger/Zipkin 等标准工具链。

## 相关实体

- [[entity/harness-observability]] — 双层可观测性 + 冲刺合同核心概念
- [[entity/completion-validation]] — Evaluator 和评分标准是完成校验的可观测形式
- [[entity/harness-5-subsystems]] — 可观测性属于反馈子系统的扩展

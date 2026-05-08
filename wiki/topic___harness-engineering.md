---
type:: Topic
tags:: #harness #harness-engineering #agent-infrastructure #long-running-agents
created:: [[2026-05-08]]
sources:: [[source/harness-what-it-actually-is]] [[source/why-repo-is-system-of-record]] [[source/instruction-file-architecture]] [[source/session-continuity-across-sessions]] [[source/initialization-independent-phase]] [[source/wip-limit-task-boundaries]] [[source/feature-list-as-harness-primitive]] [[source/prevent-premature-completion]] [[source/e2e-testing-changes-results]] [[source/why-observability-belongs-in-harness]] [[source/why-sessions-must-leave-clean-state]]
---

# Harness Engineering

> 如何系统地设计和维护 AI coding agent 的运行框架（harness），使 agent 在长期、多会话的真实项目中保持高可靠性。

课程来源：[Learn Harness Engineering](https://walkinglabs.github.io/learn-harness-engineering/zh/)（walkinglabs.github.io，Lectures 02-12）

## 核心问题

Agent 单次跑通原型很容易，但要在真实项目里持续、可靠地工作，需要解决：

- **失忆问题**：每次新会话 agent 都从头开始，如何让知识跨会话积累？
- **漂移问题**：多个会话累积下来，实现方向如何不偏离原始需求？
- **完成问题**：agent 系统性地过度自信，如何确保"说完成"就真的完成？
- **熵增问题**：不加干预的系统复杂性必然增加，如何对抗代码库退化？

## 11 讲总览

### 基础层：框架定义与基础设施

| 讲次 | 主题 | 核心实体 | 关键数据 |
|------|------|---------|---------|
| L02 | [[entity/harness-5-subsystems]] | 五子系统（指令/工具/环境/状态/反馈） | 成功率 20%→100% |
| L03 | [[entity/repo-as-system-of-record]] | 仓库即规范 + 知识可见性缺口 | 人工介入降低 60% |
| L04 | [[entity/instruction-architecture]] | 路由文件 + 中间迷失效应（Liu 2023） | 任务成功率 45%→72% |

### 连续性层：跨会话稳定性

| 讲次 | 主题 | 核心实体 | 关键数据 |
|------|------|---------|---------|
| L05 | [[entity/session-continuity]]（连续性工件） | PROGRESS.md + DECISIONS.md + 上下文焦虑 | 重建时间降 78% |
| L06 | [[entity/session-continuity]]（初始化阶段） | 自举契约四条件 + 冷/热启动 | 完成率高 31% |
| L12 | [[entity/clean-session-state]] | 清洁状态五维度 + 会话完整性 | 12 周熵增对比 |

### 任务层：范围控制与完成保证

| 讲次 | 主题 | 核心实体 | 关键数据 |
|------|------|---------|---------|
| L07 | [[entity/wip-limit]] | WIP=1 + Overreach/Under-finish + VCR | 完成率 87.5% vs 37.5% |
| L08 | [[entity/feature-list-primitive]] | 功能清单三元组 + 通过状态门控 | 完成率高 45% |
| L09 | [[entity/completion-validation]]（完成校验） | 三层终止校验 + planner/generator/evaluator | $9 不可用 vs $200 可用 |
| L10 | [[entity/completion-validation]]（E2E 测试） | 单元测试盲区 + E2E 改变 agent 行为 | 5 个缺陷全捕获 |

### 可观测性层

| 讲次 | 主题 | 核心实体 | 关键数据 |
|------|------|---------|---------|
| L11 | [[entity/harness-observability]] | 双层可观测性 + 冲刺合同 + 三 agent 实验 | 3h50m，$124.70 |

## 核心原则

1. **Harness 是五子系统，不是一个 prompt 文件** — 缺任何一个都不完整
2. **仓库是唯一的事实来源** — 知识必须在仓库里可发现，不能在脑子里
3. **先打地基再砌墙** — 初始化和实现的目标不同，混在一起互相拖后腿
4. **WIP=1 是默认安全设置** — "少做但做完"永远优于"多做但做半"
5. **完成判定必须外部化** — agent 系统性地过度自信，harness 独立验证
6. **清洁状态是完成的必要条件** — 熵增是默认状态，主动清理才能对抗
7. **Harness 和代码一样会腐化** — 随模型能力提升，定期简化不再必要的组件

## 参见

- [[entity/harness]] — Harness 驾驭层核心概念
- [[entity/coding-harness]] — 编程运行框架六大组件（Raschka 视角）
- [[topic/agent-production]] — Agent 生产化（与本 topic 部分重叠）
- [[topic/agentic-developer-practices]] — 开发者实践（任务管理视角）

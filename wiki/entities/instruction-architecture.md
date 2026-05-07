---
type:: Entity
created:: [[2026-05-07]]
updated:: [[2026-05-07]]
sources:: [[instruction-file-architecture]]
related:: [[harness]], [[harness-5-subsystems]], [[repo-as-system-of-record]], [[session-continuity]]
---

# 指令文件架构（Instruction File Architecture）

指令膨胀是 harness 工程的常见陷阱——自然的恶性循环：agent 犯错 → 加规则 → 文件膨胀 → 性能更差 → 更多规则。三个月后 600 行的 AGENTS.md 反而让 agent 表现变差。

## 巨型指令文件的三个核心问题

| 问题 | 说明 |
|------|------|
| **上下文预算被吃掉** | 600 行指令 ≈ 10,000-20,000 tokens，占 128K 窗口 8-15% |
| **中间迷失效应** | Liu et al. 2023 证明 LLM 对长文本中间部分的信息利用率显著低于两端 |
| **优先级冲突** | 硬约束和历史备注在文件里看起来一模一样，agent 无法区分 |

## 中间迷失效应（Lost in the Middle）

Liu et al. 2023 NeurIPS 论文：当关键信息出现在长文本中间时，LLM 的利用率显著下降——哪怕输入完全在上下文窗口内。

**实践含义**：600 行 AGENTS.md 里，第 300 行的安全硬约束（如"所有数据库查询必须用参数化查询"），被 agent 有效忽略的概率非常高。

## 路由文件架构（Router File Pattern）

**短 AGENTS.md（50-200 行）** 作为路由文件：
- 项目概览（2-3 句话）
- 启动/测试命令（具体命令，不解释）
- 全局硬约束（不超过 15 条）
- 指向专题文档的链接（一行描述 + 适用场景）

**专题文档（50-150 行/文件）** 按需加载：
```
docs/api-patterns.md      — 添加新端点时读
docs/database-rules.md    — 涉及数据库修改时读
docs/testing-standards.md — 编写测试时读
```

## 渐进式披露（Progressive Disclosure）

好的 harness 设计和好的 UI 设计一样：先给概要，需要时再给细节。

**指令 SNR（信噪比）**：文件中与当前任务相关的指令占总指令的比例。做 bug 修复时被要求读 50 行部署指令——SNR 很低，降低 agent 性能。路由文件架构最大化 SNR。

## 实战数据

一个 SaaS 团队把 600 行 AGENTS.md 重构为 80 行路由文件 + 3 个专题文档：

- 任务成功率：**45% → 72%**
- 安全约束遵循率：**60% → 95%**

## 参考来源

- [[instruction-file-architecture]] — 路由文件架构详细讲解 + 中间迷失效应实践含义

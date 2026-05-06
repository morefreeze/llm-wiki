---
type:: Entity
created:: [[2026-05-06]]
sources:: [[从玩具到生产力-用真实项目讲透AI-Agent的Harness-Engineering]], [[当我们在讨论Harness的时候我们在讨论什么]], [[Anthropic-MCP-博客]]
related:: [[mcp]], [[skills]], [[code-mode]], [[agent]], [[tool-use]], [[safety]]
---

# Harness（驾驭层）

Harness 是 [[agent]] 与外部世界交互时的「安全带」和「方向盘」——一个介于 AI 推理能力与真实世界之间的**约束层 / 驾驭层**。

## 核心定义

Harness **不是框架，也不是工具**。它是包裹在 Agent 外部的一层控制结构，负责回答一个关键问题：

> Agent 有了能力之后，**怎么安全地、可控地**使用这些能力？

如果把 [[agent]] 的 LLM 推理能力比作发动机，那么 Harness 就是变速箱、刹车系统和方向盘的总称。

## 核心组件

| 组件 | 职责 |
|------|------|
| **输入验证** | 校验用户输入与外部数据的合法性、安全性，防止注入攻击 |
| **输出过滤** | 过滤 Agent 生成内容中的敏感信息、有害内容或格式错误 |
| **权限控制** | 限定 Agent 可访问的资源范围与操作边界 |
| **错误处理** | 捕获异常、优雅降级、防止连锁故障 |
| **日志记录** | 全链路追踪 Agent 行为，支撑审计与调试 |

## 与相关概念的区别

### Harness vs 工具（Tools）
工具是 Agent 的「手」，解决「能做什么」；Harness 是 Agent 的「缰绳」，解决「能安全地做什么」。工具扩展能力，Harness 约束行为。

### Harness vs [[skills]]
[[skills]] 描述 Agent 会什么（能力层），Harness 描述 Agent 怎么用这些能力（治理层）。两者正交组合。

### Harness vs [[mcp]]
[[mcp]]（Model Context Protocol）提供了标准化的工具调用协议，是 Harness 可以**接入**的底层基础设施之一。Harness 可以基于 MCP 协议实现权限拦截、调用审计等治理逻辑。

### Harness vs [[code-mode]]
[[code-mode]] 是 Agent 的一种工作模式（直接生成和执行代码），而 Harness 定义了 code-mode 运行时的安全边界——比如沙箱隔离、文件系统白名单、执行超时等。

## 为什么重要

从玩具到生产力的关键跃迁，不在于模型能力的提升，而在于 Harness 的成熟度：

1. **可靠性**：没有 Harness 的 Agent 在生产环境中是不可信的
2. **可观测性**：Harness 提供的日志与追踪是运维的基础
3. **合规性**：企业场景对数据安全和行为可控有硬性要求
4. **迭代效率**：良好的 Harness 设计让 Agent 能力的迭代与安全策略解耦

## 设计原则

- **最小权限**：默认拒绝，按需授权
- **纵深防御**：不依赖单一安全机制，多层校验
- **显式优于隐式**：关键决策点应有明确的拦截点和日志
- **可配置可热更新**：安全策略应能独立于 Agent 逻辑进行调整

## 参考来源

- [[从玩具到生产力-用真实项目讲透AI-Agent的Harness-Engineering]] — 系统性阐述 Harness Engineering 的工程实践
- [[当我们在讨论Harness的时候我们在讨论什么]] — MiniMax × Hermes Agent 对谈，厘清 Harness 的概念边界
- [[Anthropic-MCP-博客]] — 间接涉及安全、认证、可控性等 Harness 关注的核心议题

---
type:: Entity
tags:: #agent #coding #developer-workflow
created:: [[2026-05-07]]
sources:: [[karpathy-vibe-coding-to-agentic-engineering]]
related:: [[agentic-coding]], [[software-3-0]], [[harness]], [[claude-md-files]]
---

# Vibe Coding（凭感觉编程）

Karpathy 于 2025 年 2 月在 X 上提出的词汇（Collins 词典 2025 年度词汇）：放弃对代码本身的直接控制，顺着感觉让 AI 模型往前走的开发体验。

## 定义

> 人用自然语言持续提出意图，模型生成、修改、调试代码，人不再像过去那样逐行写、逐行读 diff。

Vibe Coding 的核心特征：
- 人提供**方向**（意图、目标、约束），不提供**实现**
- 对模型输出的信任逐步建立，最终进入"不再修改"的状态
- 适合 side project、探索性开发、快速原型

Karpathy 的个人转折点（2025 年 12 月）：最新模型生成的代码块开始"直接能用"，他进入真正的 Vibe Coding 状态，已经记不清上次修改 AI 生成的代码是什么时候了。

## Vibe Coding vs Agentic Engineering

这是 Karpathy 访谈中最重要的区分之一：

| 维度 | Vibe Coding | Agentic Engineering |
|------|------------|---------------------|
| **目标** | 抬高软件创作的**下限** | 保住专业软件的**质量上限** |
| **适用** | 个人工具、side project、探索性开发 | 生产级系统、有安全/合规要求的软件 |
| **对代码的态度** | 能跑就好，可能很丑 | 质量、安全、可维护性不妥协 |
| **责任** | 个人承担 | 工程纪律（规格、验证、审计） |
| **门槛** | 任何人 | 需要经验：规格设计、风险识别、质量判断 |

> Vibe Coding 抬高的是所有人能做软件的下限；Agentic Engineering 要保住的是专业软件过去已有的质量门槛。

## Vibe Coding 的现实张力

**Karpathy 同时承认两件事：**
1. 他已经很久没有修改模型输出了（信任感建立）
2. 他有时看到模型生成的代码会"心脏病发作"——能跑，但臃肿/复制粘贴/结构脆弱

这种"用着丑的，但用着"的状态，可能比任何 hype 都更接近 Vibe Coding 的真实现状：**信任并没有解决品味的问题**。

## Agentic Engineering 的工程纪律

Agent 是"spiky entities"（有尖刺的实体）：能力很强，会犯错，有随机性，不稳定。

Agentic Engineering 不是工具，而是工程纪律：如何设计、协调、监督一组 AI Agent，在不牺牲质量/安全/可维护性的情况下加速开发。

具体：
- 把 Agent 放进合适的流程（生成→测试→验证→回滚）
- **规格（spec）是人的工作**：Agent 负责实现细节，人负责系统边界、数据归属、质量标准
- 设置安全验证机制（如"用多个 Agent 作为红队攻击"）
- 识别 Agent 能力边界（锯齿状智能的高峰和断崖）

> "10x 不是你获得的加速倍数。" — 真正熟练的人加速幅度远不止 10 倍

## 关联

- [[agentic-coding]] — Vibe Coding 和 Agentic Engineering 都属于 Agentic Coding 范式，但分别对应不同成熟度和场景
- [[software-3-0]] — Vibe Coding 是 Software 3.0 时代的一种编程形式
- [[harness]] — Agentic Engineering 需要 Harness 层来保住质量上限
- [[living-specs]] — "规格是人的工作"与活规格文档实践高度一致
- [[checkpoint-workflow]] — Agentic Engineering 中重要的安全网机制

## 来源

- [[karpathy-vibe-coding-to-agentic-engineering]] — Karpathy 在 Sequoia AI Ascent 2026 的访谈，系统阐述 Vibe Coding vs Agentic Engineering

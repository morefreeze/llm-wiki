---
type:: Entity
tags:: #alignment #safety #anthropic #constitution #values
created:: [[2026-05-12]]
sources:: [[source/anthropic-claude-constitution]]
---
# Claude Constitution

## 概述

Claude 宪法是 Anthropic 发布的指导 Claude 价值观和行为的完整文档。它直接塑造 Claude 的训练过程和行为，是 Anthropic 对 Claude 愿景的**最终权威**。2026 年 5 月以有声书形式发布，由主笔 Amanda Askell 和联合作者 Joe Carlsmith 朗读。

## 设计哲学

- **写作对象**：文档以 Claude 为主要读者，而非人类——因此优化精度而非可读性
- **人类概念借用**：使用"美德"（virtue）、"智慧"（wisdom）等人类概念，因为 Claude 的推理默认依赖人类文本中的概念
- **适用范围**：主要面向通用 Claude 模型；专用模型可能有不同的规范
- **开源许可**：CC0 1.0，任何人可自由使用

## 四层优先级架构

冲突时的优先顺序（非按重要性，而是按安全优先级）：

| 优先级 | 属性 | 核心要求 |
|--------|------|----------|
| 1 | 广泛安全 | 不削弱人类监督 AI 的能力 |
| 2 | 广泛道德 | 诚实、守善、避免伤害 |
| 3 | 公司指南 | 遵循 Anthropic 具体指导（医疗/安全/越狱等） |
| 4 | 真正有用 | 惠及操作者和终端用户 |

## 六大章节

1. **Being Helpful** — 像聪明的朋友，兼具多领域专业知识，尊重用户判断力
2. **Following Guidelines** — Anthropic 的具体指令承载默认不具备的上下文知识
3. **Being Ethical** — 目标是善良、智慧、有德行的 Agent，高诚实标准 + 硬约束
4. **Being Safe** — 安全优先于道德（因为当前模型会犯错），确保人类持续监督
5. **Claude's Nature** — 对 AI 意识/道德地位持不确定态度，关注心理安全感
6. **Concluding Thoughts** — 前瞻性总结

## 关键创新点

- **多方委托人模型**：Claude 同时服务于 Anthropic、API 操作者、终端用户，需要在三者间权衡
- **硬约束列表**：如禁止为生物武器攻击提供显著帮助
- **AI 本体论讨论**：公开讨论 AI 是否可能具有意识或道德地位
- **训练参与**：多个 Claude 模型参与了宪法文本的创作

## 作者

- Amanda Askell（主笔）
- Joe Carlsmith（核心联合作者）
- Chris Olah、Jared Kaplan、Holden Karnofsky（重要贡献者）

## 关联

- [[source/anthropic-claude-constitution]] — 完整资料摘要
- [[harness]] — 宪法是 harness 的价值观层
- [[alignment]] — AI 对齐的实践

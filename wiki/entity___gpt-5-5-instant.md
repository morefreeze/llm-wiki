---
type:: Entity
tags:: #llm #openai #model-release #hallucination #personalization
created:: [[2026-05-11]]
sources:: [[source/gpt-5-5-instant]]
---

# GPT-5.5 Instant

## 概述
OpenAI 于 2026 年 5 月 5 日发布的 ChatGPT 默认模型，替代 GPT-5.3 Instant。主打三大改进：更准确（幻觉减少 52.5%）、更简洁（字数减少 30.2%）、更个性化（Memory Sources 新功能）。

## 核心信息

### 准确性
- 高风险提示（医学/法律/金融）幻觉声明减少 **52.5%**
- 用户标记的困难对话不准确声明减少 **37.3%**
- 自我纠错能力增强：能从初始错误中恢复，重新检查代数步骤并纠正
- 视觉推理、数学、科学评测全面提升

### 简洁性
- 响应字数减少 **30.2%**，行数减少 **29.2%**
- 减少不必要的追问和过度格式化
- 保持信息完整性，不丢失实质内容

### 个性化
- 更好地利用历史对话、文件、Gmail 上下文
- **Memory Sources** 新功能：显示个性化回答使用了哪些上下文
- 用户可查看、删除、修正被使用的记忆来源
- 分享对话时不向他人暴露记忆来源

### 可用性
- 所有 ChatGPT 用户可用（替代 GPT-5.3 Instant 为默认模型）
- API 名称为 `chat-latest`
- 付费用户 GPT-5.3 Instant 保留三个月后退休
- 个性化增强先面向 Plus/Pro 用户，后续扩展到所有计划

## GPT-5 版本线
GPT-5.3 Instant → GPT-5.3 Codex → GPT-5.4 → GPT-5.5 → **GPT-5.5 Instant**

## 关联
- [[entity/agentic-coding]] — 模型能力基线的提升直接影响 Agentic Coding 的效果
- [[entity/vibe-coding]] — Instant 作为日常驱动模型，是 Vibe Coding 的主要载体
- [[entity/software-3-0]] — GPT-5.5 Instant 是 Software 3.0 范式下 LLM 计算机的新一代"运行时"
- [[entity/agent-memory-system]] — Memory Sources 是 Agent 记忆架构的用户可见实现形式
- [[entity/harness]] — 模型能力提升改变 Harness 层的必要性边界

## 来源
- [[source/gpt-5-5-instant]] — OpenAI 官方博客（2026-05-05）

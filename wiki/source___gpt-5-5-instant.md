---
type:: Source
source-type:: article
author:: OpenAI
date:: 2026-05-05
url:: https://openai.com/index/gpt-5-5-instant
raw-file:: _raw/gpt-5-5-instant.txt
created:: [[2026-05-11]]
---

# GPT-5.5 Instant: smarter, clearer, and more personalized

## 一句话总结
> OpenAI 发布 GPT-5.5 Instant 作为 ChatGPT 新默认模型，幻觉减少 52.5%，响应更简洁（字数减少 30.2%），并推出 Memory Sources 个性化控制功能。

## 关键要点

1. **幻觉大幅减少** — 在高风险提示（医学、法律、金融）上，幻觉声明比 GPT-5.3 Instant 减少 52.5%；在用户标记的事实错误对话中，不准确声明减少 37.3%
2. **更简洁的回答** — 响应使用 30.2% 更少的词、29.2% 更少的行，同时保持信息完整性；减少不必要的追问和过度格式化（如滥用 emoji）
3. **自我纠错能力增强** — 在数学推理对比示例中，GPT-5.5 Instant 能从初始错误中恢复，发现代数步骤错误并纠正，而 GPT-5.3 停在"无实数解"的错误结论
4. **更强的个性化** — 更有效地利用历史对话、文件、Gmail 上下文，更快速搜索历史对话找到相关上下文
5. **Memory Sources（记忆来源）** — 新增功能，让用户看到个性化回答使用了哪些上下文（保存的记忆、历史对话），可删除或修正过时信息；分享对话时不会向他人展示记忆来源
6. **可用性** — 所有 ChatGPT 用户可用，API 中为 `chat-latest`；付费用户 GPT-5.3 Instant 保留三个月后退休

## 详细笔记

### 准确性提升
- GPT-5.5 Instant 在内部评测中展现了全面的准确性改进
- 视觉推理、数学、科学等领域评测分数均有提升
- 在 STEM 相关问题解答和图片分析方面有改进
- 更智能地判断何时需要调用网络搜索以提供更好的答案

### 回答质量对比
文章提供了多个 GPT-5.3 vs GPT-5.5 的对比示例：
- **数学推理**：GPT-5.5 能发现用户代数步骤错误（展开 $(x-1)^2$ 错误），重新求解正确的二次方程，给出精确解 $\frac{3+\sqrt{33}}{2}$
- **写作建议**：GPT-5.5 更简洁实用，直接给出不同场景的脚本，围绕边界而非对方性格来框架问题

### 个性化与隐私
- Memory Sources 功能向所有 ChatGPT 消费用户开放（Web 端先上，移动端即将推出）
- 增强的个性化功能（历史对话/文件/Gmail）先面向 Plus 和 Pro 用户（Web），后续扩展到 Free/Go/Business/Enterprise
- 用户始终控制记忆内容：可删除对话、修改保存的记忆、使用不更新记忆的临时对话

### 产品定位
- Instant 是"日常驱动"模型，服务数亿用户
- GPT-5 系列版本线：GPT-5.3 Instant → GPT-5.3 Codex → GPT-5.4 → GPT-5.5 → GPT-5.5 Instant
- 从导航栏可见 OpenAI 同期还在测试 ChatGPT 广告和推出 GPT-Realtime-2

## 与其他资料的关系
- 与 [[source/karpathy-vibe-coding-to-agentic-engineering]] 中的"锯齿状智能"概念相关：GPT-5.5 的自我纠错能力体现了 LLM 能力曲线的非线性特征
- 与 [[source/hermes-agent-memory-system]] 中的记忆架构相关：Memory Sources 是 Agent/助手记忆系统的一种用户可见实现
- 补充了 [[entity/agentic-coding]] 中模型能力基线的信息：新一代模型在推理和简洁性上的进步直接影响编码 Agent 的表现

## 引用此资料的页面
- [[entity/gpt-5-5-instant]]
- [[entity/agentic-coding]]

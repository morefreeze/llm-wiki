---
type:: Source
source-type:: article
author:: 宝玉（整理/翻译）
date:: 2026-04-29
url:: https://baoyu.io/blog/andrej-karpathy-from-vibe-coding-to-agentic-engineering
raw-file:: _raw/karpathy-vibe-coding-to-agentic-engineering.txt
created:: [[2026-05-07]]
---

# Karpathy 最新访谈：Vibe Coding 只是开始，真正重要的是 Agentic Engineering

## 一句话总结
> Vibe Coding 抬高了所有人做软件的下限；Agentic Engineering 要保住专业软件的质量上限——代码生成变便宜，但理解、规格和判断变得更珍贵。

## 关键要点

1. **Software 3.0 范式** — LLM 是新的可编程计算机；context window 是程序，prompt 是源码；"哪一段文字该复制给 Agent"是新的编程问题
2. **Vibe Coding vs Agentic Engineering** — Vibe Coding 抬高软件创作的下限（所有人都能做）；Agentic Engineering 在使用 Agent 时保住质量、安全、责任的上限
3. **锯齿状智能（jagged intelligence）** — LLM 能力曲线不是平滑上升，而是有高峰和断崖；能力分布由 RL 训练覆盖的领域决定，不由"模型整体智能"决定
4. **可验证性驱动 RL** — 传统软件自动化"你能写进代码的"；LLM 自动化"你能验证的"；可验证=能进入 RL 环境=能力突破
5. **幽灵心智模型** — LLM 是幽灵（pretraining 统计 + RL 奖励塑造），不是动物（进化/内在动机）；不要对 Agent 大喊，要理解它的训练分布边界
6. **规格是人的工作** — "细节可以外包，理解不能外包"；人必须负责 spec（系统边界、身份归属、质量标准），Agent 填补实现细节
7. **Agent-first 基础设施** — 今天一切工具、文档、流程为人设计；未来需要为 Agent 重写；测试标准：给 LLM 一句"Build MenuGen"，它能自动完成部署+配置
8. **MenuGen 被吃掉的警示** — 很多 AI 应用会被模型原生能力直接吞掉，不是做得更快，而是整个中间层失去存在必要

## 详细笔记

### Software 3.0 概念

Software 1.0：传统代码，人写规则。
Software 2.0：神经网络，通过训练得到模型权重（Karpathy 2017 年提出）。
Software 3.0：LLM 成为可编程解释器，context window 成为新的"把手"。

程序边界扩大：一段说明 + 一个上下文窗口 + 一组工具权限 + 一个测试环境 + 模型内部统计结构 = 一个 Software 3.0 程序。

### Vibe Coding 的准确定义

Karpathy 2025 年 2 月在 X 上提出这个词：一种"放弃对代码本身的直接控制、顺着感觉让模型往前走"的开发体验。人用自然语言持续提出意图，模型生成/修改/调试代码，人不再逐行写和读 diff。

2025 年 12 月是个人转折点：最新模型生成的代码开始"直接能用"，不需要修改，信任感持续增加。

### 锯齿状智能（jagged intelligence）

能力边界由 RL 训练覆盖的领域决定：
- 数学、代码等可验证领域：能力高峰，因为有明确的奖励信号
- 常识推理、日常空间理解：可能出现断崖（洗车题）

这是产品决策，不是自然进化。GPT-3.5→GPT-4 国际象棋能力大提升，是因为有人在 OpenAI 决定把大量国际象棋数据加进了预训练。

### 幽灵 vs 动物

| 维度 | 动物 | 幽灵（LLM） |
|------|------|------------|
| 来源 | 进化、身体互动 | pretraining 统计 + RL |
| 动机 | 内在（好奇心、乐趣） | 奖励函数 |
| 学习 | 生命过程中持续适应 | 固定（训练完成后） |
| 错误 | 环境反馈塑造 | 训练分布外 |

实用价值：不要对 Agent 大喊大叫，不要去"激励"它，要理解它的训练分布边界。

### Agentic Engineering 的要素

Agent 是"spiky entities"（有尖刺的实体）：能力很强，会犯错，有随机性，不稳定。

工程纪律：
- 把 Agent 放进合适的流程（生成→测试→验证→回滚）
- 设置边界（系统边界、权限、数据归属）
- 持续质量判断（代码能跑 ≠ 代码好）

AI-native 面试：算法题→大项目（Twitter clone）；然后用多个 Agent 作为红队攻击；评估：能否把模糊目标变成清晰规格，能否识别安全风险。

## 与其他资料的关系

- 与 [[source/10-lessons-for-agentic-coding]] 强烈共鸣：Breunig 的"记录意图"、"投资端到端测试"、"培养品味"与 Karpathy 的"规格是人的工作"、"理解不能外包"高度一致，均强调经验被放大而非取代
- 与 [[source/how-anthropic-teams-use-claude-code]] 互补：Anthropic 内部实践（claude-md-files, checkpoint-workflow）正是 Agentic Engineering 纪律在团队级别的具体落地
- 与 [[source/llm-wiki-pattern]] 直接相关：Karpathy 在访谈中明确提及 LLM Knowledge Bases 是他感兴趣的项目——"把文章、事实重新投影成 wiki，不是让 AI 代替理解，而是用 AI 增强理解"
- 与 [[source/harness-knowledge-moat]] 呼应：两者都强调工具/工作流可替换，人的理解/判断/领域知识是不可替换的护城河
- 与 [[source/bestblogs-2.0-reading-workflow]] 呼应：BestBlogs 的 AI 伴读和 Karpathy 的 LLM Knowledge Bases 都是"用 AI 增强理解，而非代替理解"

## 引用此资料的页面
- [[entities/software-3-0]]
- [[entities/vibe-coding]]
- [[entities/agentic-coding]]
- [[topics/agentic-developer-practices]]

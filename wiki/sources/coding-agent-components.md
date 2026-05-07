---
type:: Source
tags:: #coding-agent #harness #context-management #tool-use #memory #subagents
created:: [[2026-05-07]]
url:: https://baoyu.io/translations/2026-04-04/components-of-a-coding-agent
original:: https://magazine.sebastianraschka.com/p/components-of-a-coding-agent
author:: Sebastian Raschka（宝玉译）
raw:: [[coding-agent-components]]
---

# 编程智能体的核心组件

> **一句话**：编程智能体的六大核心组件——Harness，不是模型，才是真正拉开差距的关键。

## 关键观点

### 1. Harness 比模型更重要

> "在我看来，现在的原味基础版大模型（GPT-5.4、Opus 4.6、GLM-5）能力已经非常接近了。在这个阶段，真正拉开差距的决定性因素，往往就是外围 Harness。"

如果把同等优质的 Harness 套在最强开源模型上，表现很可能与顶级商业产品不相上下。

### 2. 层次分类（Taxonomy）

| 层级 | 定义 |
|------|------|
| LLM | 基础模型（下一词预测器） |
| 推理模型 | LLM + test-time compute（Chain of Thought，自我验证） |
| Agent | 模型 + 工具 + 记忆 + 环境反馈循环 |
| Agent harness | 管理上下文/工具/提示词/状态/控制流的软件脚手架 |
| Coding harness | 专门为软件工程特化的 Agent harness（代码上下文/开发工具/代码执行/迭代反馈） |

### 3. 六大核心组件（Coding harness 的组成）

| 编号 | 组件 | 核心职责 |
|------|------|---------|
| 1 | **实时代码仓库上下文 (Live Repo Context)** | Git 状态/分支/文件结构/AGENTS.md → 工作区摘要，模型知道"自己在哪里" |
| 2 | **提示词形态与缓存复用 (Prompt Shape & Cache Reuse)** | 稳定前缀（系统指令+工具+工作区摘要）vs 变动部分（最新请求+近期对话）；复用缓存，不每次重建 |
| 3 | **工具的接入与调用 (Tool Access & Use)** | 白名单工具箱；Harness 验证（合法？需审批？越界？）；受控执行 |
| 4 | **给上下文瘦身 (Minimizing Context Bloat)** | 截断（Clipping）+ 对话摘要（Transcript reduction）；近期保细节，远期重压缩；去重文件读取 |
| 5 | **结构化会话记忆 (Structured Session Memory)** | 工作记忆（小巧/主动维护/任务连贯性）+ 完整记录（持久日志/可恢复/JSONL） |
| 6 | **任务委派与受限子智能体 (Delegation With Bounded Subagents)** | 子智能体继承足够上下文；但受严格约束（只读/递归深度/任务范围） |

### 4. 上下文质量 ≠ 模型能力

> "我们平时夸赞的所谓'这个模型真聪明'，很大程度上其实归功于'这个系统喂给它的上下文质量真高'。"

Context bloat（上下文膨胀）是编程 Agent 的特有压力：频繁文件读取 + 工具输出日志使上下文飞速膨胀。

### 5. 工作记忆 vs 精简对话（重要区分）

两者目的不同，不能混淆：
- **精简版对话**：为重组提示词服务，给模型近期历史压缩包
- **工作记忆**：为任务连贯性服务，手动维护的核心关键点备忘录（当前任务/核心文件/关键笔记）

### 6. Coding harness vs OpenClaw（通用 Agent 平台）

| | Coding harness | OpenClaw |
|--|---------------|---------|
| 定位 | 专门为"趴在代码库里干活"极致优化 | 通用多智能体平台（代码只是其中一项能力） |
| 优化方向 | 深度单仓库工作（文件检查/代码修改/本地工具） | 多聊天窗口/频道/工作区，长期存活的持久 Agent |
| 子智能体约束 | 通常只读模式 + 深度限制 | 继承沙箱权限，更多约束在任务范围和上下文大小 |

## 相关实体

- [[coding-harness]] — 六大组件架构及 Harness 层次分类
- [[harness]] — Agent 驾驭层（Coding harness 的上位概念）
- [[agent-memory-system]] — 记忆系统对比（Hermes 四层 vs Raschka 双层）
- [[skills]] — 可复用能力单元（Coding harness 工具体系的一部分）
- [[progressive-disclosure]] — 按需加载工具（与组件 2/3 一致）

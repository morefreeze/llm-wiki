---
type:: Entity
tags:: #coding-agent #harness #context-management #tool-use #memory #subagents #architecture
created:: [[2026-05-07]]
sources:: [[coding-agent-components]]
related:: [[harness]], [[agent-memory-system]], [[progressive-disclosure]], [[skills]], [[vibe-coding]], [[agentic-coding]]
---

# Coding Harness（编程运行框架）

**Coding harness** 是专门针对软件工程任务特化的 Agent harness——管理代码仓库上下文、开发工具调用、代码执行和迭代反馈的软件脚手架。

> **核心洞察（Sebastian Raschka）**：在前沿基础模型能力已经非常接近的今天，真正拉开产品差距的，是外围 Harness，而不是模型本身。

## 层次分类（Taxonomy）

| 层级 | 定义 |
|------|------|
| **LLM** | 基础模型（下一词预测器） |
| **推理模型** | LLM + test-time compute（Chain of Thought，自我验证） |
| **Agent** | 模型 + 工具 + 记忆 + 环境反馈的控制循环 |
| **Agent harness** | 围绕 Agent 的软件脚手架（管理上下文/工具/提示词/状态/控制流） |
| **Coding harness** | Agent harness 的软件工程特化版（代码上下文/开发工具/代码执行/迭代反馈） |

典型 Coding harness：Claude Code、Codex CLI、Mini Coding Agent

## 六大核心组件

### 1. 实时代码仓库上下文 (Live Repo Context)

模型在动手之前，必须知道"自己在哪里"：

- Git 状态、当前分支、最近 commits
- 项目根目录结构
- `AGENTS.md` / `README.md`（开发规范和测试命令）

Harness 将这些"稳定的事实"打包成**工作区摘要（Workspace Summary）**，一次生成，多次复用。

### 2. 提示词形态与缓存复用 (Prompt Shape & Cache Reuse)

将提示词拆分为两层：

| 部分 | 内容 | 变化频率 |
|------|------|---------|
| **稳定前缀** | 系统指令 + 工具说明 + 工作区摘要 | 极少变化，可缓存 |
| **变动部分** | 最新用户请求 + 近期对话记录 + 短期记忆 | 每轮更新 |

聪明的 Harness 尽可能缓存稳定前缀（Prompt Cache），每轮只重建变动部分。

→ 与 [[agent-memory-system]] 的 Prompt Cache 设计原则高度一致（热/冷分离，缓存友好）

### 3. 工具的接入与调用 (Tool Access & Use)

Harness 提供预定义**白名单工具箱**（list dir / read file / search / shell / write file 等），每次工具调用前执行安检：

1. 这是已知工具吗？
2. 参数格式合法吗？
3. 高危操作，需要人工批准吗？
4. 文件路径超出代码仓库范围了吗？

Harness 限制操作边界（文件路径白名单），牺牲部分自由度，换取安全性和实用性。

→ 与 [[progressive-disclosure]] 的按需发现工具思路互补

### 4. 给上下文瘦身 (Minimizing Context Bloat)

编程 Agent 的特有压力：频繁文件读取 + 工具输出日志 = 上下文飞速膨胀。

两个基本武器：
- **截断（Clipping）**：长文档/工具输出/日志，毫不留情地截断
- **对话摘要（Transcript reduction）**：把历史记录提炼成轻量摘要

核心原则：**越近的事越详细，越远的事越压缩**；同一文件多次读取需去重。

> "我们平时夸赞的所谓'这个模型真聪明'，很大程度上归功于'这个系统喂给它的上下文质量真高'。"

### 5. 结构化会话记忆 (Structured Session Memory)

Agent 将状态分为两层，目的不同，不能混淆：

| 层 | 大小 | 目的 | 更新方式 |
|----|------|------|---------|
| **工作记忆** | 小 | 任务连贯性（当前任务/核心文件/关键笔记） | 主动修改和提炼 |
| **完整记录** | 大（JSONL） | 可恢复性（完整历史存档） | 只增不减 |

精简版对话（为重组提示词）≠ 工作记忆（为任务连贯性）——两者服务不同目的。

→ 与 [[agent-memory-system]] 的双层记忆架构（提示词记忆 + SQLite 冷存储）形成对照

### 6. 任务委派与受限子智能体 (Delegation With Bounded Subagents)

主 Agent 可以将子任务委派给受限子 Agent 并行处理，加快主线进度。

约束设计（防止失控）：
- **只读访问**：子 Agent 默认只能读文件，不能写
- **深度限制**：禁止子 Agent 再生成子 Agent（防止无限递归）
- **任务范围限制**：绑定到特定查询（变量定义/配置内容/失败原因）

不同产品策略对比：
- **Claude Code**：子 Agent 进入只读模式
- **Codex**：子 Agent 继承主 Agent 的沙箱权限，约束更多在任务范围和上下文大小

## 与相关概念的区分

### Coding harness vs Agent harness

Coding harness 是 Agent harness 的特化版，增加了：代码仓库感知、开发工具集成、代码执行反馈、迭代式问题解决。

### Coding harness vs OpenClaw

| | Coding harness | OpenClaw（通用 Agent 平台） |
|--|---------------|--------------------------|
| 定位 | 深度单仓库工作 | 多窗口/多频道长期存活 Agent |
| 写代码 | 核心能力 | 众多能力之一 |
| 优化方向 | 文件检查/代码修改/本地工具 | 持久化、跨工作区 Agent 管理 |
| 子 Agent 约束 | 只读 + 深度限制 | 继承沙箱，约束在范围和深度 |

## 开放问题

- 工作记忆的最优大小是多少？什么时机触发提炼（re-distillation）？
- 截断策略（Clipping）如何设定边界？边界错误会导致什么失败模式？
- 子 Agent 的递归深度限制如何动态调整？
- 多个子 Agent 并行修改同一仓库如何防止冲突？
- 专门针对 Coding harness 做后训练（post-training）能带来多大提升？

## 参见

- [[harness]] — Harness 的上位概念（安全带 + 方向盘）
- [[agent-memory-system]] — Hermes 四层记忆架构对照
- [[progressive-disclosure]] — 工具按需加载
- [[agentic-coding]] — 使用 Agent 辅助编码的范式
- [[vibe-coding]] — Vibe Coding vs Agentic Engineering 的上限/下限区分

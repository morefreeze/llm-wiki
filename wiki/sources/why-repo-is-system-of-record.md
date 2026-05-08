---
type:: Source
tags:: #harness #knowledge-visibility #system-of-record #agent-infrastructure
created:: [[2026-05-07]]
url:: https://walkinglabs.github.io/learn-harness-engineering/zh/lectures/lecture-03-why-the-repo-is-the-system-of-record/
author:: walkinglabs.github.io
raw:: [[repo-as-system-of-record]]
---

# 让代码仓库成为唯一的事实来源（Learn Harness Engineering L03）

> **一句话**：仓库即规范——agent 需要的所有知识必须在仓库里可发现，而不是散落在脑子里、Slack 消息里、或者某人的本地环境里。

## 关键观点

### 1. 知识可见性缺口（Knowledge Visibility Gap）

团队里有人知道"数据库连接字符串格式有个历史遗留问题"，但这件事只存在于那个人的脑子里。新来的 agent 不知道，踩了一遍坑，浪费了大量上下文。这就是知识可见性缺口。

知识可见性缺口 = 团队实际拥有的知识 - agent 通过查看仓库能访问到的知识

缺口越大，agent 需要越多人类介入，agent 犯同样错误的频率就越高。

### 2. 冷启动测试：5 个基本问题

判断仓库是否是"事实来源"的最佳测试：给一个全新的 agent 会话看仓库内容（不给任何口头上下文），让它回答：

1. 这个项目是干什么的？（一句话）
2. 怎么把项目跑起来？（具体命令）
3. 怎么跑测试并确认都通过了？
4. 这周正在进行什么工作？
5. 下一步该做什么？

如果 agent 答不上来，那些知识就在缺口里。这就是冷启动测试——衡量你的仓库作为事实来源的质量。

### 3. 发现成本（Discovery Cost）与知识衰减率（Knowledge Decay Rate）

**发现成本**：一个全新 agent 找到并验证完成任务所需信息的时间成本。发现成本高 = 时间浪费在找资料上，而不是做任务上。

**知识衰减率**：随着时间推移，文档和代码之间的差距增大的速度。没有明确维护策略的文档会以约 20% 的月衰减率失去准确性——每过一个月，这些文档变成错误信息的概率就增加 20%。

### 4. 用 ACID 原则管理 Agent 状态

Agent 的状态文件（PROGRESS.md、DECISIONS.md）应该像数据库事务一样管理：
- **原子性（Atomicity）**：状态更新是完整的，不存在"更新了一半"的状态
- **一致性（Consistency）**：状态文件始终反映代码库的真实状态
- **隔离性（Isolation）**：不同 agent 会话不会互相干扰状态
- **持久性（Durability）**：状态变更在 git 提交后永久保存

### 5. 四个让仓库成为事实来源的原则

1. **知识靠近代码**：文档和它描述的代码放在一起，而不是放在单独的 wiki 里。`src/auth/` 旁边放 `src/auth/CONTEXT.md`，解释认证系统的设计决策。
2. **标准化入口**：有一个且只有一个"从这里开始"的入口——通常是根目录的 AGENTS.md 或 README。Agent 知道从哪里开始找信息。
3. **最小但完备**：只放 agent 完成任务所必需的知识，不放无关的背景资料。质量优于数量。
4. **和代码一起更新**：每次改代码，同时更新相关文档。把文档更新纳入 PR 的完成标准。

### 6. 实战数据

一个 30 个微服务的电商平台，改造前：70% 的 agent 任务需要至少一次人类介入来提供缺失的上下文，每次介入平均需要 15 分钟。改造后（让仓库成为完整的事实来源，所有微服务有标准化的 AGENTS.md）：需要人工介入的任务比例降低了 60%，单个 agent 会话内完成的任务比例提升了 40%。

## 相关实体

- [[repo-as-system-of-record]] — 仓库即规范核心概念
- [[harness-5-subsystems]] — 五子系统（状态子系统与此密切相关）
- [[session-continuity]] — 跨会话连续性（依赖仓库作为事实来源）

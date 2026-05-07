---
type:: Source
tags:: #harness #initialization #bootstrap-contract #cold-start #session-continuity
created:: [[2026-05-07]]
url:: https://walkinglabs.github.io/learn-harness-engineering/zh/lectures/lecture-06-why-initialization-needs-its-own-phase/
author:: walkinglabs.github.io
raw:: [[initialization-independent-phase]]
---

# 让 Agent 每次工作前先初始化（Learn Harness Engineering L06）

> **一句话**：初始化和实现目标不同，混在一起只会互相拖后腿——"先打地基再砌墙"的独立初始化阶段让后续 3-4 个会话全部收回前期投资。

## 关键观点

### 1. 初始化 vs 实现：两种完全不同的优化目标

实现阶段目标：最大化已验证功能的数量和质量。初始化阶段目标：最大化后续所有实现的可靠性和效率。混在一起时 agent 面临多目标优化，自然倾向写代码（直接可见产出）而牺牲基础设施（价值只在后续会话体现）。

### 2. 自举契约（Bootstrap Contract）：四个条件

项目能被全新 agent 会话无歧义操作的充要条件：

| 条件 | 说明 |
|------|------|
| 能启动 | `make dev` 能成功 |
| 能测试 | `make test` 至少一个测试通过 |
| 能看进度 | 任务分解文件存在且机器可读 |
| 能接手下一步 | 新 agent 只看仓库能知道下一步做什么 |

### 3. 冷启动 vs 热启动

**冷启动**：从空目录开始，agent 要猜项目结构。**热启动**：从模板或已有项目开始，基础设施已就位。推荐用项目模板（create-react-app、fastapi-template 等）预置标准目录结构和测试框架，把通用初始化步骤移入模板。

### 4. 混合方式的隐性代价

- 地基不牢（配了但没验证）→ 第二个会话才暴露
- 未验证的累积：测试框架配好之前写的代码，补测试时发现设计有问题
- 上下文预算浪费在配环境上，留给实现的反而不够
- 隐式决策埋雷：后续会话做出矛盾选择

### 5. 实战数据

Anthropic 实验：使用独立初始化阶段的项目，多会话场景中功能完成率比混合方式高 **31%**。初始化阶段投入在后续 3-4 个会话中完全收回。

一个 React 前端项目对比：混合方式第二个会话花约 20 分钟推断项目结构；独立初始化第二个会话重建时间不到 3 分钟。整个项目周期混合方式总重建时间多约 **60%**。慢即是快。

## 相关实体

- [[session-continuity]] — 跨会话连续性（初始化是跨会话可靠性的前提）
- [[harness-5-subsystems]] — 指令+状态子系统在初始化阶段建立
- [[repo-as-system-of-record]] — 自举契约文档是仓库即规范的组成部分

---
type:: Entity
tags:: #agent #hooks #harness
created:: [[2026-05-16]]
sources:: [[source/agent-hooks-deterministic-control]]
---
# Agent Hooks

## 概述
Agent Hooks 是在 AI Agent 工作流生命周期节点注入确定性控制流的机制。通过挂载用户自定义 handler 到特定生命周期点，实现规则的自动化执行，而非依赖 LLM 记忆和自愿遵守。

## 核心原则
**用 Prompts 给引导，用 Hooks 保证每次都执行的行为。**

Prompts 是软约束（模型可能忘记或忽略），Hooks 是硬约束（代码级别保证执行）。

## 六个生命周期点

1. **SessionStart** — 会话开始时加载上下文（项目惯例、约束、环境信息）
2. **UserPromptSubmit** — 用户输入后、模型处理前（添加上下文/路由/拦截）
3. **PreToolUse** — 工具调用前按策略拦截/批准/修改
4. **PostToolUse** — 工具调用后跑验证（测试/格式化/扫描/日志）
5. **Stop** — Agent 想结束轮次时检查是否满足完成条件
6. **SessionEnd** — 会话结束时清理（日志/指标/临时状态）

## Handler 机制

每个 hook handler：
- 接收事件数据（如工具名、参数、上下文）
- 可通过 matcher/filter 缩窄触发范围
- 可返回：上下文注入、决策（通过/拦截）、副作用

## 典型用例

| 场景 | Hook 类型 | 行为 |
|------|-----------|------|
| 禁止编辑生成文件 | PreToolUse | 拦截对 generated/ 的写操作 |
| 编辑后自动测试 | PostToolUse | 检测文件变更触发测试套件 |
| 阻止未通过测试的完成 | Stop | 检查最近测试结果 |
| 加载项目规范 | SessionStart | 注入 AGENTS.md 内容 |
| 拦截危险 prompt | UserPromptSubmit | 过滤 rm -rf 等危险命令 |
| 会话归档 | SessionEnd | 导出日志和指标 |

## 关联
- [[harness]] — Hooks 是 harness 确定性执行层的具体实现
- [[harness-5-subsystems]] — 指令子系统的代码级补充
- [[completion-validation]] — Stop hook 实现自动化完成检查
- [[clean-session-state]] — SessionEnd hook 实现自动清理
- [[coding-harness]] — Hooks 是工具和环境子系统的守门人
- [[instruction-architecture]] — 指令靠模型遵守，hooks 靠代码执行

## 来源
- [[source/agent-hooks-deterministic-control]] — nader dabit 原文

---
type:: Source
source-type:: article
author:: nader dabit
date:: 2026-05-16
url:: https://x.com/dabit3/status/2055319214202777894
raw-file:: _raw/agent-hooks-deterministic-control.txt
created:: [[2026-05-16]]
---
# Agent Hooks: Deterministic Control for Agent Workflows

## 一句话总结
> 用 Hooks 在 Agent 工作流的生命周期节点注入确定性控制——让规则自动执行而非依赖模型记忆。

## 关键要点
1. **核心问题**：反复提醒 Agent 不要改某些文件、跑测试、遵守发布规则——这些都是 Hooks 的用例
2. **机制**：在 Agent 会话的特定生命周期点挂载用户自定义 handler，handler 接收事件数据，可被 matcher/filter 缩窄，返回上下文/决策/副作用
3. **价值主张**：确定性控制——脚本、测试、策略检查、runbook 中已有的规则在已知生命周期点自动执行，不依赖模型主动记忆
4. **黄金法则**：**用 Prompts 给引导，用 Hooks 保证每次都执行的行为**
5. **六个生命周期点**：
   - `SessionStart`：加载会话上下文（项目惯例、约束、环境信息）
   - `UserPromptSubmit`：在模型看到用户输入前拦截，添加上下文/路由/拦截
   - `PreToolUse`：工具调用前检查，按策略拦截/批准/修改
   - `PostToolUse`：工具调用后验证（测试、格式化、扫描、日志）
   - `Stop`：检查 Agent 是否被允许结束当前轮次
   - `SessionEnd`：会话结束时写日志、flush 指标、导出摘要

## 详细笔记

### 为什么需要 Hooks

项目指令可以说"不要编辑生成的文件"，但 `PreToolUse` hook 可以在编辑发生前直接拦截；项目指令可以说"完成前跑测试"，但 `PostToolUse` hook 可以在编辑后自动跑测试，`Stop` hook 可以在最后一次测试失败时阻止完成。

这是从"依赖模型记忆"到"确定性执行"的范式转变。

### 六个生命周期点详解

| 生命周期点 | 时机 | 典型用途 |
|-----------|------|---------|
| SessionStart | 会话开始 | 加载项目惯例、约束、环境信息 |
| UserPromptSubmit | 用户输入后、模型处理前 | 添加上下文、路由、拦截有害 prompt |
| PreToolUse | 工具调用前 | 按策略拦截/批准/修改 |
| PostToolUse | 工具调用后 | 跑测试、格式化、扫描、日志 |
| Stop | Agent 想结束轮次时 | 阻止不合格的完成 |
| SessionEnd | 会话结束 | 写日志、flush 指标、清理临时状态 |

### 与 Harness 的关系

Hooks 本质上是 [[harness]] 中"确定性执行层"的具体实现：
- 与 [[harness-5-subsystems]] 中的"指令子系统"互补：指令靠模型遵守，hooks 靠代码执行
- 与 [[completion-validation]] 的三层终止校验呼应：`Stop` hook 实现了自动化的完成检查
- 与 [[clean-session-state]] 的清洁状态呼应：`SessionEnd` hook 实现了自动清理

## 与其他资料的关系
- 补充了 [[harness]] 的概念：hooks 是 harness 的确定性执行机制
- 与 [[coding-harness]] 的六大组件互补：hooks 是工具和环境子系统的"守门人"
- 呼应 [[prevent-premature-completion]]：`Stop` hook 是防止过早完成的确定性方案

## 引用此资料的页面
- [[agent-hooks]]
- [[harness]]
- [[completion-validation]]

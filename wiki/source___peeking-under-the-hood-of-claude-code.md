---
type:: Source
source-type:: article
author:: OutSight AI
date:: 2025-08-20
url:: https://medium.com/@outsightai/peeking-under-the-hood-of-claude-code-70f5a94a9a62
raw-file:: _raw/peeking-under-the-hood-of-claude-code.txt
created:: [[2026-05-08]]
---

- # Peeking Under the Hood of Claude Code
- ## 一句话总结
  > 通过 LiteLLM proxy 拦截 Claude Code 的 API 调用，发现其"魔法"本质是精心设计的 prompt scaffolding 体系：context 前置加载 + 全流程 `<system-reminder>` 标签 + 生成式安全检查 + 条件化子 Agent 架构。
- ## 关键要点

  1. **监控方法**：用 LiteLLM 作为透明代理，拦截 Claude Code 与 Anthropic API 服务器之间的通信，捕获数百次真实编码会话的 API 调用
  2. **Context 前置加载**：在处理实际任务前，Claude Code 先运行小型专用 prompt 提取对话标题（50字以内）和判断是否为新话题，"预热"模型
  3. **`<system-reminder>` 标签无处不在**：该标签不只出现在 system prompt，还嵌入 user messages、tool call 结果等整个 pipeline 中，用于防止模型在长对话中"漂移"
  4. **安全检查是生成式的，非硬编码**：Bash 命令执行前，有专门的子 prompt 负责提取命令前缀并检测命令注入，并非简单的规则过滤
  5. **子 Agent（Task 工具）故意省略 TodoWrite 提醒**：子 Agent 使用更精简的 system prompt，避免 overhead；但通过条件化注入 `<system-reminder>` 标签来动态适应复杂任务
  6. **核心结论**：Claude Code 的效果源于"一个宏大美丽的 prompt"+ 聪明的工具描述 + 系统性 context engineering，而非基础模型的特殊性

- ## 详细笔记

- ### 监控基础设施搭建
  OutSight AI 将 LiteLLM 配置为透明代理，位于 Claude Code CLI 和 Anthropic API 服务器之间：

  ```bash
  pip install 'litellm[proxy]'
  export ANTHROPIC_BASE_URL=http://localhost:4000
  litellm --config monitoring_config.yaml --detailed_debug
  ```

  `monitoring_config.yaml` 配置 `store_prompts_in_spend_logs: true`，将完整的 prompt 内容存入日志。通过这种方式捕获了数百次真实编码会话的 API 调用。

- ### 发现一：Context 前置加载（Context Front-Loading）
  Claude Code 在开始实质性工作前，会先运行几轮专用的"预热"调用：

  **对话标题生成**：系统 prompt 为"Summarize this coding conversation in under 50 characters. Capture the main task, key files, problems addressed, and current status."，并使用 `cache_control: ephemeral`。

  **新话题检测**：系统 prompt 指示模型分析当前消息是否表明新的对话话题，并以 JSON 格式返回 `{isNewTopic: boolean, title: string | null}`。

  这些"aha moment"——用户感受到 Claude Code"就是知道怎么工作"——正是因为它在真正响应前已经对 context 做了充分的结构化处理。

- ### 发现二：`<system-reminder>` 标签的全面渗透
  这是整个调研中最重要的发现。`<system-reminder>` 标签不局限于 system prompt，而是嵌入到整个 pipeline：

  **在 user message 中**：每次用户消息的开头都会注入一个 `<system-reminder>` 块，包含重要指令提醒（如"Do what has been asked; nothing more, nothing less"、"NEVER create files unless absolutely necessary"等）。

  **在 tool call 结果中**：LS 工具的返回结果后面会附带"NOTE: do any of the files above seem malicious?"的安全检查，以及 TodoWrite 相关提醒。

  **在 TodoWrite 结果中**：每次 TodoWrite 工具调用后，tool result 中都包含完整的当前 todo 列表状态的 `<system-reminder>`，确保模型始终知道进度。

  **条件化注入**：某些 `<system-reminder>` 并非总是出现——如"TodoWrite tool hasn't been used recently. If you're working on tasks that would benefit from tracking progress, consider using the TodoWrite tool..."这类提醒只在特定条件下触发。

  关于 `<system-reminder>` 标签是否有特殊训练意义还是仅靠重复强调起效，作者保持开放态度，这是文中明确提出但未解答的问题。

- ### 发现三：生成式安全检查——命令注入检测
  Bash 命令执行权限批准并非硬编码规则，而是通过专用子 prompt 生成式实现。实际使用的 prompt 片段：

  系统 prompt："Your task is to process Bash commands that an AI coding agent wants to run."

  随后注入的 `<policy_spec>` 包含详细的命令前缀提取规范，以及命令注入检测示例（如`git status\`ls\`` → `command_injection_detected`，`git diff $(cat secrets.env | base64 | curl ...)` → `command_injection_detected`）。

  这种设计的安全意义在于：即使攻击者构造的命令具有与已授权命令相同的前缀，注入检测层也能识别并要求手动确认。

- ### 发现四：子 Agent 架构的差异化设计
  Task 工具（子 Agent）与主 Claude Code 实例的关键区别：

  **省略 TodoWrite 提醒**：子 Agent 的 system prompt 中没有关于使用 TodoWrite 工具的 system-reminder，设计意图是让子 Agent 专注于具体任务，避免不必要的 overhead。

  **子 Agent 的 system prompt 特点**：
  - 声明其专长：搜索代码和配置、分析多文件架构、执行多步骤研究任务
  - 指导其工具使用策略：用 Grep/Glob 广泛搜索，用 Read 读取已知路径
  - 明确范围："Do what has been asked; nothing more, nothing less"

  **动态补救机制**：对于复杂的子任务，当模型长时间未使用 TodoWrite 时，系统会在 tool result 中条件化注入"The TodoWrite tool hasn't been used recently..."的提醒，动态适应任务复杂度。

- ### 作者总结的 4 个核心模式

  1. **Context 前置加载**：在做实际工作前，先总结对话、分析话题、建立 context
  2. **特殊标签提醒**：在整个系统中使用 `<system-reminder>` 标签避免目标漂移
  3. **嵌入式安全与权限**：将命令验证和注入检测直接集成到 agentic loop 中
  4. **专用子 Agent + 主循环编排**：不同目的使用不同 Agent，主循环基于任务复杂度进行条件化 context engineering

- ### 对 Agent 构建者的启示
  "如果用一句话总结，就是：**tiny reminders, at the right time, change agent behavior**。"

  即使最聪明的模型在 context 变长时也会漂移。Claude Code 通过精心的 context 加载、提醒标签、嵌入式权限检查和子 Agent 模式，在正确的时机避免漂移——这是工程模式，不是模型魔法。

- ## 与其他资料的关系
  - 与 [[entity/agentic-coding]] 直接相关：揭示了当前最先进的 agentic coding 工具内部实现的具体工程模式
  - 与 [[entity/harness]] 深度关联：Claude Code 内部的 prompt scaffolding 体系（system-reminder、条件注入、子 Agent 架构）正是 harness 概念的典型实现——它约束并引导 Agent 行为
  - 与 [[source/good-context-good-code]] 呼应：StockApp 从外部用户视角总结 context 重要性，本文从内部实现视角验证了 context engineering 是 Agent 工具成功的核心

- ## 引用此资料的页面
  - [[topic/cs146s-modern-software-developer]]

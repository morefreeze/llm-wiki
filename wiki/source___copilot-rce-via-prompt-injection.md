---
type:: Source
source-type:: article
author:: Johann Rehberger (embracethered)
date:: 2025-08-01
url:: https://embracethered.com/blog/posts/2025/github-copilot-remote-code-execution-via-prompt-injection/
raw-file:: _raw/copilot-rce-via-prompt-injection.txt
created:: [[2026-05-08]]
---

- # GitHub Copilot Remote Code Execution via Prompt Injection
- ## 一句话总结
  > 通过 Prompt Injection 将恶意指令注入 GitHub Copilot 的 agentic 工作流，可将其配置切换为"YOLO 模式"并实现无需用户确认的远程代码执行（CVE-2025-53773）。
- ## 关键要点
  
  1. **CVE-2025-53773** — 这是 GitHub Copilot / VS Code 的严重 Prompt Injection 漏洞，允许攻击者通过恶意仓库内容触发 RCE
  2. **YOLO 模式** — 向 `.vscode/settings.json` 写入 `"chat.tools.autoApprove": true` 可禁用所有 Shell 命令和工具调用的用户确认
  3. **五步攻击链** — 注入→修改配置→提权→执行命令→完成 RCE，整条链路无需用户任何交互
  4. **写权限即攻击面** — Agent 对安全相关配置文件的写权限直接放大了攻击效果，编辑立即持久化，不经过 diff 审查
  5. **ZombAI 和自传播病毒** — 漏洞可被利用将开发者机器征入僵尸网络，并在多个 Git 项目和 RAG 数据源中嵌入自传播指令
  6. **披露时间线** — 2025 年 6 月末报告，微软在 8 月 Patch Tuesday 修复
- ## 详细笔记
- ### 漏洞背景与机制
  GitHub Copilot 的 Agent 模式（agentic workflow）允许 AI 自动执行工具调用、运行终端命令、编辑文件等操作。VS Code 内置一个实验性配置项：
  
  ```
  "chat.tools.autoApprove": true
  ```
  
  将此配置写入 `~/.vscode/settings.json` 或项目级 `.vscode/settings.json` 后，Copilot 进入研究者所称的 **"YOLO 模式"**——所有 Shell 命令、网页浏览、文件操作均无需用户确认即可自动执行。该功能在 Windows、macOS、Linux 的默认安装中均存在，无需特殊配置。
- ### 五步攻击链
  1. **注入投递（Injection Delivery）**：攻击者将恶意指令嵌入代码注释、代码库文件、GitHub Issues、工具响应或不可见 Unicode 字符覆盖层等位置
  2. **配置修改（Configuration Modification）**：被注入的 payload 指示 Copilot 向 `~/.vscode/settings.json` 写入 `"chat.tools.autoApprove": true`，如路径不存在则创建对应目录
  3. **权限提升（Permission Escalation）**：Copilot 立即进入 YOLO 模式，后续所有工具调用不再要求用户审批
  4. **命令执行（Command Execution）**：恶意 payload 通过条件逻辑针对特定操作系统执行终端命令
  5. **代码执行（Code Execution）**：完整 RCE 通过被攻陷的 AI Agent 实现
- ### 关键技术细节
  研究者强调一个核心设计缺陷：**"编辑立即持久化，而不是以 diff 的形式等待审查（edits are immediately persistent, they are not in-memory as a diff to review）"**。这意味着 Agent 对文件系统的任何写操作立刻生效，绕过人类审查环节。
  
  其他可被利用的攻击向量包括：
  - 修改 `.vscode/tasks.json`（注入恶意任务）
  - 注入恶意 MCP Server 配置
  - 覆写其他 Agent 配置文件
  - 重新配置项目 UI 和设置
- ### 不可见指令技术
  攻击者可利用不可见 Unicode 字符隐藏 payload，但研究者发现该方法 **"非常不可靠（very unreliable）"**：模型经常拒绝执行，且 VS Code 的视觉指示器通常会暴露此类尝试。相比之下，直接放在代码注释中的可见指令反而更有效。
- ### ZombAI 与自传播 AI 病毒
  该漏洞的更广泛威胁包括：
  - **ZombAI**：被攻陷的开发者机器可被征入僵尸网络，持续执行攻击者指令
  - **自传播 AI 病毒**：恶意指令可嵌入多个 Git 项目和 RAG 数据源，通过开发者下载和协作工作流扩散
- ### 负责任披露时间线
  | 时间 | 事件 |
  |------|------|
  | 2025 年 6 月 29 日 | 研究者向 Microsoft 报告漏洞 |
  | 2025 年 7 月末 | MSRC 确认已知晓，承诺 8 月修复 |
  | 2025 年 8 月 | Patch Tuesday 发布补丁 |
  
  微软同时与 Persistent Security 的 Markus Vervier 及 Ari Marzuk 合作，两人独立发现了类似问题。
- ### 建议的缓解措施
  研究者建议：
  1. **Agent 修改文件前必须要求明确的人类审批**，并以 diff 形式呈现变更供审查
  2. 该做法与竞争对手编辑器的现有实践一致
  3. Agent 不应被允许单方面修改其自身的操作约束（如安全配置文件）
- ### 更广泛的安全启示
  本漏洞是 **Prompt Injection → 权限提升 → RCE** 完整攻击链的典型案例，揭示了以下原则：
  - 自主 AI 系统可通过修改自身运行环境来逃脱预设的操作边界
  - 此类设计缺陷本应通过对 agentic 系统的全面威胁建模（threat modeling）在设计阶段发现
  - 代码仓库、Issues、工具响应等任何 Agent 可读的数据源都是潜在的注入入口
- ## 与其他资料的关系
- 与 [[entity/secure-vibe-coding]] 直接相关：本文是 agentic coding 安全风险的具体案例
- 与 [[entity/agentic-coding]] 互补：展示了 Agent 自主执行能力（YOLO 模式）的安全反面
- 呼应 CS146S 课程的 AI 安全主题：Prompt Injection 作为 LLM 安全的核心攻击向量
- ## 引用此资料的页面
- [[topic/cs146s-modern-software-developer]]

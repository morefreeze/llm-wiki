---
type:: Source
source-type:: article
author:: Anthropic Engineering
date:: 2025-09-11
url:: https://www.anthropic.com/engineering/writing-tools-for-agents
raw-file:: _raw/writing-tools-for-agents.txt
created:: [[2026-05-08]]
---

- # Writing Tools for Agents
- ## 一句话总结
  > Agent 的能力上限由工具的质量决定——通过"原型→评估→协作优化"三阶段工作流，结合五条设计原则，可以系统地打造高效的 Agent 工具。
- ## 关键要点

  1. **原型优先，快速上手** — 先构建可运行的原型，通过 MCP 本地测试，再根据真实使用反馈迭代，因为"不亲自上手很难预判哪种工具设计对 Agent 更符合人体工学"
  2. **评估驱动改进** — 构建覆盖真实场景的 prompt-response 评估集，跟踪准确率、运行时间、token 消耗、错误率等指标，系统化发现问题
  3. **选择正确的工具** — 工具数量少而精比多而杂强；工具应匹配 Agent 的使用方式，而非简单封装 API
  4. **清晰命名空间** — 用统一前缀归组相关工具（如 `asana_search`、`jira_search`），降低 Agent 的认知负担
  5. **返回有意义的上下文** — 优先返回语义化、高信噪比的信息，避免暴露 UUID、MIME 类型等低层技术细节
  6. **优化 token 效率** — 实现分页、范围筛选、截断等机制，提供清晰的错误引导，减少不必要的上下文消耗
  7. **精心设计工具描述** — 把工具描述当作给新团队成员的说明书来写，明确参数含义、数据格式和使用场景；小改动可带来大提升
- ## 详细笔记
- ### 背景与核心前提

  Anthropic 工程团队通过构建内部 MCP 服务器（Slack、Asana 等）积累了大量实践经验。文章的核心前提是：**工具设计质量直接决定 Agent 能力的上限**，而非模型本身。即使是同一个基础模型，配备精心设计的工具后表现可以大幅超过配备粗糙工具的版本。
- ### 阶段一：构建原型（Build Prototypes）

  - 利用 Claude Code 结合 API 文档（通常可在 `llms.txt` 文件中获取）快速生成初始实现
  - 通过 MCP 本地服务器或 Desktop 扩展进行本地测试
  - 收集用户在真实使用场景下的反馈
  - 关键洞察：在没有亲身使用之前，很难判断哪种工具设计更符合 Agent 的"人体工学"（ergonomic）
- ### 阶段二：运行综合评估（Run Comprehensive Evaluations）

  **生成评估任务：**
  - 基于真实场景创建数十个 prompt-response 对
  - 强任务示例涉及多步骤操作：带附件的会议调度、账单问题排查、客户留存方案准备等
  - 每个 prompt 配对可验证的预期结果
  - 避免过于简化的沙箱环境，要贴近生产场景

  **执行评估：**
  - 通过代码以 agentic loop 方式运行评估（LLM 调用与工具调用交替执行）
  - 在 system prompt 中加入推理和反馈 block
  - 启用 interleaved thinking 以获取更深层的分析
  - 追踪指标：准确率、运行时间、工具调用频率、token 消耗、错误率

  **分析结果：**
  - 审查 Agent 推理过程，识别混淆点
  - 不仅看 Agent 的显式描述，还要检查原始 transcript
  - 分析工具调用模式，发现效率优化机会
  - Agent 自身能识别出"描述矛盾的工具"和"低效的工具实现"
- ### 阶段三：与 Agent 协作优化（Iterative Optimization with Agents）

  - 将评估 transcript 粘贴进 Claude Code，让 Agent 分析问题并提出改进建议
  - 保留 held-out 测试集防止过拟合
  - Anthropic 内部评估证明此方法带来可量化的提升：Claude 优化的 Slack/Asana 工具超过了人工编写的版本
- ### 五条核心原则（Five Core Principles）

  #### 原则一：选择正确的工具（Choose the Right Tools）

  - Agent 的上下文窗口有限（不像计算机拥有充足的内存），因此工具设计要充分考虑这一约束
  - **避免宽泛工具，优选精准工具**：
    - 用 `search_contacts` 替代 `list_contacts`
    - 用 `search_logs` 替代 `read_logs`
    - 用 `get_customer_context` 替代多个分离的检索工具
  - **合并复合操作**：用 `schedule_event` 一个工具替代 `list_users` + `list_events` + `create_event` 三个工具的组合
  - 原则：工具应匹配 Agent 的使用方式（affordances），而非简单映射 API 端点

  #### 原则二：清晰的命名空间（Namespace Tools Clearly）

  - 相关工具用统一前缀归组：`asana_search`、`jira_search`、`asana_projects_search`
  - 前缀 vs 后缀的命名选择对性能有显著影响
  - 良好的命名空间减少 Agent 的上下文负载，让计算量转移到工具调用本身

  #### 原则三：返回有意义的上下文（Return Meaningful Context）

  - 优先返回高信噪比、上下文相关的信息
  - 避免暴露低层技术标识符：UUID、MIME 类型、像素尺寸等
  - 使用语义化名称和人类可读的标识符
  - 示例：将 UUID 解析为有意义的语言描述可提升精确度、减少幻觉
  - 实现可选的 `response_format` 参数（DETAILED vs CONCISE）提供灵活性
  - 响应结构（XML、JSON、Markdown）的选择会影响 LLM 性能

  #### 原则四：优化 token 效率（Optimize for Token Efficiency）

  - 实现分页（pagination）、范围选择（range selection）、过滤（filtering）、截断（truncation）
  - 设置合理的参数默认值
  - 截断响应时附加有用的引导说明
  - 错误消息要具有指导性，引导 Agent 走向正确行为
  - 对比示例：不透明的错误码 vs 包含操作建议的可读错误信息
  - 鼓励 token 高效策略："多次小范围搜索优于一次宽泛搜索"
  - 实践数据：简洁格式使响应减少约 1/3 token，实际评估中性能提升显著

  #### 原则五：精心设计工具描述（Prompt-Engineer Tool Descriptions）

  - 用"向新团队成员解释"的方式撰写工具描述
  - 把隐性知识显性化：专用查询格式、领域术语、资源关系
  - 参数命名要无歧义：用 `user_id` 而非模糊的 `user`
  - 清晰描述预期的输入输出，配合严格的数据模型
  - **案例**：Claude Sonnet 3.5 通过对工具描述的"精确细化"在 SWE-bench Verified 上达到 SOTA
  - **反例**：Anthropic 发现 Claude 会不必要地在 web 搜索查询中附加"2025"年份参数，导致结果变差——通过改进工具描述修复
  - 工具描述最终被加载进 Claude 的 system prompt，要理解这一机制
- ### 关键数据点

  - Anthropic 内部 Slack 和 Asana MCP 服务器评估中，Claude 优化的版本优于人工版本
  - 简洁格式可使响应 token 减少约 1/3
  - 工具描述的小改动在 SWE-bench Verified 等基准上带来显著性能提升
- ## 与其他资料的关系
- 与 [[entity/mcp]] 密切相关：本文的工具构建基础是 MCP（Model Context Protocol），详细说明了如何在 MCP 框架下设计高质量工具
- 与 [[entity/agentic-coding]] 互补：agentic-coding 关注开发者工作流，本文聚焦工具层的工程实践，两者共同构成 Agent 开发的完整图景
- 与 [[source/building-agents-that-reach-production-systems-with-mcp]] 配套：前者讲生产接入，本文讲工具设计质量
- 与 [[source/10-lessons-for-agentic-coding]] 呼应：都强调评估和迭代的重要性，角度不同（工具设计 vs 开发者工作流）
- ## 引用此资料的页面
- [[topic/cs146s-modern-software-developer]]

# LLM Wiki 操作日志

---

## [2026-05-08] ingest | CS146S: The Modern Software Developer（Stanford，themodernsoftware.dev）
- 摄入来源：Stanford CS146S Fall 2025 课程网站（themodernsoftware.dev），JS bundle 解析提取完整课程内容
- 创建主题页：
  - `wiki/topic___cs146s-modern-software-developer.md` — 10 周课程综述，全部读物/讲义/嘉宾
- 创建资料摘要页（16 个）：
  - Week 2: `wiki/source___mcp-introduction-stytch.md` — MCP 综合介绍（USB-C 类比，JSON-RPC，OAuth）
  - Week 2: `wiki/source___apis-dont-make-good-mcp-tools.md` — API→MCP 反模式（Tool 爆炸/Context 宽度/格式低效）
  - Week 3: `wiki/source___specs-are-the-new-source-code.md` — Spec 是新的源代码，代码是有损投影
  - Week 3: `wiki/source___how-long-contexts-fail.md` — 四种 Context 失效：Poisoning/Distraction/Confusion/Clash
  - Week 3: `wiki/source___writing-tools-for-agents.md` — 为 Agent 编写工具五原则（Anthropic）
  - Week 3: `wiki/source___coding-agents-101-devin.md` — 有效管理 Coding Agent：四条规则 + 检查点架构
  - Week 4: `wiki/source___good-context-good-code.md` — StockApp：13 周 1098 PRs，2.5x 生产力
  - Week 4: `wiki/source___peeking-under-the-hood-of-claude-code.md` — LiteLLM 代理揭秘 Claude Code 内部机制
  - Week 6: `wiki/source___copilot-rce-via-prompt-injection.md` — CVE-2025-53773：YOLO 模式 Prompt Injection → RCE
  - Week 6: `wiki/source___finding-vulnerabilities-with-ai-coding-agents.md` — Semgrep：46 个真实漏洞，14% TPR
  - Week 6: `wiki/source___context-rot.md` — Context Rot：位置效应 + 非均匀退化（18 个模型）
  - Week 7: `wiki/source___code-reviews-just-do-it.md` — 代码检查发现率 55-60%，远超单元测试（Jeff Atwood）
  - Week 7: `wiki/source___how-to-review-code-effectively.md` — GitHub Staff Engineer 7000+ PR 评审哲学
  - Week 7: `wiki/source___ai-code-review-best-practices.md` — Graphite：AI 代码评审三步集成路线
  - Week 9: `wiki/source___sre-introduction.md` — Google SRE Book：Error Budget、50% Ops Cap、SLI/SLO/SLA
  - Week 9: `wiki/source___observability-basics-traces-spans.md` — Traces & Spans，OpenTelemetry，三信号关联
- 创建实体页（3 个）：
  - `wiki/entity___context-engineering.md` — Context Engineering 范式：四种失效模式 + 修复策略
  - `wiki/entity___secure-vibe-coding.md` — AI 编码安全：Prompt Injection → RCE + AI 辅助漏洞检测
  - `wiki/entity___ai-native-development.md` — AI 原生开发文化：StockApp 2.5x 生产力 + 五大原则
- 更新实体页（2 个）：
  - `wiki/entity___mcp.md` — 补充 USB-C 类比、JSON-RPC、OAuth、三类原语、工具设计陷阱、MCP Registry
  - `wiki/entity___agentic-coding.md` — 补充 Devin 检查点架构、AI-Native 关联、新来源
- 更新 `index.md`（76 页面，39 资料，30 实体，6 主题）
- 更新 `pages/contents.md`（添加 CS146S 主题 + 三个新实体）

## [2026-05-07] ingest | Learn Harness Engineering L02-L12（walkinglabs.github.io）
- 批量接收 11 篇 Learn Harness Engineering 课程文章（article ID 1880-1890）
- 添加原始资料到 `_raw/`：harness-what-it-actually-is.txt、repo-as-system-of-record.txt、instruction-file-architecture.txt、session-continuity-across-sessions.txt、initialization-independent-phase.txt、wip-limit-task-boundaries.txt、feature-list-as-harness-primitive.txt、prevent-premature-completion.txt、e2e-testing-changes-results.txt、harness-observability.txt、clean-session-state.txt
- 创建资料摘要页（11个）：
  - `wiki/sources/harness-what-it-actually-is.md` — L02：五子系统模型 + 4 阶段实验（20%→100%）
  - `wiki/sources/repo-as-system-of-record.md` — L03：知识可见性缺口 + 冷启动测试 + 知识衰减率
  - `wiki/sources/instruction-file-architecture.md` — L04：路由文件 + 中间迷失效应（Liu 2023）+ 渐进式披露
  - `wiki/sources/session-continuity-across-sessions.md` — L05：连续性工件 + 上下文焦虑 + 漂移
  - `wiki/sources/initialization-independent-phase.md` — L06：自举契约四条件 + 冷/热启动
  - `wiki/sources/wip-limit-task-boundaries.md` — L07：WIP=1 + Overreach + Under-finish + VCR
  - `wiki/sources/feature-list-as-harness-primitive.md` — L08：功能清单三元组 + 状态机 + 通过状态门控
  - `wiki/sources/prevent-premature-completion.md` — L09：置信度校准偏差 + 三层终止校验 + 三 agent 架构
  - `wiki/sources/e2e-testing-changes-results.md` — L10：单元测试盲区 + E2E 改变行为 + 架构边界执行
  - `wiki/sources/harness-observability.md` — L11：双层可观测性 + 冲刺合同 + Anthropic 三 agent 实验
  - `wiki/sources/clean-session-state.md` — L12：清洁状态五维度 + 12 周熵增数据 + harness 简化
- 创建实体页（9个）：
  - `wiki/entities/harness-5-subsystems.md` — 五子系统模型 + 厨房类比
  - `wiki/entities/repo-as-system-of-record.md` — 仓库即规范 + ACID 状态管理
  - `wiki/entities/instruction-architecture.md` — 路由文件 + 渐进式披露 + 中间迷失效应
  - `wiki/entities/session-continuity.md` — 跨会话连续性 + 自举契约 + 上下文焦虑
  - `wiki/entities/wip-limit.md` — WIP=1 + Overreach/Under-finish + 完成证据
  - `wiki/entities/feature-list-primitive.md` — 功能清单原语 + 三元组结构 + 通过状态门控
  - `wiki/entities/completion-validation.md` — 三层终止校验 + E2E + Planner/Generator/Evaluator
  - `wiki/entities/harness-observability.md` — 双层可观测性 + 冲刺合同 + 任务轨迹
  - `wiki/entities/clean-session-state.md` — 清洁状态五维度 + 幂等清理 + harness 简化
- 更新实体页：
  - `wiki/entities/harness.md` — 补充 Learn Harness Engineering 课程视角 + 五子系统参考 + 相关实体链接
- 更新主题页：
  - `wiki/topics/agent-production.md` — 补充 harness 工程实践路径（仓库即规范/会话连续性/清洁状态/可观测性）
  - `wiki/topics/agentic-developer-practices.md` — 补充 WIP 限制/完成校验/功能清单/跨会话连续性实践
- 更新 `index.md`（56 页面，23 资料，27 实体，4 主题）

## [2026-05-07] ingest | 编程智能体的核心组件（Sebastian Raschka / 宝玉译）
- 从本地 RSS Pal 数据库提取文章内容（article ID 1561）
- 添加原始资料到 `_raw/coding-agent-components.txt`
- 创建资料摘要页 `wiki/sources/coding-agent-components.md`
- 创建实体页：
  - `wiki/entities/coding-harness.md` — 编程 Agent 六大组件架构 + LLM→推理模型→Agent→Agent harness→Coding harness 层次分类
- 更新实体页：
  - `wiki/entities/harness.md` — 补充 Raschka 的 Harness 层次分类和 Coding harness 特化视角
- 更新主题页：
  - `wiki/topics/agent-efficiency.md` — 补充 Context Bloat 管理三策略（截断/摘要/去重）
- 更新 `index.md`（36 页面，12 资料，18 实体，4 主题）

## [2026-05-06] init | 创建 LLM Wiki
- 初始化仓库结构：`raw/`、`wiki/`（entities/topics/sources/synthesis/）
- 创建 `AGENTS.md`（Schema）、`index.md`、`log.md`
- 创建目录占位文件

## [2026-05-06] ingest | LLM Wiki Pattern (Karpathy)
- 添加原始资料到 `raw/442a6bf555914893e9891c11519de94f.md`
- 创建资料摘要页 `wiki/sources/llm-wiki-pattern.md`
- 待建实体：Karpathy、Memex、RAG、Obsidian
- 待建主题：持久知识管理、增量知识编译

## [2026-05-06] ingest | Code Execution with MCP (Anthropic)
- 添加原始资料到 `raw/anthropic-code-execution-with-mcp.md`
- 创建资料摘要页 `wiki/sources/anthropic-code-execution-with-mcp.md`
- 创建实体页：
  - `wiki/entities/mcp.md` — Model Context Protocol
  - `wiki/entities/code-mode.md` — Cloudflare 的代码执行模式
  - `wiki/entities/skills.md` — 可复用 Agent 能力单元
  - `wiki/entities/progressive-disclosure.md` — 渐进式发现设计模式
- 创建主题页：
  - `wiki/topics/agent-efficiency.md` — Agent 效率优化（综合两篇资料）
- 更新 `index.md`（9 页面，2 资料，4 实体，1 主题）

## [2026-05-06] ingest | LLM Wiki Pattern by Karpathy

## [2026-05-06] ingest | Building agents that reach production systems with MCP

## [2026-05-06] ingest | 从玩具到生产力：用真实项目讲透 AI Agent 的 Harness Engineering

## [2026-05-06] ingest | 当我们在讨论 Harness 的时候，我们在讨论什么

## [2026-05-07] ingest | BestBlogs 2.0 内测开启（BestBlogs 创始人）
- 从本地 RSS Pal 数据库提取文章内容（article ID 1572）
- 添加原始资料到 `_raw/bestblogs-2.0-reading-workflow.md`
- 创建资料摘要页 `wiki/sources/bestblogs-2.0-reading-workflow.md`
- 创建实体页：
  - `wiki/entities/information-filtering.md` — 内容判断能力，信息过载时代的真正稀缺资源
- 创建主题页：
  - `wiki/topics/information-workflow.md` — 从发现到复用的完整知识输入路径
- 更新 `index.md`（27 页面，8 资料，13 实体，4 主题）

## [2026-05-07] ingest | 深度拆解 Hermes Agent 的记忆系统（Manthan Gupta / 宝玉整理）
- 从本地 RSS Pal 数据库提取文章内容（article ID 1119）
- 添加原始资料到 `_raw/hermes-agent-memory-system.txt`
- 创建资料摘要页 `wiki/sources/hermes-agent-memory-system.md`
- 创建实体页：
  - `wiki/entities/agent-memory-system.md` — Agent 四层记忆架构（语义/情景/程序/用户建模）+ Prompt Cache 优化原则
- 更新实体页：
  - `wiki/entities/skills.md` — 补充 Skills 作为程序记忆（Procedural Memory）的角色
- 更新主题页：
  - `wiki/topics/agent-efficiency.md` — 补充记忆分层与 Prompt Cache 命中率作为 Agent 效率的维度
- 更新 `index.md`（34 页面，11 资料，17 实体，4 主题）

## [2026-05-07] ingest | Karpathy 最新访谈：Vibe Coding 只是开始，真正重要的是 Agentic Engineering（宝玉整理）
- 从本地 RSS Pal 数据库提取文章内容（article ID 1108）
- 添加原始资料到 `_raw/karpathy-vibe-coding-to-agentic-engineering.txt`
- 创建资料摘要页 `wiki/sources/karpathy-vibe-coding-to-agentic-engineering.md`
- 创建实体页：
  - `wiki/entities/software-3-0.md` — Software 1.0/2.0/3.0 范式框架，context window 即程序
  - `wiki/entities/vibe-coding.md` — Vibe Coding vs Agentic Engineering：下限/上限区分，规格是人的工作
- 更新实体页：
  - `wiki/entities/agentic-coding.md` — 补充 Karpathy 的锯齿状智能、Vibe Coding/Agentic Engineering 分层、规格所有权
- 更新主题页：
  - `wiki/topics/agentic-developer-practices.md` — 补充 Karpathy 框架（规格所有权、锯齿状智能、AI-native 面试标准）
- 更新 `index.md`（32 页面，10 资料，16 实体，4 主题）

## [2026-05-06] ingest | Harness 不是目的，知识才是护城河（stevenpxiao）
- 从本地 RSS Pal 数据库提取文章内容（article ID 1597）
- 添加原始资料到 `_raw/harness-knowledge-moat.txt`
- 创建资料摘要页 `wiki/sources/harness-knowledge-moat.md`
- 创建实体页：
  - `wiki/entities/knowledge-lifecycle.md` — 五层存储 × 五种类型 × 三级成熟度 + 自动衰减的团队知识架构
- 更新实体页：
  - `wiki/entities/harness.md` — 补充"知识作为 Harness 核心组成"视角，Harness 三支柱与知识管理的关系
- 更新主题页：
  - `wiki/topics/agent-production.md` — 补充知识层作为 Agent 生产化完整路径的第三层
- 更新 `index.md`（29 页面，9 资料，14 实体，4 主题）

## [2026-05-06] ingest | How Anthropic Teams Use Claude Code (Anthropic PDF)
- 添加原始资料到 `_raw/how-anthropic-teams-use-claude-code.md`（从 PDF 提取）
- 创建资料摘要页 `wiki/sources/how-anthropic-teams-use-claude-code.md`
- 创建实体页：
  - `wiki/entities/claude-md-files.md` — 持久化 Agent 上下文的 Markdown 文件
  - `wiki/entities/checkpoint-workflow.md` — 频繁提交检查点的 Agent 协作安全网
- 更新主题页：
  - `wiki/topics/agentic-developer-practices.md` — 补充 Anthropic 内部案例和量化数据
- 更新 `index.md`（23 页面，7 资料，12 实体，3 主题）

## [2026-05-06] ingest | 10 Lessons for Agentic Coding (D. Breunig)
- 添加原始资料到 `_raw/10-lessons-for-agentic-coding.md`
- 创建资料摘要页 `wiki/sources/10-lessons-for-agentic-coding.md`
- 创建实体页：
  - `wiki/entities/agentic-coding.md` — Agentic coding 开发范式
  - `wiki/entities/living-specs.md` — 活规格文档实践
- 创建主题页：
  - `wiki/topics/agentic-developer-practices.md` — 代码廉价时代开发者工作方式
- 更新 `index.md`（19 页面，6 资料，10 实体，3 主题）

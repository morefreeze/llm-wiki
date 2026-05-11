# LLM Wiki 操作日志

---

## [2026-05-11] ingest | GPT-5.5 Instant: smarter, clearer, and more personalized（OpenAI Blog）
- 添加原始资料到 `_raw/gpt-5-5-instant.txt`
- 创建资料摘要页 `wiki/source___gpt-5-5-instant.md`
- 创建实体页：
  - `wiki/entity___gpt-5-5-instant.md` — OpenAI 新默认模型：幻觉↓52.5%、字数↓30.2%、Memory Sources 个性化控制
- 更新 `index.md`（83 页面，27 资料，35 实体，4 主题）

---

## [2026-05-11] ingest | HTML 的不合理有效性（Simon Willison / Thariq Shihipar）
- 添加原始资料到 `_raw/unreasonable-effectiveness-of-html.txt`
- 创建资料摘要页 `wiki/source___unreasonable-effectiveness-of-html.md`
- 创建实体页：
  - `wiki/entity___html-as-llm-output-format.md` — HTML 替代 Markdown 作为 LLM 输出格式：9 大场景 + Prompt 模式 + 对比表
- 更新实体页：
  - `wiki/entities/agentic-coding.md` — 补充 HTML 输出格式交叉引用
- 更新 `index.md`（67 页面，27 资料，35 实体，4 主题）

     4|
     5|## [2026-05-11] ingest | AI CLI 反代/中转/号池生态全景（@laozhang2579 / X）
     6|- 添加原始资料到 `_raw/laozhang-ai-proxy-ecosystem.txt`
     7|- 创建资料摘要页 `wiki/sources/laozhang-ai-proxy-ecosystem.md`
     8|- 创建实体页：
     9|  - `wiki/entities/ai-cli-proxy-ecosystem.md` — 8 大类 30+ 反代项目全景 + 四大技术路线 + 平台成熟度矩阵
    10|- 更新 `index.md`（65 页面，26 资料，34 实体，4 主题）
    11|
    12|## [2026-05-11] ingest | 朋友想复刻我的 AI 写作流程——扣子替代 Claude Code（@dotey / X）
    13|- 添加原始资料到 `_raw/dotey-ai-writing-workflow-coze.txt`
    14|- 创建资料摘要页 `wiki/sources/dotey-ai-writing-workflow-coze.md`
    15|- 创建实体页：
    16|  - `wiki/entities/content-director-pattern.md` — "内容导演"模式：人把控选题/观点/审美，AI 执行六步工作流
    17|  - `wiki/entities/coze-skills-platform.md` — 扣子 Skills 平台：Claude Code 的低门槛替代
    18|- 更新实体页：
    19|  - `wiki/entities/skills.md` — 补充扣子 Skills 作为商业化实现 + 宝玉的 Skills 化写作实践
    20|  - `wiki/entities/agentic-coding.md` — 补充 content-director-pattern 作为内容创作领域的对应模式
    21|- 更新 `index.md`（62 页面，25 资料，32 实体，4 主题）
    22|
    23|## [2026-05-11] ingest | 如何不背公式解开魔方（Philo Li / philoli.com）
    24|- 添加原始资料到 `_raw/solve-rubiks-cube-without-formulas.txt`
    25|- 创建资料摘要页 `wiki/sources/solve-rubiks-cube-without-formulas.md`
    26|- 创建实体页：
    27|  - `wiki/entities/rubiks-cube-group-theory.md` — 群论解魔方：交换子原理 + Roux 桥式 + 非阿贝尔群 + 解法对比
    28|  - `wiki/entities/commutator-technique.md` — 交换子 A B A⁻¹ B⁻¹：开门-操作-关门的核心模式
    29|- 更新 `index.md`（59 页面，24 资料，29 实体，4 主题）
    30|
    31|## [2026-05-07] ingest | Learn Harness Engineering L02-L12（walkinglabs.github.io）
    32|- 批量接收 11 篇 Learn Harness Engineering 课程文章（article ID 1880-1890）
    33|- 添加原始资料到 `_raw/`：harness-what-it-actually-is.txt、repo-as-system-of-record.txt、instruction-file-architecture.txt、session-continuity-across-sessions.txt、initialization-independent-phase.txt、wip-limit-task-boundaries.txt、feature-list-as-harness-primitive.txt、prevent-premature-completion.txt、e2e-testing-changes-results.txt、harness-observability.txt、clean-session-state.txt
    34|- 创建资料摘要页（11个）：
    35|  - `wiki/sources/harness-what-it-actually-is.md` — L02：五子系统模型 + 4 阶段实验（20%→100%）
    36|  - `wiki/sources/repo-as-system-of-record.md` — L03：知识可见性缺口 + 冷启动测试 + 知识衰减率
    37|  - `wiki/sources/instruction-file-architecture.md` — L04：路由文件 + 中间迷失效应（Liu 2023）+ 渐进式披露
    38|  - `wiki/sources/session-continuity-across-sessions.md` — L05：连续性工件 + 上下文焦虑 + 漂移
    39|  - `wiki/sources/initialization-independent-phase.md` — L06：自举契约四条件 + 冷/热启动
    40|  - `wiki/sources/wip-limit-task-boundaries.md` — L07：WIP=1 + Overreach + Under-finish + VCR
    41|  - `wiki/sources/feature-list-as-harness-primitive.md` — L08：功能清单三元组 + 状态机 + 通过状态门控
    42|  - `wiki/sources/prevent-premature-completion.md` — L09：置信度校准偏差 + 三层终止校验 + 三 agent 架构
    43|  - `wiki/sources/e2e-testing-changes-results.md` — L10：单元测试盲区 + E2E 改变行为 + 架构边界执行
    44|  - `wiki/sources/harness-observability.md` — L11：双层可观测性 + 冲刺合同 + Anthropic 三 agent 实验
    45|  - `wiki/sources/clean-session-state.md` — L12：清洁状态五维度 + 12 周熵增数据 + harness 简化
    46|- 创建实体页（9个）：
    47|  - `wiki/entities/harness-5-subsystems.md` — 五子系统模型 + 厨房类比
    48|  - `wiki/entities/repo-as-system-of-record.md` — 仓库即规范 + ACID 状态管理
    49|  - `wiki/entities/instruction-architecture.md` — 路由文件 + 渐进式披露 + 中间迷失效应
    50|  - `wiki/entities/session-continuity.md` — 跨会话连续性 + 自举契约 + 上下文焦虑
    51|  - `wiki/entities/wip-limit.md` — WIP=1 + Overreach/Under-finish + 完成证据
    52|  - `wiki/entities/feature-list-primitive.md` — 功能清单原语 + 三元组结构 + 通过状态门控
    53|  - `wiki/entities/completion-validation.md` — 三层终止校验 + E2E + Planner/Generator/Evaluator
    54|  - `wiki/entities/harness-observability.md` — 双层可观测性 + 冲刺合同 + 任务轨迹
    55|  - `wiki/entities/clean-session-state.md` — 清洁状态五维度 + 幂等清理 + harness 简化
    56|- 更新实体页：
    57|  - `wiki/entities/harness.md` — 补充 Learn Harness Engineering 课程视角 + 五子系统参考 + 相关实体链接
    58|- 更新主题页：
    59|  - `wiki/topics/agent-production.md` — 补充 harness 工程实践路径（仓库即规范/会话连续性/清洁状态/可观测性）
    60|  - `wiki/topics/agentic-developer-practices.md` — 补充 WIP 限制/完成校验/功能清单/跨会话连续性实践
    61|- 更新 `index.md`（56 页面，23 资料，27 实体，4 主题）
    62|
    63|## [2026-05-07] ingest | 编程智能体的核心组件（Sebastian Raschka / 宝玉译）
    64|- 从本地 RSS Pal 数据库提取文章内容（article ID 1561）
    65|- 添加原始资料到 `_raw/coding-agent-components.txt`
    66|- 创建资料摘要页 `wiki/sources/coding-agent-components.md`
    67|- 创建实体页：
    68|  - `wiki/entities/coding-harness.md` — 编程 Agent 六大组件架构 + LLM→推理模型→Agent→Agent harness→Coding harness 层次分类
    69|- 更新实体页：
    70|  - `wiki/entities/harness.md` — 补充 Raschka 的 Harness 层次分类和 Coding harness 特化视角
    71|- 更新主题页：
    72|  - `wiki/topics/agent-efficiency.md` — 补充 Context Bloat 管理三策略（截断/摘要/去重）
    73|- 更新 `index.md`（36 页面，12 资料，18 实体，4 主题）
    74|
    75|## [2026-05-06] init | 创建 LLM Wiki
    76|- 初始化仓库结构：`raw/`、`wiki/`（entities/topics/sources/synthesis/）
    77|- 创建 `AGENTS.md`（Schema）、`index.md`、`log.md`
    78|- 创建目录占位文件
    79|
    80|## [2026-05-06] ingest | LLM Wiki Pattern (Karpathy)
    81|- 添加原始资料到 `raw/442a6bf555914893e9891c11519de94f.md`
    82|- 创建资料摘要页 `wiki/sources/llm-wiki-pattern.md`
    83|- 待建实体：Karpathy、Memex、RAG、Obsidian
    84|- 待建主题：持久知识管理、增量知识编译
    85|
    86|## [2026-05-06] ingest | Code Execution with MCP (Anthropic)
    87|- 添加原始资料到 `raw/anthropic-code-execution-with-mcp.md`
    88|- 创建资料摘要页 `wiki/sources/anthropic-code-execution-with-mcp.md`
    89|- 创建实体页：
    90|  - `wiki/entities/mcp.md` — Model Context Protocol
    91|  - `wiki/entities/code-mode.md` — Cloudflare 的代码执行模式
    92|  - `wiki/entities/skills.md` — 可复用 Agent 能力单元
    93|  - `wiki/entities/progressive-disclosure.md` — 渐进式发现设计模式
    94|- 创建主题页：
    95|  - `wiki/topics/agent-efficiency.md` — Agent 效率优化（综合两篇资料）
    96|- 更新 `index.md`（9 页面，2 资料，4 实体，1 主题）
    97|
    98|## [2026-05-06] ingest | LLM Wiki Pattern by Karpathy
    99|
   100|## [2026-05-06] ingest | Building agents that reach production systems with MCP
   101|
   102|## [2026-05-06] ingest | 从玩具到生产力：用真实项目讲透 AI Agent 的 Harness Engineering
   103|
   104|## [2026-05-06] ingest | 当我们在讨论 Harness 的时候，我们在讨论什么
   105|
   106|## [2026-05-07] ingest | BestBlogs 2.0 内测开启（BestBlogs 创始人）
   107|- 从本地 RSS Pal 数据库提取文章内容（article ID 1572）
   108|- 添加原始资料到 `_raw/bestblogs-2.0-reading-workflow.md`
   109|- 创建资料摘要页 `wiki/sources/bestblogs-2.0-reading-workflow.md`
   110|- 创建实体页：
   111|  - `wiki/entities/information-filtering.md` — 内容判断能力，信息过载时代的真正稀缺资源
   112|- 创建主题页：
   113|  - `wiki/topics/information-workflow.md` — 从发现到复用的完整知识输入路径
   114|- 更新 `index.md`（27 页面，8 资料，13 实体，4 主题）
   115|
   116|## [2026-05-07] ingest | 深度拆解 Hermes Agent 的记忆系统（Manthan Gupta / 宝玉整理）
   117|- 从本地 RSS Pal 数据库提取文章内容（article ID 1119）
   118|- 添加原始资料到 `_raw/hermes-agent-memory-system.txt`
   119|- 创建资料摘要页 `wiki/sources/hermes-agent-memory-system.md`
   120|- 创建实体页：
   121|  - `wiki/entities/agent-memory-system.md` — Agent 四层记忆架构（语义/情景/程序/用户建模）+ Prompt Cache 优化原则
   122|- 更新实体页：
   123|  - `wiki/entities/skills.md` — 补充 Skills 作为程序记忆（Procedural Memory）的角色
   124|- 更新主题页：
   125|  - `wiki/topics/agent-efficiency.md` — 补充记忆分层与 Prompt Cache 命中率作为 Agent 效率的维度
   126|- 更新 `index.md`（34 页面，11 资料，17 实体，4 主题）
   127|
   128|## [2026-05-07] ingest | Karpathy 最新访谈：Vibe Coding 只是开始，真正重要的是 Agentic Engineering（宝玉整理）
   129|- 从本地 RSS Pal 数据库提取文章内容（article ID 1108）
   130|- 添加原始资料到 `_raw/karpathy-vibe-coding-to-agentic-engineering.txt`
   131|- 创建资料摘要页 `wiki/sources/karpathy-vibe-coding-to-agentic-engineering.md`
   132|- 创建实体页：
   133|  - `wiki/entities/software-3-0.md` — Software 1.0/2.0/3.0 范式框架，context window 即程序
   134|  - `wiki/entities/vibe-coding.md` — Vibe Coding vs Agentic Engineering：下限/上限区分，规格是人的工作
   135|- 更新实体页：
   136|  - `wiki/entities/agentic-coding.md` — 补充 Karpathy 的锯齿状智能、Vibe Coding/Agentic Engineering 分层、规格所有权
   137|- 更新主题页：
   138|  - `wiki/topics/agentic-developer-practices.md` — 补充 Karpathy 框架（规格所有权、锯齿状智能、AI-native 面试标准）
   139|- 更新 `index.md`（32 页面，10 资料，16 实体，4 主题）
   140|
   141|## [2026-05-06] ingest | Harness 不是目的，知识才是护城河（stevenpxiao）
   142|- 从本地 RSS Pal 数据库提取文章内容（article ID 1597）
   143|- 添加原始资料到 `_raw/harness-knowledge-moat.txt`
   144|- 创建资料摘要页 `wiki/sources/harness-knowledge-moat.md`
   145|- 创建实体页：
   146|  - `wiki/entities/knowledge-lifecycle.md` — 五层存储 × 五种类型 × 三级成熟度 + 自动衰减的团队知识架构
   147|- 更新实体页：
   148|  - `wiki/entities/harness.md` — 补充"知识作为 Harness 核心组成"视角，Harness 三支柱与知识管理的关系
   149|- 更新主题页：
   150|  - `wiki/topics/agent-production.md` — 补充知识层作为 Agent 生产化完整路径的第三层
   151|- 更新 `index.md`（29 页面，9 资料，14 实体，4 主题）
   152|
   153|## [2026-05-06] ingest | How Anthropic Teams Use Claude Code (Anthropic PDF)
   154|- 添加原始资料到 `_raw/how-anthropic-teams-use-claude-code.md`（从 PDF 提取）
   155|- 创建资料摘要页 `wiki/sources/how-anthropic-teams-use-claude-code.md`
   156|- 创建实体页：
   157|  - `wiki/entities/claude-md-files.md` — 持久化 Agent 上下文的 Markdown 文件
   158|  - `wiki/entities/checkpoint-workflow.md` — 频繁提交检查点的 Agent 协作安全网
   159|- 更新主题页：
   160|  - `wiki/topics/agentic-developer-practices.md` — 补充 Anthropic 内部案例和量化数据
   161|- 更新 `index.md`（23 页面，7 资料，12 实体，3 主题）
   162|
   163|## [2026-05-06] ingest | 10 Lessons for Agentic Coding (D. Breunig)
   164|- 添加原始资料到 `_raw/10-lessons-for-agentic-coding.md`
   165|- 创建资料摘要页 `wiki/sources/10-lessons-for-agentic-coding.md`
   166|- 创建实体页：
   167|  - `wiki/entities/agentic-coding.md` — Agentic coding 开发范式
   168|  - `wiki/entities/living-specs.md` — 活规格文档实践
   169|- 创建主题页：
   170|  - `wiki/topics/agentic-developer-practices.md` — 代码廉价时代开发者工作方式
   171|- 更新 `index.md`（19 页面，6 资料，10 实体，3 主题）
   172|
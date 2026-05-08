---
type:: Source
source-type:: article
author:: StockApp Team (Waleed Kadous, Charles Feng, Justin Berman, Dennis Yilmaz, Amr Elsayed, Mohammed Mogasbe, James Feng, Bruno Fantauzzi)
date:: 2025-08-06
url:: https://blog.stockapp.com/good-context-good-code/
raw-file:: _raw/good-context-good-code.txt
created:: [[2026-05-08]]
---

- # Good Context, Good Code: How We Built an AI-Native Eng Culture
- ## 一句话总结
  > 好代码是好 context 的副产品——AI-native 开发的核心不是工具，而是人类与 Agent 共同构建、精炼、消费 shared context 的系统性过程。
- ## 关键要点

  1. **2.5x 生产力提升**：StockApp 从零构建 AI-native 工程文化，比纯手工开发效率高 ~2.5x，比"现有文化叠加 AI"方式高 ~2x；传统 AI 增强只带来 30-50% 提升
  2. **核心洞见**：Good code is a side effect of good context——代码本身是中间产物，关键在于 context 的构建与共享
  3. **Monorepo 即共享工作空间**：代码库同时为人类和 Agent 组织，自然语言文档与编程语言同等重要，文档是一等公民
  4. **层级式开发流程**：Design → Plan → Implement → Backstop → Review → Update & Refine，每层人类与 Agent 协作共同构建 context
  5. **Agent 无处不在，但需监督**：对所有任务优先考虑使用 Agent，但不允许无人监管的"vibe coding"，要求深度技术专业性来审查 Agent 输出
  6. **MCP 服务器扩展 context 获取能力**：通过 Notion、Linear、AWS、SQL、Git/GitHub 等 MCP server，让 Agent 能直接访问外部信息源
  7. **Ensemble 胜过单个 Agent**：结合 Claude、Gemini、o3 等多个 LLM 进行评审，不同模型有不同优势（如 Gemini 在安全问题预判上表现更好）

- ## 详细笔记

- ### 背景与数据
  StockApp 于 2025 年 1 月开始从零构建 AI-native 工程文化。Q2 2025 客观数据：13 周内交付 1,098 个 PR（84.5 PR/周），人均 10.6 PR/周，而行业标准（LinearB 2025）约为 1 PR/开发者/周。团队成员来自 Google 等顶级工程组织，认为这是他们经历过的效率最高的开发环境。

  技术栈：Web 前端 TypeScript，后端 Python + TypeScript，单一 monorepo。日常编码工具：Claude Code（大多数人在 Cursor 内运行以获得实时自动补全）。

- ### 原则一：Repo 是人类和 Agent 的共享工作空间
  仓库组织要同时考虑人类和机器的可读性，因为 AI 性能高度依赖可访问的 context。这是"context engineering"比"prompt engineering"更重要的原因，也是 monorepo 作为操作流程核心的原因。

  关键目录结构：
  - `docs/designs/`：产品需求、高层目标、schema——回答"为什么"和"是什么"
  - `docs/plans/`：详细的分阶段实现计划，通常由人类和 Agent 共同生成——回答"怎么做"
  - `docs/guides/`：API 和工具的教程，通常由 Agent 阅读相关文档后起草
  - `schema.sql`：整个项目的单一权威 schema，提供数据结构的 ground truth
  - `README.md & CLAUDE.md`：分布在 repo 各处，为人类和 Agent 提供局部化指令

- ### 原则二：层级式开发允许渐进构建 context
  1. **Design**：人类提供关键需求和约束，Agent 起草设计文档，双方迭代并提交
  2. **Plan**：Agent 将设计转换为分阶段任务，人类审查批准
  3. **Implement**：Agent 承担大部分编码，人类审查结果
  4. **Backstop**：测试和其他保障机制确保后续变更不损害已积累的 context；不仅是测试，还包括任何强制已建立 context 的机制
  5. **Review**：人类和 Agent 对功能进行最终审查，确保符合设计文档中的目标
  6. **Update & Refine**：更新文档、CLAUDE.md 和 schema，让未来的 Agent 继承准确的 context

- ### 原则三：对一切使用 Agent，除非有充分理由不用
  StockApp 将 Agent 用于几乎所有工作，但明确反对"vibe coding"。一些非常规用法：
  - 用 Agent 写 commit 和 PR 消息（因为 Agent 有足够的设计文档和计划上下文）
  - 指示 Agent 更新文档和 CLAUDE.md，而不是人类直接编辑（"它比我们更清楚如何指导自己"）
  - 让 Agent 编写提示词（prompt），而不是人类写——提供 context 和"meta prompt"后让 Agent 来写
  - Agent 写测试，但注意防止"over-mock"；测试在 AI-native 代码库中更重要，因为 Agent 有上下文窗口限制，容易"局部解决、全局破坏"
  - 调试是人机协作：人类提出根因假设，Agent 验证——"Agent 验证假设的能力远强于自己提出假设"；同时 Agent 擅长插桩（instrumentation），可以跨多个库同时添加调试语句并分析日志
  - 让 Agent 主动寻找重复代码、死代码、安全问题、隐私问题并修复

- ### 原则四：MCP 和命令行工具让 context 获取更便捷
  团队维护 `install_mcp.sh` 脚本，新建 repo 时一键安装约 6 个 MCP server：
  - **Notion 和 Linear**：读取功能描述以辅助决策，更新任务状态，从高层设计创建 issue（如"把 Notion 这个页面的任务列表添加到 Linear"）
  - **AWS 和 SQL Dev 数据库**：Agent 直接读取 AWS 日志分析、检查开发数据库数据正确性
  - **Git 和 GitHub 命令**：研究历史版本、分析 commit 历史、创建 PR、解决 repo 问题

  MCP 最大的价值在于"桥接 gap"：如"读取 Linear 中的 bug 描述，然后查看最近 10 个 commit，找出最可能导致该 bug 的那个"。

- ### 原则五：Ensemble 胜过单个个体
  借鉴传统机器学习的 ensemble 思想（random forest、stacking、bagging、boosting）：多分类器 + 投票机制，只要有足够的多样性，ensemble 效果明显优于任何单个个体。

  StockApp 使用 **Zen MCP server** 让 Claude Code 也能获取其他 LLM（Gemini、o3）的反馈。例如 Claude Code 完成设计后，同时让 Gemini 审查。不同模型各有优劣——Gemini 在预判安全问题上表现显著更好。

  实际案例：关于 MCP server auth 实现方案，Gemini 强烈推荐 payload-based auth（称其为"最务实和可扩展的解决方案"），而 o3 更谨慎，将 per-user clients 列为生产系统首选，并警告 payload-based auth 的 token 泄露风险。

  最终，人类和 Agent 共同构成 ensemble，而让这个 ensemble 效果超越任何单个成员的桥梁正是 **shared context**。

- ### 重要警示
  这种方式需要*更多*的软件工程专业知识，而非更少：
  - 有效定义 context 在技术上至少和写好代码一样有挑战性
  - Agent 出错时"爆炸半径"可能很大（Agent 曾多次清空开发数据库）
  - 使用 Agent 时需要全程专注监督
  - Agent 目前确实会引导你走向错误方向，需要警觉、专注、有经验的眼睛来阻止

- ## 与其他资料的关系
  - 与 [[entity/ai-native-development]] 呼应：本文是 AI-native 开发实践的一手案例，核心主题与 entity 定义高度吻合
  - 与 [[entity/agentic-coding]] 互补：本文从团队文化和流程角度，而非工具角度描述 agentic coding 实践
  - 与 [[source/10-lessons-for-agentic-coding]] 对比：D. Breunig 更关注个人开发者的心态调整，StockApp 更关注团队级系统性流程
  - 与 [[entity/harness]] 关联：StockApp 的 CLAUDE.md + docs/ 体系是一种具体的 harness 实现形态

- ## 引用此资料的页面
  - [[topic/cs146s-modern-software-developer]]

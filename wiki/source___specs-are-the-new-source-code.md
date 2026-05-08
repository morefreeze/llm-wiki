---
type:: Source
source-type:: article
author:: Ravi Mehta
date:: 2025-05-01
url:: https://blog.ravi-mehta.com/p/specs-are-the-new-source-code
raw-file:: _raw/specs-are-the-new-source-code.txt
created:: [[2026-05-08]]
---

- # Specs Are the New Source Code
- ## 一句话总结
  > 在 AI 加速开发的时代，代码变成了 spec 的"有损投影"——spec 才是真正的 source of truth，写清楚需求比写代码更有价值。
- ## 关键要点
  
  1. **代码是 spec 的有损投影** — Sean Grove（OpenAI）的核心论点：就像反编译二进制文件会丢失注释和变量名，从 spec 生成代码也会丢失完整意图；spec 才是完整的信息
  2. **开发流程已经倒转** — 旧流程：模糊想法 → 线框图 → 设计 → MVP → 反馈 → 修改 spec；新流程：模糊想法 → 快速原型 → 用户反馈 → 结晶化 spec → AI 实现
  3. **Spec 能生成一切** — 一份足够健壮的 spec 可以生成 TypeScript、Rust、服务端、客户端、文档、教程、博客甚至 podcast
  4. **PM 成为新的瓶颈** — AI 让工程速度大幅提升后，限制从实现转移到了定义；有观点认为公司需要配备两倍于工程师数量的 PM
  5. **代码廉价，spec 稀缺** — 当代码生成成本趋近于零，能够清晰定义问题的能力反而成为稀缺资源
- ## 详细笔记
- ### Sean Grove 的"Spec 即源代码"论点
  
  Sean Grove（OpenAI）提出了一个颠覆性视角：当前开发者使用 AI 的方式是倒退的。
  
  传统编程中，我们高度珍视 source code（源代码），而把编译后的二进制文件视为产出物。没有人会把 `.exe` 文件提交到版本控制——真正的知识在源代码里。
  
  但现在很多开发者：
  1. 写出详细的 spec（prompt）来驱动 AI
  2. 收到 AI 生成的代码
  3. **保留代码，丢弃 spec**
  
  这是完全反过来的做法。生成的代码就像反编译的二进制——它是 spec 的"有损投影"（lossy projection），丢失了原始的意图、权衡和设计决策。
  
  Grove 的结论：**spec 才应该被提交到版本控制，代码应该被视为构建产物。**
  
  > "A sufficiently robust spec can generate good TypeScript, good Rust, servers, clients, documentation, tutorials, blog posts, and even podcasts."
- ### 开发流程的倒转
  
  **旧流程**（线性、瀑布式）：
  - 模糊想法 → 线框图 → 视觉设计 → 工程 MVP → 用户反馈 → 修改 spec → 重新构建
  - 问题：spec 写得过早，在获得用户反馈之前就被锁定；修改代价高昂
  
  **新流程**（原型优先）：
  - 模糊想法 → v0/Lovable/Replit 快速原型（数小时内，无需工程介入）→ 用户反馈 → 结晶化 spec → AI 实现
  - 优势：spec 是在真实用户反馈之后才写的，因此更加准确；AI 实现基于明确需求，质量更高
  
  关键变化：**spec 从"开发前的猜测"变成了"用户验证后的结晶"**。
- ### 非技术 PM 直接贡献代码的案例
  
  文章以 Danny Martinez（decimals 创始人）为例，展示非技术 PM 如何用 AI 工具直接向代码库贡献变更：
  
  **工具链**：Linear（项目管理）+ VS Code + GitHub Copilot Pro + Claude Sonnet 4 + Linear MCP Server
  
  **流程**：
  1. 将 Slack 消息转化为 Linear ticket
  2. 通过 AI 协助澄清需求细节
  3. 让 Claude 分析代码库并实现变更
  4. 测试后创建 Pull Request
  
  这个案例的意义不在于"PM 可以替代工程师"，而在于：**当 spec 足够清晰，实现变成了可以委托的事情**。
- ### 成功要素：三个必要条件
  
  1. **Specificity（具体性）** — 模糊的 spec 产生混乱的代码；AI 不会自动填补意图的空白，必须明确写出所有假设和约束
  2. **Selectivity（选择性）** — 自助式实现适合简单任务；复杂功能、系统架构决策仍然需要有经验的工程师
  3. **Gatekeeping（把关）** — 工程师的 code review 保证质量；速度与可维护性的平衡仍然需要人类判断
- ### 对 PM 角色的影响
  
  Andrew Ng 观察到有管理者提议配备两倍于工程师的 PM——这反映了一个现实：**AI 加速了实现，但没有加速问题定义**。
  
  AI 能够以"AI speed"运行的领域：
  - 代码生成
  - 文档写作
  - 测试用例创建
  
  仍然以"human speed"运行的领域：
  - 用户调研和需求发现（Customer Discovery）
  - 问题定义
  - 优先级判断
  - 跨团队对齐
  
  结论：**理解用户需求、清晰定义问题、设计优雅解决方案**——这些原本就是顶级 PM 的核心能力，在 AI 时代的价值被指数级放大。
- ### Spec 的双重角色
  
  在 AI 驱动的开发世界中，spec 同时服务于两个受众：
  - **人类团队**：作为对齐工具，确保所有人理解目标和约束
  - **AI 系统**：作为"源代码"，直接驱动实现
  
  这使得 spec 的质量比以往任何时候都更加关键——一份写得好的 spec 能被 AI 忠实实现，一份模糊的 spec 则会被 AI 放大其中的每一处含糊。
- ## 与其他资料的关系
- 与 [[entity/living-specs]] 直接呼应：本文从 PM 和产品视角论证 spec 的中心地位；living-specs 探讨 spec 在工程流程中的持续演化
- 与 [[entity/context-engineering]] 相关：spec 的精确性决定了给 AI 的 context 质量，是 context engineering 的上游环节
- 与 [[source/10-lessons-for-agentic-coding]] 互补：Breunig 从开发者视角讲实践规范，本文从 PM 视角讲 spec 的新地位
- 与 [[source/karpathy-vibe-coding-to-agentic-engineering]] 互补：Karpathy 讲开发者的角色转变，本文讲产品定义者（PM）的角色转变
- ## 引用此资料的页面
- [[topic/cs146s-modern-software-developer]]

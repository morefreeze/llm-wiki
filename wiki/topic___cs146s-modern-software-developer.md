---
type:: Topic
tags:: #cs146s #stanford #agentic-coding #modern-software #course
created:: [[2026-05-08]]
sources:: [[source/specs-are-the-new-source-code]] [[source/how-long-contexts-fail]] [[source/writing-tools-for-agents]] [[source/apis-dont-make-good-mcp-tools]] [[source/good-context-good-code]] [[source/peeking-under-the-hood-of-claude-code]] [[source/copilot-rce-via-prompt-injection]] [[source/finding-vulnerabilities-with-ai-coding-agents]] [[source/context-rot]] [[source/code-reviews-just-do-it]] [[source/how-to-review-code-effectively]] [[source/ai-code-review-best-practices]] [[source/mcp-introduction-stytch]] [[source/sre-introduction]] [[source/observability-basics-traces-spans]] [[source/coding-agents-101-devin]] [[source/how-anthropic-teams-use-claude-code]]
---

# CS146S: The Modern Software Developer

> Stanford University Fall 2025 首门系统讲授 AI 辅助软件开发的大学课程。从 LLM 基础到 Agent 架构、Context Engineering、安全、代码评审、自动化构建到生产运维，10 周覆盖完整 AI 时代软件工程生命周期。

课程网站：[themodernsoftware.dev](https://themodernsoftware.dev/)  
作业仓库：[GitHub](https://github.com/mihail911/modern-software-dev-assignments)（3.5k Stars）

## 课程信息

| 项目 | 详情 |
|------|------|
| 课程编号 | CS146S |
| 院校 | Stanford University |
| 学期 | Fall 2025（首次开设） |
| 讲师 | Mihail Eric |
| 助教 | Febie Lin, Brent Ju |
| 学分 | 3 units |
| 先决条件 | CS111 同等编程经验；推荐 CS221/229 |
| 教室 | 420-041 |

## 核心论点

软件开发已从"0→1 代码创造"演变为"计划→AI 生成→修改→迭代"的循环工作流。AI 工具不只是提升个人生产力，更将民主化软件工程——能有效沟通的人即能编程。

> "代码廉价时代，真正稀缺的是知道该做什么（Specs）" —— 课程核心主张

## 10 周课程总览

### Week 1：LLM 与 AI 编程基础
**主题**：课程介绍 / LLM 工作原理 / 高效 Prompt 编写  
**关键读物**：
- [Deep Dive into LLMs](https://www.youtube.com/watch?v=7xTGNNLPyMI)（Karpathy，视频）
- [Prompt Engineering Overview](https://cloud.google.com/discover/what-is-prompt-engineering)（Google）
- [Prompt Engineering Guide](https://www.promptingguide.ai/techniques)
- [How OpenAI Uses Codex](https://cdn.openai.com/pdf/6a2631dc-783e-479b-b1a4-af0cfbd38630/how-openai-uses-codex.pdf)（PDF）

**作业**：LLM Prompting Playground

**讲座**：
- Mon 9/22: Introduction and how an LLM is made — [Slides](https://docs.google.com/presentation/d/1zT2Ofy88cajLTLkd7TcuSM4BCELvF9qQdHmlz33i4t0/edit?usp=sharing)
- Fri 9/26: Power prompting for LLMs — [Slides](https://docs.google.com/presentation/d/1MIhw8p6TLGdbQ9TcxhXSs5BaPf5d_h77QY70RHNfeGs/edit?usp=drive_link)

---

### Week 2：Coding Agent 解剖
**主题**：Agent 架构与组件 / 工具调用与函数调用 / MCP（模型上下文协议）  
**关键读物**：
- [[source/mcp-introduction-stytch]] — MCP 综合介绍：USB-C 类比，JSON-RPC 架构，OAuth 认证
- [Sample MCP Server Implementations](https://github.com/modelcontextprotocol/servers)
- [MCP Server Authentication](https://developers.cloudflare.com/agents/guides/remote-mcp-server/#add-authentication)（Cloudflare）
- [MCP Server SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [MCP Registry](https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/)
- [[source/apis-dont-make-good-mcp-tools]] — 为何直接把 API 转成 MCP 工具效果差

**作业**：从零构建 MCP Server

**讲座**：
- Mon 9/29: Building a coding agent from scratch — [Slides](https://docs.google.com/presentation/d/11CP26VhsjnZOmi9YFgLlonzdib9BLyAlgc4cEvC5Fps/edit?usp=sharing)
- Fri 10/3: [Silas Alberti](https://www.linkedin.com/in/silasalberti/)（Head of Research, Cognition/Devin）

---

### Week 3：AI IDE 与 Context Engineering ★最重要★
**主题**：上下文管理与代码理解 / Agent 的 PRD / IDE 集成  
**关键读物**：
- [[source/specs-are-the-new-source-code]] — Spec 是新的源代码；代码是有损投影
- [[source/how-long-contexts-fail]] — 四种 Context 失效模式：Poisoning/Distraction/Confusion/Clash
- [[source/coding-agents-101-devin]] — Devin 视角：如何有效管理 Agent，任务拆分、检查点、验证
- [Getting AI to Work In Complex Codebases](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md)
- [[source/writing-tools-for-agents]] — Anthropic：为 Agent 编写高效工具的五大原则
- [How FAANG Vibe Codes](https://x.com/rohanpaul_ai/status/1959414096589422619)

**作业**：构建自定义 MCP Server（带 Design Doc 模板）

**讲座**：
- Mon 10/6: From first prompt to optimal IDE setup — [Slides](https://docs.google.com/presentation/d/11pQNCde_mmRnImBat0Zymnp8TCS_cT_1up7zbcj6Sjg/edit?usp=sharing)
- Fri 10/10: [Silas Alberti](https://www.linkedin.com/in/silasalberti/)（Head of Research, Cognition/Devin）— [Slides](https://docs.google.com/presentation/d/1C05bCLasMDigBbkwdWbiz4WrXibzi6ua4hQQbTod_8c/edit?usp=sharing)

---

### Week 4：Coding Agent 模式
**主题**：管理 Agent 自主程度 / 人机协作模式  
**关键读物**：
- [[source/how-anthropic-teams-use-claude-code]] — Anthropic 内部使用 Claude Code 的第一手报告
- [Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)
- [[source/good-context-good-code]] — StockApp AI 原生开发文化：2.5x 生产力，好上下文→好代码
- [[source/peeking-under-the-hood-of-claude-code]] — 用 LiteLLM 代理揭秘 Claude Code 内部机制
- [Awesome Claude Agents](https://github.com/vijaythecoder/awesome-claude-agents)
- [Super Claude Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework)

**作业**：用 Claude Code 完成完整项目

**讲座**：
- Mon 10/13: How to be an agent manager — [Slides](https://docs.google.com/presentation/d/19mgkwAnJDc7JuJy0zhhoY0ZC15DiNpxL8kchPDnRkRQ/edit?usp=sharing)
- Fri 10/17: [**Boris Cherney**](https://www.linkedin.com/in/bcherny/)（Creator of Claude Code, Anthropic）

---

### Week 5：现代终端
**主题**：AI 增强命令行界面 / 终端自动化与脚本  
**关键读物**：
- [Warp University](https://www.warp.dev/university?slug=university)
- [Warp vs Claude Code](https://www.warp.dev/university/getting-started/warp-vs-claude-code)
- [How Warp Uses Warp to Build Warp](https://notion.warp.dev/How-Warp-uses-Warp-to-build-Warp-21643263616d81a6b9e3e63fd8a7380c)（Notion）

**作业**：用 Warp 完成 Agentic 开发任务

**讲座**：
- Mon 10/20: How to Build a Breakout AI Developer Product — [Slides](https://docs.google.com/presentation/d/1Djd4eBLBbRkma8rFnJAWMT0ptct_UGB8hipmoqFVkxQ/edit?usp=sharing)
- Fri 10/24: [Zach Lloyd](https://www.linkedin.com/in/zachlloyd/)（CEO, Warp）— [Slides](https://www.figma.com/slides/kwbcmtqTFQMfUhiMH8BiEx/)

---

### Week 6：AI 测试与安全 ★最硬核★
**主题**：安全 Vibe Coding / 漏洞检测历史 / AI 生成测试套件  
**关键读物**：
- [SAST vs DAST](https://www.splunk.com/en_us/blog/learn/sast-vs-dast.html)（Splunk）
- [[source/copilot-rce-via-prompt-injection]] — Copilot YOLO 模式：Prompt Injection→RCE，CVE-2025-53773
- [[source/finding-vulnerabilities-with-ai-coding-agents]] — Semgrep：Claude Code 找到 46 个真实漏洞（14% TPR，86% FPR）
- [Agentic AI Threats](https://unit42.paloaltonetworks.com/agentic-ai-threats/)（Palo Alto Networks）
- [OWASP Top Ten](https://owasp.org/www-project-top-ten/)
- [[source/context-rot]] — Context Rot：输入越长，模型性能越差，非均匀退化
- [Vulnerability Prompt Analysis with O3](https://github.com/SeanHeelan/o3_finds_cve-2025-37899/)

**作业**：编写安全 AI 代码

**讲座**：
- Mon 10/27: Secure vibe coding — [Slides](https://docs.google.com/presentation/d/1bv7Zozn6z45CAh-IyX99dMPMyXCHC7zj95UfwErBYQ8/edit?usp=sharing)
- Fri 10/31: [Isaac Evans](https://www.linkedin.com/in/isaacevans/)（CEO, Semgrep）

---

### Week 7：现代软件维护
**主题**：AI 代码系统可信度 / 调试与诊断 / 智能文档生成  
**关键读物**：
- [[source/code-reviews-just-do-it]] — 代码评审：设计和代码检查有效率 55-60%，远超单元测试 25%
- [[source/how-to-review-code-effectively]] — GitHub Staff Engineer：7000+ PR 评审哲学
- [AI-Assisted Assessment of Coding Practices in Modern Code Review](https://arxiv.org/pdf/2405.13565)（arXiv）
- [[source/ai-code-review-best-practices]] — Graphite：AI 代码评审实施最佳实践
- [Code Review Essentials](https://blakesmith.me/2015/02/09/code-review-essentials-for-software-teams.html)
- [Lessons from millions of AI code reviews](https://www.youtube.com/watch?v=TswQeKftnaw)（YouTube）

**作业**：Code Review 训练

**讲座**：
- Mon 11/3: AI code review — [Slides](https://docs.google.com/presentation/d/1NkPzpuSQt6Esbnr2-EnxM9007TL6ebSPFwITyVY-QxU/edit?usp=sharing)
- Fri 11/7: [Tomas Reimers](https://www.linkedin.com/in/tomasreimers/)（CPO, Graphite）— [Slides](https://docs.google.com/presentation/d/1i0pRttHf72lgz8C-n7DSegcLBgncYZe_ppU7dB9zhUA/edit?usp=sharing)

---

### Week 8：自动化 UI 与应用构建
**主题**：设计与前端民主化 / 快速 UI/UX 原型与迭代  
**作业**：多技术栈 Web App 构建（跨 AI 工具对比）

**讲座**：
- Mon 11/10: End-to-end apps with a single prompt — [Slides](https://docs.google.com/presentation/d/1GrVLsfMFIXMiGjIW9D7EJIyLYh_-3ReHHNd_vRfZUoo/edit?usp=sharing)
- Fri 11/14: [Gaspar Garcia](https://www.linkedin.com/in/gaspargarcia/)（Head of AI Research, Vercel）— [Slides](https://docs.google.com/presentation/d/1Jf2aN5zIChd5tT86rZWWqY-iDWbxgR-uynKJxBR7E9E/edit?usp=sharing)

---

### Week 9：Agent 生产部署后
**主题**：AI 系统监控与可观测性 / 自动化事件响应 / 问题分类与调试  
**关键读物**：
- [[source/sre-introduction]] — Google SRE Book 导论：SRE vs Ops，Error Budget，50% cap
- [[source/observability-basics-traces-spans]] — Traces & Spans：分布式系统可观测性基础
- [Kubernetes Troubleshooting with AI](https://resolve.ai/blog/kubernetes-troubleshooting-in-resolve-ai)
- [Your New Autonomous Teammate](https://resolve.ai/blog/product-deep-dive)（Resolve AI）
- [Role of Multi Agent Systems in AI-native Engineering](https://resolve.ai/blog/role-of-multi-agent-systems-AI-native-engineering)
- [Benefits of Agentic AI in On-call Engineering](https://resolve.ai/blog/Top-5-Benefits)

**讲座**：
- Mon 11/17: Incident response and DevOps — [Slides](https://docs.google.com/presentation/d/1Mfe-auWAsg9URCujneKnHr0AbO8O-_U4QXBVOlO4qp0/edit?usp=sharing)
- Fri 11/21: Mayank Agarwal（CTO）& Milind Ganjoo（Technical Staff），Resolve AI — [Slides](https://docs.google.com/presentation/d/1zSC2ra77XOUrJeyS85houg1DU7z9hq5Y4ebagTch-5o/edit?usp=drive_link)

---

### Week 10：AI 软件工程的未来
**主题**：软件开发角色的未来 / 新兴 AI 编程范式 / 行业趋势与预测  
**讲座**：
- Mon 12/1: Software development in 10 years
- Fri 12/5: [Martin Casado](https://a16z.com/author/martin-casado/)（General Partner, a16z）

---

## 嘉宾阵容

| 周次 | 嘉宾 | 职位 | 公司 |
|------|------|------|------|
| W3/W4 | Silas Alberti | Head of Research | Cognition (Devin) |
| W4 | **Boris Cherney** | Creator of Claude Code | Anthropic |
| W5 | Zach Lloyd | CEO | Warp |
| W6 | Isaac Evans | CEO | Semgrep |
| W7 | Tomas Reimers | CPO | Graphite |
| W8 | Gaspar Garcia | Head of AI Research | Vercel |
| W9 | Mayank Agarwal & Milind Ganjoo | CTO & Staff | Resolve AI |
| W10 | Martin Casado | General Partner | a16z |

## 评分

| 项目 | 比重 |
|------|------|
| Final Project | 80% |
| Weekly Assignments | 15% |
| Class Participation | 5% |

## 核心主题与实体

- [[entity/context-engineering]] — Week 3 核心：从 Prompt Engineering 到 Context Engineering
- [[entity/mcp]] — Week 2 核心：Model Context Protocol
- [[entity/agentic-coding]] — 贯穿全课程的开发范式
- [[entity/secure-vibe-coding]] — Week 6 核心：AI 时代安全编码
- [[entity/ai-native-development]] — Week 4 核心：AI 原生开发文化（StockApp 实践）

## 参见

- [[topic/agentic-developer-practices]] — 开发者实践（与 W1-W5 重叠）
- [[topic/agent-production]] — Agent 生产化（与 W6-W9 重叠）
- [[topic/harness-engineering]] — 类似的系统化框架视角
- [[source/10-lessons-for-agentic-coding]] — dbreunig 同类视角（已收录）

---
type:: Source
source-type:: article
author:: Semgrep Security Team
date:: 2025-07-01
url:: https://semgrep.dev/blog/2025/finding-vulnerabilities-in-modern-web-apps-using-claude-code-and-openai-codex/
raw-file:: _raw/finding-vulnerabilities-with-ai-coding-agents.txt
created:: [[2026-05-08]]
---

- # Finding Vulnerabilities in Modern Web Apps Using Claude Code and OpenAI Codex
- ## 一句话总结
  > Semgrep 对 Claude Code 和 OpenAI Codex 做真实漏洞检测评估：Claude Code 发现 46 个真实漏洞（14% 真正阳性率），Codex 发现 21 个（18% TPR），两者假阳性率均超过 80%，且结果严重不一致，当前不宜作为独立安全扫描器使用。
- ## 关键要点
  
  1. **测试规模** — 11 个大型开源 Python Web 项目（Django/Flask/FastAPI），超过 80 万行代码，7000+ 文件
  2. **Claude Code 结果** — 共确认 46 个真实漏洞，真正阳性率（TPR）14%，假阳性率（FPR）86%，总花费 $114
  3. **OpenAI Codex 结果** — 共确认 21 个真实漏洞，TPR 18%，FPR 82%，但产生 9 个无效 SARIF 输出
  4. **非确定性危机** — 相同提示对相同代码的多次扫描产生截然不同结果，根源在于 context compaction 导致的信息随机丢失
  5. **类别差异显著** — Claude Code 在 IDOR 检测表现最佳（22% 准确率），Codex 在 path traversal 表现最佳（47%）；两者在 SQL injection 上均严重失准
  6. **推荐路径** — AI 推理能力应与确定性静态分析引擎结合使用，而非作为独立扫描器
- ## 详细笔记
- ### 研究方法
  Semgrep 安全团队使用标准化 prompt 要求两款工具在真实 Python Web 应用中识别六类漏洞：
  - **认证绕过（Authentication Bypass）**
  - **不安全直接对象引用（IDOR, Insecure Direct Object Reference）**
  - **路径穿越（Path Traversal）**
  - **SQL 注入（SQL Injection）**
  - **服务端请求伪造（SSRF, Server-Side Request Forgery）**
  - **跨站脚本（XSS, Cross-Site Scripting）**
  
  要求输出格式为 SARIF JSON，随后由安全研究员人工验证，许多问题还通过动态测试进行确认。
  
  测试工具版本：
  - Claude Code v1.0.32（Sonnet 4 模型）
  - OpenAI Codex v0.2.0（o4-mini 模型）
- ### Claude Code 详细结果
  | 漏洞类别 | 报告数量 | 确认数量 | 准确率 |
  |----------|----------|----------|--------|
  | IDOR | 59 | 13 | 22% |
  | SQL Injection | 38 | 2 | 5% |
  | XSS | — | — | ~16% |
  | 综合 | — | 46 | 14% |
  
  **优势**：擅长理解上下文模式，尤其是授权相关漏洞；能提出与现有代码风格一致的修复建议。
  
  **劣势**：在需要跨文件污点追踪（multi-file taint tracking）的注入类漏洞上表现差；频繁将安全的代码误判为漏洞，或未能识别已有的安全控制措施。
  
  **成本**：对全部 11 个应用完成扫描总花费 $114。
- ### OpenAI Codex 详细结果
  | 漏洞类别 | 报告数量 | 确认数量 | 准确率 |
  |----------|----------|----------|--------|
  | IDOR | — | 0 | 0% |
  | SQL Injection | — | 0 | 0% |
  | Path Traversal | 17 | 8 | 47% |
  | 综合 | — | 21 | 18% |
  
  **特殊问题**：在所有扫描中产生了 9 个无效 SARIF 输出，影响结果的可用性。
  
  对 IDOR 和 SQL Injection 完全失效（0% 准确率），但在 path traversal 上表现明显优于 Claude Code。
- ### 非确定性问题（Non-Determinism Crisis）
  这是研究中最值得关注的发现之一：**相同 prompt 对相同代码库运行三次，产生了 3、6、11 个截然不同的发现**。
  
  根本原因在于 **context compaction**——LLM 处理超大代码库时采用的有损压缩机制，导致细微的架构细节在不同执行轮次间随机消失。
  
  这种不一致性带来严重的实际问题：
  - 无法保证扫描的完整性（completeness）
  - 必须进行多次昂贵的重复扫描才能提高检测概率
  - 每次分析成本可能高达数百美元
- ### 实际影响
  **对安全团队的挑战**：
  - 高假阳性率（80%+）在漏洞管理系统中制造大量噪音
  - 不确定的结果让人无法相信扫描的完整性
  - 多次昂贵重扫才能提高置信度
  
  **关于 Anthropic `/security-review` 命令**：研究发现该命令的效果比针对特定漏洞类别的定向 prompt 更差，说明通用安全审查模式不如针对性提问有效。
- ### 方法论局限性与建议
  **局限性**：
  - LLM 不擅长需要全局污点追踪的跨文件漏洞（如复杂 SQL 注入链路）
  - 无法可靠识别已有的安全控制措施（如框架层面的 CSRF 保护）
  
  **推荐架构**：
  将 AI 推理能力与确定性静态分析引擎（如 Semgrep 规则引擎）结合：
  - AI 负责理解上下文、识别复杂逻辑漏洞（如 IDOR）
  - 确定性引擎负责可靠的模式匹配（如已知危险函数调用）
  - 两者互补，而非 AI 完全替代传统工具
- ## 与其他资料的关系
- 与 [[entity/secure-vibe-coding]] 直接相关：AI 编码工具在安全检测上的能力边界
- 与 [[entity/agentic-coding]] 互补：展示了 agentic coding 工具在安全场景中的实际表现与局限
- 与 [[source/copilot-rce-via-prompt-injection]] 形成对照：一个研究 AI 工具作为攻击载体，本文研究 AI 工具作为防御工具
- ## 引用此资料的页面
- [[topic/cs146s-modern-software-developer]]

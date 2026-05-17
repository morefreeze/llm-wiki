---
type:: Index
updated:: [[2026-05-17]]
---

# LLM Wiki Index

> 📊 **105 pages** | 55 sources · 44 entities · 6 topics

---

## 📚 Sources（资料）

| 页面 | 一句话 | 来源 |
|------|--------|------|
| [[llm-wiki-pattern]] | 用 LLM 增量构建持久知识库的模式 | Karpathy Gist |
| [[anthropic-code-execution-with-mcp]] | 通过代码执行调用 MCP，token 消耗降 98.7% | Anthropic Blog |
| [[building-agents-that-reach-production-systems-with-mcp]] | 三种 Agent 连接方式对比，MCP 成为生产标准 | Anthropic Blog |
| [[从玩具到生产力用真实项目讲透-ai-agent-的-harness-engineering]] | Harness 层将 Agent 从玩具提升到生产力 | BestBlogs |
| [[当我们在讨论-harness-的时候我们在讨论什么]] | MiniMax × Hermes Agent 关于 Harness 的深度对谈 | BestBlogs |
| [[10-lessons-for-agentic-coding]] | 代码廉价时代开发者的 10 条实践原则 | dbreunig.com |
| [[how-anthropic-teams-use-claude-code]] | Anthropic 10 个内部团队的 Claude Code 实战报告 | Anthropic PDF |
| [[bestblogs-2.0-reading-workflow]] | 内容判断才是稀缺资源，BestBlogs 转型为阅读工作流工具 | BestBlogs |
| [[harness-knowledge-moat]] | Harness 不是目的，知识才是护城河——AI 工程团队的知识沉淀实践 | BestBlogs |
| [[karpathy-vibe-coding-to-agentic-engineering]] | Vibe Coding 只是开始，真正重要的是 Agentic Engineering | baoyu.io |
| [[hermes-agent-memory-system]] | Hermes Agent 四层记忆架构：冷热分离 + 缓存优先 + 程序记忆 | baoyu.io |
| [[coding-agent-components]] | 编程 Agent 六大核心组件：Harness 比模型更重要 | baoyu.io |
| [[harness-what-it-actually-is]] | 五子系统模型（厨房类比）+ 4 阶段实验，成功率 20%→100% | walkinglabs.github.io |
| [[why-repo-is-system-of-record]] | 仓库即规范：知识可见性缺口 + 冷启动测试 + 知识衰减率 20%/月 | walkinglabs.github.io |
| [[instruction-file-architecture]] | 路由文件 + 渐进式披露：600 行 AGENTS.md → 80 行路由文件，成功率 45%→72% | walkinglabs.github.io |
| [[session-continuity-across-sessions]] | PROGRESS.md + DECISIONS.md：重建时间从 15 分钟降到 3 分钟（78%降低） | walkinglabs.github.io |
| [[initialization-independent-phase]] | 自举契约四条件：独立初始化让多会话功能完成率高 31% | walkinglabs.github.io |
| [[wip-limit-task-boundaries]] | WIP=1：少做但做完，完成率 87.5% vs 37.5%，代码行数与功能呈负相关 | walkinglabs.github.io |
| [[feature-list-as-harness-primitive]] | 功能清单三元组是 harness 脊梁骨，完成率高 45%，诊断时间降 60-80% | walkinglabs.github.io |
| [[prevent-premature-completion]] | 置信度校准偏差（Guo 2017）+ 三层终止校验 + 三 agent 架构（$9 不可用 vs $200 可用） | walkinglabs.github.io |
| [[e2e-testing-changes-results]] | E2E 测试不仅改变结果还改变 agent 编码行为 + 架构边界执行规则 | walkinglabs.github.io |
| [[why-observability-belongs-in-harness]] | 双层可观测性 + 冲刺合同 + Anthropic 三 agent 实验（3h50m，$124.70） | walkinglabs.github.io |
| [[why-sessions-must-leave-clean-state]] | 清洁状态五维度 + 12 周熵增数据 + harness 简化原则（Lehman 定律） | walkinglabs.github.io |
| [[solve-rubiks-cube-without-formulas]] | 交换子 A B A⁻¹ B⁻¹ 替代死记公式 + Roux 桥式解法四步复原 | philoli.com |
| [[dotey-ai-writing-workflow-coze]] | "内容导演"六步工作流：素材搜集→分析→大纲→写作→润色配图→发布，扣子替代 Claude Code | @dotey / X |
| [[unreasonable-effectiveness-of-html]] | HTML 替代 Markdown 作为 LLM 输出格式：20 个示例覆盖 9 大场景 | Simon Willison / Thariq Shihipar |
| [[laozhang-ai-proxy-ecosystem]] | AI CLI 反代/中转/号池生态全景：8 大类 30+ 项目，Claude/Gemini/Codex/Copilot/Cursor/Kiro/Grok 全覆盖 | @laozhang2579 / X |
| [[gpt-5-5-instant]] | ChatGPT 新默认模型：幻觉减少 52.5%、字数减少 30.2%、Memory Sources 个性化控制 | OpenAI Blog |
| [[anthropic-claude-constitution]] | Claude 完整宪法：四层优先级架构（安全→道德→指南→有用）+ 六大章节 + 有声书 | Anthropic |
| [[dow-ufo-uap-release]] | 美国战争部 PURSUE 系统发布首批 158 个 FBI 解密 UAP 文件 | war.gov |
| [[agentic-coding-is-a-trap]] | 监督的悖论：Agentic coding 侵蚀监督 AI 所需技能，47% 调试技能下降 | larsfaye.com |
| [[thariq-html-effectiveness-x-thread]] | HTML > Markdown 的 5 条理由与 5 大场景：11M 浏览的原始第一手论证 | @trq212 / X |
| [[agent-hooks-deterministic-control]] | Hooks 在 Agent 生命周期节点注入确定性控制，规则自动执行不依赖模型记忆 | @dabit3 / X |
| [[一文带你看懂_火爆全网的Skills到底是个啥]] | Skills = Agent持久化能力模块，.md格式指令文件，区别于Prompt和MCP | 数字生命卡兹克 |
| [[Claude悄悄更新了Skills生成器_这绝对是一次史诗级升级]] | Anthropic官方Skills生成器重大升级，支持YAML frontmatter和自动测试 | 数字生命卡兹克 |
| [[安利一个11万Star的必装插件_能让你的Agent体验直接质变]] | superpowers插件集成大量Skills，Agent自动加载最佳实践 | 数字生命卡兹克 |
| [[分享6个我觉得应该必装的Skills]] | 6个必装Skills：代码审查、TDD、文档生成、安全审计、性能优化、协作规范 | 数字生命卡兹克 |
| [[所有用OpenClaw的朋友_我都劝你先装上这个能保命的Skill]] | 安全类Skill自动拦截Agent危险操作，给Agent装安全带 | 数字生命卡兹克 |
| [[今天_我决定把_卡兹克风格创作_skill_开源了]] | 风格蒸馏Skill：将个人创作风格编码为可复用指令文件 | 数字生命卡兹克 |
| [[开源_洁癖_skill_让你的Agent越用越聪明]] | 洁癖Skill：Agent自动维护优化Skills的元Skill，形成自优化闭环 | 数字生命卡兹克 |
| [[装了这个AI热点Skill之后_你再也不需要自己去刷AI新闻了]] | AIHOT免费AI新闻聚合平台+对应Skill，Agent自动追踪AI热点 | 数字生命卡兹克 |

## 🧩 Entities（实体）

| 页面 | 类型 | 核心定义 |
|------|------|----------|
| [[mcp]] | Protocol | Model Context Protocol，Agent 连接外部系统的开放标准 |
| [[code-mode]] | Pattern | Agent 通过编写代码（非直接调用）与 MCP 交互 |
| [[skills]] | Concept | 可复用的 Agent 能力单元（指令 + 脚本 + 资源） |
| [[progressive-disclosure]] | Pattern | 按需发现和加载工具定义的设计模式 |
| [[harness]] | Concept | Agent 驾驭层——安全带 + 方向盘 |
| [[tool-search]] | Pattern | 运行时按需搜索工具目录，token 减少 85%+ |
| [[mcp-apps]] | Extension | MCP 首个官方扩展，返回交互式界面 |
| [[elicitation]] | Feature | MCP server 中途暂停请求用户输入 |
| [[agentic-coding]] | Concept | 使用 AI Agent 辅助编码的开发范式，经验被放大 |
| [[living-specs]] | Practice | 随实现持续演进的活规格文档 |
| [[claude-md-files]] | Practice | 持久化 Agent 上下文的 Markdown 文件，持续改进飞轮 |
| [[checkpoint-workflow]] | Practice | 频繁提交 Git 检查点、失败时回滚的 Agent 协作安全网 |
| [[information-filtering]] | Concept | 内容判断能力——信息过载时代真正稀缺的资源 |
| [[knowledge-lifecycle]] | Concept | 五层存储 × 五种类型 × 三级成熟度 + 自动衰减的团队知识架构 |
| [[software-3-0]] | Paradigm | LLM 作为新的可编程计算机，context window 作为程序 |
| [[vibe-coding]] | Practice | 凭感觉编程（Karpathy 提出）vs Agentic Engineering 的下限/上限区分 |
| [[agent-memory-system]] | Architecture | Agent 四层记忆架构：语义/情景/程序/用户建模 + Prompt Cache 优化 |
| [[coding-harness]] | Architecture | 编程运行框架六大组件：仓库上下文/缓存复用/工具/瘦身/记忆/子 Agent |
| [[harness-5-subsystems]] | Model | 五子系统（指令/工具/环境/状态/反馈）+ 厨房类比 + 成功率 20%→100% |
| [[repo-as-system-of-record]] | Principle | 仓库即规范：知识可见性缺口 + 冷启动测试 + ACID 状态管理 |
| [[instruction-architecture]] | Pattern | 路由文件 + 渐进式披露：防止指令膨胀，中间迷失效应（Liu 2023） |
| [[session-continuity]] | Practice | 跨会话连续性工件 + 自举契约 + 上下文焦虑 + 漂移 |
| [[wip-limit]] | Practice | WIP=1 + Overreach/Under-finish + VCR + 完成证据 |
| [[feature-list-primitive]] | Pattern | 功能清单三元组（行为/验证/状态）+ 通过状态门控 + 状态机模型 |
| [[completion-validation]] | Practice | 三层终止校验 + E2E 测试 + Planner/Generator/Evaluator 架构 |
| [[harness-observability]] | Pattern | 双层可观测性（运行时+过程）+ 冲刺合同 + 任务轨迹 |
| [[clean-session-state]] | Practice | 清洁状态五维度 + 会话完整性 + 质量文档 + 幂等清理 |
| [[rubiks-cube-group-theory]] | Method | 群论解魔方：交换子原理 + Roux 桥式 + 非阿贝尔群 |
| [[commutator-technique]] | Technique | A B A⁻¹ B⁻¹ 交换子：开门-操作-关门的核心模式 |
| [[content-director-pattern]] | Pattern | 人做"导演"（选题/观点/审美），AI 做执行团队，六步写作工作流 |
| [[coze-skills-platform]] | Platform | 字节跳动扣子 Skills，Claude Code 的低门槛替代，内置画图/脚本/沙盒 |
| [[html-as-llm-output-format]] | Practice | HTML 替代 Markdown 作为 LLM 输出格式：9 大场景 + 关键 Prompt 模式 |
| [[ai-cli-proxy-ecosystem]] | Ecosystem | AI CLI 反代/中转 30+ 项目全景：OAuth 中转/协议逆向/进程代理/号池四大路线 |
| [[gpt-5-5-instant]] | Model | OpenAI 新默认模型：幻觉↓52.5%、字数↓30.2%、Memory Sources 个性化控制 |
| [[claude-constitution]] | Document | Anthropic Claude 宪法：四层优先级（安全→道德→指南→有用）+ AI 意识讨论 |
| [[dow-uap-pursue]] | System | PURSUE 总统解封系统：滚动发布 UAP 解密文件，首批 158 个 FBI 文件 |
| [[uap-declassification]] | Movement | UAP 解密运动：从海军视频到 PURSUE 系统的政策演变里程碑 |
| [[agent-hooks]] | Mechanism | Agent 生命周期六节点确定性控制：Prompts 引导，Hooks 保证执行 |
| [[Skills]] | Concept | Agent持久化能力模块，.md格式指令文件，区别于Prompt和MCP |
| [[OpenClaw]] | Platform | AI Agent平台，支持通过Skills系统扩展Agent能力 |
| [[superpowers]] | Project | 11万Star开源Skills集合，Agent自动加载最佳实践工作流 |
| [[Agent安全]] | Concept | Agent执行危险操作时自动拦截的安全护栏 |
| [[风格蒸馏]] | Technique | 将个人创作风格编码为可复用Skill指令文件 |
| [[洁癖Skill]] | Meta-Skill | Agent自动维护和优化其他Skills的元Skill |
| [[AIHOT]] | Platform | 免费AI热点新闻聚合平台，自动追踪AI领域最新动态 |
| [[数字生命卡兹克]] | Author | 微信公众号作者，专注AI Agent和Skills生态科普 |

## 🌐 Topics（主题）

| 页面 | 核心问题 | 涉及实体 |
|------|---------|----------|
| [[cs146s-modern-software-developer]] | Stanford CS146S：AI 辅助软件开发全生命周期 10 周课程 | [[agentic-coding]] [[context-engineering]] [[mcp]] |
| [[harness-engineering]] | AI coding agent 长期可靠运行框架（11 讲课程） | [[harness]] [[harness-5-subsystems]] [[session-continuity]] [[clean-session-state]] |
| [[agent-efficiency]] | Agent 规模化后 token 和效率挑战 | [[code-mode]] [[progressive-disclosure]] [[tool-search]] |
| [[agent-production]] | Agent 从玩具到生产化的路径 | [[mcp]] [[harness]] [[harness-5-subsystems]] [[session-continuity]] [[clean-session-state]] |
| [[agentic-developer-practices]] | 代码廉价时代开发者如何调整工作方式 | [[agentic-coding]] [[wip-limit]] [[completion-validation]] [[feature-list-primitive]] [[session-continuity]] |
| [[information-workflow]] | 从发现到复用的完整知识输入路径 | [[information-filtering]] [[llm-wiki-pattern]] |

## 📊 Stats

- Sources: 55
- Entities: 44
- Topics: 6
- Synthesis: 0

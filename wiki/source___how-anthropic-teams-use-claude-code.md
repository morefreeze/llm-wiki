---
type:: Source
source-type:: report
author:: Anthropic
date:: 2026-05-01
url:: https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf
raw-file:: _raw/how-anthropic-teams-use-claude-code.txt
created:: [[2026-05-06]]
---

# How Anthropic Teams Use Claude Code

## 一句话总结
> Anthropic 10 个内部团队（含法务、市场等非技术团队）的 Claude Code 实战报告：跨职能采用、量化收益、通用模式与最佳实践。

## 关键要点

1. **非技术团队同样受益** — 法务、市场、产品设计师用 Claude Code 构建生产级工具，不需要工程师介入
2. **量化收益显著** — 基础设施调试：15分钟→5分钟；广告文案：2小时→15分钟；数据科学：2-4倍提速；ML研究：节省80%时间
3. **Claude.md 文件是核心** — 所有团队都强调写详细的 Claude.md；这是持续改进的飞轮
4. **Checkpoint 工作流** — 频繁提交、实验失败时回滚，是与 Agent 协作的基本纪律
5. **同步 vs 异步任务分类** — 外围功能/原型可异步（auto-accept），核心业务逻辑需同步监督
6. **先 Claude.ai 规划，再 Claude Code 实现** — 多个团队（产品设计、法务）的两步工作流

## 10 个团队详述

| 团队 | 核心用法 | 代表性收益 |
|------|---------|-----------|
| Data Infrastructure | Kubernetes 调试截图、非技术人员 plain-text 工作流 | 无需网络专家解决 K8s 问题 |
| Product Development | auto-accept 快速原型、Vim mode（70% 由 Claude 写） | 更快的功能迭代速度 |
| Security Engineering | Terraform 审查、TDD 工作流、自定义 slash 命令（占 monorepo 50%） | 调试 15分钟→5分钟 |
| Inference | ML 概念解释、跨语言翻译（写 Rust 无需学 Rust） | ML 研究时间减少 80% |
| Data Science & ML | 构建 5000 行 TypeScript 应用（几乎没有 JS 经验）、slot machine 策略 | 2-4x 重构提速 |
| API Knowledge | 把 Claude Code 作为每个任务的"第一站" | 独立调试陌生代码库 |
| Growth Marketing | Google Ads 创意自动化、Figma 插件（100个变体/秒）、Meta Ads MCP server | 广告文案：2h→15min；10x 产出 |
| Product Design | 粘贴设计稿截图生成原型、非设计师做 state management 修改 | 2-3x 执行速度；周→2次30分钟通话 |
| RL Engineering | 监督式自主功能开发、checkpoint 工作流（~1/3成功率） | 实验性开发方式成为可能 |
| Legal | 1小时构建无障碍辅助工具、法律"电话树"系统 | 非开发者构建生产级工具 |

## 跨团队通用模式

### 普遍使用场景（几乎每个团队都有）
1. **代码库理解与上手** — 秒级找到相关文件，替代问同事
2. **测试生成** — 自动补充 edge case，节省大量精力
3. **文档维护** — [[entity/claude-md-files]] 作为持续改进飞轮
4. **独立调试** — 敢于在陌生代码库中独立工作

### 通用技巧
- 写详细的 [[entity/claude-md-files]]（workflows、tools、expectations 都要记录）
- 使用 [[entity/checkpoint-workflow]]（频繁提交，失败时回滚）
- 外围任务用 auto-accept，核心功能需监督
- 在 Claude.ai 规划，在 Claude Code 实现
- 从最少信息开始，迭代而非一次性解决

## 与其他资料的关系
- 与 [[source/10-lessons-for-agentic-coding]] 互补：Breunig 是理论原则，本文是 Anthropic 内部的实战案例
- 与 [[entity/harness]] 的关联：本文的 Claude.md 文件和 checkpoint 实践正是 Harness 思想的具体落地
- 与 [[entity/agentic-coding]] 直接相关：大量具体案例验证了"经验放大"、"代码廉价但要谨慎"等原则
- 补充 [[entity/living-specs]]：end-of-session documentation updates 是 living specs 在实践中的具体形式

## 引用此资料的页面
- [[entities/claude-md-files]]
- [[entities/checkpoint-workflow]]
- [[entities/agentic-coding]]
- [[topics/agentic-developer-practices]]

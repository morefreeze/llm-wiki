---
type:: Source
source-type:: article
author:: Sarah Vessels (GitHub Staff Engineer)
date:: 2023-09-12
url:: https://github.blog/developer-skills/github/how-to-review-code-effectively-a-github-staff-engineers-philosophy/
raw-file:: _raw/how-to-review-code-effectively.txt
created:: [[2026-05-08]]
---
# How to Review Code Effectively: A GitHub Staff Engineer's Philosophy

## 一句话总结
> 代码审查是对话而非裁决——审查者应以提问代替命令，以具体证据支撑反馈，并把及时解锁队友视为高于推进自己工作的优先级。

## 关键要点
1. Sarah Vessels 在 8 年内审查了超过 7,000 个 PR，她把代码审查视为与自己写代码同等重要的核心职责
2. Pull request 是"对话的开始"，审查者是"第二双眼睛"，而非代码质量的终审法官
3. 好的反馈区分 blocker（阻断合并的问题）与 suggestion（可选改进），并提供具体例子和"为什么"的解释
4. 审查者应主动认可好的代码——正向反馈与批评性反馈同样重要，能建立心理安全感
5. 已审查的代码比进行中的代码更接近上线，因此优先审查队友的 PR 能最大化团队整体速度

## 详细笔记

### 作者背景与核心立场

Sarah Vessels 是 GitHub 的 Staff Engineer，拥有 8 年代码审查经验，审查过 7,000+ 个 pull request。她的核心立场是：**代码审查是一项职业责任，而非负担**。她甚至会暂停自己的开发工作，优先审查队友标记为"ready to merge"的 PR。

理由是：已经被审查过的代码比正在开发中的代码更接近上线，因此从团队整体交付速度的角度看，及时给出反馈是更高价值的行为。

### 发现与管理 PR 的策略

**发现 PR 的方法**
- 将 GitHub notifications inbox 固定为浏览器标签页，保持持续关注
- 使用 Slack 频道和 GitHub-Slack 集成，通过 team-specific label 过滤相关 PR
- 执行精准搜索查询，例如：`is:open archived:false is:pr org:github -is:draft team-review-requested:github/relevant-codeowner-team`

**避免通知疲劳**
Vessels 特别强调 CODEOWNERS 文件中团队范围的重要性。过于宽泛的 code owner 团队会产生两个问题：
1. "通知洪水"——关键审查者在噪音中错过重要变更
2. "责任扩散"——每个人都以为别人会处理，最终没人处理

**自动化工具**
- CODEOWNERS 文件定义清晰边界
- Branch protection rules 保证流程一致性
- First-responder 轮换系统（可集成 PagerDuty API）
- 自动化评论设置审查者预期

### 高质量审查 vs. 低质量审查的特征

**好的审查应该**
- 明确区分个人偏好（preference）和阻断性问题（blocker）
- 提供具体示例，最好来自同一个代码库中已有的模式
- 引用具体的代码细节和证据
- 解释建议背后的"为什么"，而非仅给出"改成什么"

**差的审查的典型表现**
- 缺乏具体性：只说"我不喜欢这个"，没有任何上下文
- 模糊断言："这个不会工作"，却不解释原因
- 错过提供支持性证据的机会
- 没有说明建议是否需要在合并前解决

**优秀审查评论的实例**（文章中引用）
> "I see your new method matches the existing style...Having that many parameters hurts readability...What do you think about refactoring this method in a later pull request?"

这个例子展示了三个要素：先肯定符合规范之处、解释问题的原因（可读性），以及通过提问而非命令来推进讨论，并给出了在后续 PR 中解决的灵活路径。

### 反馈方式：提问优于命令

Vessels 的核心原则之一是：**把代码作者视为自己变更的领域专家（subject matter expert）**。

审查者的提问式反馈效果好于命令式，例如：
- 询问数据的形状（data shape）
- 询问边界情况（edge cases）如何处理
- 询问某操作的资源消耗和性能影响
- 邀请作者通过测试或指标来验证假设

这种方式既尊重作者的判断，也可能从对话中获得审查者自己没有的上下文信息。

### 正向反馈的重要性

Vessels 强调审查者应该主动认可好的代码，例如：
- "Looks like this matches the pattern used in other classes"
- "Thanks for adding a test!"

正向确认（affirmation）的作用是建立心理安全感（psychological safety），让作者在收到批评性反馈时不会感到纯粹的否定。这对于初级开发者尤其重要。

她还特别指出：**不清楚之处对初级开发者来说是完全合理的提问机会**——"If it's not obvious to you, that's valid. It won't be obvious to someone else either!"（如果对你来说不明显，这个疑问就是合理的，因为对别人来说也不会明显。）

### 审批哲学：谨慎使用"Request Changes"

Vessels 很少使用"Request Changes"，认为它"过于强硬"（too heavy-handed）。她更倾向于信任团队知道何时合并合适。

她对反馈的分级处理：
- **Blocker（阻断合并）**：安全漏洞、会导致生产故障的变更
- **Suggestion（可选改进）**：重构建议、代码风格改进、可选增强

非关键性的反馈可以在合并后解决，不应以此阻止交付。她还鼓励"feature flag + minimal diff"策略：变更越小越容易在生产中快速回滚。

### 管理自己的 PR：提交前自我审查

Vessels 建议在请求他人审查之前先做自我审查（self-review）：
- 对不明显的逻辑留下解释性评论
- 识别是否需要将过大的 PR 拆分
- 向审查者展示自己的认真态度

**Draft PR 的使用策略**：用 draft 状态标记未完成的工作。在根据反馈修改时，将 PR 改回 draft 状态，避免重复打扰已经给过反馈的审查者。

**合并后审查**：即使 PR 已经合并，记录下来的反馈仍然有价值，可以作为未来读者的"面包屑路径"（breadcrumb trail）。

### 审查作为职业资产

Vessels 指出，代码审查评论是可链接的产出物（linkable artifacts），在晋升对话中能够证明：
- 技术影响力
- 沟通能力
- 跨领域专业知识

这使得高质量的代码审查不仅对团队有价值，对个人职业发展也有直接回报。

### AI 编码工具的注意事项

文章末尾提到：尽管 AI 工具有各种安全措施，人类审查者仍然是最后一道防线，对 AI 生成的代码需要保持同等甚至更高的警惕性。

## 与其他资料的关系
- 与 [[source/code-reviews-just-do-it]] 的关系：Atwood 用数据回答"为什么做审查"，Vessels 用 7,000+ PR 的实战经验回答"怎么做好审查"；两篇文章在价值观上高度一致，在层次上互补
- 与 [[source/ai-code-review-best-practices]] 的关系：Vessels 提到人类是 AI 代码的最后防线，Graphite 的文章则从工具实现角度讨论如何让 AI 审查辅助而非替代人类审查；两者共同构成"人机协作审查"的完整图景

## 引用此资料的页面
- [[topic/cs146s-modern-software-developer]]

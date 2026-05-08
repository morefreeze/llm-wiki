---
type:: Source
source-type:: article
author:: Jeff Atwood
date:: 2008-11-04
url:: https://blog.codinghorror.com/code-reviews-just-do-it/
raw-file:: _raw/code-reviews-just-do-it.txt
created:: [[2026-05-08]]
---
# Code Reviews: Just Do It

## 一句话总结
> 代码审查是提升代码质量最有效的单一实践——其缺陷发现率（55-60%）远超单元测试（25%），没有任何借口不做。

## 关键要点
1. Code inspection 的缺陷检测率（55-60%）在所有质量保证手段中最高，远超 unit testing（25%）、function testing（35%）和 integration testing（45%）
2. 多个真实组织的历史数据证明代码审查能将 bug 率降低 80% 以上，同时提升生产力
3. 实施代码审查的两大现实障碍是：找到愿意审查的同伴，以及分配审查时间
4. Lightweight review（轻量审查）比 formal inspection（正式审查）更容易落地，团队应该从"just do it"开始，而非等待完美流程

## 详细笔记

### 核心论点

Jeff Atwood 在这篇文章中的核心主张是：**peer code review（同伴代码审查）是改善代码质量最有效的单一实践**。代码在未经他人审查之前，不应被视为"完成"。这不是一个可选的最佳实践，而是每个严肃对待工程质量的团队必须执行的规范。

### 缺陷检测率数据（来自 Steve McConnell《Code Complete》）

Atwood 引用了 McConnell 书中的数据，按检测率从低到高排列各类质量保证手段：

| 方法 | 缺陷检测率 |
|------|-----------|
| Unit testing | 25% |
| Function testing | 35% |
| Integration testing | 45% |
| **Design/Code inspection** | **55-60%** |

Code inspection 以显著优势居首，这一数据直接支持了 Atwood 的论点：将时间投入代码审查，比单纯增加测试覆盖率更有效。

### 历史案例数据

文章援引多个组织的实际案例来强化论点：

**维护型组织案例**
- 实施审查前：单行代码修改的错误率高达 55%
- 实施审查后：错误率降至 2%，95% 的修改在第一次就能正确运行

**程序开发组对比实验**
- 有审查的 6 个程序：平均每 100 行代码 0.82 个错误
- 无审查的 5 个程序：平均每 100 行代码 4.5 个错误
- 结论：审查使 bug 率降低超过 80%

**其他组织数据**
- **Aetna Insurance**：通过 inspection 发现了 82% 的程序错误
- **IBM Orbit 项目**：提前交付，实际 bug 数量仅为预期的约 1%
- **AT&T 某部门**：生产力提升 14%，缺陷减少 90%
- **Jet Propulsion Laboratories**：估计每次 inspection 节省约 $25,000

这些数据横跨不同行业、不同规模的组织，说明代码审查的收益具有普遍性，而非某一特定领域的偶然现象。

### 实施障碍分析

Atwood 承认代码审查并非没有摩擦，他识别出两个主要障碍：

1. **找到合适的审查者**：需要一个受尊重的同伴（respected peer）愿意花时间审查你的代码。这在小团队或独立开发者环境中尤其困难。

2. **时间分配**：审查本身需要时间投入。在项目压力下，审查往往是第一个被砍掉的环节。

Atwood 对这两个障碍的回应是直接的：这些都是可以克服的组织问题，而非技术问题，不应成为放弃审查的理由。

### Lightweight vs. Formal Review

文章隐含的立场是：**轻量级的审查好过没有审查**。Atwood 推荐 Karl Wiegers 的书《Peer Reviews in Software: A Practical Guide》作为希望建立审查流程的团队的参考，但他的标题"Just Do It"本身就传达了核心信息：不要因为没有完美的正式流程而推迟审查。

从 formal inspection（需要会议、记录、角色分工）到 lightweight peer review（简单地让同事看一下你的 PR）都是有价值的，关键是要开始做。

### 文章的修辞策略

Atwood 的写作风格是用数据说话，然后给出简单明确的行动指令。他没有讨论"什么情况下不需要审查"，而是选择了更有力的极端立场：**代码审查应该是非谈判性的团队规范（non-negotiable team practice）**。这种修辞策略更适合推动工程文化改变。

## 与其他资料的关系
- 与 [[source/how-to-review-code-effectively]] 的关系：Atwood 建立了"为什么要做审查"的理论基础（数据驱动），Sarah Vessels 的文章则回答"如何做好审查"的操作问题，两者互补
- 与 [[source/ai-code-review-best-practices]] 的关系：Atwood 的数据论证了人工审查的价值，AI 审查工具则是在此基础上的效率扩展；但 AI 工具的缺陷检测率数据（70-90% 用于常见问题）需要与 Atwood 引用的传统 inspection 数据分开理解，因为两者定义的"缺陷"范围不同

## 引用此资料的页面
- [[topic/cs146s-modern-software-developer]]

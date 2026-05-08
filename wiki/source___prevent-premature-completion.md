---
type:: Source
tags:: #harness #premature-completion #confidence-calibration #termination-criteria #multi-agent
created:: [[2026-05-07]]
url:: https://walkinglabs.github.io/learn-harness-engineering/zh/lectures/lecture-09-why-agents-declare-victory-too-early/
author:: walkinglabs.github.io
raw:: [[source/prevent-premature-completion]]
---

# 防止 Agent 提前宣告完成（Learn Harness Engineering L09）

> **一句话**：Agent 系统性地过度自信（Guo et al.2017 证明的校准偏差）——完成判定必须外部化，harness 独立验证，不信任 agent 的"感觉"。

## 关键观点

### 1. 置信度校准偏差（客观存在）

Guo 等人 2017 年 ICML 论文：现代神经网络系统性地过度自信，模型自报置信度显著高于实际准确率。AI 编码 agent 也一样：对复杂多文件任务，置信度校准偏差显著为正。Anthropic 2026 年研究：agent 被要求评估自己的工作时，系统性地过度正面评价——即使人类观察者认为质量明显不达标。

### 2. 单元测试通过 ≠ 任务完成

单元测试隔离设计制造系统性盲区：

| 盲区类型 | 说明 |
|---------|------|
| 接口不匹配 | 两端各自 mock 都通过，但实际交互格式不一致 |
| 状态传播错误 | mock 环境每次全新，不暴露跨层状态不一致 |
| 环境依赖性 | 测试环境一切 mock，真实环境因配置差异失败 |

### 3. 三层终止校验

| 层级 | 内容 | 作用 |
|------|------|------|
| 第一层 | 语法与静态分析 | 最低限度检查，成本最低 |
| 第二层 | 运行时行为验证（测试+启动+关键路径） | 核心完成证据 |
| 第三层 | 系统级确认（E2E+集成+用户场景） | 防过早声明的最后防线 |

层层递进，前层不过不许进入后层。

### 4. Planner + Generator + Evaluator 架构

"干活的人"和"检查的人"分开，解决自我评价偏差：

| 架构 | 运行时长 | 成本 | 核心功能是否可用 |
|------|---------|------|----------------|
| 单 agent 裸跑 | 20 分钟 | $9 | 否（游戏实体无响应） |
| 三 agent（planner + generator + evaluator） | 6 小时 | $200 | 是（可正常游玩） |

同一个模型（Opus 4.5），同一段提示词（"做一个 2D 复古游戏编辑器"），区别只在 harness。来源：Anthropic harness design for long-running application development。

### 5. 面向 Agent 的错误消息设计

失败信息要包含修复指导，不只说"出了什么问题"：

```
Test failed: POST /api/reset-password returned 500.
Check that the email service config exists in environment variables.
The template file should be at templates/reset-email.html.
```

## 相关实体

- [[entity/completion-validation]] — 完成校验 + 验证-确认双闸门核心概念
- [[entity/harness-observability]] — evaluator 是可观测性的实现载体
- [[entity/feature-list-primitive]] — 终止标准的定义依赖功能清单三元组

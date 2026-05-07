---
type:: Entity
created:: [[2026-05-07]]
updated:: [[2026-05-07]]
sources:: [[harness-what-it-actually-is]]
related:: [[harness]], [[coding-harness]], [[session-continuity]], [[repo-as-system-of-record]], [[clean-session-state]]
---

# Harness 五子系统模型

Harness 不是一个 prompt 文件——它由五个子系统组成，缺少任何一个都不是完整的 harness。就像餐厅只有食材没有灶台、刀具、菜谱和出菜流程，那不叫餐厅，那叫冰箱。

## 五子系统（厨房类比）

| 子系统 | 厨房类比 | 核心作用 |
|--------|---------|---------|
| **指令**（AGENTS.md 50-200行） | 菜谱架 | Agent 知道"该做什么" |
| **工具**（shell + 最小权限） | 刀具架 | Agent 有能力执行 |
| **环境**（锁定依赖 + 版本） | 灶台 | 稳定的运行基础 |
| **状态**（PROGRESS.md） | 备菜台 | 跨会话的工作记录 |
| **反馈**（验证命令） | 出菜检查口 | 判断是否做对了 |

## 实验数据：成功率 20% → 100%

四阶段实验：

| 阶段 | 配置 | 成功率 |
|------|------|--------|
| 阶段 1（空厨房） | 无 harness | ~20% |
| 阶段 2（加菜谱架） | 仅 AGENTS.md | ~45% |
| 阶段 3（加出菜检查口） | 指令 + 验证 | ~80% |
| 阶段 4（加备菜台） | 完整五子系统 | ~100% |

**反馈子系统的 ROI 最高**：一个简单的 `make test` 命令就能把成功率从 20% 提升到接近 100%——因为 agent 现在知道自己做没做对，而不是凭感觉猜。

## Harness 也会腐化

> "Harness 和代码一样会腐化，要还 harness 债。"

如果 harness 不随项目一起更新，它描述的项目状态就和实际代码脱节——就像菜谱上写的是上个月的食材，而厨房里的食材已经全换了。随着模型能力提升，应定期审查并移除不再必要的 harness 组件（见 [[clean-session-state]] 的 harness 简化原则）。

## 与其他概念的关系

- **指令子系统** → [[instruction-architecture]]：路由文件 + 专题文档架构，防止指令膨胀
- **状态子系统** → [[session-continuity]]：PROGRESS.md + DECISIONS.md 实现跨会话连续性
- **状态子系统** → [[repo-as-system-of-record]]：仓库是状态的唯一权威来源
- **反馈子系统** → [[completion-validation]]：三层终止校验 + E2E 测试
- **反馈子系统** → [[harness-observability]]：双层可观测性扩展

## 参考来源

- [[harness-what-it-actually-is]] — Harness 五子系统完整定义 + 实验数据

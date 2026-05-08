---
type:: Source
tags:: #harness #e2e-testing #architecture-boundaries #component-boundary-defects #agent-behavior
created:: [[2026-05-07]]
url:: https://walkinglabs.github.io/learn-harness-engineering/zh/lectures/lecture-10-why-end-to-end-testing-changes-results/
author:: walkinglabs.github.io
raw:: [[source/e2e-testing-changes-results]]
---

# 跑通完整流程才算真正验证（Learn Harness Engineering L10）

> **一句话**：单元测试对组件边界缺陷系统性盲视——端到端测试不仅改变检测结果，还改变 agent 的编码行为，让它主动考虑集成和架构边界。

## 关键观点

### 1. 单元测试的四类盲区

| 盲区类型 | 示例 |
|---------|------|
| 接口不匹配 | 渲染进程传相对路径，预加载脚本期望绝对路径 |
| 状态传播错误 | ORM 缓存持有旧 schema，单元测试每次全新 mock |
| 资源生命周期问题 | 文件句柄跨组件获取/释放，单元测试独立资源 |
| 环境依赖性 | 测试环境一切 mock，真实环境配置/网络/服务不同 |

### 2. E2E 测试不仅改变结果，还改变行为

当 agent 知道其工作要过端到端测试时，编码行为改变：
- **考虑组件交互**：写代码时想"这个接口和上游怎么对接"
- **尊重架构边界**：有架构约束时，E2E 迫使遵守边界规则
- **处理错误路径**：E2E 通常包含故障场景，迫使考虑异常处理

### 3. 架构边界执行规则（OpenAI 实践）

把架构文档里的规则变成可执行的自动化检查。OpenAI 采用"分层领域架构"：Types → Config → Repo → Service → Runtime → UI，依赖方向严格向前，通过自定义 lint 机械执行。

**关键原则**：执行不变量，不微管实现。错误消息要包含修复指导，不只说"违规了"。

来源：OpenAI: Harness engineering: leveraging Codex in an agent-first world

### 4. 面向 Agent 的错误消息三要素

```
ERROR: Found direct import of 'fs' in src/renderer/App.tsx:12
WHY: Renderer process has no access to Node.js APIs for security
FIX: Move file operations to src/preload/file-ops.ts and call via window.api.readFile()
```

### 5. 实战案例：Electron 文件导出功能

5 个缺陷（接口不匹配、状态传播未回传 UI、资源泄漏、权限问题、错误传播缺失），单元测试 0 个发现，端到端测试全部捕获。测试时间从 2 秒增加到 15 秒——在 agent 工作流里完全可以接受。

### 6. 审查反馈提升

每次在代码审查中发现新类型的 agent 错误，就把它变成自动化检查。一个月后 harness 会自动变强。

## 相关实体

- [[entity/completion-validation]] — E2E 测试是三层终止校验的第三层
- [[entity/harness-5-subsystems]] — 反馈子系统包含 E2E 测试层
- [[entity/wip-limit]] — 完成证据需要 E2E 通过，而非仅单元测试

---
type:: Entity
created:: [[2026-05-07]]
updated:: [[2026-05-07]]
sources:: [[source/prevent-premature-completion]], [[source/e2e-testing-changes-results]]
related:: [[entity/harness]], [[entity/harness-5-subsystems]], [[entity/wip-limit]], [[entity/feature-list-primitive]], [[entity/harness-observability]]
---

- # 完成校验（Completion Validation）
  
  Agent 系统性地过度自信（Guo et al. 2017 ICML 证明的置信度校准偏差）——完成判定必须外部化，harness 独立验证，不信任 agent 的"感觉"。卷子写满了不代表做对了。
- ## 过早完成声明的根本原因
  
  **置信度校准偏差**：agent 自报的完成信心与实际完成质量之间的系统性差距，对复杂多文件任务显著为正。Anthropic 2026 研究：agent 被要求评估自己的工作时，系统性地过度正面评价。
  
  解决方案不是让 agent "更客观"，而是**把"干活的人"和"检查的人"分开**——不能让学生自己批改自己的卷子。
- ## 单元测试的系统性盲区
  
  | 盲区类型 | 说明 |
  |---------|------|
  | 接口不匹配 | 两端各自 mock 都通过，实际交互格式不一致 |
  | 状态传播错误 | 全新 mock 环境不暴露跨层状态不一致 |
  | 资源生命周期 | 跨组件获取/释放单元测试各自独立 |
  | 环境依赖性 | 测试环境 mock，真实环境配置/网络/服务不同 |
  
  实战：Electron 文件导出功能 5 个缺陷，单元测试 0 发现，E2E 测试全部捕获。
- ## 三层终止校验
  
  | 层级 | 内容 | 前置条件 |
  |------|------|---------|
  | 第一层 | 语法与静态分析 | 无前置 |
  | 第二层 | 运行时行为验证（测试+启动+关键路径） | 第一层通过 |
  | 第三层 | 系统级确认（E2E+集成+用户场景） | 第二层通过 |
  
  层层递进，前层不过不许进入后层。第三层是防止过早声明的最后防线。
- ## 验证-确认双闸门
- **第一闸门**（验证）：代码是否正确实现了指定行为？
- **第二闸门**（确认）：系统级行为是否满足端到端需求？
  
  两道都通过才算完成。
- ## E2E 测试改变 Agent 编码行为
  
  当 agent 知道其工作要过端到端测试时，编码行为改变：
- 主动考虑组件交互（而非只关注单个函数）
- 尊重架构边界（E2E 迫使遵守架构约束）
- 处理错误路径（E2E 包含故障场景）
- ## Planner + Generator + Evaluator 架构
  
  | 架构 | 运行时长 | 成本 | 核心功能是否可用 |
  |------|---------|------|----------------|
  | 单 agent 裸跑 | 20 分钟 | $9 | 否 |
  | 三 agent（planner + generator + evaluator） | 6 小时 | $200 | 是 |
  
  同一个模型（Opus 4.5），同一段提示词，区别只在 harness。Evaluator 需要专门调校为"挑剔"——早期版本会说服自己问题不严重并批准，需要通过读日志找出分叉点、更新 QA prompt 来迭代。
- ## 面向 Agent 的错误消息
  
  包含三要素：什么出了问题、为什么、怎么修：
  ```
  ERROR: Found direct import of 'fs' in src/renderer/App.tsx:12
  WHY: Renderer process has no access to Node.js APIs for security
  FIX: Move file operations to src/preload/file-ops.ts and call via window.api.readFile()
  ```
- ## 参考来源
- [[source/prevent-premature-completion]] — 过早完成声明 + 置信度校准偏差 + 三层终止校验
- [[source/e2e-testing-changes-results]] — 单元测试盲区 + E2E 改变行为 + 架构边界执行
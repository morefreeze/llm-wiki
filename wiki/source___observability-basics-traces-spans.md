---
type:: Source
source-type:: article
author:: Last9 Team
date:: 2024-01-15
url:: https://last9.io/blog/traces-spans-observability-basics/
raw-file:: _raw/observability-basics-traces-spans.txt
created:: [[2026-05-08]]
---

- # Traces & Spans: Observability Basics
- ## 一句话总结
  > Trace 是一次请求穿越分布式系统全程的完整记录，Span 是其中每个操作单元——通过 Context Propagation 串联，形成可视化的调用链，让微服务调试从"大海捞针"变为"精准定位"。
- ## 关键要点

  1. **Trace 与 Span 的层级关系** — 一个 Trace 由多个 Span 组成，Span 嵌套表达父子调用关系，共同还原请求完整路径
  2. **Context Propagation（上下文传播）** — Trace ID 和 Span ID 随请求跨服务传递（通常通过 HTTP 头），是跨边界追踪的核心机制
  3. **Span 包含丰富元数据** — 不仅有时间戳，还包括操作名、状态、自定义属性、事件和关联链接
  4. **采样策略** — 全量追踪代价过高，头部采样 vs 尾部采样各有适用场景，尾部采样更适合捕获错误
  5. **三大信号的关联** — Traces、Metrics、Logs 相互关联才能发挥可观测性的最大价值
  6. **OpenTelemetry 是行业标准** — 提供厂商中立的 API/SDK，支持主流语言的自动和手动 instrumentation
  7. **Microservices 调试的核心工具** — Traces 让跨服务性能瓶颈和故障根因变得可见
  8. **生产环境开销可控** — 正确配置下追踪库的性能影响低于 3%，采样进一步降低影响
- ## 详细笔记
- ### 核心概念：Trace 与 Span

  **Trace** 表示一次请求从发起到完成穿越分布式系统的完整旅程。

  **Span** 是这段旅程中的最小工作单元，代表一次具体操作：一次数据库查询、一次 API 调用、一次函数执行。

  两者的层级关系：
  ```
  Trace
  ├── Span (API Gateway)       # 根 Span
  │   ├── Span (Auth Service)  # 子 Span
  │   └── Span (User Service)  # 子 Span
  │       └── Span (DB Query)  # 孙 Span
  └── Span (Response Format)
  ```

  通过这种嵌套结构，可以直观还原一次请求在系统中的完整调用图谱，以及每段操作的耗时分布。

- ### Span 的数据结构

  Span 不只包含时间信息，而是一个富含上下文的数据单元：

  | 字段 | 说明 |
  |------|------|
  | **Operation Name** | 操作的标识名称，如 `user-service/get-profile` |
  | **Start / End Time** | 精确的开始和结束时间戳 |
  | **Status** | 成功或错误状态码 |
  | **Attributes** | 自定义键值对，如 `user_id`、`feature_flag` |
  | **Events** | Span 生命周期内的重要事件记录 |
  | **Links** | 与其他 Span 的关联引用 |
  | **Span ID / Trace ID** | 身份标识，用于传播和关联 |

- ### 分布式追踪的核心机制：Context Propagation

  追踪跨越服务边界依靠**上下文传播**：当请求进入系统时，生成唯一的 Trace ID，该 ID 随请求在所有服务间传递（通常通过 HTTP 请求头）。

  **W3C Trace Context 标准**规定了两个核心头字段：
  - **`traceparent`**：包含 Trace ID 和父 Span ID，格式标准化
  - **`tracestate`**：允许携带厂商自定义的上下文数据

  这一标准确保不同服务、不同语言、不同厂商的追踪实现能够无缝互通。

  常见传播场景：
  - HTTP/gRPC 请求头
  - 消息队列消息元数据（Kafka、RabbitMQ）
  - 异步任务上下文
  - 数据库连接注释

- ### 采样策略（Sampling）

  全量追踪会产生海量数据，实践中必须采样。三种主要策略：

  | 策略 | 时机 | 优点 | 缺点 |
  |------|------|------|------|
  | **头部采样（Head-based）** | 请求进入时决定 | 实现简单，开销低 | 无法保证捕获低概率错误 |
  | **尾部采样（Tail-based）** | 请求完成后决定 | 可优先保留错误 Trace | 需要缓冲全量数据，成本高 |
  | **优先级采样（Priority）** | 混合策略 | 兼顾重要操作和资源限制 | 配置复杂 |

  **推荐实践**：对错误请求和慢请求始终采样（尾部采样），对正常请求按比例采样。

- ### 与 Logs、Metrics 的关联（三大可观测性信号）

  可观测性的真正价值来自三类信号的协同：

  - **Metrics（指标）**：聚合数值，展示系统整体健康状态，如 QPS、错误率、延迟 P99
  - **Logs（日志）**：离散事件记录，包含详细上下文信息
  - **Traces（追踪）**：请求级别的端到端调用链路

  **关联手段**：
  - **Exemplar Trace**：将 Metric 数据点链接到产生该数据点的具体 Trace，快速从"指标异常"跳转到"具体请求"
  - **Trace ID 注入日志**：在每条日志中携带当前 Trace ID，实现"Trace → 关联日志"的无缝跳转
  - **统一 Attribute 命名**：在所有遥测数据中使用一致的属性（如 `service.name`、`host.name`），支持跨信号查询

- ### OpenTelemetry：行业标准实现

  OpenTelemetry（OTel）已成为分布式追踪领域的行业标准，由 CNCF 维护：

  **核心优势**：
  - **厂商中立**：同一套 API/SDK，数据可导出到任意后端（Jaeger、Zipkin、Grafana Tempo、Last9 等）
  - **多语言支持**：覆盖 Java、Python、Go、Node.js、Ruby、.NET 等主流语言
  - **自动 Instrumentation**：对主流框架（Express、Spring、Django 等）自动注入追踪，无需修改业务代码
  - **标准数据模型**：统一的 Trace、Metric、Log 数据格式

  **典型代码模式（Node.js 伪代码）**：
  ```javascript
  const tracer = opentelemetry.trace.getTracer('my-service');
  const span = tracer.startSpan('operation-name');
  span.setAttribute('user.id', userId);
  try {
    // 业务逻辑
    span.setStatus({ code: SpanStatusCode.OK });
  } catch (err) {
    span.recordException(err);
    span.setStatus({ code: SpanStatusCode.ERROR });
  } finally {
    span.end();
  }
  ```

  **OpenTelemetry Collector** 作为中间件，接收、处理和转发遥测数据，解耦应用与后端存储。

- ### Microservices 调试的实际价值

  Traces 为微服务调试提供的核心能力：

  1. **定位性能瓶颈**：瀑布图（Waterfall View）直观展示哪个服务/操作占用了最多时间
  2. **跨服务边界调试**：不再需要在多个服务的日志中手动拼接请求路径
  3. **可视化依赖关系**：Service Map 展示服务间的调用拓扑和流量关系
  4. **精准性能优化**：找到 P99 慢请求的具体慢点，而非猜测
  5. **降低 MTTR**：故障发生时快速定位根因，缩短排查时间

- ### 有效追踪的最佳实践

  **推荐做法**：
  - 使用一致的命名规范，如 `{service_name}/{operation_type}`
  - 只为有意义的操作创建 Span，不要追踪每一个函数调用
  - 确保上下文在所有通信渠道中正确传播（包括异步消息）
  - 在 Span Attribute 中携带排查相关的业务上下文（user ID、request ID、feature flag）
  - 监控 Span 创建本身的性能开销

  **反模式（应避免）**：
  - **过度 Instrumentation**：每个函数都创建 Span，产生噪声并影响性能
  - **上下文断裂**：在异步边界未正确传播 Trace Context，导致 Trace 断链
  - **命名不一致**：不同团队/服务使用不同命名规范，无法跨服务查询
  - **Span 携带大载荷**：将大型数据结构作为 Attribute，增加存储成本
  - **遗漏第三方服务**：外部 API 调用未追踪，产生"黑盒"节点

- ### 业务价值维度

  Traces 不仅是技术工具，也能提供业务洞察：

  - **用户旅程追踪**：端到端追踪用户完整操作路径（如下单流程）
  - **SLO 数据来源**：从 Trace 数据中计算延迟 SLI，驱动 SLO 设置
  - **性能成本量化**：将慢操作转化为用户体验损失的具体数字
  - **业务上下文附加**：在 Span 中携带订单金额、用户等级等业务属性，关联技术性能与业务影响

- ### 主流工具生态

  | 工具 | 类型 | 特点 |
  |------|------|------|
  | **Jaeger** | 开源自托管 | 成熟稳定，UI 友好 |
  | **Zipkin** | 开源自托管 | 简单轻量，入门门槛低 |
  | **Grafana Tempo** | 开源/托管 | 与 Grafana 生态深度集成 |
  | **Last9** | 商业 SaaS | 一体化可观测性，事件计费 |
  | **OTel Collector** | 基础设施组件 | 数据收集和路由管道 |

- ### 性能开销

  现代追踪库在**正确配置**下的性能影响低于 **3%**。合理的采样率可进一步将实际开销降至可忽略水平，使追踪在生产环境全面部署成为可行方案。

- ## 与其他资料的关系
- 与 [[source/sre-introduction]] 互补：SRE 介绍定义了"为何需要监控（SLO/Error Budget）"，本文说明"如何实现分布式系统的追踪监控"
- 与 [[topic/cs146s-modern-software-developer]] 关联：Traces/Spans 是现代软件工程师在微服务架构下必须掌握的可观测性工具
- ## 引用此资料的页面
- [[topic/cs146s-modern-software-developer]]

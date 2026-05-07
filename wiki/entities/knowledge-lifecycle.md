---
type:: Entity
tags:: #knowledge #harness #agent-production
created:: [[2026-05-06]]
sources:: [[harness-knowledge-moat]]
related:: [[harness]], [[progressive-disclosure]], [[llm-wiki-pattern]], [[living-specs]]
---

# 知识生命周期（Knowledge Lifecycle）

团队知识库的系统化管理方法——通过分层存储、类型分类和成熟度跟踪，让知识从个人经验变成团队的复利资产。

## 核心理念

> 工作流只是管道，知识才是流过管道的活水。

知识管理并非 Harness Engineering 的附属品，而是其核心能力：
- 上下文工程支柱 = 知识检索注入 + 长/短期记忆
- 持续治理支柱 = 知识生命周期 + 自动衰减

## 三维架构（五层 × 五型 × 三级）

### 维度一：存储层（知识在哪里）

| 层级 | 路径 | 范围 | 说明 |
|------|-----|------|------|
| Layer 0-P | `~/.ai-team/` | 个人 | 个人偏好，纯本地不共享 |
| Layer 0-T | `team-conventions/` | 团队 | 团队约定、Commit 规范（"宪法"） |
| Layer 1 | `tech-wiki/` | 团队跨项目 | 通用技术经验，如设计模式、反模式 |
| Layer 2 | `biz-wiki/{domain}/` | 团队按领域 | 特定业务的领域模型、业务规则 |
| Layer 3 | `docs/knowledge/` | 项目 | 仅在当前项目有意义的上下文 |

**知识向上提升**：Layer 3 的项目知识，若被判定为跨项目通用，自动提升到 Layer 1（技术知识）或 Layer 2（业务知识）。

### 维度二：知识类型（是什么，MECE）

| 类型 | 描述 | 示例 |
|------|-----|------|
| **model** | 实体定义、数据结构、关系图 | 广告计划包含预算/出价/投放时段三个核心字段 |
| **decision** | 技术选型、架构决策及理由 | 选择事件驱动而非 RPC 同步，因为广告状态变更需要解耦 |
| **guideline** | 推荐做法（recommend）或禁止（avoid） | 公共模块变更后的兼容性检查清单 |
| **pitfall** | 已知风险、故障模式、排查步骤 | 广告预算扣减在高并发下会超扣，需用 Redis+Lua 保证原子性 |
| **process** | 业务流程、状态机、操作步骤 | 广告审核：提交→机审→人审→上线 |

### 维度三：成熟度（可信程度）

```
draft（新提取，单一来源，置信度 0.5-0.6）
  ↓ 在 1 个工作流中被成功引用
verified（单项目验证）
  ↓ 在 ≥2 个不同项目中被验证，且 ≥2 人确认
proven（成熟/可信赖）
```

## 自动衰减机制

知识也会过时。自动衰减让过时知识退出活跃库，而非误导 Agent：

| 触发条件 | 衰减动作 |
|---------|---------|
| proven 条目 12 个月未被引用 | 降级为 verified |
| verified 条目 6 个月未被引用 | 降级为 draft |
| draft 条目持续未引用 + Lint 标记 | 归档，移出活跃索引 |

> 设计借鉴 Karpathy [[llm-wiki-pattern]] 的 Lint 操作。

## 团队知识库实现

### 独立 Git 仓库

团队知识库是独立 Git 仓库，不寄生于任何业务项目：
- **跨项目共享**：项目 A 沉淀的知识，项目 B 自动受益
- **生命周期独立**：业务项目归档，知识不消失
- **权限独立**：贡献和消费权限独立于代码仓库管理

### 三种角色

| 角色 | 权限 |
|------|------|
| **maintainer** | 裁决内容冲突、审批 proven 提升、管理成员 |
| **contributor** | 通过工作流自动贡献（创建/验证/标记矛盾） |
| **reader** | 只消费知识（查询/注入），不贡献 |

### 区块链式贡献模式

- **append-only log**：每条变更记录贡献者、时间、会话哈希
- **贡献可溯源**：类似 Git blame，粒度为知识条目级
- **共识机制**：draft→verified 需 1 人验证；verified→proven 需 ≥2 人 + ≥2 项目

## 三级渐进式索引（借鉴 Karpathy）

| 层级 | 文件 | 大小 | 用途 |
|------|-----|------|------|
| Layer A | `knowledge-catalog.md` | ~50 行 | 全景目录，了解知识库有什么 |
| Layer B | `catalog.md`（各目录下） | ~100-300 行 | 分类清单，每条一行摘要 |
| Layer C | `TK-*.md` / `BK-*.md` | ~50-200 行 | 完整条目，含背景和适用场景 |

相比"一次性推送 50 条完整知识"（5000-10000 行），上下文效率提升一个数量级。

## 知识的工作流三时刻

1. **INIT（注入）**：工作流启动时 git pull 知识仓库，注入全景目录到 Agent
2. **执行中（消费）**：各阶段 Agent 按需查询，每个 Agent 有独立查询预算（精准而非贪婪）
3. **ARCHIVE（提取）**：@archiver 自动从产物提取知识条目，执行层级提升判定，git push 到团队知识仓库

## Lint 机制

知识库不能只进不出：

| 检查项 | 处理方式 |
|--------|---------|
| 索引不一致 | 自动修复 |
| 孤儿条目（无引用、无验证） | 降级为 draft |
| 矛盾检测（同主题相反结论） | 标记冲突，等待 maintainer 裁决 |
| 过时检测（6 月未引用的 draft） | 自动归档 |
| 重复/相似条目 | 标记合并候选 |

## 关联

- [[harness]] — 知识管理是 Harness Engineering 的核心组成
- [[progressive-disclosure]] — 三级索引与渐进式发现的同构关系
- [[llm-wiki-pattern]] — Karpathy LLM Wiki 的 ingest/query/lint 三操作是本框架的思想来源
- [[living-specs]] — decision/guideline 知识类型与活规格文档的关联

## 来源

- [[harness-knowledge-moat]] — stevenpxiao 的 AI Team 知识架构实践

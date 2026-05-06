---
type:: Entity
created:: [[2026-05-06]]
---

# Tool Search

**Tool Search** 是 [[Anthropic]] 在 [[MCP]] 生态中提出的一种客户端优化模式，旨在解决大规模工具集场景下的上下文效率问题。

## 核心思想

传统模式下，[[Agent]] 启动时需要将所有可用工具的完整定义一次性加载到上下文窗口中。当工具数量增长到成百上千时，这会消耗大量 [[Token]]，并降低模型的推理效率。

Tool Search 改变了这一范式——**按需加载**工具定义，而非全量注入：

1. Agent 维护一个**工具目录索引**（通常仅包含工具名称和简短描述）
2. 在运行时，Agent 根据当前任务**搜索**工具目录
3. 只将**相关工具**的完整定义拉取到上下文中
4. 执行完成后可释放不再需要的工具定义

## 性能表现

- **Token 消耗减少 85% 以上**：仅加载必要的工具定义，大幅压缩上下文长度
- **高选择准确率**：通过语义匹配检索，仍能准确找到所需工具
- 在大规模 [[MCP]] 工具集场景下效果尤为显著

## 与渐进式发现的关系

Tool Search 是 [[progressive-disclosure]]（渐进式发现）在工具调用领域的具体应用。其核心理念一致：**只在需要时才暴露必要信息**，避免一次性呈现所有细节。

## 适用场景

- [[MCP]] 生态中连接了多个工具服务器，工具总量较大
- 工具之间存在功能重叠或需要按场景动态选择
- 对上下文窗口利用率有较高要求的 [[Agent]] 系统
- 需要控制 [[Token]] 成本的大规模生产部署

## 相关概念

- [[MCP]] — Model Context Protocol，提供标准化的工具集成协议
- [[progressive-disclosure]] — 渐进式发现，按需暴露信息的通用设计模式
- [[Agent]] — 自主智能体，Tool Search 的主要受益方

## 来源

- [Building Agents That Reach Production Systems with MCP](https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp) — [[Anthropic]] 官方博客

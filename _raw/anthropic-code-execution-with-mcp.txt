# Code Execution with MCP: Building More Efficient AI Agents

- 原作者：Adam Jones, Conor Kelly (Anthropic)
- 来源：https://www.anthropic.com/engineering/code-execution-with-mcp
- 发布日期：Nov 04, 2025
- 主题：MCP、代码执行、Agent效率、Token优化

## 问题：工具膨胀导致 Agent 效率低下

随着 MCP 生态扩展，Agent 连接的工具从数十到数百甚至数千。两种常见的 token 浪费模式：

### 1. 工具定义占满上下文窗口
- 大多数 MCP 客户端将所有工具定义直接加载到 context 中
- 数千工具 = 数十万 token，Agent 还没开始工作就消耗大量 token

### 2. 中间结果反复经过模型
- 直接工具调用模式：每次工具调用结果必须经过模型
- 例：Google Drive → 获取会议纪要 → Salesforce 写入，全文经过模型两次
- 2小时会议可能 = 额外 50,000 token
- 大文档可能超出上下文限制，导致工作流中断

## 解决方案：代码执行 + MCP

将 MCP 工具呈现为代码 API（文件系统上的 TypeScript 文件），Agent 通过编写代码来调用工具：

```
servers/
├── google-drive/
│   ├── getDocument.ts
│   └── index.ts
├── salesforce/
│   ├── updateRecord.ts
│   └── index.ts
└── ... (other servers)
```

Agent 通过浏览文件系统发现工具，只加载需要的定义。
**Token 从 150,000 → 2,000，节省 98.7%**。Cloudflare 也有类似发现，称之为 "Code Mode"。

## 五大优势

### 1. 渐进式发现 (Progressive Disclosure)
- 模型擅长浏览文件系统
- 按需读取工具定义，而非一次性全部加载
- 可添加 `search_tools` 工具搜索相关定义
- 支持不同详细级别（仅名称 / 名称+描述 / 完整定义+Schema）

### 2. 上下文高效的结果处理
- 在执行环境中过滤和转换数据，只返回必要结果给模型
- 例：10,000 行表格 → 过滤后只看 5 行
- 支持聚合、跨数据源 join、特定字段提取

### 3. 更强大的控制流
- 循环、条件、错误处理用标准代码实现
- 避免通过 Agent 循环串联多个工具调用
- 降低 "time to first token" 延迟

### 4. 隐私保护 (Privacy-Preserving Operations)
- 中间结果默认留在执行环境中
- MCP 客户端可自动 tokenization 敏感数据（PII）
- 数据从 Google Sheets → Salesforce，但不经过模型
- 可定义确定性的数据流安全规则

### 5. 状态持久化和技能积累
- Agent 可写入中间结果到文件，支持断点续传
- Agent 可保存可复用的代码函数（Skills）
- 结合 SKILL.md 创建结构化技能，逐步积累高级能力
- 这与 "Skills" 概念紧密关联

## 代价与注意事项

- 需要安全的执行环境（沙箱、资源限制、监控）
- 增加了运营开销和安全考量
- 需要权衡：Token节省 vs 实现成本

## 关键引述

> "LLMs are adept at writing code and developers should take advantage of this strength to build agents that interact with MCP servers more efficiently."

> "Although many of the problems here feel novel—context management, tool composition, state persistence—they have known solutions from software engineering."

## 相关实体与概念
- [[MCP]] — Model Context Protocol
- [[Code Mode]] — Cloudflare 的类似发现
- [[Skills]] — 可复用的 Agent 能力单元
- [[Progressive Disclosure]] — 渐进式发现模式
- [[PII Tokenization]] — 隐私数据脱敏

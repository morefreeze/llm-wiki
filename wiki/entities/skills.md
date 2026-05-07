---
type:: Entity
tags:: #agent #reusability #automation
created:: [[2026-05-06]]
sources:: [[anthropic-code-execution-with-mcp]]
---

- # Skills
- ## 概述
  Skills 是可复用的 Agent 能力单元——包含指令、脚本和资源的文件夹。Agent 在代码执行环境中积累的可复用代码函数，结合 SKILL.md 文件形成结构化技能。
- ## 关键信息
- 文件夹结构：可复用代码 + SKILL.md（结构化描述）
- Agent 开发出工作代码后保存为 Skill
- 后续执行可直接 import 使用
- 逐步积累高级能力工具箱
- ## 代码示例
  ```typescript
  // ./skills/save-sheet-as-csv.ts
  import * as gdrive from './servers/google-drive';
  export async function saveSheetAsCsv(sheetId: string) {
  const data = await gdrive.getSheet({ sheetId });
  const csv = data.map(row => row.join(',')).join('\n');
  await fs.writeFile(`./workspace/sheet-${sheetId}.csv`, csv);
  }
  ```
- ## 与其他系统的关系
- Hermes Agent 的 Skills 系统（`~/.hermes/skills/`）采用相同理念——作为**程序记忆（Procedural Memory）**：如何做事（知识）vs 记住什么（语义/情景记忆）
- 每个 Skill 包含 SKILL.md + 可选的脚本/模板/资源文件
- Hermes 的技能索引 + 按需加载设计 = [[progressive-disclosure]] 的具体实现：提示词中只有技能索引（轻量），完整技能内容按需加载
- 这正是 LLM Wiki 模式中 Schema 层的实践
- 参见 [[agent-memory-system]] 了解 Skills 在 Hermes 四层记忆架构中的位置
- ## 关联
- [[mcp]] — Skills 基于代码执行 + MCP 环境
- [[llm-wiki-pattern]] — Wiki 本身可视为一种 Skill
- ## 来源
- [[anthropic-code-execution-with-mcp]] — Anthropic 工程博客
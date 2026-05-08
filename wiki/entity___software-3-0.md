---
type:: Entity
tags:: #llm #paradigm #software-engineering
created:: [[2026-05-07]]
sources:: [[source/karpathy-vibe-coding-to-agentic-engineering]]
related:: [[entity/agentic-coding]], [[entity/vibe-coding]], [[entity/harness]], [[source/llm-wiki-pattern]]
---

- # Software 3.0
  
  Karpathy 提出的软件范式分类框架中的第三阶段：LLM 成为可编程的计算机，context window 成为程序，prompt 成为源码。
- ## 软件三代范式
  
  | 范式 | 时代 | 核心范式 |
  |------|------|---------|
  | **Software 1.0** | 传统软件 | 人写显式代码，计算机按规则执行 |
  | **Software 2.0** | 神经网络（2017-） | 设计数据集和目标函数，通过训练得到模型权重 |
  | **Software 3.0** | LLM 时代 | 通过 prompt 和 context 操作 LLM 解释器 |
  
  > Karpathy 2017 年在《Software 2.0》一文中提出了软件分期框架；Software 3.0 是他在 2026 年访谈中的延伸。
- ## Software 3.0 的核心概念
- ### Context Window 是程序
  
  在 Software 3.0 里，你不再只是在代码编辑器里写函数，而是在以下要素之间组织"上下文程序"：
- **prompt**：给 LLM 的指令
- **context window**：模型一次调用中能看到的全部信息（指令、历史对话、文件、错误日志、代码片段、图片、工具返回结果）
- **工具权限**：模型可以调用的动作接口
- **外部环境**：测试环境、文件系统、API 等
  
  > **现在的问题变成：哪一段文字应该复制给你的 Agent？这就是新的编程范式。**
- ### 程序边界扩大
  
  **旧范式：** 程序 = 代码文件（处理结构化数据：表格、数组、数据库字段、明确规则）
  
  **新范式：** 程序 = 一段说明 + 上下文窗口 + 工具权限 + 测试环境 + 模型内部统计结构
  
  LLM 能处理更一般的信息重组，例如把文章、文档、事实重新编译成个人 wiki——这是传统程序天然不擅长的（需要理解文本关系、重排序信息、生成新知识结构）。
- ### OpenCL 安装的类比
  
  传统做法：写一个 shell script，适配各种机器、平台、环境，脚本不断膨胀。
  
  Software 3.0：安装说明本身可能就是一段可以复制给 Agent 的文本，Agent 读取你的机器环境，执行步骤，遇到错误再调试。
- ## MenuGen 的启示：App 被模型吞掉
  
  MenuGen（旧范式）：上传照片→OCR→抽取菜名→调用图像生成→重新排版→部署。
  
  Software 3.0 版本：直接把菜单照片交给 Gemini，Nano Banana 直接把菜品图叠加回菜单，中间所有步骤消失。
  
  > 我的整个 MenuGen 都是多余的。它还停留在旧范式里。那个 App 不应该存在。
  
  **商业判断：** 很多 AI 应用以为在做"更快的软件"，但模型原生能力可能直接吞掉中间层。更重要的是那些以前根本不可能存在的东西。
- ## 神经计算机（远期设想）
  
  Karpathy 的更大胆设想：未来可能出现"神经计算机"，神经网络成为 host process，CPU 和传统代码变成协处理器。设备接收原始视频/音频，神经网络理解场景，扩散模型实时生成独特 UI。
  
  他自己为这个设想加了限制：很怪，路径 TBD，不会一夜之间发生，更像是方向性的心智模型。
- ## Agent-first 基础设施
  
  当 Agent 不只聊天，而是拥有权限、本地上下文、能代表人采取行动时，今天的工具、文档、服务和设置流程都要重写。
  
  目标：把世界拆成 Agent 能读懂的输入，以及 Agent 能安全调用的动作接口。
  
  Karpathy 的测试标准：给 LLM 一句"Build MenuGen"，它不仅能写代码，还能完成部署、上线到互联网、配置好依赖服务，而不需要人去一个个菜单里操作。
- ## 关联
- [[entity/agentic-coding]] — Software 3.0 时代开发者的新角色（判断者/引导者/架构师）
- [[entity/vibe-coding]] — Software 3.0 的极端形式：让模型完全主导代码生成
- [[entity/harness]] — 在 Software 3.0 下如何安全地约束和引导 Agent
- [[source/llm-wiki-pattern]] — Karpathy 提到的 LLM Knowledge Bases 是 Software 3.0 应用的典型例子
- ## 来源
- [[source/karpathy-vibe-coding-to-agentic-engineering]] — Karpathy 在 Sequoia AI Ascent 2026 的访谈
# How Anthropic Teams Use Claude Code

**Source:** https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf
**Author:** Anthropic
**Date:** 2026

---

## Overview
Anthropic's internal teams are transforming their workflows with Claude Code, enabling developers and non-technical staff to tackle complex projects, automate tasks, and bridge skill gaps. Based on interviews with Anthropic's own Claude Code power users.

## 1. Data Infrastructure Team
**Team:** Organizes all business data across the company.

**Use cases:**
- Kubernetes debugging with screenshots (diagnosed pod IP exhaustion, got exact commands without networking specialists)
- Plain text workflows for finance team (non-coders describe workflows in plain text, Claude executes them)
- Codebase navigation for new hires (replaces data catalogs)
- End-of-session documentation updates (continuous improvement loop for Claude.md)
- Parallel task management across multiple instances

**Impact:** Resolved infra problems without specialized expertise; accelerated onboarding; cross-team self-service for finance

**Tips:** Write detailed Claude.md files; use MCP servers instead of CLI for sensitive data; share usage sessions across team

## 2. Product Development Team (Claude Code team)
**Team:** Uses their own product to build Claude Code updates.

**Use cases:**
- Fast prototyping with auto-accept mode (shift+tab): give abstract problems, let it work autonomously, review 80% solution
- Synchronous coding for core features with detailed prompts and real-time monitoring
- Building Vim mode: 70% of implementation came from Claude's autonomous work
- Test generation and bug fixes via GitHub Actions integration

**Impact:** Faster feature implementation; improved development velocity; enhanced code quality through automated testing

**Tips:** Create self-sufficient loops (builds + tests + lints automatically); develop task classification intuition (async vs synchronous); form clear detailed prompts

## 3. Security Engineering Team
**Team:** Secures the software development lifecycle, supply chain, and development environments.

**Use cases:**
- Complex infrastructure debugging: feed stack traces + docs, reduces 10-15 min manual scanning to ~5 min
- Terraform code review: "what's this going to do? Am I going to regret this?"
- Documentation synthesis and runbooks from multiple sources
- Test-driven development workflow: pseudocode → TDD → periodic check-ins
- Context switching and project onboarding (contribute within days instead of weeks)

**Impact:** Reduced incident resolution from 10-15 min to ~5 min; faster Terraform review; better cross-functional contribution; better documentation

**Tips:** Use custom slash commands extensively (50% of entire monorepo's custom commands); let Claude talk first (work autonomously with periodic check-ins); leverage for documentation synthesis

## 4. Inference Team
**Team:** Manages the memory system that stores information while Claude reads prompts.

**Use cases:**
- Codebase comprehension and onboarding (find files in seconds instead of asking colleagues)
- Unit test generation with edge case coverage
- ML concept explanation (reduces research time by 80%, from 1 hour to 10-20 min)
- Cross-language code translation (write Rust without learning it)
- Kubernetes command recall and management

**Impact:** 80% reduction in ML research time; faster codebase navigation; comprehensive test coverage; language barrier elimination

**Tips:** Test knowledge base first (see if Claude is faster than Google); start with code generation to build trust; use it for test writing

## 5. Data Science & ML Engineering Teams
**Team:** Need sophisticated visualization tools to understand model performance.

**Use cases:**
- Building JS/TypeScript dashboard apps (5,000-line TypeScript app despite minimal JS experience)
- Handling repetitive refactoring tasks ("slot machine": commit state, let Claude work 30 min, accept or restart)
- Creating persistent analytics tools instead of throwaway Jupyter notebooks
- Zero-dependency task delegation for unfamiliar codebases/languages

**Impact:** 2-4x time savings; built complex apps in unfamiliar languages; shifted from throwaway notebooks to persistent React dashboards

**Tips:** Treat like a slot machine (commit, let it run 30 min, accept or start fresh); interrupt for simplicity when needed

## 6. API Knowledge Team
**Team:** Works on features like PDF support, citations, and web search.

**Use cases:**
- First-step workflow planning (ask Claude which files to examine before starting any task)
- Independent debugging across codebases
- Model iteration testing through dogfooding (automatically uses latest research model snapshots)
- Eliminating context-switching overhead (ask directly in Claude Code instead of dragging files into Claude.ai)

**Impact:** Increased confidence in unfamiliar areas; significant context-gathering time savings; faster rotation onboarding; enhanced developer happiness

**Tips:** Treat as iterative partner, not one-shot solution; use for building confidence in unfamiliar areas; start with minimal information

## 7. Growth Marketing Team
**Team:** Non-technical team of one managing paid search, paid social, email marketing, SEO.

**Use cases:**
- Automated Google Ads creative generation: CSV → identify underperforming ads → generate hundreds of variations with specialized sub-agents (headline agent + description agent)
- Figma plugin for mass creative production (up to 100 ad variations per batch, reduces hours to half a second)
- Meta Ads MCP server for campaign analytics directly in Claude Desktop
- Advanced prompt engineering with memory system (logs hypotheses/experiments across iterations)

**Impact:** Ad copy creation reduced from 2 hours to 15 minutes; 10x increase in creative output; operating like a larger team

**Tips:** Identify API-enabled repetitive tasks; break complex workflows into specialized sub-agents; thoroughly brainstorm in Claude.ai before coding

## 8. Product Design Team
**Team:** Supports Claude Code, Claude.ai, and Anthropic API design, specializing in AI products.

**Use cases:**
- Front-end polish and state management changes (directly implement visual tweaks without engineer back-and-forth)
- GitHub Actions automated ticketing (file issues, Claude proposes code solutions automatically)
- Rapid interactive prototyping (paste mockup images → generate functional prototypes)
- Edge case discovery and system architecture understanding during design phase
- Complex copy changes and legal compliance (removed "research preview" messaging across entire codebase in two 30-min calls instead of a week)

**Impact:** 2-3x faster execution; weeks-to-hours cycle time; designers making "large state management changes you typically wouldn't see a designer making"

**Tips:** Get proper setup help from engineers; use custom memory files (tell Claude you're a designer needing incremental changes); leverage image pasting for prototyping

## 9. RL Engineering Team
**Team:** Focuses on efficient sampling in RL and weight transfers across the cluster.

**Use cases:**
- Feature development with supervised autonomy (write most code, steer when it goes off track)
- Test generation and code review
- Debugging and error investigation (mixed results—works ~1/3 of the time on first attempt)
- Codebase comprehension and call stack analysis
- Kubernetes operations guidance

**Impact:** Experimental "try and rollback" approach enabled; documentation acceleration; speed-up with limitations (~1/3 success rate on first attempt)

**Tips:** Customize Claude.md to prevent repeated tool-calling mistakes; checkpoint-heavy workflow (commit frequently, rollback experiments); try one-shot first, then collaborate

## 10. Legal Team
**Team:** Discovered Claude Code through experimentation and desire to understand Anthropic products.

**Use cases:**
- Custom accessibility solution: built communication assistant for family member with speaking difficulties in 1 hour (predictive text + voice banks)
- Legal department workflow automation: "phone tree" to connect with right lawyer
- Team coordination tools: G Suite apps for weekly updates and legal review status tracking
- Rapid prototyping for solution validation (show to domain experts like UCSF specialists)

**Work style:**
- Planning in Claude.ai first, building in Claude Code
- Visual-first approach (screenshots to show what interfaces should look like)
- Prototype-driven innovation (overcome fear of sharing "silly" prototypes)
- Security/compliance awareness: concerned about MCP integration security implications

**Tips:** Plan extensively in Claude.ai first; work incrementally and visually; share prototypes early

## Cross-Team Patterns

**Universal use cases (appear in almost every team):**
1. Codebase comprehension and onboarding
2. Test generation
3. Documentation (Claude.md files, runbooks)
4. Independent debugging

**Common tips across teams:**
- Write detailed Claude.md files
- Commit checkpoints frequently, roll back when needed
- Use auto-accept mode for peripheral tasks, supervise core features
- Plan in Claude.ai, build in Claude Code
- Start with minimal info, iterate

**Quantified impacts:**
- Security: 10-15 min infra debugging → ~5 min
- Marketing: 2 hours ad copy → 15 min; 10x creative output
- Data Science: 2-4x time savings on refactoring
- Inference: 80% reduction in ML research time
- Product Design: weeks → 2 thirty-minute calls; 2-3x faster execution
- Legal: 1 hour to build accessibility app from scratch

---
name: agentic-coding-foundations
description: Introduce engineers to agentic coding with Claude Code — how it differs from autocomplete and chat-based assistants, how a two-phase workflow (context gathering + planning, then implementation + coordination) plays out, what permission model to expect, and which onboarding prompts produce immediate value. Use when explaining Claude Code to a new team, deciding which workflows to delegate first, or grounding a pitch in the Rakuten case study.
---

## Instructions

This Skill operationalizes "Introduction to agentic coding" (Claude blog, 2025-10-30). The post defines agentic coding as a shift from autocomplete (next-line prediction) and chat (advice on pasted snippets) to autonomous task execution that reads files across a codebase, runs commands, and iterates.

Use the [evolution-of-ai-coding reference](./references/evolution-of-ai-coding.md) to set context with new users, and the [first-prompts examples](./examples/first-prompts.md) when running a hands-on session.

### When to reach for Claude Code

Choose Claude Code over a chat assistant when any of the following is true:

- The task spans multiple files (refactor, dependency upgrade, cross-module rename).
- The task requires running tests or commands and adjusting based on the result.
- You want the AI to maintain consistency with existing project conventions instead of generating snippets you splice in by hand.
- The task is high-toil but well-understood (test backfill, docs, routine refactor) and would otherwise consume a senior engineer's day.

Stay with chat (Claude.ai) when the question is conceptual ("explain this algorithm"), the codebase is not available, or you are still scoping the problem.

### The two-phase workflow

Phase 1 — context gathering and planning:

1. Claude Code reads configuration files (e.g. `package.json`, `requirements.txt`) to understand the project setup.
2. It examines test files for existing coverage patterns.
3. It traces imports to map dependencies between modules.
4. It produces an adaptive plan that evolves as more is learned. Example from the post: for "add authentication to the API," the plan includes analyzing existing route definitions, identifying endpoints that need protection, checking for existing middleware, and planning where session management lives.

Phase 2 — implementation and coordination:

1. Claude Code modifies multiple related files (route handlers, middleware, schemas, API client code, docs, tests) to keep the change consistent.
2. It runs the test suite and iterates on failures.
3. It surfaces a summary of changes for review.

You stay in the loop by approving the plan and reviewing diffs.

### Install and launch

```
npm install -g @anthropic-ai/claude-code
```

```
claude
```

Run `claude` from inside the project directory you want Claude Code to operate on.

### Permission model

Claude Code asks for approval before modifying files and shows the planned changes. You can approve, request revisions, or reject. This applies to file edits, shell commands, and external tool invocations.

### Onboarding prompts

Use these three prompts from the post to give a new user a sense of Claude Code's capabilities:

- `Explain the structure of this codebase and how the main components interact` — produces an architectural overview.
- `Review the authentication module for potential security issues` — surfaces concerns like exposed credentials or insufficient validation.
- `Find all N+1 query problems in our GraphQL resolvers and implement DataLoader batching` — exercises full multi-file analysis and implementation.

### Quick-win categories ("Start slow, then expand")

- Test automation for uncovered code paths.
- Documentation generation for legacy systems.
- Routine refactoring of technical debt.
- Feature implementation for well-understood requirements.

Begin with one category, build intuition, and expand from there.

### CLAUDE.md persistence

Use a `CLAUDE.md` file at the project root to record coding standards, architectural decisions, and project-specific requirements. Claude Code reads this on each session, keeping implementations consistent over time.

### MCP extensions

For tools and systems beyond your repository (issue trackers, design systems, internal docs), connect Model Context Protocol (MCP) servers. Claude Code uses the additional context to inform planning and implementation.

## Examples

See [examples/first-prompts.md](./examples/first-prompts.md) for the verbatim onboarding prompts and a summary of the Rakuten vLLM case study cited in the post — including the 7-hour autonomous implementation, 99.9% numerical accuracy, and the team's 5x parallel-task multiplier.

## Source

Distilled from [Introduction to agentic coding](https://claude.com/blog/introduction-to-agentic-coding) (published 2025-10-30).

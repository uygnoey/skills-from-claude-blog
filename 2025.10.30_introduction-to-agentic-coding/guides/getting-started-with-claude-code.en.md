**English** · [한국어](./getting-started-with-claude-code.ko.md) · [Español](./getting-started-with-claude-code.es.md) · [日本語](./getting-started-with-claude-code.ja.md)

# Getting started with Claude Code

A short adoption guide derived from [Introduction to agentic coding](https://claude.com/blog/introduction-to-agentic-coding) (2025-10-30). Use it as your day-one checklist when bringing Claude Code into a project.

## 1. Confirm the workflow fits

Before installing, sanity-check that the next task you want to delegate is a fit:

- It spans multiple files, or
- It needs commands run and results interpreted, or
- It is high-toil but well-understood (test backfill, docs, routine refactor).

If the task is conceptual or you are still scoping the problem, stay with Claude.ai for now.

## 2. Install Claude Code

```
npm install -g @anthropic-ai/claude-code
```

## 3. Launch in your project

Navigate to the project root, then:

```
claude
```

Claude Code reads configuration files, tests, and imports to build an internal map before it does anything else.

## 4. Try the three onboarding prompts

In order:

```
Explain the structure of this codebase and how the main components interact
```

```
Review the authentication module for potential security issues
```

```
Find all N+1 query problems in our GraphQL resolvers and implement DataLoader batching
```

The first builds intuition for how Claude Code reads the project. The second exercises analysis. The third exercises full multi-file implementation.

## 5. Approve, revise, or reject

Claude Code asks for approval before modifying files and shows the planned diff. Approve only what you understand. Reject or revise anything that looks off.

## 6. Persist project knowledge in CLAUDE.md

Add a `CLAUDE.md` at the project root capturing coding standards, architectural decisions, and project-specific requirements. Claude Code reads it on every session.

## 7. Expand to quick-win categories

After the first session, plan three deliberate uses in the categories the post highlights:

- Test automation for uncovered code paths.
- Documentation generation for legacy systems.
- Routine refactoring of technical debt.
- Feature implementation for well-understood requirements.

Use the experience to decide where Claude Code earns trust on your team.

## 8. Optional: connect MCP servers

If your workflow depends on tools beyond the repository (issue trackers, design systems, internal docs), connect MCP servers so Claude Code can pull that context into its planning.

## Source

[Introduction to agentic coding](https://claude.com/blog/introduction-to-agentic-coding) (published 2025-10-30).

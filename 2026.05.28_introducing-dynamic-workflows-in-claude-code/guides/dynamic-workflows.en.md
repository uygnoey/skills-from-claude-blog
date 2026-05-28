**English** · [한국어](./dynamic-workflows.ko.md) · [Español](./dynamic-workflows.es.md) · [日本語](./dynamic-workflows.ja.md)

# Dynamic workflows in Claude Code: how to use them effectively

## What are dynamic workflows?
Dynamic workflows are a Claude Code capability where Claude can generate orchestration scripts that coordinate tens to hundreds of parallel subagents in a single session, and verify work before it reaches you.

## When to use (and not use)
Use dynamic workflows when:
- the task spans a large surface area (many files, many modules, many unknowns)
- you want broad discovery/review across a large codebase
- you want a plan stress-tested before you commit

Avoid (or start smaller) when:
- the task is already well-scoped and can be completed in a single focused pass
- you are budget-sensitive on tokens (workflows can consume substantially more)

## Recommended setup
- Turn on **auto mode** for the best experience.
- Start with a **scoped** task to learn the cost/benefit for your workflow.

## Two ways to start
1. Ask Claude directly to create a workflow.
2. Enable **ultracode** from the effort menu (effort level xhigh) so Claude can decide when to use a workflow automatically.

## What to expect during execution
- The first time a workflow triggers, Claude Code will show what it’s about to run and ask you to confirm.
- Workflows are designed for long-running work (hours or days).
- Progress is saved as the run goes, so interrupted jobs can resume.

## Source
- https://claude.com/blog/introducing-dynamic-workflows-in-claude-code

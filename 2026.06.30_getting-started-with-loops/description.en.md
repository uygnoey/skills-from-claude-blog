**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
This post explains how the Claude Code team thinks about **agentic loops**: repeated cycles of work that continue until a stop condition is met.

It introduces a progression from **turn-based** work to **goal-based**, **time-based**, and **proactive** loops, and highlights when each approach is appropriate.

## When is it useful?
- When you’re deciding whether you need a one-off interactive session, a verifiable goal loop, a periodic loop, or a fully automated routine.
- When you want to improve reliability (self-verification) and manage cost/token usage in long-running automation.

## Key points
- Start with the simplest approach; not all tasks need complex looping.
- Define clear **stop conditions** and (for goal loops) explicit **turn caps**.
- Prefer **verifiable, deterministic success criteria** (tests, scores, thresholds) over subjective judgment.
- Improve quality by giving Claude ways to **verify** results (tools, skills, quantitative checks) and by using a second agent for review when needed.
- Manage tokens by choosing the right primitive/model, piloting before large runs, and using scripts for deterministic work.

## Bundled resources
- Example `SKILL.md` template for verifying frontend changes (see `skills/verify-frontend-change/SKILL.md`).
- Example commands shown in the post (see `skills/loops-playbook/examples/commands.md`).

## Source
- https://claude.com/blog/getting-started-with-loops

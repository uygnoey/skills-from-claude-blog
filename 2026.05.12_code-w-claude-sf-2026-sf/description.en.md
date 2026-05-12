**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Code w/ Claude SF 2026: Building on the AI exponential

## What is this post?

Anthropic's May 12, 2026 recap of Code w/ Claude SF, the annual developer conference. The post announces doubled rate limits on Claude Code, raised Claude Opus API limits, and four new capabilities for Claude Managed Agents on the Claude Platform — Dreaming, Multiagent orchestration, Outcomes, and Webhooks — and points to the YouTube recordings of keynotes and breakout sessions.

## When is it useful?

- When a team building on Claude Managed Agents needs to decide whether to adopt Dreaming, Multiagent orchestration, Outcomes, or Webhooks now that they are generally available.
- When planning agent architecture that splits work across a lead agent and parallel specialist subagents on a shared filesystem.
- When designing a quality bar for agent output and wiring a separate grader plus revision loop into a production pipeline.
- When wiring async agent runs into existing systems via webhooks instead of polling.

## Key points

- Claude Code rate limits doubled; Claude Opus API limits raised. Both live as of the announcement.
- Four new Claude Managed Agents capabilities available to all developers:
  - **Dreaming** — a scheduled process that reviews past agent sessions, surfaces patterns, and curates memory so agents improve between runs.
  - **Multiagent orchestration** — a lead agent delegates to specialist subagents working in parallel on a shared filesystem, each with its own model, prompt, and tools; the whole flow is traceable in the Claude Console.
  - **Outcomes** — developers define a rubric, a separate grader evaluates each result in its own context window, and the agent revises until the bar is met. Anthropic reports up to a 10-point lift on the hardest internal benchmark problems.
  - **Webhooks** — once an outcome is defined, the agent runs to completion and notifies via webhook when done.
- Customer talks referenced: Asana, Cursor, GitHub, Replit, Vercel.
- Code w/ Claude continues to London (May 19–18 [sic per source]) and Tokyo (June 5–6); Day 1 keynotes and breakout sessions are streamed live.

## Bundled resources

- `skills/managed-agents-new-capabilities/SKILL.md` — playbook for adopting the four new Managed Agents capabilities.
- `skills/managed-agents-new-capabilities/references/announcements-from-post.md` — verbatim catalog of the conference announcements and customer references in the post.
- `skills/managed-agents-new-capabilities/examples/outcomes-and-multiagent-patterns.md` — worked patterns combining Outcomes, Multiagent orchestration, and Webhooks against a sample task.

## Source

- [Code w/ Claude SF 2026: Building on the AI exponential](https://claude.com/blog/code-w-claude-sf-2026-sf) (Anthropic blog, May 12, 2026)

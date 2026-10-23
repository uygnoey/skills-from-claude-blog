**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
An announcement (September 17, 2026) of redesigned projects, in beta in Claude Code: you describe a goal,
and a coordinator manages the work across multiple threads instead of you splitting tasks, handling
handoffs, and merging results.

## When is it useful?
- When long-running, multi-part work spans several repos or many parallel sub-tasks.
- When you want to delegate outcomes (e.g. "reduce checkout p75 latency") rather than individual prompts.
- When deciding how to configure and steer a project and keep usage in check.

## Key points
- Start with a goal and a repo or context; configure environment, connectors, plugins, instructions, model.
- The coordinator is briefed like a chief of staff and routes tasks to new or existing threads.
- Each thread is a Claude Code cloud session on its own branch and repo copy; threads open PRs and run
  tests, and overlap is resolved as normal merge conflicts. Threads can use subagents, loops, and workflows.
- Shared memory across threads plus a library of files and artifacts; check-in frequency, thread creation,
  and update detail are adjustable.
- Steer from your phone; work continues when you step away.
- Parallel threads can hit usage limits faster; project usage and per-role model/effort are configurable.
- Beta for select Pro/Max cloud-session users first; local threads "coming very soon."

## Bundled resources
- Skill: `goal-driven-multi-thread-projects` (`templates/coordinator-brief.md`,
  `references/availability-and-limits.md`).

## Source
- https://claude.com/resources/articles/projects-redesigned

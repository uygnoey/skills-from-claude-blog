---
name: goal-driven-multi-thread-projects
description: Set up and steer a redesigned Claude Code project (beta, September 2026) where you state a goal and a coordinator routes work to parallel threads - each thread a Claude Code cloud session on its own branch - backed by shared memory and a library. Covers choosing the goal and repos/context, configuring environment, connectors, plugins, instructions, and model/effort for coordinator and workers, briefing the coordinator like a chief of staff, steering threads (including from a phone), handling merge order and conflicts, tuning check-in frequency and update detail, and watching project usage. Use when long-running, multi-part work (latency reduction, multi-repo migrations, endpoint retirement) would otherwise require you to split tasks, hand off context, and merge results by hand.
---

## Purpose
The source announcement describes projects that move "from folder to conversation": you describe a goal
and Claude manages the work across multiple sessions instead of you splitting tasks, managing handoffs,
and merging results. This skill turns that model into a setup-and-steering procedure.

## When to use
- Work spans several repos or many independent sub-tasks that can run in parallel.
- The effort runs for days or weeks and decisions must persist (shared memory).
- You want to delegate at the level of outcomes, not individual prompts.

## Instructions

1. **Write the goal as an outcome.** Pick one measurable goal and the repos or documents it needs.
   Claude then suggests work it can start immediately. Use
   [templates/coordinator-brief.md](templates/coordinator-brief.md).
2. **Configure the project.** Cloud environment, connectors, plugins, project instructions, and the model
   and effort level for both the coordinator and the worker threads.
3. **Brief the coordinator like a chief of staff.** State priorities, constraints, who to consult, and what
   "done" means. The coordinator routes tasks to new or existing threads.
4. **Let threads do the work.** Each thread is a Claude Code cloud session on its own branch and copy of the
   repo. With repos connected, threads open PRs and run tests; with documents, they read and draft.
   Threads may split work further with subagents, loops, and workflows.
5. **Steer at the right level.** Follow progress in the main project chat; open a single thread only to
   steer details. You can steer from your phone, and work continues after you step away.
6. **Treat overlap as normal PR work.** Overlapping changes surface as merge conflicts, as with any PR.
   Ask the coordinator which PRs must merge first.
7. **Use shared memory instead of heavy prompt engineering.** Every thread adds to and draws from it (e.g.
   a release moved to Friday, why an export was dropped, who to consult before changing billing). Put
   reusable files in the library; artifacts Claude produces land there too.
8. **Tune the working style.** Adjust how often Claude checks in, how often it starts new threads, and how
   detailed its updates are.
9. **Watch usage.** Several full sessions run at once, so limits can be reached faster. Check
   project-specific usage and lower model/effort for worker threads when appropriate.

Availability and limits as of the announcement are in
[references/availability-and-limits.md](references/availability-and-limits.md).

## Examples

**Latency goal**
> Goal: reduce checkout p75 latency. Repo: checkout service.
> Claude profiles each endpoint, tests optimizations, and opens PRs in parallel threads.

**Endpoint retirement across repos**
> Connect the API, web, and mobile repos. Goal: retire the deprecated v1 endpoint.
> The coordinator creates one thread per repo to migrate callers, run tests, and open PRs, then reports
> which PRs must merge first.

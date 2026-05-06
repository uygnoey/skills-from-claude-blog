**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
This post announces new Claude Managed Agents capabilities: dreaming (research preview), outcomes, multiagent orchestration, and webhooks.

## When is it useful?
It is useful when you want agents that improve over time (memory + dreaming), enforce a quality bar with automated grading (outcomes), and run parallel specialist workstreams (multiagent orchestration).

## Key points
- Dreaming is a scheduled process that reviews past agent sessions and memories to extract patterns and refine what the agent remembers.
- Outcomes let you define a rubric for success; a separate grader evaluates outputs against it and the agent iterates to meet the rubric.
- Multiagent orchestration uses a lead agent that delegates work to specialist agents (with their own model, prompt, and tools) working in parallel on a shared filesystem.
- Webhooks can notify you when an outcome evaluation is complete.

## Bundled resources
- Skill: `managed-agent-orchestration` (rubrics for outcomes, a dreaming/memory review checklist, and a role glossary).

## Source
- https://claude.com/blog/new-in-claude-managed-agents

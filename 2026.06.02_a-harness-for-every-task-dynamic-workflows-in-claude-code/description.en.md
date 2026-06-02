**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
This post introduces “dynamic workflows” in Claude Code: a feature that lets Claude Code write and orchestrate a multi-agent harness on the fly to solve complex tasks more natively.

## When is it useful?
Dynamic workflows are best suited for complex, high-value tasks where orchestration helps (e.g., triage, verification, multi-step engineering work), and where you benefit from splitting work across multiple focused subagents.

## Key points
- Dynamic workflows run a JavaScript workflow file and can spawn and coordinate subagents.
- Common workflow patterns include classify-and-act, fan-out-and-synthesize, adversarial verification, generate-and-filter, tournament selection, and looping until a stop condition is met.
- Workflows can choose which model each agent uses and whether subagents run in their own worktree.
- Workflows can be resumed if interrupted.
- Workflows can be saved locally (e.g., under `~/.claude/workflows`) and distributed via a skill.

## Bundled resources
- Skill: `skills/dynamic-workflows-harness/` (pattern library + reusable prompt templates)
- Guide: `guides/dynamic-workflows.en.md` (long-form explanation + use cases)

## Source
- https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code

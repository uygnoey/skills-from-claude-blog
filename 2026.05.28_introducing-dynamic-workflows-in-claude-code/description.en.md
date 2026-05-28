**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
This post introduces **dynamic workflows** in Claude Code: an execution mode where Claude can write orchestration scripts that coordinate tens to hundreds of parallel subagents in a single session, and check its own work before it reaches you.

## When is it useful?
Use dynamic workflows when the task is too large for a single pass (especially in complex or legacy codebases), such as:
- a bug hunt across an entire service
- a migration touching hundreds of files
- a plan you want stress-tested before committing

## Key points
- Workflows are designed for **parallel, long-running work** that may run for hours or days.
- Progress is saved during runs so interrupted jobs can resume.
- The first time a workflow triggers, Claude Code shows what it’s about to run and asks for confirmation.
- You can start a workflow by asking Claude directly, or by enabling **ultracode** (effort level set to xhigh) so Claude can decide when to use a workflow.
- Workflows may consume substantially more tokens than typical sessions.

## Bundled resources
- Skill: guidance for deciding when to use dynamic workflows and how to structure workflow requests.

## Source
- https://claude.com/blog/introducing-dynamic-workflows-in-claude-code

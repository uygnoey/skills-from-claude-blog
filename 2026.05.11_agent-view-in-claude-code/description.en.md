**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Agent view in Claude Code

## What is this post?
Agent view is a full-screen terminal UI for managing multiple Claude Code background sessions from one place.

## When is it useful?
Use it when you want to run several independent tasks in parallel (for example, bug fixing, PR review, or log investigation) and only step in when a session needs input.

## Key points
- Open agent view with `claude agents`.
- Dispatch new background sessions, monitor their state, peek and reply, or attach/detach.
- Agent view is a research preview and requires Claude Code v2.1.139+.
- Sessions run under a supervisor process and persist on disk between terminal restarts.

## Bundled resources
- Skill: `manage-agent-view-sessions` (commands, filter syntax, and repeatable session-management checklists)
- Guide: `agent-view-quickstart` (how to adopt agent view in day-to-day work)

## Source
- https://claude.com/blog/agent-view-in-claude-code
- https://code.claude.com/docs/en/agent-view

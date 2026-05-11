**English** · [한국어](./agent-view-quickstart.ko.md) · [Español](./agent-view-quickstart.es.md) · [日本語](./agent-view-quickstart.ja.md)

# Agent view quickstart (Claude Code)

## Overview
Agent view helps you run and manage many Claude Code background sessions from one screen.

## Prerequisites
- Claude Code v2.1.139+
- Feature may change (research preview)

## Start using agent view
1. Run `claude agents`.
2. Type a prompt and press `Enter` to dispatch a background session.
3. Repeat to dispatch multiple sessions.

## Day-to-day workflow
- Monitor which sessions are working vs. blocked.
- Use `Space` to peek and reply without leaving the table.
- Attach (`Enter`) only when you need to collaborate deeply.
- Detach with `←` on an empty prompt to return to the table.

## Safe parallel file edits
If multiple sessions will edit files, expect worktree isolation. Worktrees live under `.claude/worktrees/` and are removed when you delete the session.

## Source
- https://code.claude.com/docs/en/agent-view

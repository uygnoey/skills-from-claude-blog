---
name: manage-agent-view-sessions
description: Run and manage multiple Claude Code background sessions efficiently using agent view (dispatch, peek/reply, attach/detach, filtering, and lifecycle commands).
---

## Instructions

Use this skill when you are working in Claude Code and need to manage multiple background sessions via **agent view**.

### 1) Open agent view and confirm requirements

- Open agent view:
  - `claude agents`
- Confirm your Claude Code version supports agent view (requires v2.1.139+):
  - `claude --version`

### 2) Dispatch sessions (from agent view or shell)

- In agent view, type a prompt and press `Enter` to dispatch.
- Dispatch and attach immediately:
  - `Shift+Enter`
- From the shell, start a background session directly:
  - `claude --bg "<prompt>"`
- To run a specific custom subagent as the *main agent* of the session:
  - `claude --agent <agent-name> --bg "<prompt>"`

### 3) Monitor, peek, reply, attach, detach

- Peek without leaving agent view:
  - select a row → `Space`
- Send a reply from the peek panel:
  - type your reply → `Enter`
- If the session is asking a multiple-choice question:
  - press the number key
- Fill the input with a suggested reply (then edit):
  - `Tab`
- Attach to take over the session interactively:
  - `Enter` or `→`
- Detach back to agent view:
  - `←` on an empty prompt
- If a dialog is stuck and `←` doesn’t respond:
  - `Ctrl+Z` to detach immediately

### 4) Filter instead of dispatching

Type these into the dispatch input to filter the list:

- `a:<name>` — sessions running the named agent
- `s:<state>` — sessions in a given state (for example `s:blocked`)
- `#<number>` or a PR URL — the session working on that pull request

### 5) Organize the list

- Toggle grouping (state ↔ directory): `Ctrl+S`
- Pin/unpin: `Ctrl+T`
- Rename: `Ctrl+R`
- Reorder: `Shift+↑` / `Shift+↓`
- Collapse a group: select header → `Enter`

### 6) Stop / remove / respawn sessions

- Stop a session: `Ctrl+X` (or `claude stop <id>`)
- Delete a session row: press `Ctrl+X` again within two seconds (or `claude rm <id>`)
- Restart a stopped session:
  - `claude respawn <id>`
  - `claude respawn --all`

### 7) Safe parallelism for file edits (worktree isolation)

When multiple sessions might edit files, avoid conflicts:

- Sessions dispatched from agent view share the current working directory by default.
- Claude Code may block writes until it moves into an isolated worktree.
- Worktrees are created under `.claude/worktrees/` and removed when you delete the session.
- To force a custom subagent to always use a worktree, set in the agent frontmatter:
  - `isolation: worktree`

## Examples

See:
- [templates/dispatch-prompts.md](./templates/dispatch-prompts.md)
- [examples/agent-view-quickstart.md](./examples/agent-view-quickstart.md)

## Source

- Claude Code Docs: https://code.claude.com/docs/en/agent-view
- Blog URL (may be unavailable to automated fetch): https://claude.com/blog/agent-view-in-claude-code

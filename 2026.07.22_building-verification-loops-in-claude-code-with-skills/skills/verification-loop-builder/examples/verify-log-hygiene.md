# Example: `verify-log-hygiene`

The simplest possible verification skill from the post — a project-specific logging rule no
generic linter enforces, written as a few lines of frontmatter plus a body.

```markdown
# .claude/skills/verify-log-hygiene/SKILL.md
---
name: verify-log-hygiene
description: Check that error logs include the request ID and never
  include the request body. Use when the diff touches error handling
  or logging.
allowed-tools: [Read, Edit, Grep]
---
Read the error-handling paths in the current diff.

For each log call on an error path, confirm it includes the request ID
and does not pass the request body, headers, or any user-supplied payload.

Report each violation with file:line, then fix it: add the request ID
where it's missing and strip the payload from the log call.
```

## What makes it work

- **The `description` carries the trigger.** "Use when the diff touches error handling or logging"
  is what pulls the skill in without you invoking it.
- **`allowed-tools` is the minimum.** `Read` and `Grep` to find the log calls, `Edit` to fix them.
  No `Bash` needed — the check is a read of the diff, not a command run.
- **The body is three moves**: what to read, what to confirm, how to report and fix. Report with
  `file:line` so the finding is actionable, then fix rather than only flag.

## How this one was found

It came from repetition: the same small correction after every feature — the request ID missing
from a log line, the request body dumped into it. That is the trigger for turning a manual check
into a loop.

## Source

[Building verification loops in Claude Code with skills](https://claude.com/blog/building-verification-loops-in-claude-code-with-skills)

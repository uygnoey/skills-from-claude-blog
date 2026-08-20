# How auto mode's permission model works

Source: https://claude.com/blog/auto-mode-default-in-claude-code

## The basic loop

1. A permission rule from a settings file fires first, if one matches — with one exception
   below.
2. Otherwise the tool call goes to the auto mode classifier, which targets actions that are
   **irreversible**, **destructive**, or **aimed outside your environment**.
3. On a block, Claude usually finds a safer way to proceed on its own, or asks the user
   directly for the go-ahead.
4. If Claude cannot make progress — **three blocks in a row, or twenty across a session** —
   Claude Code falls back to manual approvals.

## The allow-rule exception

Permission rules still fire before the classifier, **except allow-rules broad enough to
grant arbitrary code execution** — for example `Bash(python:*)` or `Bash(node:*)`. Those are
set aside while in auto mode, because they would let commands skip the classifier entirely.

Two consequences worth stating explicitly:

- Settings files are **not modified**. The rules apply again the moment the session switches
  to another mode.
- Deny rules are unaffected. Teams that deny recursive deletes or similar commands outright
  keep those guardrails, and the classifier makes its judgment calls inside them.

## Context the classifier is given

Hardening from the Apollo Research engagement worked primarily by giving the classifier more
context about the environment it is protecting:

- **Repository visibility** — whether a destination is public, private, or trusted.
- **Git state** — the repository's current `git status`.
- **Data-handling rules** — explicit rules distinguishing secrets from potentially sensitive
  or confidential information, and where each may be accessed and shared.

## Named hardening features

| Feature | What it does |
| --- | --- |
| **Hard denies** | Data exfiltration — sending code or secrets somewhere external — sits in a category the classifier is designed never to approve. To run such an action you must switch out of auto mode or run the command yourself. Hard deny rules are customizable via settings, so an organization can add rules that are never allowed even when a user asks. |
| **Data access and sharing rules** | The classifier carries explicit rules for secrets versus sensitive/confidential information, and checks whether the destination of a git push or pull request is public, private, or trusted before the action runs. The same push can be routine or exfiltration depending on where it lands. |
| **Git status before destructive git actions** | Before a command that could discard uncommitted work — `git reset --hard`, for example — the classifier sees the repository's current git status. |
| **Prompt injection screening** | When Claude pulls content from external sources such as web pages, file contents, or tool outputs, an API-side probe checks that content for attempts to hijack Claude's behavior. When something looks like an injection attempt, a warning is added to Claude's context before the result is shared with the user. |

Auto mode also checks that actions are aligned with user intent, which is the second half of
its prompt-injection defense alongside the tool-result probes.

## Modes and controls

| Control | Where | Effect |
| --- | --- | --- |
| `Shift+Tab` | CLI | Cycle permission modes for the current session. |
| Mode dropdown | Desktop app | Same, from the UI. |
| `defaultMode` | Managed settings | Pin an org-wide default permission mode. |
| `disableAutoMode` | Managed settings | Turn auto mode off entirely. |

Full configuration syntax lives in the auto mode documentation; the post names only these
settings.

## Where auto mode is the default

| Surface | Status as of the post |
| --- | --- |
| Claude Code — Pro, Max, Team | Default for new sessions from August 14, 2026. Classifier overhead no longer billed. |
| Claude Enterprise | Opt-in; admins can set it as the default via managed settings. Default planned "in the coming month". |
| Claude API | Opt-in, same plan. |
| Claude Platform on AWS, Amazon Bedrock, Google Cloud Agent Platform, Microsoft Foundry | Opt-in, same plan, in coordination with the cloud partners. |
| Internal Claude Code usage at Anthropic | Already the default. |

## The stated limit

Auto mode reduces risk for most users but relies on classification systems, so it does not
eliminate risk. The post recommends reviewing Claude's actions yourself for high-stakes
changes to production infrastructure.

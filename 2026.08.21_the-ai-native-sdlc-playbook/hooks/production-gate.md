# Hook — production deploy gate

A `PreToolUse` hook on `Bash` that blocks a production deploy unless a named release authorization is
present in the environment.

The build phase uses hooks as guardrails that allow or block with no human involved. A hook can also
**ask**, pausing the action until a specific person approves — which is what release gating needs.
The release gate is the clearest case, but hooks are not deploy-specific: they run wherever Claude
acts.

## Files

- `production-gate.json` — the hook registration, to merge into `.claude/settings.json`.
- `production-gate.sh` — the gate itself. Ships executable; deploy it at
  `.claude/hooks/production-gate.sh`.

## Install

1. Copy the script to `.claude/hooks/production-gate.sh` in the repo and keep it executable
   (`chmod +x`).
2. Merge the `hooks` block from `production-gate.json` into `.claude/settings.json`, or into managed
   settings when the gate must not be switchable off by an engineer.
3. Make sure `jq` is available on the machines and runners where Claude Code runs — the script parses
   the tool input with it.
4. Define what sets `RELEASE_APPROVAL`. This is the organization's definition of approval: an
   approved change ticket, or the release manager's sign-off. The gate is only as strong as what
   populates that variable.

## How it behaves

- Reads the hook payload from stdin and extracts `.tool_input.command`.
- Passes through (`exit 0`) anything that is not a production deploy.
- On a command containing both `deploy` and `production` with no `RELEASE_APPROVAL` set, writes the
  reason to stderr and exits `2`, which blocks the action and sends the message to Claude.

`exit 2` is the blocking exit code; the stderr message is what Claude sees, which is why the message
names the reason and the route to approval rather than just refusing.

## Notes and cautions

- **A block should explain itself.** When a hook stops an action, the reason and the route to
  approval must appear in Claude's output, or the session has no way to proceed correctly.
- **Placement matters.** A hook that asks a human for approval does not belong in the build phase —
  an approval prompt during the build puts a person back on the critical path of every session
  running in parallel.
- **Team versus managed.** Team hooks go in `.claude/settings.json` in git. Non-negotiable hooks go in
  managed settings owned by the platform or IT admin, where individual engineers cannot switch them
  off. Setting `allowManagedHooksOnly` makes the managed gates the only hooks that run.
- **The matcher is broad on purpose.** Matching all `Bash` calls means the gate cannot be dodged by
  invoking the deploy through a different wrapper, at the cost of running the script on every shell
  command — so keep it fast.
- **String matching is a starting point.** `deploy` and `production` as substrings is the shape of the
  check, not a finished policy. Tighten the condition to the organization's actual deploy commands
  and environment names before relying on it.

## Governance

Hooks are the approval gates. The gate condition is enforced every time, for everyone. Allow and
block decisions are logged with a timestamp, and every hook decision is written to the OpenTelemetry
export with an allow or block verdict — which is also how you measure time spent waiting on each
gate. The lagging measure is gate violations reaching production before and after the hooks, from the
incident tracker.

The governing principle behind the gate: the agent may act up to the production gate and cannot pass
it.

## Source

[The AI-Native SDLC playbook](https://claude.com/blog/the-ai-native-sdlc-playbook) — Stage 5, the
"hooks as approval gates" play. Published 2026-08-21.

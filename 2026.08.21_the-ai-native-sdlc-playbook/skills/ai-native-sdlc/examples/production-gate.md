# Hooks as approval gates — the production deploy gate

The build phase uses hooks as guardrails that allow or block with no human involved. A hook can
also **ask**, pausing the action until a specific person approves — which is what release gating
needs. Hooks are not deploy-specific; they run wherever Claude acts.

## The registration

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PROJECT_DIR}/.claude/hooks/production-gate.sh"
          }
        ]
      }
    ]
  }
}
```

## The gate

```bash
#!/bin/bash
# Production deploys require a named release authorization
cmd=$(jq -r '.tool_input.command' < /dev/stdin)
if [[ "$cmd" == *"deploy"* && "$cmd" == *"production"* ]]; then
  if [ -z "$RELEASE_APPROVAL" ]; then
    echo "Production deploys need a release authorization." >&2
    exit 2   # exit 2 blocks the action; the message goes to Claude
  fi
fi
exit 0
```

## Standing the gates up

1. Engineering leadership, with change management and compliance, lists the human approval gates
   that must survive — change management sign-off, release authorization, edits to protected
   paths.
2. The platform engineer expresses each gate as a hook: a script that runs before Claude acts and
   can allow, ask, or block.
3. Team hooks go in `.claude/settings.json` in git. Non-negotiable hooks go in managed settings
   owned by the platform or IT admin, where individual engineers cannot switch them off.
4. A block should explain itself. When a hook stops an action, the reason and the route to
   approval appear in Claude's output.

**Governance.** The gate condition is enforced every time, for everyone. Allow and block decisions
are logged with a timestamp. The gate also defines what counts as approval — an approved change
ticket, or the release manager's sign-off.

**Measuring the gates themselves.** Leading: time spent waiting on each gate, since every hook
decision is written to the OpenTelemetry export with a timestamp and an allow or block verdict.
Lagging: gate violations reaching production before and after hooks, from the incident tracker.

**Placement.** A hook that asks a human for approval does not belong in the build phase — an
approval prompt during the build puts a person back on the critical path of every session running
in parallel.

---
name: managed-agents-scheduled-deployments
description: Use Claude Managed Agents scheduled deployments and vault environment variables to run routine work on a cron schedule and securely authenticate CLI tools without exposing secrets to the model.
---

## Instructions

Use this skill to:

1) Decide whether a task should be a scheduled deployment.
- Good fits: recurring syncs, routine compliance checks, periodic validation, daily/weekly digests.
- Not a fit: highly interactive work that requires continuous human decisions.

2) Structure the agent task for scheduled runs.
- Make the task fully self-contained, since each scheduled run starts a new session.
- Include clear success criteria (what to produce and where to store it).
- Prefer idempotent behavior: re-running should not create duplicates.

3) Use vault environment variables for secure CLI authentication.
- Store secrets (e.g., API keys) as environment variables in a vault.
- Restrict where they can be used by allow-listing domains.
- Assume the agent cannot read the real secret; design CLI usage accordingly.

4) Operational controls to plan for.
- Pausing/resuming and archiving scheduled deployments.
- Triggering extra runs on demand.

## Examples

### Example: nightly spreadsheet report
Goal: On a nightly schedule, analyze a spreadsheet and produce a report (or deck) for stakeholders.

### Example: periodic catalog validation
Goal: On a schedule, validate a public catalog (e.g., a list of browser skills) to keep it accurate.

### Example: scheduled answer refresh for sales
Goal: Refresh answers periodically so sales teams get up-to-date guidance without maintaining separate scheduling infrastructure.

## Source

- https://claude.com/blog/whats-new-in-claude-managed-agents

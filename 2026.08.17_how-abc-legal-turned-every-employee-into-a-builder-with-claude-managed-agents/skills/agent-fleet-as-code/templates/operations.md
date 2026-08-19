# Operations — <agent-name>

Owner: <name>  ·  Workspace: <workspace>  ·  Mode: recommend | automate

## What this agent does

<One paragraph. The single job, and the business process it sits inside.>

## Trigger

<Event or schedule. If scheduled, state the cadence and where the schedule is configured.>

## Dependencies

| Dependency | Purpose | Failure behaviour |
|---|---|---|
| <MCP server / internal platform> | <what it is used for> | <what the agent does when it is unavailable> |

## Credentials

Which vault entries this agent reads, and who can rotate them. Never the values.

## Deployment

Merging to the main branch deploys this agent. See `deploy.sh` in this folder for what the pipeline runs.

Rollback: every push creates a new version with optimistic locking — roll back to the previous version rather than reverting by hand.

## Human-in-the-loop

- **Current mode:** recommend | automate
- **Where recommendations appear:** <job banner / chat channel>
- **Who reviews:** <role>
- **Promotion criteria:** the evidence required before this agent moves from recommend to automate — typically evals showing it matches or beats humans on this task.

## Feedback loop

- Harvested? yes / no
- If yes: which harvester, on what cadence, and where the labeled data lands.
- If no: state why — most single-task runners have no grading signal and need none.

## Value reporting

What this agent reports back to the warehouse on each run, in hours and dollars, and where to read its efficiency ratio.

## Known issues and gotchas

| Date | Issue | Resolution |
|---|---|---|

## Runbook

**If it did not run:** <first thing to check>
**If it produced a wrong recommendation:** <how to flag it so the harvester picks it up, and who to tell>
**If it is costing more than it saves:** <what to try — evals, a cheaper model, trimming tokens — before retiring it>

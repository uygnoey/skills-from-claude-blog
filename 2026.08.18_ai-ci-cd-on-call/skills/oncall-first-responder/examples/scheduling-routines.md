# Setup and routines

The concrete setup steps and routine requests described in the source post, plus the operational notes worth keeping alongside them.

## Setup

The source account describes the setup as taking hours rather than days.

1. **A Team or Enterprise plan** is required.
2. **The organization owner adds the agent to the on-call channel** — in the source account, via Claude Tag.
3. **The organization owner connects it** to the appropriate connectors and the GitHub repository holding the standing instructions, and sets up remote access for the coding agent.
4. **Add the agent to the incident channel** and instruct it to monitor for incidents and triage immediately.

The team also published a generalized on-call setup kit that turns a team's own incident history into triage playbooks and leaves a read-only agent in the incident channel that diagnoses, escalates, and learns. It can be run against a fictional team's history in about ten minutes. See the source post for the link.

## Scheduling routines in natural language

Routines are scheduled by asking for them in the on-call channel, in plain language. The example given in the post is a weekly handoff:

> run CI handoff every Monday at 9:00am EST

Routines worth having, following the same pattern:

| Routine | Why |
|---|---|
| Weekly handoff summary | So the next person in the rotation starts with context |
| Daily summary | So a multi-day incident does not lose its thread overnight |
| Periodic public status report | So the rest of the company stops asking the on-call whether it is safe to merge |

Each routine's output format belongs in the standing instructions, not in the scheduling request — the request says *when*, the instruction file says *what*.

## Access to grant

A service account with the tools an on-call engineer actually needs. In the source account those included observability platforms such as Datadog and Grafana; the full investigation set spans:

- Metrics and dashboards
- Log store
- Paging system
- Source control
- Cluster access
- Incident channels

All reached through MCP connectors, granted once by an administrator.

Grant read access first. Every write capability is a separate decision with its own blast radius, and the post's own division keeps write actions — merges, deploys, flag changes, infrastructure edits — under a named human's permissions.

## Channels to watch

Beyond the on-call channel itself, add the agent to channels carrying context it will need mid-incident:

- Service alerts
- Configuration changes
- Deploys
- PR updates

The value shows up at triage time: correlating a symptom with a change made hours earlier only works if the agent saw the change.

## Source

- https://claude.com/blog/ai-ci-cd-on-call

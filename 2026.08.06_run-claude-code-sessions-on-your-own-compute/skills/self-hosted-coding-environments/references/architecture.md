# Architecture: runners, modes, isolation, and routing

Derived from the August 6, 2026 announcement of self-hosted environments for
Claude Code.

## Runners

A self-hosted environment is a set of **runners** you deploy. A runner is a
long-lived process that:

1. picks up sessions, and
2. starts a Claude Code process for each session it picks up.

Runners are the thing you build an image for, deploy, update, and keep running.
They are the unit of operational work.

## The two modes

### Fixed

A set number of runners stay running, and sessions are distributed across them.

- Simplest model: capacity is a decision you make once and revisit occasionally.
- Idle runners cost capacity whether or not sessions are in flight.
- No orchestrator to operate.

### On-demand

An orchestrator watches for queued sessions, starts a runner as sessions arrive,
and stops runners when work finishes, so capacity tracks demand.

- Capacity follows the workload instead of the calendar.
- Adds a component — the orchestrator — that your team now runs and maintains.

Choose on-demand when demand is spiky enough that idle capacity dominates.
Otherwise fixed is less to operate.

## Isolation

A runner can serve more than one session. **Each session runs in its own
checkout**, and that per-session checkout is what keeps work isolated between
developers and between accounts.

Design consequence: isolation is a property of the session, not of the runner.
Do not build a per-developer-runner topology on the assumption that the runner
is the security boundary.

## Routing across surfaces

Sessions from every supported surface — web, mobile, desktop, and routines —
route to the same environment. You set the environment up once and it applies
wherever a team member starts a session.

## Relationship to Remote Control

These are distinct features and are easy to conflate:

| | Self-hosted environments | Remote Control |
|---|---|---|
| Execution host | Shared infrastructure operated by a platform team | The developer's own machine |
| Tied to | The organization | The user who ran `claude` |
| Session lifetime | Independent of any single machine | Ends when that machine stops running the session |
| Who can use it | Any user | That one user |

Remote Control lets a developer continue a session running on their own machine
from a phone or browser. It is not a way to run sessions on controlled shared
infrastructure.

## What the announcement does not specify

Runner image contents, host requirements, orchestrator implementation, scaling
parameters, and networking topology are left to the documentation:
https://code.claude.com/docs/en/self-hosted-environments

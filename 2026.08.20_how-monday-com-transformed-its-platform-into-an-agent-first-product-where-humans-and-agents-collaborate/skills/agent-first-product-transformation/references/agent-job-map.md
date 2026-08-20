# The agent job map

monday's agents are defined per function with named jobs, rather than as one
general-purpose assistant. Below are the roles the source names, grouped by the
function that runs them, with the job each one is described as doing.

Use this as a starting inventory when you are deciding what to define for your
own organization — not as a set to copy wholesale. The value is in the *shape*:
each entry is a job, with a trigger and a handback, not a capability.

---

## IT

| Agent | Job |
| --- | --- |
| **Intake & Triage Agent** | Classify incoming requests, auto-resolve what it can, escalate the rest. |
| **Knowledge Agent** | Detect gaps in the knowledge base and draft articles to fill them. |
| **Incident Agent** | Detect incidents and open war rooms. |

Note the division: one agent stands at the front door, one works on the
long-lived asset, one responds to the exception. Those are three different
tempos, which is why they are three agents.

---

## HR

| Agent | Job |
| --- | --- |
| **Resume Screener** | Screen incoming applications. |
| **Interview Scheduler** | Schedule interviews. |
| **Hiring Coordinator** | Coordinate the hiring process. |
| **Feedback Manager** | Manage feedback. |

A pipeline, split by stage. Each hands off to the next rather than one agent
owning "recruiting."

---

## Marketing

| Agent | Job |
| --- | --- |
| **Competitive Intelligence Agent** | Track and report on the competitive landscape. |
| **Battlecard Agent** | Produce and maintain battlecards. |

Plus, in the campaign production example, a **Strategist Agent** that structures
a brief, a **Landing Page Builder** (a Claude Managed Agent) that generates page
variants, and a **Brand Reviewer** that checks output against brand guidelines
and flags issues.

---

## Executive office

| Agent | Job |
| --- | --- |
| **Operator Agent** | Operational support for the executive office. |
| **Org Health Agent** | Organizational health. |
| **Strategy Consultant Agent** | Strategy support. |

---

## What makes these work as jobs

Reading across the map, four properties recur:

1. **A trigger, not a button.** Each agent has a moment it activates — a request
   arrives, an incident is detected, a brief is ready — rather than waiting to
   be invoked.
2. **A bounded verb.** "Classify, auto-resolve, escalate" is a job description.
   "Help with IT" is not.
3. **A defined handback.** Escalation, a drafted article, a flagged issue — each
   agent produces something a person or another agent picks up.
4. **A name and an avatar.** They are addressable teammates, mentioned in the
   workflow, not menu items.

When you write your own, the test is whether you can state all four before you
build. If you cannot name the trigger or the handback, the agent is a feature.

## Subagent definitions

Five of these roles are written out as Claude Code subagent definitions in the
`agents/` folder of this post: `intake-triage-agent`, `knowledge-gap-agent`,
`incident-response-agent`, `brief-strategist-agent`, and `brand-reviewer-agent`.

## Source
[How monday.com transformed its platform into an agent-first product where humans and agents collaborate](https://claude.com/blog/how-monday-com-transformed-its-platform-into-an-agent-first-product-where-humans-and-agents-collaborate) (published 2026-08-20).

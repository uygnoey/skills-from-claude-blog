# Team auto mode policy

Copy, fill in, and keep it with the team's settings. Every section below corresponds to a
control one of Nuro, Gusto, or Garner Health described in the source post.

## 1. Scope

- **Team / org:**
- **Owner:**
- **Date, and date of next review:**
- **Default permission mode for this team:**
- **Who this applies to:**

## 2. Hard guardrails (independent of the classifier)

Commands and actions denied outright in settings, regardless of context.

| Denied action | Where the rule lives | Why |
| --- | --- | --- |
| e.g. recursive deletes | settings | irreversible, no legitimate agent use |
| | | |

## 3. Governed layers in front of the tools

- **MCP traffic routed through a proxy?** (yes / no — describe the tool guards and prompt
  inspection in place)
- **Scope of credentials available to agents:**
- **Integrations reachable by agents:** (e.g. CRM, ticketing, data warehouse)

## 4. Classifier tuning

- **Actions never auto-approved beyond the defaults:**
  - [ ] Actions that communicate with other people (Slack messages, email)
  - [ ] ______________________
- **Per-team permissiveness adjustments, and who owns them:**

## 5. When to step out of auto mode

| Situation | Mode to use instead | Owner of the judgment |
| --- | --- | --- |
| Reviews or output that go to other teams | interactive | |
| Production infrastructure (IaC, cloud console, live API writes) | accept edits, verify each call | |
| | | |

Guiding question to apply per session: *weigh the time saved against what the agent could
reasonably get wrong, and how catastrophic that would be. You are still responsible for what
happens.*

## 6. Unattended runs

- **Task shapes approved for unattended/overnight running** (must have a measurable signal
  the agent can iterate against):
- **Required output form:** (finished PRs for review / report / other — not merged changes)
- **Kickoff and review ritual:**

## 7. Standardized workflow

- **Is the lifecycle packaged as shared skills / a plugin?** (yes / no — link or name it)
- **Stages:** (e.g. explore context → commit context files → antagonistic research →
  implement → pause for human when context is missing)
- **What triggers a pause for a human:**

## 8. Telemetry

Telemetry is treated here as the precondition for the rollout, not a follow-up.

- **What we capture:** (sessions, transcripts, denials, modes used)
- **Where it lands, and who reviews it:**
- **Denial rate we observe:** ______ % of sessions include a classifier denial
- **What we do if that rate is near zero:**
- **What we do if it is high enough to interrupt routine work:**

## 9. Open questions and review

- **Unresolved:**
- **Next review date and trigger:**

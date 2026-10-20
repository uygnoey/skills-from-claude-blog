# Matching model and effort level to each agent's job

Scheduled agents run every day whether anyone is watching or not, so waste adds up in both cost and
reliability. Two things keep a fleet efficient: how it is designed, and which model each agent runs
on.

## What the design contributes
- **One job per agent**, so its instructions stay focused on that job.
- **Each working agent runs on a schedule** — it wakes up, does its pass, and stops.
- **The agents share memory**, so a correction made once is reused everywhere instead of being
  re-explained in every prompt.

## Choosing the model
Once an agent's job is well defined, it may not need the most capable model.

| Agent | Nature of the work | Model in the source fleet |
| --- | --- | --- |
| Furiwake (routing) | Follows a written rulebook | Sonnet (smaller) |
| Shoudan (CRM updates) | Follows a written rulebook | Sonnet (smaller) |
| Sabaki (triage + first-touch draft) | Needs judgment per lead | Opus (larger) |
| Nokori (meeting summaries + follow-ups) | Needs judgment per meeting | Opus (larger) |
| Coordinator | Needs judgment most — it edits the other agents' instructions, and one bad edit reaches every agent | Opus (larger) |
| Henji (hourly reply drafts) | Needs as much judgment as Sabaki, but runs most often | Sonnet + advisor strategy |

## The advisor strategy, for the frequent judgment-heavy agent
Henji needs Sabaki-level judgment but runs all through the working day, so running it on the larger
model every time would be the most expensive option. Instead:

1. Henji runs on Sonnet.
2. When it reaches a decision it cannot make on its own, it asks Opus for advice.
3. The advisor reads what Henji has done so far and sends back a plan, a correction, or a stop
   signal.
4. Henji finishes the draft for human review.

## Effort level
Effort level — how long the model thinks before it answers — is set per agent, separately from the
model. Raise it only where the reasoning is hard, as with the reply agent's drafts.

## The common mistakes
- Adding to existing instructions rather than updating them.
- Giving agents more context than they need for their tasks.
- Running every job on the biggest model at the highest effort level.

## Source
[How an Anthropic BDR in Japan runs his day with Claude Managed Agents](https://claude.com/resources/articles/how-an-anthropic-japan-business-development-representative-runs-his-day)
(published 2026-10-16), which also links the advisor strategy in Managed Agents.

# The six roles in the source fleet

The fleet is called the Nakama — "the crew", or more literally the companions you work with. Every
agent has one clear job, and every agent in the source fleet carries a Japanese name because the work
is mostly in Japanese. Five agents do the work; the sixth is the fleet's operations manager.

Use this as a model for splitting a workflow, not as a fixed roster: the useful part is that each
role is one step of a day, with a defined trigger, a defined output, and a defined place it reports.

## Furiwake — "sorting"
- **Runs:** first, at the start of the day.
- **Job:** reads the daily inbound queue and routes each lead to the right rep on the team.
- **Inputs it weighs:** the number of leads per rep, the priority of each lead, and who is in that
  day.
- **Guarantee:** every lead has an owner before anyone on the team starts their day.
- **Report:** posts a run report to a dedicated Slack channel — every lead in, every lead assigned —
  so the handoff is traceable.
- **Model:** follows a written rulebook, so it runs on the smaller model (Sonnet).

## Sabaki — "handling"
- **Runs:** on a schedule, after routing.
- **Job:** triages the leads assigned to its owner.
- **Steps:** qualifies each lead, categorizes it against pre-set criteria, takes the defined next
  step for that category (point the lead to self-serve, or craft a customized first email), updates
  the lead record in Salesforce, and drafts the first-touch email.
- **Source of draft content:** the fleet's shared knowledge base (the memory store every agent reads
  and writes).
- **Model:** judgment-heavy, so it runs on the larger model (Opus).

## Henji — "reply"
- **Runs:** hourly, through the working day.
- **Job:** scans the inbox for customer emails that need a response and prepares a draft reply in
  Japanese or English, depending on the thread.
- **Source of draft content:** the same shared knowledge base as Sabaki.
- **Handoff:** the human reviews, edits, and sends.
- **Model:** needs as much judgment as Sabaki but runs far more often, so it runs on the smaller
  model and uses the advisor strategy to consult the larger model when it reaches a decision it
  cannot make on its own. Its effort level is raised because the reasoning is hard.

## Shoudan — "opportunity"
- **Runs:** on a schedule.
- **Job:** reads recent customer interactions and pushes updates into Salesforce, so opportunity
  records stay current without manual data entry.
- **Model:** follows a written rulebook, so it runs on the smaller model (Sonnet).

## Nokori — "what remains"
- **Runs:** at the end of the day.
- **Job:** scans the calendar, reads the attached meeting transcripts, summarizes each meeting, and
  drafts the follow-ups.
- **Source of draft content:** the same shared knowledge base.
- **Model:** judgment-heavy, so it runs on the larger model (Opus).

## The coordinator
- **Runs:** between the other agents' runs, on a short cycle (roughly every 15 minutes).
- **Job:** the fleet's operations manager. It updates the agents' instructions and the shared
  knowledge base.
- **Trigger:** a plain-language request posted in the fleet's Slack channel. Only the fleet's owner
  may post requests for changes to agents' instructions and system prompts.
- **Also picks up:** the morning brief of product and pricing updates posted by Claude Tag, and
  writes the necessary changes into the shared knowledge base.
- **Model:** the larger model, at the highest need for judgment in the fleet — it edits the other
  agents' instructions, and one bad edit would reach every agent.

## Shared conventions across the roles
- Every draft arrives with a short summary at the top of what is going on, so the reviewer does not
  have to trace the whole thread for context.
- A written rulebook defines each agent's lane; pricing questions, sensitive accounts, and ambiguous
  asks route to the human.
- Items that need a follow-up step outside the routine are posted to the fleet's channel and tagged
  to Claude Tag rather than queued for the human.

## Source
[How an Anthropic BDR in Japan runs his day with Claude Managed Agents](https://claude.com/resources/articles/how-an-anthropic-japan-business-development-representative-runs-his-day)
(published 2026-10-16).

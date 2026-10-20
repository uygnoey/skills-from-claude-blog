**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
A business development representative on Anthropic's Japan team describes the fleet of scheduled
agents — the "Nakama" — that clears his inbound queue, drafts bilingual customer email, and keeps
Salesforce current. He prototyped every agent in Claude as a skill plus a scheduled task plus a
shared folder, then moved the fleet onto Claude Managed Agents (beta), and hands follow-up steps to
Claude Tag in Slack.

## When is it useful?
- When a repetitive, daily workflow (lead routing, triage, reply drafting, CRM updates, follow-ups)
  is large enough to split across several single-purpose agents.
- When agents prototyped in Claude have outgrown what you can track by editing skills from whatever
  chat happens to be open, and you want each agent defined once with a versioned history.
- When scheduled agents need to run while your laptop is closed, share one memory, and reach
  outside services through credentials you can scope and revoke.
- When you want to control the cost of agents that run every day by matching model and effort level
  to each agent's job.

## Key points
- One job per agent. Six agents in the fleet: Furiwake (routes the inbound queue to reps), Sabaki
  (triages and drafts the first-touch email for the author's leads), Henji (hourly inbox scan and
  reply drafts in Japanese or English), Shoudan (pushes updates into Salesforce), Nokori (end-of-day
  meeting summaries and follow-up drafts), and a coordinator that updates the other agents'
  instructions and the shared knowledge base.
- Prototype in Claude first: a skill per agent, a scheduled task per skill, and a shared folder as
  the knowledge base. Move to Managed Agents when you have more agents than you can comfortably
  track.
- On Managed Agents the skill becomes the agent's system prompt, the scheduled task becomes a
  schedule on the agent's deployment, and the shared folder becomes a memory store; each instruction
  change is saved as a new version, and in-progress edits do not reach scheduled runs.
- Every agent reads and writes the same memory store, saving the difference between what it drafted
  and what the author actually sent, so one correction propagates across the fleet.
- Credentials live in managed vaults with scoped, revocable permissions; each deployment uses only
  the vaults its job needs and never sees the credentials.
- Change requests are posted in plain language in the fleet's Slack channel (only the author may
  request instruction changes); the coordinator checks roughly every 15 minutes and applies them.
- Items outside the routine are handed to Claude Tag in Slack, which lays out options, drafts what
  is needed, sets its own check-back reminders, and tags a human for review or sign-off.
- Cost control is design plus model choice: rulebook-driven agents (Furiwake, Shoudan) run on
  Sonnet; judgment-heavy ones (Sabaki, Nokori, the coordinator) run on Opus; Henji runs on Sonnet
  all day and uses the advisor strategy to ask Opus when it is stuck. Effort level is set separately
  from the model.
- The author's measured result: around 60 hours of work per week handled by the fleet, counting each
  task at the time it would have taken manually.
- Lessons: describe the job once and let Claude keep your corrections; the knowledge base matters
  more than the prompt; hand the agents more of the work sooner.

## Bundled resources
- Skill: `scheduled-agent-fleet` — designing, prototyping, and operating a fleet of single-purpose
  scheduled agents, with references on the roles, shared memory and credentials, and model/effort
  tiering, plus a prototype-to-Managed-Agents migration example.
- Agents: the six roles named in the post (`furiwake-lead-router`, `sabaki-lead-triage`,
  `henji-reply-drafter`, `shoudan-crm-updater`, `nokori-day-closer`, `fleet-coordinator`).
- Guide: "Designing a scheduled agent fleet" in four languages.

## Source
- https://claude.com/resources/articles/how-an-anthropic-japan-business-development-representative-runs-his-day

**English** · [한국어](./designing-a-scheduled-agent-fleet.ko.md) · [Español](./designing-a-scheduled-agent-fleet.es.md) · [日本語](./designing-a-scheduled-agent-fleet.ja.md)

# Designing a scheduled agent fleet

A methodology for replacing a repetitive daily workflow with a small group of scheduled agents —
drawn from how a business development representative on Anthropic's Japan team built the "Nakama"
fleet, prototyped it in Claude, and moved it to Claude Managed Agents.

## The shape of the problem

The manual version of this work is not hard; it is early and constant. A couple of hours each
morning routing and qualifying leads, then writing email in Japanese or English, then updating the
CRM in whatever time is left — usually a day or more behind.

What changes with a fleet is not that the work disappears, but who produces the first version. The
agents prepare most of it before the day starts, and the human reviews.

## Stage 1 — Split the work, one job per agent

Write down the day as the steps you actually perform, then give each step its own agent. A single
responsibility keeps each agent easy to reason about and easy to track when something is off.

The source fleet came out as six agents: a router that gives every inbound lead an owner before the
team starts, a triager that qualifies and drafts the first touch, an hourly reply drafter, a CRM
updater, an end-of-day summarizer, and a coordinator that changes the other five.

Two rules make the split work:

1. **Every agent reports somewhere.** The router posts a run report — every lead in, every lead
   assigned — to a dedicated channel, so the handoff is traceable rather than assumed.
2. **A written rulebook defines each lane.** Pricing questions, sensitive accounts, and ambiguous
   asks route to the human. Nothing improvises its way past that boundary.

## Stage 2 — Prototype in Claude, not in infrastructure

You do not need managed infrastructure to start. The prototype is three pieces per agent: a skill
holding the instructions for one job, a scheduled task so it runs without you, and one shared folder
as the knowledge base every skill writes back into.

The first version will be scrappy and will still work. Hand Claude one piece of the work at a time,
correct what it got wrong, and save the correction. Do not write a detailed prompt for every run.
Describe the job once, let Claude draft, fix the draft, keep the fix.

## Stage 3 — Move when tracking becomes the problem

The prototype breaks down for two reasons, neither of which is capability.

- **Sharing is a zip file.** Teammates who want the setup get skills and a few Markdown files they
  must upload and then answer setup questions about before anything runs.
- **Nothing has one definition.** Each agent is a skill, a scheduled task, and a folder, edited from
  whatever chat happens to be open — so the same skill gets changed from many conversations.

The goal of moving is to define each agent once, in one place, with every change visible. The
migration is a mapping, not a rewrite: the skill becomes the system prompt, the scheduled task
becomes a schedule on the deployment, the shared folder becomes a memory store, and service logins
become scoped vaults.

It does not require a developer. Describe each agent's job in plain language, let Claude write the
short setup scripts, and run them from a terminal. Starting from scratch instead, the Console
quickstart ships ready-made agent templates.

## Stage 4 — Operate the fleet

Three properties do the operational work.

**Background runs.** Agents run on their schedule whether a laptop is open or not, with no cron jobs
maintained on the side. A failed run can be opened and inspected step by step. While a change is
being tried out, scheduled runs keep using the deployed version, so a half-finished edit never lands
in tomorrow's run.

**One shared memory.** Every agent reads and writes the same store: the difference between what it
drafted and what the human sent, plus whatever it dug up while researching. A phrasing fixed once in
the reply agent stops the triager and the end-of-day agent from repeating it. This is why the
knowledge base matters more than the prompt — context comes from the store, so prompts stay short.

**Scoped credentials.** Credentials live in managed vaults. Each deployment uses only the vaults its
job needs, never sees the credentials, and access is revocable in one step.

Changes to the fleet go through the coordinator: post the request in plain language in one channel,
restricted to whoever is allowed to change instructions, and the coordinator picks it up on a short
cycle and saves the edit as a new version.

## Stage 5 — Hand off what falls outside the routine

Some items need a step the routine does not cover: an upgrade path, a purchasing route, an escalation
to another team. The agents do not stop and wait. They post the item to the shared channel and tag
Claude Tag, which reads the thread, checks the applicable rules and terms, lays out the options,
drafts what is needed, and tags a human for review or sign-off. When someone else has to reply first,
it sets its own reminder to check back and reports where things stand in the same thread.

## Stage 6 — Keep it efficient

Scheduled agents run every day whether anyone is watching, so waste compounds. Most of the efficiency
is the design: one job per agent, a schedule rather than a loop, and shared memory so a correction is
made once.

The rest is model choice. Rulebook-driven agents run on the smaller model. Judgment-heavy agents run
on the larger one — the coordinator most of all, since one bad edit reaches every agent. The agent
that needs judgment *and* runs constantly is the interesting case: run it small and let it ask the
larger model for advice when it is stuck, taking back a plan, a correction, or a stop signal. Effort
level is set separately from the model; raise it only where the reasoning is hard.

The three common mistakes are worth naming, because they are easy to drift into: adding to
instructions instead of updating them, handing agents more context than their task needs, and running
everything on the biggest model at the highest effort.

## What to expect

In the source fleet, counting each task at the time it would have taken manually, the agents handle
around 60 hours of work a week. The time that frees up goes to what agents cannot do effectively yet:
customer conversations, outbound strategy, cross-functional projects, and helping teammates build
their own fleets.

Three lessons from the author worth carrying into your own build:

- You do not need a detailed prompt every time. Describe the job once, fix the draft, let Claude keep
  the fix.
- The knowledge base matters more than the prompt. It took a few hundred cheap rounds of drafting,
  fixing, and saving to get the drafts to sound like him.
- Give the agents more room, sooner. The tasks he assumed needed him — updating the knowledge base,
  editing instructions by hand — worked fine once he let go of them.

## Source

[How an Anthropic BDR in Japan runs his day with Claude Managed Agents](https://claude.com/resources/articles/how-an-anthropic-japan-business-development-representative-runs-his-day)
(published 2026-10-16).

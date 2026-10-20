---
name: scheduled-agent-fleet
description: Design, prototype, and operate a fleet of single-purpose scheduled agents for a repetitive daily workflow — one job per agent, one shared memory, scoped credentials, and a model and effort level matched to each job. Use when a recurring workflow (lead routing, triage, reply drafting, CRM updates, end-of-day follow-ups) should be split across several agents that run on a schedule, or when agents prototyped as skills plus scheduled tasks have outgrown ad-hoc editing and need one definition per agent with a versioned history.
---

## Purpose
Turn a repetitive daily workflow into a small fleet of scheduled agents that prepare the work before
the day starts, so the human reviews output instead of producing it. Distilled from how an Anthropic
BDR in Japan built the "Nakama" fleet, prototyped it in Claude, and moved it onto Claude Managed
Agents.

## When to use
- A daily workflow has several distinct steps that each repeat the same way (routing, qualifying,
  drafting, record-keeping, follow-up).
- Agents already exist as skills edited from whatever chat is open, and the setup has become hard to
  track or share with teammates.
- Runs must happen on a schedule whether or not a laptop is open, and runs need to be inspectable
  after the fact.
- Daily runs make cost and reliability matter enough to tier models and effort levels.

## Instructions

1. **Split the workflow, one job per agent.**
   - Write down the workflow as the steps you actually perform in a day, then give each step to its
     own agent. A single responsibility keeps each agent easy to reason about and easy to debug when
     something is off.
   - Name the agents for what they do. See [references/fleet-roles.md](./references/fleet-roles.md)
     for the six roles in the source fleet and the shape of each job description.
   - Decide what each agent reports and where. In the source fleet the router posts a run report
     (every lead in, every lead assigned) to a dedicated Slack channel so the handoff is traceable.

2. **Write a rulebook that defines every agent's lane.**
   - State in writing which items each agent handles and which route to a human. In the source fleet
     pricing questions, sensitive accounts, and ambiguous asks go to the human.
   - Have each draft arrive with a short summary at the top of what is going on, so the reviewer does
     not have to trace a whole thread for context.

3. **Prototype the fleet in Claude before moving anywhere.**
   - One skill per agent (the instructions for one job), one scheduled task per skill, and one shared
     folder as the knowledge base every skill writes its learnings back into.
   - Hand over one piece of work at a time, correct what the agent got wrong, and save the
     correction. Do not write a detailed prompt for every run — describe the job once, let Claude
     draft, fix the draft, keep the fix.

4. **Move to Managed Agents once there are more agents than you can comfortably track.**
   - The skill becomes the agent's system prompt, the scheduled task becomes a schedule on the
     agent's deployment, and the shared folder becomes a memory store. See
     [examples/prototype-to-managed-agents.md](./examples/prototype-to-managed-agents.md).
   - Describe each agent's job in plain language and let Claude write the short setup scripts; the
     Console also has a quickstart with ready-made agent templates for a fresh start.

5. **Give the fleet one shared memory and scoped credentials.**
   - Every agent reads and writes the same memory store, saving the difference between what it
     drafted and what the human sent, plus anything new it dug up while researching. One correction
     then propagates across the fleet.
   - Keep credentials in managed vaults, give each deployment only the vaults its job needs, and keep
     revocation to a single step. Details in
     [references/shared-memory-and-credentials.md](./references/shared-memory-and-credentials.md).

6. **Add a coordinator, and change agents by asking it.**
   - One coordinator agent updates the other agents' instructions and the shared knowledge base
     between runs.
   - Post change requests in plain language in one channel, restricted to the people allowed to
     change instructions and system prompts; the coordinator checks the channel on a short cycle
     (roughly every 15 minutes in the source fleet) and applies them.
   - Keep each instruction change saved as a new version so every agent carries a numbered history,
     and so a half-finished edit does not reach the next scheduled run.

7. **Hand non-routine items to a chat-resident agent instead of stopping.**
   - When an item needs a follow-up step outside the routine (an upgrade path, a purchasing route, an
     escalation), have the agent post the item to the shared channel and tag Claude Tag rather than
     waiting for the human.
   - Claude Tag reads the thread, checks the applicable rules and terms, lays out the options, drafts
     what is needed, tags a human for review or sign-off, and sets its own reminder to check back
     when someone else has to reply first.

8. **Tier model and effort level per agent.**
   - Rulebook-driven agents run on the smaller model; judgment-heavy agents run on the larger one;
     a frequent, judgment-heavy agent runs small and asks the larger model for advice when it is
     stuck. Set effort level separately from the model and raise it only where the reasoning is hard.
   - Full tiering table and the common waste patterns:
     [references/model-and-effort-tiering.md](./references/model-and-effort-tiering.md).

## Examples

- **Prototype-to-production migration.** A fleet of five working agents plus a coordinator, built in
  Claude as skills with scheduled tasks and a shared folder, mapped piece by piece onto Managed
  Agents deployments, schedules, memory stores, and vaults — see
  [examples/prototype-to-managed-agents.md](./examples/prototype-to-managed-agents.md).
- **A correction that propagates.** The human rewrites a phrase in a reply draft before sending. The
  reply agent saves the difference between its draft and the sent email as a note on how the human
  phrases things. The triage and end-of-day agents read the same memory store and stop making the
  same mistake.
- **A non-routine item.** An agent cannot determine a customer's purchasing route, so it posts the
  item to the fleet's channel and tags Claude Tag. Claude lays out the options, drafts the reply,
  sets a reminder for the following Tuesday to check whether the customer answered and whether the
  deal desk resolved the ticket, then posts where things stand in the same thread and drafts a nudge
  for the human to send.
- **What it adds up to.** In the source fleet, counting each task at the time it would have taken
  manually, the fleet handles around 60 hours of work a week; the human's remaining role is the work
  that needs judgment — customer conversations, outbound strategy, cross-functional projects.

## Anti-patterns
- Adding to existing instructions instead of updating them, so each agent's prompt grows without
  getting clearer.
- Giving agents more context than their task needs.
- Running every job on the biggest model at the highest effort level.
- Keeping work the agents could do — updating the knowledge base by hand, editing each agent's
  instructions yourself — out of caution rather than need.

## Source
Distilled from [How an Anthropic BDR in Japan runs his day with Claude Managed Agents](https://claude.com/resources/articles/how-an-anthropic-japan-business-development-representative-runs-his-day)
(published 2026-10-16).

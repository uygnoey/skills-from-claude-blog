# Example: moving a prototyped fleet onto Managed Agents

## The prototype, built in Claude
You do not need Managed Agents to start. The source fleet was prototyped entirely in Claude from
three pieces:

- **A skill per agent** — the instructions for one job.
- **A scheduled task for each skill**, so no run has to be started by hand.
- **A shared folder on the laptop** as the knowledge base every skill writes its learnings back
  into: the difference between what it drafted and what the human sent, plus anything new it dug up
  along the way.

The first version was scrappy and still did the job: hand Claude one piece of the work at a time,
correct what it got wrong, and save those corrections. Over time that grew into a handful of agents,
each covering a different routine.

## Why move
Two problems showed up as the fleet grew, and neither was about capability:

- **Sharing.** Teammates asking for the setup could only be sent a zip file of skills and a few
  Markdown files from the knowledge base, which they had to upload to Claude and then answer a round
  of setup questions before anything worked.
- **Tracking.** Each agent was a skill, a scheduled task, and a shared folder, and changes were made
  by asking Claude in whatever chat happened to be open — so the same skill was being edited from
  many different conversations.

The goal was to define each agent once, in one place, with every change to it visible.

## The mapping

| Prototype in Claude | On Managed Agents |
| --- | --- |
| The agent's skill | The agent's system prompt |
| The skill's scheduled task | A schedule on the agent's deployment (cadence and timezone set in the Console) |
| The shared folder | A memory store every agent reads and writes |
| Service logins held by the person | Managed vaults, scoped per deployment |
| "Edit the skill in some chat" | A versioned instruction change, requested in plain language in one Slack channel |

## What the migration actually took
The docs talk about schedules, tools, and credential vaults, which reads as developer territory — but
the agents already existed and only had to be moved. Describing each agent's job in plain language
was enough: Claude wrote a few short setup scripts, which were run from the terminal on a laptop.
Starting from scratch instead, the Console has a quickstart with ready-made agent templates. After
the move there is no infrastructure left to look after.

## The three things that mattered most after moving
1. **The agents run in the background** on their schedule whether the laptop is open or not, even
   offline — no cron jobs to maintain on the side, and a failed run can be opened in the Console to
   see each step the agent took. Scheduled runs keep using the deployed version while a change is
   being tried out.
2. **The fleet shares one memory and learns from edits** — any agent can use the others' learnings,
   because every agent reads and writes the same store.
3. **Credentials live in a managed vault with scoped permissions** — each deployment uses only the
   vaults its job needs, never sees the credentials, and access can be revoked in one step.

## When to make the move
Start in Claude. Move to Managed Agents once you have more agents than you can comfortably keep
track of.

## Source
[How an Anthropic BDR in Japan runs his day with Claude Managed Agents](https://claude.com/resources/articles/how-an-anthropic-japan-business-development-representative-runs-his-day)
(published 2026-10-16).

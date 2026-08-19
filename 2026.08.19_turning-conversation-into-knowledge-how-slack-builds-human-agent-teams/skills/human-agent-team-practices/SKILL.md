---
name: human-agent-team-practices
description: Set up and run a team where people and agents work together in shared channels. Use when agents have workspace access but return shallow answers because context lives in private threads; when deciding which work an agent owns and where a human reviews; when defining roles for several specialized agents instead of one general assistant; when adoption is stalling and needs peer demonstration rather than mandate; or when leadership asks for evidence of value and only usage metrics are available.
---

# Running human-agent teams

Derived from an interview with Jaime DeLanghe, Chief Product Officer at Slack,
on how a company that has argued for working in the open since long before AI
now runs teams of people and agents together.

The organizing claim: the conversation around the work is the context agents
need to be useful. Everything below follows from it.

## Instructions

### 1. Make the conversation history readable by agents

The old promise — that the exhaust of people working together would compound
into organizational knowledge — did not hold on its own. DeLanghe points to
early Slack research finding the opposite: conversation largely did not turn
into knowledge, and people kept repeating themselves. Reading all of it was
never humanly possible. That is now an agent's job, but only for what the agent
can see.

- **Default to public channels.** Decisions made in DMs or private threads are
  invisible to agents, and stay lost to the organization.
- **Ask for reasoning, not the record.** Rather than searching for what was
  decided, ask an agent to reconstruct *why* it was decided and how the context
  has shifted since.
- **Widen the surface area.** Connect meetings, email, calendar, and document
  repositories. The more context is connected, the less the team repeats itself.

### 2. Build the work around a handoff cycle

The core rhythm of a human-agent team is a cycle, not an end-to-end automation.
Agents do the production work — drafting, summarizing, monitoring, preparing —
and pass results to a person. The person reviews, decides, redirects, and hands
work back for the next step.

- **Start the day with agent-built briefings.** Recaps, escalations, meeting
  prep, and web roundups are good agent-driven tasks with human review.
- **Anchor the loop in a shared channel** so humans and agents triage together,
  with humans leading prioritization.
- **Make lightweight signals actionable.** In DeLanghe's channel, an emoji
  reaction adds an item to the list and an agent picks up the task.

Worked through in [examples/weekly-handoff-loop.md](examples/weekly-handoff-loop.md).

### 3. Give each agent a role, the way a coworker has one

A fleet of specialized agents is disorienting to anyone whose mental model is a
one-on-one chatbot. DeLanghe's framing is social rather than technical: agents
are something like coworkers, and coworkers have roles and responsibilities.

- **Route routine, transactional tasks to a general agent** — filing a help desk
  ticket, pulling last week's metrics into a status update — rather than asking
  people to remember a specialized tool for each one.
- **Let value be felt, not mandated.** If people cannot articulate what an agent
  is for, that is the signal to retire it.

### 4. Default channels to public; go private on purpose

Keep channels public unless there is a specific reason to gate the context.

- **Keep business-as-usual work in the open** — non-sensitive projects,
  announcements, Q&A.
- **Remember agents read what your team reads.** A private channel is a blind
  spot for every agent that reports on it.
- **Treat psychological safety as the real lever.** Once genuinely sensitive
  material is walled off, what drives work into DMs is usually discomfort with
  being seen mid-process, not secrecy. People need to feel safe doing everyday
  work in the open, rough drafts and half-formed questions included.

### 5. Spread adoption by demonstration, not mandate

The fastest way to learn a new way of working is to watch a teammate do it.

- **Stand up a company-wide show-and-tell channel**, public by default, so a
  technique from one function can reshape another.
- **Encourage write-ups others can copy.** A short "what I did and how" document
  turns one person's setup into a team template. Inside Slack, the push to get
  product managers using Claude was largely self-organized this way: one PM
  documented his setup, others copied the format, and teams went on to run
  workshops and build their own repos.

Use [templates/show-and-tell-writeup.md](templates/show-and-tell-writeup.md).

### 6. Measure outcomes, not activity

More messages never proved Slack was working — it can equally mean people
cannot find what they need. Measuring AI value has the same shape.

- **Treat usage metrics as a pulse check, not proof.** Token usage tells you the
  lights are on. That is worth knowing and is not sufficient.
- **Expect to use judgment.** There is no clean way to prove that how people use
  these tools produces better business results; connecting the two still takes
  leaps of faith that no dashboard will make for you.

### 7. Start small, and change the work

The advice for organizations is to reimagine workflows rather than do the same
work faster — and to treat that as a team sport. Start soon but start small:
put a group of people in a shared channel with an agent, give them the same set
of resources, and let them work. What they build tends to spread on its own.

Full detail on all six practice areas:
[references/practice-areas.md](references/practice-areas.md).

## Examples

### Example 1 — an agent that returns shallow answers

A team asks an agent why a product decision was made and gets nothing useful.
The cause is not the agent: the debate happened in a DM thread between two
leads, and only the outcome was posted publicly.

Apply step 1. Move the decision-making conversation into a public channel going
forward, and change the ask from "what did we decide" to "reconstruct why we
decided this and what has changed since." The blind spot was structural, so the
fix is structural.

### Example 2 — a Monday morning handoff loop

An executive's week opens with an agent-built daily briefing, a recap of the
previous week's workshops with escalations flagged, a report on developments
across the web, briefings for the day's meetings, and a rewritten bio waiting
for review. Each item is production work done by an agent and closed by a human
decision. Priorities are set by the human in the shared channel; an emoji
reaction is enough to add a new item for an agent to pick up.

### Example 3 — an agent nobody can describe

A specialized agent was rolled out by mandate. Six weeks later people cannot say
what it is for, and usage is concentrated in the team that built it.

Under step 3 this is a retirement signal, not a training problem. Fold its
routine tasks into the general agent, and reinvest the attention in a
show-and-tell channel where value can be demonstrated rather than announced.

### Example 4 — reporting on value

Leadership asks whether the AI rollout is working, and the only number available
is token usage. Report it as adoption, not as effect, and pair it with outcome
evidence — what work changed, what stopped being repeated, what a team now does
differently. Be explicit that the final link takes judgment rather than pretend
a dashboard settles it.

## Source

- https://claude.com/blog/turning-conversation-into-knowledge-how-slack-builds-human-agent-teams (August 19, 2026)

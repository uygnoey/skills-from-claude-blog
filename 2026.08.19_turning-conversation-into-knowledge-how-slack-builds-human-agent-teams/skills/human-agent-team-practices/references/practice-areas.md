# The six practice areas

A structured summary of the practices described in the August 19, 2026
interview with Jaime DeLanghe, Chief Product Officer at Slack. Each area pairs
the underlying claim with what it asks you to change.

---

## 1. Treat conversation history like a knowledge base

**The claim.** The long-standing hope that the by-product of people working
together would compound into organizational knowledge did not materialize on
its own — DeLanghe cites early Slack research showing conversation largely did
not become knowledge, and people went on repeating themselves. The volume was
never something humans could process. An agent can.

**What to change**

| Practice | Why |
|---|---|
| Default to public channels | Agents can only learn from what they can see; DM and private-thread decisions are invisible to them and lost to the organization |
| Ask for reasoning, not the record | Retrieving *why* a decision was made, and how context has shifted since, is more valuable than retrieving *what* was decided |
| Widen the surface area | Connecting meetings, email, calendar, and document repositories reduces how often the team repeats itself |

---

## 2. Learn when to hand off between agents and humans

**The claim.** The core rhythm of a human-agent team is a cycle of handoffs, not
a fully automated pipeline. Agents produce; humans review, decide, and redirect;
agents carry out the next step.

Typical agent-side work: drafting, summarizing, monitoring, preparing.

**What to change**

| Practice | Why |
|---|---|
| Start the day with agent-built briefings | Recaps, escalations, meeting prep, and web roundups are naturally agent-driven with human review |
| Anchor the work in a shared channel | Humans and agents triage together, with humans leading prioritization |
| Make lightweight signals actionable | An emoji reaction can add an item to a list and trigger an agent to pick it up |

---

## 3. Delegate clear roles for agents

**The claim.** Working with a fleet of specialized agents is disorienting if
your mental model is a single chatbot. The useful framing is social rather than
technical — agents resemble coworkers, and coworkers have roles, goals, and
focus areas.

**What to change**

| Practice | Why |
|---|---|
| Route routine, transactional tasks to a general agent | Better than asking people to remember a specialized tool for filing a ticket or pulling last week's metrics |
| Let value be felt, not mandated | If people cannot articulate what an agent is for, that is the signal to retire it |

---

## 4. Default shared channels to public; go private on purpose

**The claim.** Slack has recommended public-by-default channels since its
earliest days, on the grounds that open context compounds: new people onboard
into history rather than an empty inbox, and nobody repeats themselves. Agents
now benefit from the same openness, and what they learn flows back to people.

**What to change**

| Practice | Why |
|---|---|
| Keep business-as-usual work in the open | Non-sensitive projects, announcements, and Q&A are where agent coworkers gain the context that makes them useful |
| Remember agents read what your team reads | A private channel is a blind spot for every agent that reports on it |
| Let psychological safety draw the line | Once genuinely sensitive material is walled off, what pushes work into DMs is usually discomfort with being seen mid-process, not secrecy |

The last row is the one organizations tend to underweight. People need to be
confident doing everyday work in the open — rough drafts and half-formed
questions included — and trust their colleagues to meet it in good faith. As
DeLanghe puts it, "you gain trust by giving trust."

---

## 5. Spread adoption by showing what is possible

**The claim.** The fastest way to learn a new way of working is to watch a
teammate do it. DeLanghe points to a company-wide channel at Salesforce, public
by default and thousands of members strong, where employees trade skills,
debugging tips, and workflow tricks — and where a technique from a sales process
can end up reshaping an engineering one.

Inside Slack, getting product managers onto Claude was largely self-organized:
one PM got help from the developer experience lead, wrote up what he did and how
he did it, and other PMs copied the format. Teams then organized workshops and
built their own repos.

**What to change**

| Practice | Why |
|---|---|
| Stand up a company-wide show-and-tell channel | One public place where a trick from one function can reshape another |
| Encourage write-ups others can copy | A short "what I did and how" doc turns one person's setup into a team template or skill |

---

## 6. Measure outcomes, not activity

**The claim.** More messages never meant Slack was working better — it can just
as easily mean people cannot find what they need, or could not say what they
meant the first time. Measuring the value of AI has the same shape, and simple
metrics do not settle it.

**What to change**

| Practice | Why |
|---|---|
| Treat usage metrics as a pulse check | Token usage tells you the lights are on: important to know, not sufficient |
| Be ready to use your own judgment | There is no clean way to prove that tool usage produces better business results; the link still takes leaps of faith, and no dashboard supplies them |

---

## The closing advice

Reimagine workflows rather than doing the same work faster, and treat that as a
team sport. Start soon, but start small: bring a group of people into a shared
channel with an agent, give them the same set of resources, and let them work.
What they build tends to spread on its own.

## Source

https://claude.com/blog/turning-conversation-into-knowledge-how-slack-builds-human-agent-teams

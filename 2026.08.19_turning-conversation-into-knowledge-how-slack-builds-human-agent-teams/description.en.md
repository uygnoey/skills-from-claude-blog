**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
The second post in a series on building human-agent teams — an interview with Jaime DeLanghe, Chief Product Officer at Slack, on how her company runs teams made of people and agents together. She joined Slack in 2017 to work on search and machine learning with the goal of turning workplace conversation into institutional knowledge, and has long argued that this only works if people work in the open. The post extends that argument to agents: the conversation around the work is the context agents need in order to be useful.

Six practice areas are covered, each with concrete "how to put this into practice" advice: treating conversation history as a knowledge base, handoffs between people and agents, giving agents clear roles, defaulting channels to public, spreading adoption by example, and measuring outcomes rather than activity.

## When is it useful?
- When agents have access to a workspace but produce shallow results because the decisions and reasoning they would need live in DMs and private threads.
- When deciding what an agent should own and where a human must review, rather than trying to automate an end-to-end workflow.
- When a fleet of specialized agents feels disorienting to people whose mental model is a single chatbot.
- When adoption has stalled and rollout is being driven by mandate instead of by visible peer examples.
- When leadership asks for proof of AI value and the only available numbers are usage metrics.

## Key points
- **Conversation only becomes knowledge if something reads it.** DeLanghe notes that early research at Slack found the opposite of the promise: conversation largely did not turn into knowledge, and people kept repeating themselves. Making sense of that volume was never humanly possible — it is now an agent's job.
- **Ask for reasoning, not just the record.** Instead of retrieving what was decided, ask an agent to reconstruct why it was decided and how the context has shifted since.
- **Widen the surface area.** The more of meetings, email, calendar, and document repositories you connect, the less the team repeats itself.
- **The core rhythm is a handoff cycle.** Agents do production work — drafting, summarizing, monitoring, preparing — and pass results to a person, who reviews, decides, and redirects, then hands work back. DeLanghe's Monday starts with an agent-built daily briefing plus a workshop recap with flagged escalations, a report on AI developments, meeting briefings, and a rewritten bio awaiting review.
- **Anchor the loop in a shared channel**, where humans and agents triage together and humans lead prioritization. Lightweight signals should be actionable — in her channel, an emoji reaction adds an item and an agent picks it up.
- **Treat agents like coworkers with roles.** Clear goals and focus areas beat a general-purpose assistant nobody can describe. Her test: if the value of an agent feels mandated rather than clearly felt, that is a signal to retire it.
- **Public by default; private on purpose.** A private channel is a blind spot for every agent that reports on it. Once genuinely sensitive material is walled off, what pushes work into DMs is usually discomfort with being seen mid-process, not secrecy — so psychological safety, not policy, is the real lever.
- **Adoption spreads by demonstration.** A company-wide show-and-tell channel lets a trick from one function reshape another. Inside Slack, a push to get product managers using Claude was largely self-organized: one PM wrote up what he did and how, and other PMs copied the format.
- **Measure outcomes, not activity.** Token usage tells you the lights are on. It does not tell you the work got better, and no dashboard will close that gap for you.
- **The advice is to change the work, not speed it up.** Start soon but start small: put a group of people in a shared channel with an agent, give them the same resources, and let what they build spread on its own.

## Bundled resources
- `skills/human-agent-team-practices/SKILL.md` — how to set up and run a human-agent team.
- `skills/human-agent-team-practices/references/practice-areas.md` — the six practice areas with their practical advice.
- `skills/human-agent-team-practices/examples/weekly-handoff-loop.md` — the handoff cycle worked through as an example.
- `skills/human-agent-team-practices/templates/show-and-tell-writeup.md` — a "what I did and how" write-up template for spreading adoption.
- `guides/human-agent-team-operating-model.{en,ko,es,ja}.md` — the same material as a four-language guide.

## Source
- https://claude.com/blog/turning-conversation-into-knowledge-how-slack-builds-human-agent-teams (August 19, 2026)

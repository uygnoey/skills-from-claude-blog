# Example: a weekly human-agent handoff loop

An illustration of practice area 2 — the handoff cycle — built from the Monday
morning routine described in the August 19, 2026 interview with Jaime DeLanghe.
The point is the shape of the loop, not the specific items.

## The loop

```
agent produces  →  human reviews & decides  →  human redirects  →  agent executes
      ↑                                                                   │
      └───────────────────────────────────────────────────────────────────┘
```

Agents do production work. Humans do judgment. Neither runs unattended.

## Monday morning, as described

Waiting when the week starts:

| Item | Agent side | Human side |
|---|---|---|
| Daily briefing | Compiled overnight | Read, decide what matters today |
| Recap of the previous week's product workshops | Summarized, with escalations flagged | Act on the escalations |
| Report on AI developments across the web | Gathered and summarized | Decide what changes plans |
| Briefings for the day's meetings | Prepared per meeting | Use, correct where wrong |
| A stale bio handed off for rewriting | Rewritten | Approve, edit, or send back |

Each row closes with a human decision. That is what makes it a team rather than
an automation.

## The channel is the workspace

The loop is anchored in a shared channel where humans and agents triage
together, and humans lead prioritization. Two properties matter:

1. **Visible.** Work in the channel is context for every agent and every person
   who joins later.
2. **Cheap to steer.** Signals should be lightweight — in DeLanghe's channel, an
   emoji reaction adds an item to the list and an agent picks up the task. If
   adding work requires composing a prompt, the loop slows to the speed of
   typing.

## Setting one up

1. Create a shared channel and put a small group of people in it with an agent.
   Give everyone the same set of resources.
2. Name what the agent produces on a schedule (briefings, recaps, monitoring).
3. Name the human decision that closes each item.
4. Define one lightweight signal — a reaction, a keyword — that adds work.
5. Let prioritization stay with the people.

Start small and let what works spread, rather than designing the full system in
advance.

## Source

https://claude.com/blog/turning-conversation-into-knowledge-how-slack-builds-human-agent-teams

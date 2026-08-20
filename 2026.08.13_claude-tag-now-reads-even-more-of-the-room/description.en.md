**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
An update announcement for Claude Tag, the Slack integration, about **when it decides to proactively collaborate with a team**. Previously it evaluated one message at a time. Now it uses context from across the channel, along with its memory and the standing instructions it has been given, to decide when to contribute — which the announcement puts at roughly 30% better at judging when, and when not, to respond proactively.

The update also spells out the four choices Claude makes on any message, the mechanisms that let it disengage, and that the extra context it now holds does not count toward usage or spend limits.

## When is it useful?
- When a Slack-resident agent is contributing too often, or not often enough, and you need to know which control to reach for.
- When you are writing standing instructions for a channel and want to know what levers those instructions actually move.
- When someone asks what the wider context window does to the bill.
- When a thread looks unanswered and you are unsure whether the agent picked it up.

## Key points
- **Channel-wide context replaces per-message evaluation.** Claude now judges from context across the channel plus its memory and standing instructions, rather than message by message.
- **Roughly 30% better** at determining when, and when not, to proactively respond.
- **Four choices on any message:** reply inline for short, verifiable answers; start deeper work in a thread for complex issues; route the message to an existing workstream; or stay silent.
- **Silence is a real mode**, evaluated like the others — not a failure to answer.
- **Knowing when to disengage** comes from four mechanisms: channel-specific rubrics that weigh usefulness and confidence; reduced attention to inactive channels until Claude is mentioned; user controls to turn automatic responses off; and plain-language instructions for customizing behavior.
- **No additional cost today.** Holding more context does increase Claude Tag's usage, but the additional context it holds does not count toward usage or spend limits.
- **Faster acknowledgment.** Claude acknowledges messages within seconds rather than operating silently during startup.
- **Availability:** live for Claude Teams and Enterprise customers.

## Bundled resources
- `skills/channel-proactivity-tuning/SKILL.md` — pick the right response mode, write standing instructions, and use the suppression controls when the agent is too chatty.
- `skills/channel-proactivity-tuning/references/response-modes.md` — the four modes and how to choose between them per channel.
- `skills/channel-proactivity-tuning/references/suppression-controls.md` — the four disengagement mechanisms, ordered narrowest to broadest.
- `skills/channel-proactivity-tuning/templates/standing-instructions.md` — a per-channel, plain-language instruction template.

## Source
- https://claude.com/blog/claude-tag-now-reads-even-more-of-the-room

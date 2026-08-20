---
name: channel-proactivity-tuning
description: Tune when a Slack-resident agent should speak up and when it should stay quiet, now that it judges channel-wide context rather than one message at a time — pick the right response mode, write standing instructions in plain language, and use the suppression controls when it is contributing too often.
---

## Instructions
You are helping a team configure how a Slack-resident agent decides to participate in a channel. The behavior changed: instead of evaluating each message in isolation, the agent now uses **context from across the channel**, plus its memory and the standing instructions it has been given, to decide whether to contribute. The stated effect is roughly 30% better judgment about when — and when not — to respond proactively.

### 1) Know what the four choices are
On any given message the agent picks one of four responses. Get the team aligned on which they want where; the details are in [references/response-modes.md](references/response-modes.md).

1. **Reply inline** — for short, verifiable answers.
2. **Start deeper work in a thread** — for complex issues that need more than a line.
3. **Route to an existing workstream** — when the message belongs to work already underway.
4. **Stay silent** — when contributing would not help.

Silence is a first-class choice here, not a failure to respond.

### 2) Write standing instructions in plain language
Behavior is customized with plain-language instructions, not configuration syntax. Use [templates/standing-instructions.md](templates/standing-instructions.md) to draft them per channel.

Write instructions that answer, for this specific channel: what is in scope, what is explicitly not, when to thread rather than reply inline, and what should never draw a proactive response.

### 3) Use the suppression controls when it is too chatty
Four mechanisms keep the agent from over-participating; see [references/suppression-controls.md](references/suppression-controls.md):

- **Channel-specific rubrics** evaluate usefulness and confidence before it contributes.
- **Inactive channels get less attention** until the agent is explicitly mentioned.
- **Automatic responses can be turned off** by users who want mention-only behavior.
- **Plain-language instructions** adjust the threshold without turning proactivity off entirely.

Reach for the narrowest control that fixes the complaint. Turning automatic responses off in a channel that mostly benefits from them is a bigger change than tightening the rubric.

### 4) Set expectations on cost and responsiveness
- **No additional cost today.** Holding more context does increase the agent's usage, but the additional context it holds does not count toward usage or spend limits.
- **Acknowledgment is faster.** The agent acknowledges messages within seconds rather than working silently through startup, so a thread no longer looks unanswered while work is beginning.
- **Availability:** live for Teams and Enterprise customers.

## Examples

### Example: it answers in a channel where it should mostly listen
User: It keeps chiming in on #incidents and it's noise during a live page.
Assistant:
- Start with the channel rubric — tighten the usefulness and confidence bar for #incidents specifically rather than changing global behavior.
- Add a standing instruction in plain language: during an active incident, stay silent unless explicitly mentioned; when mentioned, reply inline with short verifiable facts and do not start threads.
- If it still contributes too often, turn off automatic responses for that channel so it is mention-only.
- Draft the instruction with [templates/standing-instructions.md](templates/standing-instructions.md).

### Example: replies are too shallow for the questions being asked
User: People ask real analysis questions and it fires back a one-liner.
Assistant:
- That is a mode-selection problem, not a quality problem. Inline replies are for short, verifiable answers; complex issues are supposed to open a thread.
- Write a standing instruction for the channel describing what counts as complex here — anything requiring more than one source, any question about why a number moved — and say to thread those.
- Check whether the work belongs to an existing workstream instead; routing may be the better mode for recurring topics.

### Example: worrying that more context means a bigger bill
User: If it is now reading the whole channel, what does that do to our usage?
Assistant: Holding more context does increase usage, but per the announcement the additional context does not count toward usage or spend limits, and the update comes at no additional cost today. Budget for the behavior change, not for a context surcharge.

### Example: the channel is quiet for weeks at a time
User: We have a channel that goes dormant and then spikes.
Assistant: That is handled by default — inactive channels get less attention until the agent is mentioned. When the channel spikes, mention it once to bring it back in, and let the channel rubric take over from there.

# Knowing when to disengage

The update improves judgment about when *not* to respond as much as when to respond — roughly 30% better at determining when, and when not, to contribute proactively. Four mechanisms carry that.

## Channel-specific rubrics
Each channel gets a rubric that evaluates usefulness and confidence before the agent contributes. Tightening the rubric for one channel is the narrowest available fix for over-participation — it leaves behavior elsewhere untouched.

## Reduced attention to inactive channels
Channels that have gone quiet get less attention until the agent is explicitly mentioned. Dormant-then-spiky channels are handled by this without any configuration; mention the agent once when the channel wakes up.

## User controls to disable automatic responses
Automatic responses can be turned off, leaving mention-only behavior. This is the blunt instrument: correct when a channel genuinely wants the agent on call rather than participating, and too much when the channel mostly benefits from proactivity.

## Plain-language instructions
Behavior is customized with plain-language instructions rather than configuration syntax. This is how you adjust the threshold — narrowing scope, naming what should never draw a response — without switching proactivity off.

## Choosing a control
Work from narrowest to broadest:

1. Standing instruction naming the specific unwanted behavior
2. Tighter channel rubric
3. Automatic responses off for that channel

## Related
- [response-modes.md](response-modes.md) — what the agent chooses between when it does decide to act.
- [../templates/standing-instructions.md](../templates/standing-instructions.md) — a drafting template for the plain-language instructions.

## Source
- https://claude.com/blog/claude-tag-now-reads-even-more-of-the-room

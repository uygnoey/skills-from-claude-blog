# Standing instructions template

Behavior is customized with plain-language instructions. Fill this in per channel and give it to the agent as its standing instructions for that channel. Write in ordinary sentences — this is not a configuration file.

---

## Channel
`#____________`

## What this channel is for
_One or two sentences. What the people here are actually doing._

## What you should help with here
- _…_
- _…_

## What you should not touch here
- _…_
- _…_

## When to reply inline
_Describe what counts as short and verifiable in this channel. Example shape: "Answer inline when the question is about a single documented fact and you can point at the source."_

## When to open a thread instead
_Describe what counts as complex here. Example shape: "Open a thread for anything needing more than one source, or any question about why a number moved."_

## Existing workstreams to route to
| Topic | Route to |
| --- | --- |
| _…_ | _…_ |
| _…_ | _…_ |

## When to stay silent
_Be specific. Example shapes: "During an active incident, stay silent unless mentioned." "Never respond to messages that are only social." "If your confidence is low, say nothing rather than hedging."_

## Confidence and usefulness bar for this channel
_How high should the rubric be set here? A busy channel where people mostly talk to each other wants a higher bar than a help channel._

---

## Notes on tuning
- Start from the narrowest control. A standing instruction naming the unwanted behavior is preferable to tightening the whole rubric, which is preferable to turning automatic responses off.
- Inactive channels already get less attention until the agent is mentioned; you do not need an instruction for that.
- The agent acknowledges messages within seconds, so a slow-starting thread is not a sign it missed the message.

## Source
- https://claude.com/blog/claude-tag-now-reads-even-more-of-the-room

# Effort, model, and token consumption

How the two settings interact with cost depends on the task.

## Routine work, same effort level

Both models generally get it right. The larger model consumes more tokens on extra verification
steps, at a higher per-token price.

**That's why dropping to the smaller model for routine stretches saves real money at no quality
cost.**

## Harder, multi-step work

The equation flips. The smaller model has to grind toward the limit of its ability, burning
iterations, while the larger model reaches the same quality bar in fewer steps.

You're paying more per token for the larger model, but on tasks that genuinely stretch the smaller
one, **the total cost per task can come out lower**. More importantly, the larger model can
accomplish tasks the smaller one cannot — even at the highest effort settings.

This is most pronounced with **Fable**. On long, multi-step work it pulls furthest ahead; in
Anthropic's testing it finished jobs Opus and Sonnet can't reach at any effort level. It also
costs the most per token, which is the other reason to save it for the work that needs it.

> The source article illustrates both cases with curves that are explicitly for illustration only
> and do not represent real benchmark data.

## Effort shapes consumption; it does not cap it

**Effort level picks how far Claude is willing to travel along the curve** — but that doesn't mean
Claude will need to travel that far to complete the task.

The only hard cap in the system is **`max_tokens`**, which truncates a response mid-stream when
hit. It's a blunt instrument, mostly relevant to API developers.

Softer controls are more helpful:

- task budgets
- asking Claude to keep it brief in your prompt

These serve as **guidance the model is trained to follow** — it will look to conclude its tasks as
it gets near the limit — rather than a wall it runs into.

## Practical summary

| Situation | Move | Why |
|---|---|---|
| Long routine stretch on the larger model | Drop to the smaller model | Same result, fewer tokens, lower per-token price |
| Task genuinely stretches the smaller model | Move up | Fewer iterations; total cost per task can be lower |
| Task the smaller model cannot do at any effort | Move up | Capability, not thoroughness, is the limit |
| Output is longer than you want | Task budget or "keep it brief" in the prompt | Trained guidance beats a hard truncation |

## Source

["Choosing a Claude model and effort level in Claude Code"](https://claude.com/blog/claude-model-and-effort-level-in-claude-code)

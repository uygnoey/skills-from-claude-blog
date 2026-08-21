**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
Lydia Hallie, on the Claude Code team, explains the two settings that appear to "make the answer better" — the model and the effort level — by explaining what each one actually changes. The model setting swaps which set of frozen weights handles your request, and sets what each output token costs. The effort level, sent to the model as part of the request alongside your prompt, sets how thorough and certain Claude needs to be before it considers the task done: how long it thinks, how many files it reads, how much it verifies, and how far it pushes through a multi-step task before checking in with you.

The post walks the mechanics — tokenization, the weights, one-token-at-a-time generation, why steering with context isn't teaching, and why a hallucination is the weights producing a plausible-looking sequence rather than a failed lookup — and then turns them into a practical rule. When a result misses the mark, the first move is to check the context you provided. If context was clear and Claude was still wrong, ask whether it *didn't try hard enough* (raise effort) or *didn't know enough* (pick a larger model).

## When is it useful?
- When a Claude Code session produced a wrong or shallow result and the instinct is to reach for a dial.
- When choosing a standing effort preference for a team or a domain, rather than deciding task by task.
- When deciding whether a long routine stretch of work can drop to a smaller model without a quality hit.
- When explaining to colleagues why context in a prompt does not change what the model knows.
- When reasoning about cost: which of "more capable per token" and "fewer tokens overall" wins on a given task shape.
- When output is longer than you want and you're wondering whether `max_tokens` is the right lever (it usually isn't).

## Key points
- **Model selection chooses a set of fixed weights** — the model's overall capability range. Context steers the prediction; it doesn't add to the weights.
- **Effort is not just thinking time.** It controls how much work Claude does overall: files read, tools used, and how many steps it takes before checking back in with you.
- **Every kind of output is the same kind of token.** Thinking, tool calls, and text to you all come from the same loop and are billed at the same rate — and thinking stays in context for the rest of that turn, so it becomes input when Claude moves on to writing code.
- **Effort travels with the request.** The model was trained to understand each effort level, and that behavior is baked into the frozen weights. Same prompt, high effort: roughly 7× more tokens generated to reach a higher-confidence answer.
- **Plans get revised, not executed blindly.** If step 1 of a three-hypothesis debugging plan finds the bug, Claude typically says so and skips the rest. Higher effort doesn't artificially inflate usage on simple tasks — "overthinking" is watched closely in training because it degrades effectiveness.
- **Check the context before the dial.** If you're raising effort on a task that shouldn't need it, the fix is often upstream: the prompt, `CLAUDE.md`, tools, skills, or task scoping.
- **The diagnostic.** Skipped a file, didn't run the tests, bailed on a refactor → raise effort. Had the context, clearly tried, still confidently wrong → larger model.
- **Bigger isn't the default answer.** Routine, precisely describable work belongs on a smaller model; larger models earn their price on ambiguity, subtle bugs, unfamiliar domains, and architecture decisions.
- **Specialist / expert / generalist.** Fable is the specialist who's seen problems almost no one else has, Opus is the expert, Sonnet is a really good generalist — and effort decides how much time any of them spends. Model is roughly *how capable*; effort is roughly *how thorough*.
- **Cost flips by task shape.** Routine work at the same effort: the smaller model saves money at no quality cost. Harder multi-step work: the larger model reaches the bar in fewer steps, so total cost per task can come out lower — and it can finish tasks the smaller one can't at any effort.
- **Effort shapes token consumption but doesn't limit it.** The only hard cap is `max_tokens`, which truncates mid-stream. Task budgets and asking for brevity are trained guidance the model follows, not a wall.

## Bundled resources
- `skills/model-and-effort-selection/SKILL.md` — the decision procedure: defaults first, context before dials, then the "didn't try / didn't know" diagnostic.
- `skills/model-and-effort-selection/references/how-inference-works.md` — tokenization, weights, the generation loop, and why steering isn't teaching.
- `skills/model-and-effort-selection/references/effort-mechanics.md` — what effort controls, why thinking tokens are ordinary output tokens, and why plans get revised mid-run.
- `skills/model-and-effort-selection/references/model-tiers.md` — the specialist/expert/generalist framing and a table of which work fits which model.
- `skills/model-and-effort-selection/references/cost-and-tokens.md` — how cost flips between routine and hard multi-step work, and why `max_tokens` is the wrong lever.
- `skills/model-and-effort-selection/examples/choosing-in-practice.md` — seven worked scenarios mapping a symptom to the setting to change.
- `guides/model-and-effort-in-claude-code.{en,ko,es,ja}.md` — the full guide in four languages.

## Source
["Choosing a Claude model and effort level in Claude Code"](https://claude.com/blog/claude-model-and-effort-level-in-claude-code) by Lydia Hallie, member of technical staff on the Claude Code team — published July 7, 2026.

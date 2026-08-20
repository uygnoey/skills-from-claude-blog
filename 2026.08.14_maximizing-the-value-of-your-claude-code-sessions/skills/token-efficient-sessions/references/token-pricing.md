# What a token costs

Three things set the price of any given token in a Claude Code session: which model
processes it, whether it is an input or an output token, and whether it is read from the
prompt cache.

## 1. Model

Larger models do more work on every token, input and output alike, and are priced
accordingly. The practical rule is to match the model to the problem: reach for a larger
model on genuinely hard or ambiguous work, and a smaller one for routine changes. Set it
deliberately at the start of a session rather than inheriting whatever the last session
left behind.

## 2. Input versus output

A turn has two phases:

- **Prefill.** The model reads everything it has been given — the system prompt, tool
  definitions, `CLAUDE.md`, the conversation so far, and your new message. These are
  input tokens.
- **Decode.** The model writes its response one token at a time. These are output tokens,
  and they are the expensive ones — roughly 5× the input price.

Thinking tokens are output tokens, and the **effort level** controls how many of them get
produced. `/effort` is therefore a direct lever on the expensive half of the bill. For a
session where you want no thinking at all, `MAX_THINKING_TOKENS=0` steps below
`/effort low` (it does not apply to Fable 5).

## 3. Prompt caching

The cache is what makes long conversations affordable at all.

| Operation | Price relative to input |
|---|---|
| Cache read | ~0.1× |
| Cache write | up to 2×, paid once per token |
| Uncached input | 1× |

A token is written to the cache once and then read cheaply on every subsequent turn. This
is why re-sending a long conversation each turn is survivable — and why anything that
invalidates the cache is expensive, because the whole conversation has to be prefilled
again at full price.

### What breaks the cache

| Trigger | What happens |
|---|---|
| `/model` | Different model, different cache. The entire conversation re-prefills at full price. |
| `/effort` | Effort level is part of the cache key. Same full re-prefill. |
| Fast mode | Also part of the cache key. |
| `/compact` | Replaces the conversation with a summary; the system prompt survives. |
| Time | The cache expires after **1 hour** on a subscription, **5 minutes** on an API key. `ENABLE_PROMPT_CACHING_1H=1` extends the API-key case to an hour. |
| Resuming a session | The cache has usually expired; the system prompt is rebuilt at launch. |

### What does not break it

`/rewind` cuts turns off the end of the conversation and leaves everything before the cut
cached. It is the cheap way to back out of a wrong path. `/compact`, by contrast, rewrites
the conversation and always costs something — which is why the timing advice is to compact
*before* a break, while the cache is still warm, rather than after it has expired.

## Putting it together

The levers, in the order they appear on a bill:

1. Output tokens cost ~5× input, and effort level is the dial on them.
2. Cached input costs ~0.1× uncached input, so preserving the cache dominates almost every
   other micro-optimization.
3. Model choice multiplies both.

Set model and effort once at the start of a fresh session; after that, protecting the
cache is the main thing you control.

## Source

- https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions (August 14, 2026)

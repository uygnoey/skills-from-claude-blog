# Token levers and how they interact

The three levers from the source post, what each one changes, and what it does not.

## Lever 1 — Prompt caching

**Changes:** the cost and latency of resending a long, mostly-static prefix.

**Reported effect:** up to 90% cost reduction and up to 85% latency reduction for long prompts.

**How it is used:** set a cache breakpoint. The model automatically reads from the longest previously cached prefix, so the application does not have to track which prefix was cached most recently.

**What defeats it:** any variation early in the prompt. Timestamps, request IDs, non-deterministic ordering, or a rotating greeting placed before the static block will each invalidate the prefix.

**Does not help with:** output tokens, or context that genuinely differs every request.

## Lever 2 — Cache-aware rate limits

**Changes:** throughput, not the bill.

**Reported behaviour:** on the Anthropic API with Claude 3.7 Sonnet, cache read tokens no longer count against Input Tokens Per Minute (ITPM).

**Why it matters separately from lever 1:** an application can be paying little for a cached prefix while still being throttled as though it were sending the full prefix. Removing cache reads from ITPM lifts that ceiling.

**Depends on:** lever 1 actually working. If the prefix is not being cached, there are no cache reads to exclude.

**Verify before relying on it:** this is a per-model, per-platform property. Confirm it for the model and platform you target.

## Lever 3 — Token-efficient tool use

**Changes:** output token consumption in tool-calling workflows.

**Reported effect:** up to 70% reduction, averaging around 14%. In beta at the time of the post.

**Related tooling:** the `text_editor` tool supports targeted edits to parts of a text — code, documents — rather than regenerating the whole artifact. This matters most in loops, where whole-artifact regeneration multiplies output cost by iteration count.

**Does not help with:** input-heavy workloads with little tool use.

## Choosing between them

| Symptom | Lever |
|---|---|
| Bill dominated by input tokens on repeated context | 1 |
| Hitting ITPM limits despite caching being enabled | 2 |
| Bill dominated by output tokens in an agent loop | 3 |
| Latency spikes on long prompts | 1 |
| Whole files regenerated for small edits | 3 |

## Diagnostic order

1. Split a representative request into static context, variable context, and output.
2. If static context dominates, apply lever 1 and confirm via the cache read/write ratio.
3. If throughput is still limited, check whether lever 2 applies to your model and platform.
4. If output dominates, apply lever 3 and prefer targeted-edit tools over regeneration.

## Source

- https://claude.com/blog/token-saving-updates

---
name: reduce-token-usage
description: Cut cost, latency, and rate-limit pressure in an API application by applying prompt caching, cache-aware rate limits, and token-efficient tool use. Use when an application repeatedly sends long mostly-static context such as documents, codebase excerpts, or policies; when input-token rate limits are the throughput bottleneck; or when tool-calling workflows emit large outputs.
---

# Reduce token usage

Three levers, in the order worth pulling them: stop re-paying for context that does not change, stop letting cached reads consume your input rate limit, and stop emitting output tokens you did not need.

## Instructions

### 1. Find out where the tokens actually go

Before changing anything, split a representative request into three buckets:

- **Static context** — system prompt, tool definitions, documents, policies, code excerpts that are identical across requests.
- **Variable context** — conversation history, retrieved passages, per-request data.
- **Output** — what the model generates, including tool-call arguments and results.

The lever you need follows directly from which bucket dominates. Optimizing the wrong bucket is the usual reason a token-reduction effort produces no measurable change.

### 2. Apply prompt caching to the static prefix

Prompt caching is the largest single lever for applications that resend long, mostly-static context. The reported effect for long prompts is a cost reduction of up to 90% and a latency reduction of up to 85%.

The mechanics that matter when structuring a prompt:

- **Order matters.** Put the static material first and the variable material last, so the unchanging prefix is as long as possible. A single variable token near the front invalidates everything after it.
- **Set a cache breakpoint** and the model automatically reads from the longest previously cached prefix. You do not have to track which prefix was cached last.
- **Stability beats cleverness.** A prompt assembled in a deterministic order caches; one assembled from an unordered map does not.

See [references/token-levers.md](references/token-levers.md) for how the three levers interact.

### 3. Check whether cache reads still count against your rate limit

Cache-aware rate limiting is the lever people miss, because it changes throughput rather than the bill.

On the Anthropic API with Claude 3.7 Sonnet, cache read tokens no longer count against Input Tokens Per Minute (ITPM). For an application whose bottleneck was ITPM on a large repeated prefix, this can raise throughput without any change to the prompt beyond enabling caching.

Confirm the current behaviour for the model and platform you actually target before planning capacity around it — this is a per-model, per-platform property, not a universal one.

### 4. Reduce output tokens in tool-calling workflows

Token-efficient tool use, introduced in beta, reduces output token consumption — reported as up to 70%, averaging around 14%.

Separately, prefer tools that express **targeted edits** over tools that regenerate whole artifacts. The `text_editor` tool supports editing parts of a text such as code or a document, rather than rewriting it wholesale. A workflow that rewrites a 500-line file to change 3 lines pays for 500 lines of output on every iteration.

### 5. Measure, do not assume

For each change, record before and after:

| Metric | Why |
|---|---|
| Input tokens per request | Confirms the prefix is actually being cached |
| Cache read vs cache write tokens | A high write ratio means the prefix is unstable |
| Output tokens per request | The tool-use lever shows up here |
| End-to-end latency, p50 and p95 | Caching gains appear at the tail |
| Rate-limit rejections | The cache-aware limit lever shows up here |

A caching change that does not move the cache-read ratio is not working, regardless of what the bill does next month.

## Examples

### Example 1: a document-grounded assistant

An application sends a 40-page policy document plus a short user question on every request.

1. Restructure the prompt so the document and system instructions come first, the user question last.
2. Set a cache breakpoint after the static block.
3. Verify cache read tokens dominate cache write tokens after the first few requests.
4. Observe that cache reads no longer count against ITPM, so the concurrency ceiling rises.

The user question changing every request costs nothing, because it sits after the cached prefix.

### Example 2: a code-editing agent

An agent loops over a file, making small changes.

- **Before:** each turn regenerates the whole file. Output tokens scale with file size times iteration count.
- **After:** the agent uses a text-editing tool that applies targeted edits. Output scales with the size of the change instead.

Combine with token-efficient tool use to cut the remaining tool-call overhead.

### Example 3: a caching change that does nothing

A team enables caching but assembles the system prompt by iterating a dictionary, so key order varies between processes. Every request produces a cache write and no cache reads.

The fix is not more caching configuration — it is making prompt assembly deterministic. Check the cache read/write ratio first whenever caching appears to have no effect.

## Notes

- The specific percentages and the ITPM behaviour cited here come from the source post and applied to Claude 3.7 Sonnet on the Anthropic API at that time. Verify current limits, model support, and beta status in the platform documentation before relying on them.
- Token-efficient tool use was in beta at the time of the post.
- These levers compose: caching reduces what you pay for input, cache-aware limits raise how much input you may send, and tool-use efficiency reduces what you pay for output.

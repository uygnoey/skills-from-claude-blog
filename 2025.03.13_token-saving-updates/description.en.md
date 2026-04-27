**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
This post announces updates to the Anthropic API focused on reducing token usage and improving throughput with Claude 3.7 Sonnet: cache-aware rate limits, simpler prompt caching behavior, and token-efficient tool use (including a new `text_editor` tool).

## When is it useful?
- When your app repeatedly sends long, mostly-static context (docs, codebase excerpts, policies) and you want lower cost and latency.
- When you are rate-limit constrained on input tokens and want higher throughput with prompt caching.
- When your tool-calling workflows generate large outputs and you want to reduce output tokens.

## Key points
- Prompt caching can reduce costs (up to 90%) and latency (up to 85%) for long prompts.
- Cache read tokens no longer count against Input Tokens Per Minute (ITPM) for Claude 3.7 Sonnet on the Anthropic API.
- Prompt caching is easier: set a cache breakpoint and Claude automatically reads from the longest previously cached prefix.
- Token-efficient tool use (beta) can reduce output token consumption (up to 70%, ~14% average).
- The new `text_editor` tool supports targeted edits to parts of text (e.g., code, documents), helping reduce tokens and latency.

## Bundled resources
- None (announcement post).

## Source
- https://claude.com/blog/token-saving-updates

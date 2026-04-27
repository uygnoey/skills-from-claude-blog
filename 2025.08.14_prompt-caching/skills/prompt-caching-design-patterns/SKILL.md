---
name: prompt-caching-design-patterns
description: Decide when prompt caching helps, structure prompts so the cacheable prefix and dynamic suffix are cleanly separated, estimate cost and latency wins from the benchmarks reported in Anthropic's launch post, and pick the right Claude model among those that support caching.
---

# Prompt caching design patterns

Anthropic launched prompt caching in public beta on August 14, 2025. It lets API callers reuse frequently used context across calls, with reported reductions of up to 90% in cost and 85% in latency on long prompts. This skill collects the post's guidance into actionable design rules for shaping prompts that benefit from caching.

Prompt caching is supported on Claude 3.5 Sonnet, Claude 3 Opus, and Claude 3 Haiku at launch (per the post). A December 17, 2024 update referenced in the same post notes general availability on the Anthropic API and preview availability on Amazon Bedrock and Google Cloud's Vertex AI.

## Instructions

Apply these rules when you are deciding whether to use prompt caching and when you are restructuring a prompt to make it cache-friendly.

### 1. Confirm the workload matches a use case from the post

Prompt caching pays off when the same large block of context is sent over and over. The launch post calls out these use cases:

- Conversational agents that need to keep long instructions or uploaded documents available across turns.
- Coding assistants that keep a summarized version of the codebase in the prompt.
- Large document processing where the document is fixed and the question changes.
- Detailed instruction sets containing dozens of high-quality examples (many-shot prompting).
- Agentic search and tool use over many iterations.
- "Talk to" experiences over books, papers, documentation, podcast transcripts, and similar long-form corpora.

If the workload does not look like one of the above, do not assume caching helps. The post does not promise wins outside these patterns.

The verbatim use case list and the benchmark numbers behind them are kept in [references/use-cases-and-benchmarks.md](./references/use-cases-and-benchmarks.md).

### 2. Split the prompt into a cacheable prefix and a dynamic suffix

The mental model from the post is: cache the part that does not change, vary only the tail.

- Put the system prompt, persistent instructions, retrieved documents, conversation history snapshot, or many-shot examples in the prefix. This is the part you mark for caching.
- Put the new user message, the latest tool result, or the changing slot variables in the suffix. This is the part that varies per call.

Concrete shapes for these prefixes and suffixes are in [examples/prompt-structure-patterns.md](./examples/prompt-structure-patterns.md).

### 3. Estimate the win from the benchmark table before building

The post publishes a benchmark table for three flagship scenarios. Use it as the back-of-the-envelope reference, not your own guesses.

- Chat with a 100,000-token book: time-to-first-token drops from 11.5 seconds to 2.4 seconds (-79%) and cost drops by 90%.
- Many-shot prompting with about 10,000 tokens of examples: latency drops 31% and cost drops 86%.
- 10-turn conversation with a long system prompt: latency drops about 75% and cost drops 53%.

Match your workload to the closest row. If your prompt is much shorter than 10,000 tokens or your reuse rate is low, expect smaller wins than the headline 90% number.

### 4. Apply the pricing math the post gives

The post states two adjustments versus base input pricing:

- Cache write: base input price multiplied by 1.25.
- Cache read: base input price multiplied by 0.10.

The break-even point therefore depends on how many times the cached prefix is read after a single write. The full pricing note plus the benchmark table are reproduced verbatim in [references/use-cases-and-benchmarks.md](./references/use-cases-and-benchmarks.md).

### 5. Pick a supported model and platform

The post lists Claude 3.5 Sonnet, Claude 3 Opus, and Claude 3 Haiku as the launch surface. The December 17, 2024 update notes general availability on the Anthropic API and preview availability on Amazon Bedrock and Google Cloud's Vertex AI. Do not assume support on models or platforms not listed in the post.

### 6. Treat the Notion testimonial as the social proof, not a feature claim

Simon Last, Co-founder of Notion, is quoted in the post: "We're excited to use prompt caching to make Notion AI faster and cheaper, all while maintaining state-of-the-art quality." Use this as evidence that real production teams are adopting the feature. It is not a substitute for measuring your own workload.

## Examples

### Example A: Talk-to-book chatbot

A reading-companion app loads a 100,000-token book and lets the user ask repeated questions.

- Prefix to cache: system instructions, the entire book text, any persona description.
- Dynamic suffix: the user's current question and the recent chat turns.
- Expected win: closest to the post's 100k chat-with-book row, so plan around the 2.4-second time-to-first-token and 90% cost reduction figures rather than guessing.

A worked-out prefix/suffix layout is in [examples/prompt-structure-patterns.md](./examples/prompt-structure-patterns.md).

### Example B: Many-shot classifier

A support triage prompt carries dozens of labeled examples plus the new ticket.

- Prefix to cache: the role description and the example block.
- Dynamic suffix: the new ticket text.
- Expected win: closest to the 10k-token many-shot row, so plan around 31% latency reduction and 86% cost reduction.

### Example C: Long-context coding assistant

A coding agent summarizes the repo into a system prompt and answers iterative questions.

- Prefix to cache: the codebase summary plus persistent style and review rules.
- Dynamic suffix: the latest user request and tool outputs.
- Expected win: closest to the 10-turn long system prompt row, so plan around 75% latency reduction and 53% cost reduction.

For the full quoted use-case list and benchmark table that back these expectations, see [references/use-cases-and-benchmarks.md](./references/use-cases-and-benchmarks.md).

## Source

Prompt caching with Claude — Anthropic, August 14, 2025: <https://www.anthropic.com/news/prompt-caching>

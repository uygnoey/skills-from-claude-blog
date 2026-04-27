**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Prompt caching with Claude

## What is this post?

The launch announcement for prompt caching on the Anthropic API. The post explains when prompt caching pays off, the model lineup at launch (Claude 3.5 Sonnet, Claude 3 Opus, Claude 3 Haiku), the published latency / cost reductions on three reference workloads, the pricing model (cache writes cost +25% over base input; cached reads cost 10% of base input), and a Notion customer spotlight. A December 17, 2024 update note moves prompt caching to **Generally Available** on the Anthropic API and to **preview** on Amazon Bedrock and Google Cloud Vertex AI.

## When useful

- Deciding whether prompt caching is the right lever for an existing Claude integration (vs. shorter prompts, streaming, batching, or model swaps).
- Estimating the latency / cost win on workloads similar to the post's three benchmarks before committing engineering time.
- Designing a prompt structure that maximizes cache hits — what to put in the cached prefix vs. what to keep dynamic.
- Citing the published numbers (up to 90% cost reduction, 85% latency reduction on long prompts; 79% TTFT improvement on a 100k-token "chat with a book" workload).

## Key points

- Prompt caching lets developers cache frequently used context between API calls. Use it when you send a large amount of context once and reference it repeatedly.
- Headline claims: up to **90% cost reduction** and up to **85% latency reduction** for long prompts. Available at launch on Claude 3.5 Sonnet, Claude 3 Opus, Claude 3 Haiku (in public beta at the original post; GA per the December 17, 2024 update).
- Use cases the post enumerates: conversational agents, coding assistants, large document processing, detailed instruction sets (with dozens of high-quality examples), agentic search and tool use, and "talk to" experiences over books / papers / docs / podcasts.
- Reference workload numbers from the post:
  - Chat with a book (100,000-token cached prompt): TTFT 11.5s → 2.4s (-79%); cost -90%.
  - Many-shot prompting (10,000-token prompt): TTFT 1.6s → 1.1s (-31%); cost -86%.
  - Multi-turn conversation (10-turn convo with a long system prompt): TTFT ~10s → ~2.5s (-75%); cost -53%.
- Pricing model: writing to the cache costs **25% more** than the base input token price for that model; reading from the cache costs **10%** of the base input token price.
- Customer spotlight: Notion adopted prompt caching for Notion AI to optimize internal operations and improve responsiveness. Quote attributed to Simon Last (Co-founder, Notion): "We're excited to use prompt caching to make Notion AI faster and cheaper, all while maintaining state-of-the-art quality."
- December 17, 2024 update: prompt caching is **GA** on the Anthropic API and available in **preview** on Amazon Bedrock and Google Cloud Vertex AI.

## Bundled resources

- [skills/prompt-caching-design-patterns/SKILL.md](./skills/prompt-caching-design-patterns/SKILL.md): when to use, how to structure prompts for cache hits, how to size the win.
- [references/use-cases-and-benchmarks.md](./skills/prompt-caching-design-patterns/references/use-cases-and-benchmarks.md): the launch use-case list and reference workload table verbatim.
- [examples/prompt-structure-patterns.md](./skills/prompt-caching-design-patterns/examples/prompt-structure-patterns.md): cached-prefix vs. dynamic-suffix patterns derived from the post's use cases.

## Source

Distilled from [Prompt caching with Claude](https://claude.com/blog/prompt-caching) (published 2025-08-14; updated December 17, 2024 noting GA on Anthropic API + preview on Bedrock and Vertex AI).

# Use cases, benchmarks, and pricing for prompt caching

This reference reproduces the launch-post details that the SKILL relies on. Numbers and bullets are quoted from the August 14, 2025 announcement.

## Use cases listed in the post

Prompt caching is described as useful for situations where you want to send a large amount of prompt context once and refer to it repeatedly. The post calls out:

- Conversational agents — keep long instructions or uploaded documents available across turns to reduce cost and latency for extended conversations.
- Coding assistants — improve autocomplete and codebase question-answering by keeping a summarized version of the codebase in the prompt.
- Large document processing — embed full long-form material (including images) in the prompt without increasing response latency.
- Detailed instruction sets — share extensive lists of instructions, procedures, and examples to fine-tune Claude's responses, including dozens of high-quality examples (many-shot prompting).
- Agentic search and tool use — boost performance for scenarios that involve many iterations of tool calls and changes that traditionally require new API calls each time.
- Talk to books, papers, documentation, podcast transcripts, and other long-form content — bring any knowledge base alive by embedding the entire documents into the prompt and letting users ask questions.

## Benchmark table from the post

The post publishes a comparison table summarizing three flagship scenarios. The values below match the post.

| Use case | Latency without caching (time to first token) | Latency with caching (time to first token) | Cost reduction |
| --- | --- | --- | --- |
| Chat with a book (100,000 cached tokens) | 11.5s | 2.4s (-79%) | -90% |
| Many-shot prompting (10,000 cached tokens) | 1.6s | 1.1s (-31%) | -86% |
| Multi-turn conversation (10-turn convo with a long system prompt) | ~10s | ~2.5s (-75%) | -53% |

The post highlights the same numbers in prose: up to 90% cost reduction and up to 85% latency reduction on long prompts.

## Pricing rules from the post

Cached prompts are priced based on how many input tokens are cached and how often the cache is read.

- Writing to the cache costs 25% more than the base input token price for that model.
- Reading from the cache is significantly cheaper: 10% of the base input token price.

In other words, cache write is base input × 1.25 and cache read is base input × 0.10.

## Models and platforms named in the post

- Public beta on the Anthropic API at launch: Claude 3.5 Sonnet, Claude 3 Opus, and Claude 3 Haiku. Support for Claude 3 Opus is described as "coming soon."
- December 17, 2024 update referenced in the post: prompt caching is generally available on the Anthropic API and in preview on Amazon Bedrock and Google Cloud's Vertex AI.

## Customer spotlight from the post

Notion is featured as a launch customer. Simon Last, Co-founder of Notion, is quoted:

> "We're excited to use prompt caching to make Notion AI faster and cheaper, all while maintaining state-of-the-art quality. By making this huge improvement to Notion AI's reasoning and processing capabilities, we will produce better results for users while keeping our software fast and inexpensive."

## Source

Prompt caching with Claude — Anthropic, August 14, 2025: <https://www.anthropic.com/news/prompt-caching>

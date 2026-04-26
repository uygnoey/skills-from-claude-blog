[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Introducing the Message Batches API

## ¿De qué trata este post?
This post introduces the Message Batches API, which lets you submit up to 10,000 message requests asynchronously for completion within 24 hours at a 50% token discount.

## ¿Cuándo es útil?
Useful for non-time-sensitive, high-volume workloads (dataset analysis, large-scale classification, translation, evaluations) where you want higher throughput without building your own queuing system.

## Puntos clave
- A batch can include up to 10,000 queries and is processed within 24 hours (often faster).
- Batched requests are priced at a 50% discount for both input and output tokens compared to standard calls.
- Batch processing provides enhanced throughput with higher rate limits without impacting standard API rate limits.
- The post frames the Batches API as a way to avoid managing complex queues/rate-limit handling for large jobs.
- At the time of the post, it supports Claude 3.5 Sonnet, Claude 3 Opus, and Claude 3 Haiku on the Anthropic API.

## Recursos incluidos
- No bundled code samples are included in the post; it points readers to Anthropic documentation and pricing pages.

## Fuente
- https://claude.com/blog/message-batches-api

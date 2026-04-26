---
name: message-batches-job-design
description: A reusable checklist for deciding when and how to use the Anthropic Message Batches API for asynchronous, high-volume processing at reduced cost.
---

# message-batches-job-design

## Instructions

- Use the Message Batches API when work is not time-sensitive and you can wait up to 24 hours for completion.        - Design each batch for high volume (up to 10,000 queries) and plan for asynchronous retrieval of results.        - Use batching to reduce cost (50% discount on input and output tokens) and to increase throughput without consuming standard API rate limits.        - Prefer batching for large-scale analysis/classification/translation/evaluation workloads where you would otherwise build complex queueing.

## Examples

- "We need to classify 2 million support tickets into 20 labels over the weekend—use the Batches API design checklist."        - "Translate a large set of product descriptions where same-day delivery is fine; estimate cost savings vs standard calls."        - "Run an offline model evaluation suite with 8,000 prompts; plan the batch submission and result download flow."
## Source

- https://claude.com/blog/message-batches-api

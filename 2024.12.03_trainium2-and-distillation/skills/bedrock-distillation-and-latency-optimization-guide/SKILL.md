---
name: bedrock-distillation-and-latency-optimization-guide
description: Decision checklist for using latency-optimized Claude 3.5 Haiku on AWS Trainium2 and Amazon Bedrock Model Distillation for Claude 3 Haiku, based on the official announcement.
---

## Instructions
Use this skill when choosing an AWS deployment and model strategy for Claude workloads described in the post.

1. **Choose between speed optimization vs. distillation**
   - Use *latency-optimized inference* when you need faster responses for interactive workloads.
   - Use *model distillation* when you have high-volume, repetitive tasks where a smaller model can be specialized to approach a larger model’s task accuracy.

2. **Map your workload to the post’s distillation workflow**
   - Generate synthetic training data (from the teacher model).
   - Train and evaluate the student model.
   - Host the final distilled model for inference.

3. **Validate operational constraints**
   - Confirm the AWS region and availability approach described for the faster inference option.
   - Track cost, latency, and quality tradeoffs for your specific task.

See the [distillation workflow reference](./references/distillation-workflow.md) for the exact steps as presented.

## Examples
- Real-time moderation: choose latency-optimized inference for lower end-to-end latency.
- RAG or analytics at scale: use distillation when a high-volume task benefits from improved quality at the smaller-model price point.

## Source
- https://claude.com/blog/trainium2-and-distillation

**English** · [한국어](./claude-platform-on-aws-vs-bedrock.ko.md) · [Español](./claude-platform-on-aws-vs-bedrock.es.md) · [日本語](./claude-platform-on-aws-vs-bedrock.ja.md)

# Claude Platform on AWS vs Claude on Amazon Bedrock

## What this guide covers

A short decision guide for choosing between:

- **Claude Platform on AWS** (Anthropic-operated platform accessed via AWS entry points)
- **Claude on Amazon Bedrock** (AWS-managed service within the AWS boundary)

## Decision checklist

### Choose Claude Platform on AWS when

- You want access to Anthropic’s native Claude Platform experience via AWS IAM, billing, and CloudTrail.
- Your requirements allow customer data to be processed by Anthropic outside the AWS boundary.

### Choose Claude on Amazon Bedrock when

- You require data to remain within AWS infrastructure.
- You prefer AWS-managed features and broader model selection within a single AWS service.

## Source

- https://claude.com/blog/claude-platform-on-aws

# Data boundaries: Claude Platform on AWS vs Claude on Amazon Bedrock

This note captures a key distinction mentioned in the source materials.

## Claude Platform on AWS

- Claude Platform on AWS provides access to Anthropic’s first-party Claude Platform via AWS entry points (IAM, consolidated billing, and CloudTrail).
- **Customer data is processed by Anthropic outside the AWS boundary.**

## Claude on Amazon Bedrock

- Claude on Amazon Bedrock keeps data within AWS infrastructure.

## Sources

- Claude blog post: https://claude.com/blog/claude-platform-on-aws
- AWS overview page: https://aws.amazon.com/claude-platform/

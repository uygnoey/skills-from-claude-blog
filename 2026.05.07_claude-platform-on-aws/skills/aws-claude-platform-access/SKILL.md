---
name: aws-platform-access
description: Evaluate and plan how to access Anthropic's platform through AWS entry points (IAM, billing, and CloudTrail), and document the key differences versus Claude on Amazon Bedrock.
---

## Instructions

Use this skill when you need a **deployment-ready checklist** for adopting *Platform on AWS* (Anthropic-operated, AWS-integrated) and clarifying how it differs from *Claude on Amazon Bedrock*.

### 1) Clarify which offering you are adopting

Document the intended offering explicitly:

- **Claude Platform on AWS**: Anthropic-operated platform accessed via AWS entry points (IAM, billing, CloudTrail).
- **Claude on Amazon Bedrock**: AWS-managed service for accessing Claude models within the AWS boundary.

Record your selection and the rationale in `templates/adoption-notes.md`.

### 2) Identity & access planning (IAM)

- Identify who needs access (developers, CI, service accounts).
- Define IAM policy boundaries using least privilege.
- If your org uses tags for authorization, document tag strategy and required tags.

Capture decisions in `templates/iam-checklist.md`.

### 3) Billing & cost attribution

- Decide which AWS accounts/OUs will be allowed to use the offering.
- Decide how you will attribute costs (linked account, cost allocation tags, chargeback model).

Capture decisions in `templates/billing-checklist.md`.

### 4) Audit & monitoring (CloudTrail)

- Confirm CloudTrail is enabled where required.
- Define where events should land (centralized logging account/SIEM).
- Define alerting for risky events (e.g., unexpected access from non-prod accounts).

Capture decisions in `templates/audit-checklist.md`.

### 5) Data boundary decision (critical)

Ensure stakeholders understand:

- For **Claude Platform on AWS**, customer data is processed by Anthropic **outside the AWS boundary**.
- For **Claude on Amazon Bedrock**, the service keeps data within AWS infrastructure.

Use `references/data-boundaries.md` as the canonical note for this distinction.

## Examples

### Example: Minimal adoption notes

See `templates/adoption-notes.md`.

### Example: Review checklist bundle

1. Fill `templates/iam-checklist.md`
2. Fill `templates/billing-checklist.md`
3. Fill `templates/audit-checklist.md`
4. Add a short summary in `templates/adoption-notes.md`

## Source

- Claude blog post: https://claude.com/blog/claude-platform-on-aws
- AWS overview page (used to cross-check terminology): https://aws.amazon.com/claude-platform/

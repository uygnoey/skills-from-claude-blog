**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
An announcement from October 23, 2026: the unified chat + Cowork experience, launched for Pro and Max in
September, is now generally available for Claude Enterprise. It covers what users get, how the experience
is secured, how admins manage cost, and how to get started.

## When is it useful?
- You are an Enterprise admin planning to enable the unified experience.
- Security or finance needs answers on cloud sessions, data handling, and spend before rollout.

## Key points
- One Claude on web, desktop, and mobile. Conversations start as chats; tasks that need code or file work
  continue in the cloud and return a finished document, analysis, or deck. Work keeps running after the
  laptop closes. Chats, projects, connectors, skills, and plugins carry over.
- Security: builds on SSO and the Compliance API; encryption in transit and at rest; no training by
  default; one isolated VM per cloud session; network egress off by default; connector credentials kept
  outside the sandbox; central visibility for security teams.
- Cost: usage-based pricing. Opus 5.5 costs 40% less than Opus 5 on typical workloads, Sonnet 5.5 up to 30%
  less than Sonnet 5. Admin controls: efficient mode, model entitlements, spend limits (org/group/member),
  and pooled group budgets.
- Rollout is managed in Organization settings. Organizations with zero data retention for Claude Code,
  a HIPAA-ready configuration, or customer-managed keys stay on their current configuration.

## Bundled resources
- Skill: `enterprise-unified-rollout` (`references/security-posture.md`, `references/cost-controls.md`,
  `templates/rollout-checklist.md`).

## Source
- https://claude.com/resources/articles/unified-claude-enterprise

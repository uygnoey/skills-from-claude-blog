**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Claude Security is now in public beta

## What is this post?

Anthropic's April 30, 2026 announcement opens Claude Security — previously known as Claude Code Security — to all Claude Enterprise customers in public beta. The product uses Claude Opus 4.7 to scan codebases, generate targeted patches, and route findings into existing security workflows. Access for Claude Team and Max customers is described as "coming soon." The post details how scans work, what changed since the limited research preview, the named technology and services partners, and customer testimonials.

## When useful

- You are a Claude Enterprise customer evaluating whether to roll out Claude Security across your codebases.
- You need to plan scan cadence, scope (repository, directory, branch), and how findings will flow into Slack, Jira, audit systems, or your vulnerability management program.
- You want to compare adoption paths: directly via `claude.ai/security`, embedded in a partner platform (CrowdStrike, Microsoft Security, Palo Alto Networks, SentinelOne, Trend.ai, Wiz), or with a services partner (Accenture, BCG, Deloitte, Infosys, PwC).
- You want to understand the dismiss-with-reason and confidence-rating workflow before sharing findings with engineering teams.

## Key points

- Claude Security is in public beta for Claude Enterprise customers; access for Claude Team and Max customers is coming soon.
- It is powered by Claude Opus 4.7 and accessed from the Claude.ai sidebar or `claude.ai/security` — no API integration or custom agent build required.
- Scans can be scoped to a repository, a specific directory, or a branch.
- Claude reasons about code like a security researcher: tracing data flows and how components interact across files and modules, instead of pattern-matching known signatures.
- Each finding includes a confidence rating, severity, likely impact, reproduction steps, and a targeted patch users can open in Claude Code on the Web.
- Improvements since limited preview: scheduled scans, target-by-directory, dismiss-with-documented-reason, CSV/Markdown export, and webhooks to Slack, Jira, and other tools.
- Technology partners embedding Opus 4.7: CrowdStrike, Microsoft Security, Palo Alto Networks, SentinelOne, Trend.ai, Wiz.
- Services partners: Accenture, BCG, Deloitte, Infosys, PwC.
- Customer testimonials in the post: DoorDash, plus quotes from a Staff Product Security Engineer, an Information Security Officer, a Head of Security, and another Head of Security.
- Claude Opus 4.7 ships with new cyber safeguards; organizations whose work may trigger them can join the Cyber Verification Program.

## Bundled resources

- Skill: `skills/security-public-beta-rollout-guide/SKILL.md` — when to use Claude Security, how to scope scans, how to interpret findings, and which adoption path (direct / partner platform / services partner) fits your org.
- Reference: `skills/security-public-beta-rollout-guide/references/features-and-partners-from-post.md` — verbatim summary of features, scan workflow, partners, and customer quotes.
- Examples: `skills/security-public-beta-rollout-guide/examples/scan-and-triage-workflows.md` — illustrative scoping, scheduling, and triage workflows derived from the post.

## Source

Claude Security is now in public beta — Anthropic, April 30, 2026: <https://claude.com/blog/claude-security-public-beta>

**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
An update to Claude Security, now in public beta for Claude Enterprise. Instead of waiting for
someone to start a scan, it keeps up with repositories as code changes, tracks which findings get
fixed, and uses what the team tells it about its environment to decide what matters.

## When is it useful?
- When an Enterprise security team wants scanning that stays current without scheduling.
- When findings need team context (deployment, policies, risk policy) to be prioritized well.
- When engineers want to triage and fix findings in Claude Code or pipe them into existing tools.

## Key points
- Continuous monitoring: deep baseline scan, then regular scans of changes based on risk and
  complexity. Repos connect via the Claude GitHub app (incl. GitHub Enterprise Server) or a GitLab /
  other Git provider token; a project can span several repos to catch cross-service issues.
- Fix tracking: findings are marked fixed when the fix lands (in Claude Code or elsewhere) and reopen
  automatically if the issue reappears.
- Per-project knowledge base plus a generated, editable threat model that later scans use to decide
  what to flag and what to skip.
- Each finding has a severity judged against the threat model and an attack-path explanation,
  sometimes with a diagram.
- API (projects, findings, resolve/reopen, repo management), personal access tokens scoped to the
  user, webhooks for new findings, and an MCP connector in Claude.ai and Claude Code.
- Role-based access: view projects, triage findings, create projects.
- Runs on the full model family including Claude Mythos; no Cyber Verification Program access needed.
  $25,000 in free monthly usage credits for two months (usage through Dec 31, 2026; see Help Center).

## Bundled resources
- Skill: `continuous-security-scanning` — enablement, roles, projects, knowledge base, threat model,
  triage, fix tracking, integrations (`references/feature-reference.md`,
  `templates/project-knowledge-base.md`).

## Source
- https://claude.com/resources/articles/claude-security-now-scans-continuously-and-tracks-fixes

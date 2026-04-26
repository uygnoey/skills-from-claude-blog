---
name: connected-tools-research-playbook
description: Use Claude's Integrations and advanced Research together to pull context from your work apps and produce comprehensive cited reports. Apply when deciding which third-party app to connect via remote MCP servers, when planning multi-source investigations that span the web, Google Workspace, and connected services, or when standardizing how a team uses Integrations + Research instead of building bespoke automation.
---

## Instructions

This Skill operationalizes the workflow described in "Claude can now connect to your world" (Claude blog, 2025-05-01; updated 2025-06-03). Integrations connect Claude to remote MCP servers; advanced Research breaks a request into sub-investigations across hundreds of sources and returns a cited report in 5–45 minutes.

Do not invent capabilities the post does not describe. Cross-check feature availability against the [launch-services reference](./references/launch-services.md) and the post itself.

### When to reach for Integrations

- Claude needs deep context about your work — project history, task status, organizational knowledge — that lives in a third-party app.
- You want Claude to take actions (create tasks, file bugs, post messages, query data) instead of only reading.
- A bespoke automation would otherwise require glue code, OAuth handling, and webhook plumbing — Cloudflare-hosted MCP servers handle this in as little as 30 minutes for new Integrations.

If none of the above applies and you only need a one-off lookup, plain Claude.ai (with web search if relevant) is sufficient.

### Picking which Integration to enable

Use the [launch-services reference](./references/launch-services.md) to confirm what was available and review the [example-workflows](./examples/example-workflows.md) for patterns the post highlights:

- **Zapier** — gateway to thousands of apps via pre-built workflows. Useful when no first-party Integration exists; e.g. pull HubSpot sales data, prepare meeting briefs from your calendar.
- **Atlassian Jira + Confluence** — collaborative product planning, bulk Confluence/Jira updates, summarizing across spaces.
- **Intercom** — Intercom's AI agent Fin, now an MCP client, can file Linear bugs from user reports. Use Claude to identify patterns across Intercom conversation history and user attributes.
- **Linear** — bug/issue management surface that pairs naturally with Intercom-driven workflows.
- **Cloudflare, PayPal, Plaid, Sentry, Square, Asana** — additional launch-day options for ops, finance, monitoring, and project tracking.

When evaluating a candidate, list (a) which Claude tasks need access to that data, (b) what actions Claude must take, (c) the auth model your org allows. If a service is not in the launch lineup, check whether the roadmap (Stripe, GitLab, Box) covered it before building bespoke.

### Combining Integrations with advanced Research

Toggle on the **Research** button to enable advanced Research. Claude will:

1. Break the request into smaller sub-investigations.
2. Search across the web, Google Workspace, and any connected Integrations.
3. Return a cited report — typically 5–15 minutes, up to 45 minutes for complex investigations.

Plan a research request like a brief: name the question, the scope, and the specific apps Claude should search. Citations link back to the original material — verify those before relying on a finding for downstream decisions.

### Availability

- Launch (2025-05-01): Integrations and advanced Research were beta on **Max, Team, Enterprise**. Web search was global for paid plans.
- Update (2025-06-03): Integrations and Research available on **Pro, Max, Team, Enterprise**. Web search global on **all** Claude plans.

When this Skill is consulted, treat the post as the source of truth for the launch lineup and roadmap; verify current availability against Anthropic's docs before depending on a specific service.

## Examples

See [examples/example-workflows.md](./examples/example-workflows.md) for the verbatim workflow patterns the post highlights — Zapier-driven HubSpot/calendar usage, Atlassian product planning, Intercom + Linear bug filing via the Fin AI agent — together with the expected research workflow timing.

## Source

Distilled from [Claude can now connect to your world](https://claude.com/blog/integrations) (published 2025-05-01, updated 2025-06-03).

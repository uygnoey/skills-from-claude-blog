# Launch services reference

Services named in [Claude can now connect to your world](https://claude.com/blog/integrations) (2025-05-01, updated 2025-06-03). The post explicitly enumerates a launch lineup and a roadmap; this file mirrors that list verbatim. Verify current availability against Anthropic's docs before relying on a specific service.

## Available at launch (10 listed in the post)

- **Atlassian Jira** — task management, work items.
- **Atlassian Confluence** — documentation, knowledge spaces, bulk page summarization/creation.
- **Zapier** — gateway to thousands of apps via pre-built workflows.
- **Cloudflare** — also provides built-in OAuth, transport handling, and integrated deployment for developers building their own Integrations in ~30 minutes.
- **Intercom** — customer support; Intercom's AI agent **Fin** acts as an MCP client and can file Linear bugs from user reports.
- **Asana** — project tracking.
- **Square** — payments / point of sale.
- **Sentry** — error monitoring.
- **PayPal** — payments.
- **Linear** — issue tracking.
- **Plaid** — financial data.

> The post says "10 popular services" but enumerates 11. Reproduce as published; do not silently fix.

## Roadmap (named in the post but not yet launched)

- **Stripe**
- **GitLab**
- **Box**

## Architecture notes from the post

- Integrations connect Claude to **remote MCP servers** across web and desktop, extending the November 2024 MCP release beyond local servers in Claude Desktop.
- Developers can build their own Integrations in as little as **30 minutes** using Anthropic's documentation or solutions like Cloudflare.

## Source

[Claude can now connect to your world](https://claude.com/blog/integrations) (2025-05-01, updated 2025-06-03).

**English** · [한국어](./getting-started.ko.md) · [Español](./getting-started.es.md) · [日本語](./getting-started.ja.md)

# Getting started with Integrations and advanced Research

A short guide derived from [Claude can now connect to your world](https://claude.com/blog/integrations) (2025-05-01, updated 2025-06-03). It covers what to enable first, how to think about the connected app catalog, and how to scope a Research request that uses your connections.

## 1. Confirm plan availability

After the 2025-06-03 update, Integrations and advanced Research are available on Pro, Max, Team, and Enterprise. Web search is global on **all** Claude plans.

If you are on the launch-day version of the post, Integrations and Research were beta on Max, Team, Enterprise; web search global on paid plans.

## 2. Pick the first app to connect

Choose from the launch lineup (Atlassian Jira, Atlassian Confluence, Zapier, Cloudflare, Intercom, Asana, Square, Sentry, PayPal, Linear, Plaid). For an unsupported app, check whether the Zapier Integration covers it via a pre-built workflow. The roadmap as of the post mentions Stripe, GitLab, and Box.

For each candidate, write down: which Claude tasks need access to that data, what actions Claude must take, and the auth model your org allows.

## 3. Connect via the Integrations surface

Each Integration uses a remote MCP server. Once connected, Claude can read context (project history, task state, organizational knowledge) and take actions across that app.

Builders shipping their own Integrations can use Cloudflare's hosting, which provides built-in OAuth, transport handling, and deployment — the post says a new Integration can be built in as little as 30 minutes.

## 4. Run an advanced Research request

- Toggle on the **Research** button.
- Frame your request like a brief: state the question, the scope, and which connected apps to include.
- Expect 5–15 minutes for most reports; up to 45 minutes for complex investigations.
- Verify the citations the report links to before relying on findings.

## 5. Suggested first workflows

- Zapier-driven: pull HubSpot sales data; prepare a meeting brief from your calendar.
- Atlassian: summarize a Confluence space; bulk-create Jira items from a kickoff doc.
- Intercom + Linear: identify a recurring user-feedback pattern, then file a Linear bug from the same conversation via Fin acting as an MCP client.

## Source

[Claude can now connect to your world](https://claude.com/blog/integrations) (published 2025-05-01, updated 2025-06-03).

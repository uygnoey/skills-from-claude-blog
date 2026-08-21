# Advancing MCP in Claude

Claude now lists **over 950 MCP servers** in its connectors directory, used by millions of people
every day. Alongside support for the new protocol extensions, these are the features shipped this
year that make MCP easier to build on and deploy.

## MCP Apps

Servers can render **interactive UI directly in the conversation**. Users see what a connector is
doing and work with it inline, without switching tabs.

*Build for it when* the connector's output is something a person needs to act on rather than just
read — a selection, a form, a preview, a confirmation.

## Enterprise-managed auth

Admins can **provision MCP connectors for their whole organization through their identity
provider**. An admin authorizes a connector once, users inherit access through their existing IdP
groups, and it is connected on first login: **zero-touch setup for the end user**.

*Build for it when* the connector is meant to be deployed org-wide rather than adopted one user at a
time. It pairs with the spec's auth hardening, which aligns authorization with production OAuth 2.0
and OIDC so servers connect to systems like Entra or Okta without workarounds.

## Observability for developers building connectors

Published connectors in the directory get a **dashboard showing how they perform across Claude
product surfaces**. Developers can use it to:

- track adoption,
- diagnose errors and latency,
- break down usage by product.

*Use it for* more than incident response — usage patterns also show which tools people reach for and
where a connector's surface is missing something users want.

## MCP tunnels (research preview)

Connect Claude to **MCP servers inside a private network without exposing them to the public
internet**. Teams can bring internal tools to Claude with:

- no inbound firewall rules,
- no public endpoints,
- no IP allowlisting on the origin.

*Reach for it when* the tool is internal-only and publishing an endpoint would be the wrong trade.

## Why these compose

The stateless core, standardized extensions, and hardened auth in 2026-07-28 help developers bring
more applications to Claude with a lower-friction, more consistent end-user experience. Anthropic
states it will continue investing in MCP as an open standard alongside the community, and in the
Claude features that make MCP more accessible and effective in production.

## Getting started

Explore the spec and the SDKs. Support is rolling out across Claude products. If you plan to submit
an MCP server to Claude's connectors directory, read the directory's submission guidance first.

## Source

[Bringing MCP 2026-07-28 to Claude](https://claude.com/blog/bringing-mcp-2026-07-28-to-claude) —
published 2026-07-28.

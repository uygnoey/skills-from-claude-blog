**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
The announcement of MCP 2026-07-28, the fifth spec release of the Model Context Protocol, live as of 28 July 2026. Three changes define it: MCP moves from a bidirectional stateful protocol to a **stateless request/response core**, MCP Apps and Tasks graduate into a **versioned extensions framework**, and **authorization aligns with production OAuth 2.0 and OIDC** so servers connect to enterprise identity systems like Entra or Okta without workarounds. Support is rolling out across Claude products.

The post also covers the Claude side of the story: over 950 MCP servers now listed in the connectors directory, plus MCP Apps for interactive UI in the conversation, enterprise-managed auth for IdP-provisioned org-wide connectors, an observability dashboard for connector developers, and MCP tunnels (research preview) for reaching servers inside a private network.

## When is it useful?
- When planning or refactoring an MCP server and deciding what the stateless core changes about its state and deployment.
- When deciding whether a server can move to serverless or edge infrastructure.
- When connecting a server to an enterprise identity provider, or deleting custom auth glue written around gaps in the previous spec.
- When adding interactive UI or long-running work to a server and looking for the supported path rather than a core-protocol workaround.
- When rolling connectors out organization-wide through an IdP rather than one user at a time.
- When preparing a connector for Claude's connectors directory, or using its performance dashboard afterward.
- When an internal tool sits behind a firewall and exposing a public endpoint is the wrong trade.

## Key points
- **Stateless core.** Request/response replaces the bidirectional stateful protocol. Servers can deploy on serverless and edge infrastructure, which simplifies both building for Claude and scaling as adoption grows.
- **The deployment framing from the ecosystem:** the stateless core makes MCP a first-class HTTP workload with no session management to work around.
- **Versioned extensions.** MCP Apps and Tasks ship under a formal extensions framework, so interactive UIs and long-running work are additive capabilities rather than changes to the core protocol.
- **Auth hardening.** Authorization now matches how OAuth 2.0 and OIDC are actually deployed in production, which is what makes Entra and Okta work without workarounds.
- **Scale of the standard.** MCP recently passed 400M monthly SDK downloads, a 4x increase this year; Claude lists over 950 MCP servers in its connectors directory.
- **MCP Apps** let a server render interactive UI inline, so users see what a connector is doing without switching tabs.
- **Enterprise-managed auth** is zero-touch for the end user: the admin authorizes a connector once, users inherit access through existing IdP groups, and it connects on first login.
- **Connector observability** shows adoption, errors and latency, and usage by product — useful for finding missing tools, not only broken ones.
- **MCP tunnels (research preview)** reach servers inside a private network with no inbound firewall rules, no public endpoints, and no IP allowlisting on the origin.

## Bundled resources
- `skills/mcp-2026-07-28-adoption/SKILL.md` — an adoption procedure: what the stateless core changes, when to reach for each extension, how to align auth, which Claude-side capabilities apply, and a rollout order that follows the dependencies.
- `skills/mcp-2026-07-28-adoption/references/whats-new.md` — the three spec changes in full, the ecosystem numbers, and what builders reported during the beta.
- `skills/mcp-2026-07-28-adoption/references/claude-mcp-capabilities.md` — MCP Apps, enterprise-managed auth, connector observability, and MCP tunnels, each with when to build for it.
- `guides/mcp-2026-07-28-release.{en,ko,es,ja}.md` — the release as a narrative walkthrough in four languages.

## Source
[Bringing MCP 2026-07-28 to Claude](https://claude.com/blog/bringing-mcp-2026-07-28-to-claude) — published 2026-07-28.

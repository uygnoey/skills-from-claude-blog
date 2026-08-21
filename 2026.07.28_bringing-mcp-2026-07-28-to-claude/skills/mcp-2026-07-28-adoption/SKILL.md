---
name: mcp-2026-07-28-adoption
description: Adopt the MCP 2026-07-28 specification — the fifth Model Context Protocol spec release, which moves MCP to a stateless request/response core, graduates MCP Apps and Tasks into a versioned extensions framework, and hardens authorization to align with production OAuth 2.0 and OIDC. Use when planning an MCP server against the new spec, when deciding whether to deploy a server on serverless or edge infrastructure, when connecting a server to an enterprise identity provider such as Entra or Okta, when adding interactive UI or long-running work to a server, or when preparing a connector for the Claude connectors directory. Also covers what shipped on the Claude side — MCP Apps, enterprise-managed auth, connector observability, and MCP tunnels.
---

# MCP 2026-07-28

The fifth spec release of the Model Context Protocol went live on 2026-07-28. It is described as one
of the most significant releases to date: a stateless core, a versioned extensions framework, and
hardened authorization. Support is being rolled out across Claude products.

Context for the scale of the ecosystem: MCP recently surpassed 400M monthly SDK downloads, a 4x
increase this year, and Claude now lists over 950 MCP servers in its connectors directory, used by
millions of people every day.

## Instructions

### 1. Decide what the stateless core changes for your server

MCP moves from a bidirectional stateful protocol to a **request/response model**. Two consequences
follow directly:

- **Deployment.** Servers can now deploy on serverless and edge infrastructure. MCP becomes a
  first-class HTTP workload with no session management to work around.
- **Scaling.** Building a server for Claude, and scaling it as adoption grows, gets simpler — there
  is no session state to keep coherent across instances.

When planning a server, audit anything in the current design that depends on a long-lived
connection or in-memory per-session state, and decide where that state moves: to the request, to a
store the server queries, or to a Task (below).

### 2. Use the extensions framework instead of bending the core

**MCP Apps** and **Tasks** now ship under a versioned extensions framework. This gives a formal path
to add capabilities — interactive UIs and long-running work — without changing the core protocol.

- Reach for **MCP Apps** when the server should render interactive UI directly in the conversation,
  so users can see what a connector is doing and work with it inline without switching tabs.
- Reach for **Tasks** when the work outlives a single request/response exchange.
- Because extensions are versioned, declare which extension versions your server implements rather
  than assuming a client supports everything.

### 3. Align authorization with your identity provider

Authorization now aligns with production OAuth 2.0 and OIDC deployments, so MCP servers connect to
enterprise identity systems like **Entra** or **Okta** without workarounds. If your current server
carries custom auth glue written around gaps in the old spec, this is the release in which to delete
it.

For organization-wide rollout, pair this with **enterprise-managed auth** on the Claude side: admins
provision connectors for the whole organization through their identity provider, authorize a
connector once, users inherit access through their existing IdP groups, and it connects on first
login — zero-touch setup for the end user.

### 4. Pick up the Claude-side capabilities that apply to you

- **MCP Apps** — interactive UI rendered inside the conversation.
- **Enterprise-managed auth** — IdP-provisioned connectors, inherited group access.
- **Observability for connector developers** — published connectors in the directory get a dashboard
  showing how they perform across Claude product surfaces: adoption, errors and latency, and usage
  broken down by product. Use it to find missing tools as well as broken ones.
- **MCP tunnels (research preview)** — connect Claude to MCP servers inside a private network without
  exposing them to the public internet: no inbound firewall rules, no public endpoints, no IP
  allowlisting on the origin.

Details and the ecosystem context: [references/whats-new.md](references/whats-new.md) and
[references/claude-mcp-capabilities.md](references/claude-mcp-capabilities.md).

### 5. Start building

Explore the spec and the SDKs to get started. Support is rolling out across Claude products. If you
plan to submit your MCP server to Claude's connectors directory, read the directory's submission
guidance first.

> **Scope note.** This skill covers what the announcement states. It is not a substitute for the
> specification: see the MCP 2026-07-28 release announcement for full details on the new spec, and
> the official docs for API-level guidance.

## Examples

**Deciding whether a server needs rework**

| Current design | Under 2026-07-28 |
|---|---|
| Keeps per-session state in memory on one long-lived connection | Move the state out of the process; the core is request/response |
| Runs on always-on infrastructure because sessions must persist | Serverless and edge deployment become available |
| Ships a custom OAuth shim to work with Entra or Okta | Authorization aligns with production OAuth 2.0 and OIDC; drop the shim |
| Renders results only as text the user must interpret | MCP Apps can render interactive UI inline in the conversation |
| Blocks a request while a long job runs | Tasks handle long-running work as a versioned extension |
| Sits behind a corporate firewall and cannot be exposed | MCP tunnels (research preview) reach it without a public endpoint |

**What builders reported during the beta**

Companies across the ecosystem — Figma, Intuit, Netlify, and Zoom among those identified in the
post — built on the new spec alongside the MCP community since beta. The themes they name are
consistent: the stateless core makes
MCP a first-class HTTP workload with no session management to work around, which is what lets a
service scale simply; the extensions framework covering MCP Apps and Tasks is described as a step
forward for scalability, accessibility, and capability across the ecosystem; and enterprise-managed
auth is what makes organization-scale deployment practical. Quotes and attributions are in
[references/whats-new.md](references/whats-new.md).

**A rollout order that follows the dependencies**

1. Move the server to the stateless core, since deployment and scaling choices depend on it.
2. Re-point authorization at the organization's IdP through the hardened OAuth 2.0 / OIDC alignment.
3. Add extensions where they earn their place — Apps for inline interaction, Tasks for work that
   outlives a request.
4. Publish to the connectors directory, then use the developer observability dashboard to see
   adoption, errors, latency, and per-product usage.
5. For internal-only tools, evaluate MCP tunnels rather than exposing an endpoint publicly.

## Source

[Bringing MCP 2026-07-28 to Claude](https://claude.com/blog/bringing-mcp-2026-07-28-to-claude) —
published 2026-07-28.

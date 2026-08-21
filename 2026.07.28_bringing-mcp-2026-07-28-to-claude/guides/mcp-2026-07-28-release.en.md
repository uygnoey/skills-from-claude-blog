**English** · [한국어](./mcp-2026-07-28-release.ko.md) · [Español](./mcp-2026-07-28-release.es.md) · [日本語](./mcp-2026-07-28-release.ja.md)

# Bringing MCP 2026-07-28 to Claude

The fifth spec release of the Model Context Protocol, MCP 2026-07-28, went live on 28 July 2026. The
latest spec moves MCP to a stateless core while hardening authorization and graduating official
extensions. Support is being rolled out across Claude products.

## Why this release matters

MCP recently surpassed **400M monthly SDK downloads**, a 4x increase this year, and has become the
industry standard for connecting AI agents to applications. The announcement calls 2026-07-28 one of
the most significant spec releases to date.

### Stateless core

MCP moves from a bidirectional stateful protocol to a **request/response model**. Servers can now
deploy on serverless and edge infrastructure. This simplifies the experience of building MCP servers
for Claude and scaling their usage as they grow in adoption.

For a server author, the practical question is where per-session state currently lives. Anything
that assumed a long-lived connection has to move — into the request, into a store the server queries,
or into a Task.

### Standardized extensions

**MCP Apps** and **Tasks** now ship under a **versioned extensions framework**, giving developers a
formal path to add capabilities like interactive UIs and long-running work without changing the core
protocol. Because the framework is versioned, a server can declare which extension versions it
implements instead of assuming a client supports everything.

### Auth hardening

Authorization now aligns with **production OAuth 2.0 and OIDC deployments**, so MCP servers connect
to enterprise identity systems like **Entra** or **Okta** without workarounds. Custom auth glue
written around gaps in the previous spec is the first thing to delete.

## What builders said during the beta

Companies across the ecosystem have been building on the new spec alongside the MCP community since
beta.

**Figma** (Josh Clemm, VP of Engineering) describes builders using its MCP server to bring generated
outputs into Figma's canvas, where teams explore, riff, and refine them into products. As usage
grows, a stateless architecture scales with it, and MCP Apps, Tasks, and Enterprise-Managed Auth let
Figma do more to keep design and code together in one connected flow.

**Intuit** (Chris Kasten, Chief Architect and SVP of Engineering, Platform and Development
Xceleration Group) supports the new spec: the stateless protocol core and the extensions framework,
including MCP Apps and Tasks, let its technologists and customers build and connect agentic
experiences at enterprise scale, supporting delivery of trusted financial intelligence experiences to
its 100 million consumers and businesses wherever they choose to work.

**Netlify** (Sean Roberts, VP of Applied AI) puts the deployment case plainly: the stateless core
makes MCP a first-class HTTP workload with no session management to work around. Customers wanted
MCPs on Netlify to be as simple as the rest of the platform, and the new spec unlocks that at its
core; building MCP Apps into the extensions framework is a large step forward for scalability,
accessibility, and capability across the whole ecosystem.

**Paul D'Ambra** (Product Engineer) notes that a stateless protocol makes it easier to scale the
service and to add analytics for customers' MCP servers — showing people how their MCP tools are
being used, and what tools are missing that their users would want.

**Andrew Goodman** (VP of AI) frames it as complexity removed: the stateless core reduces what the
team manages, so they can ship more features to customers, faster and at scale.

**Zoom** (Ross Mayfield, Head of Product for AI Platform) starts from organizational context being
what enables AI to deliver meaningful work, which is why Zoom built MCP servers that securely bring
meeting intelligence into AI platforms like Claude. The new spec makes it far easier to deploy and
scale MCP servers on standard HTTP infrastructure, so users get that intelligence faster and more
reliably inside the workflows they depend on every day.

## Advancing MCP in Claude

Claude now lists **over 950 MCP servers** in its connectors directory, used by millions of people
every day. Alongside support for the new protocol extensions, these features shipped this year:

- **MCP Apps** let servers render interactive UI directly in the conversation. Users can see what a
  connector is doing and work with it inline, without switching tabs.
- **Enterprise-managed auth** lets admins provision MCP connectors for their whole organization
  through their identity provider. Admins authorize a connector once, users inherit access through
  their existing IdP groups, and it is connected on first login: zero-touch setup for the end user.
- **Observability for developers building connectors** gives published connectors in the directory a
  dashboard showing how they perform across Claude product surfaces. Developers can track adoption,
  diagnose errors and latency, and break down usage by product.
- **MCP tunnels (research preview)** connect Claude to MCP servers inside a private network without
  exposing them to the public internet. Teams can bring internal tools to Claude with no inbound
  firewall rules, no public endpoints, and no IP allowlisting on the origin.

The stateless core, standardized extensions, and hardened auth will help developers bring more
applications to Claude with a lower-friction, more consistent end-user experience. Anthropic states
it will continue investing in MCP as an open standard alongside the community, and in the Claude
features that make MCP more accessible and effective in production.

## An adoption order that follows the dependencies

1. **Move to the stateless core first** — deployment and scaling choices depend on it.
2. **Re-point authorization at the organization's IdP** through the hardened OAuth 2.0 / OIDC
   alignment, and pair it with enterprise-managed auth for org-wide rollout.
3. **Add extensions where they earn their place** — Apps for inline interaction, Tasks for work that
   outlives a request.
4. **Publish to the connectors directory**, then use the developer observability dashboard to watch
   adoption, errors, latency, and per-product usage.
5. **For internal-only tools, evaluate MCP tunnels** rather than exposing an endpoint publicly.

## Getting started

Explore the spec and the SDKs to get started. Support is rolling out across Claude products soon. If
you are planning to submit your MCP server to Claude's connectors directory, read the directory's
submission guidance. For full details on the new spec, see the MCP 2026-07-28 release announcement.

## Source

[Bringing MCP 2026-07-28 to Claude](https://claude.com/blog/bringing-mcp-2026-07-28-to-claude) —
published 2026-07-28.

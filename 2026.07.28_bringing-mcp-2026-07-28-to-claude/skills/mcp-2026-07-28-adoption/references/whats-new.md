# What is new in MCP 2026-07-28

The fifth spec release of the Model Context Protocol, live 2026-07-28, and described in the
announcement as one of the most significant spec releases to date.

## Ecosystem context

- MCP recently surpassed **400M monthly SDK downloads**, a **4x increase this year**.
- It has become the industry standard for connecting AI agents to applications.

## The three headline changes

### Stateless core

MCP moves from a bidirectional stateful protocol to a **request/response model**. Servers can now
deploy on serverless and edge infrastructure. This simplifies the experience of building MCP servers
for Claude and scaling their usage as they grow in adoption.

### Standardized extensions

**MCP Apps** and **Tasks** now ship under a **versioned extensions framework**, giving developers a
formal path to add capabilities like interactive UIs and long-running work without changing the core
protocol.

### Auth hardening

Authorization now aligns with **production OAuth 2.0 and OIDC deployments**, so MCP servers connect
to enterprise identity systems like **Entra** or **Okta** without workarounds.

## What builders said during the beta

Companies across the ecosystem built on the new spec alongside the MCP community since beta. The
themes below come from the announcement's quotes.

**Figma — Josh Clemm, VP of Engineering.** More builders are using Figma's MCP server to bring
generated outputs into Figma's canvas, where teams explore, riff, and refine them. As that usage
grows, a stateless architecture can scale with it, and MCP Apps, Tasks, and Enterprise-Managed Auth
let Figma do more to keep design and code together in one connected flow.

**Intuit — Chris Kasten, Chief Architect and SVP of Engineering, Platform and Development
Xceleration Group.** MCP is the industry standard for connecting AI agents to tools and data. The
stateless protocol core and the extensions framework, including MCP Apps and Tasks, let Intuit's
technologists and customers build and connect agentic experiences at enterprise scale, supporting
delivery of trusted financial intelligence experiences to its 100 million consumers and businesses
wherever they choose to work.

**Netlify — Sean Roberts, VP of Applied AI.** The stateless core makes MCP a first-class HTTP
workload with no session management to work around. Customers wanted MCPs on Netlify to be as simple
as the rest of the platform, and the new spec unlocks that at its core. Building MCP Apps into the
new extensions framework is described as a large step forward for scalability, accessibility, and
capability across the whole ecosystem.

**Paul D'Ambra, Product Engineer.** Moving MCP to a stateless protocol makes it easier to scale the
service and easier to add analytics for customers' MCP servers — showing people how their MCP tools
are being used, and what tools are missing that their users would want.

**Andrew Goodman, VP of AI.** The stateless core in the open MCP 2026-07-28 spec reduces the
complexity the team manages, so they can ship more features to customers, faster and at scale.

**Zoom — Ross Mayfield, Head of Product for AI Platform.** Organizational context is what enables AI
to deliver meaningful work, which is why Zoom built MCP servers that securely bring Zoom meeting
intelligence into AI platforms like Claude. The new spec makes it far easier to deploy and scale MCP
servers on standard HTTP infrastructure, so users get that meeting intelligence faster and more
reliably inside the AI workflows they depend on.

## Where to go next

- The MCP 2026-07-28 release announcement carries the full details on the new spec.
- Explore the spec and the SDKs to get started.
- Support is rolling out across Claude products.

## Source

[Bringing MCP 2026-07-28 to Claude](https://claude.com/blog/bringing-mcp-2026-07-28-to-claude) —
published 2026-07-28.

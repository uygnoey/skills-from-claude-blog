# The seven deployment controls

Each control is stated twice: first as **the requirement** any agent environment should be able
to meet, then as **the enforcement** — how it is actually implemented in a personal agent
harness (the source article uses Claude Cowork as the worked example).

Take these seven to the teams and vendors building agents whom you already pay. Ask your IdP,
your SIEM, and any agent vendor which of these they can show you working in your stack today.

---

## 1. Identity comes from your IdP

**Requirement.** An agent's identity has to be issued and revoked where you already issue and
revoke everything else, with your existing groups as the unit of policy.

**Enforcement.** SAML or OIDC for sign-in, SCIM for provisioning. On Enterprise plans, custom
roles scope capability by group.

## 2. Connector allowlists draw your data boundary

**Requirement.** Allowlists for connectors (MCP servers) let you decide which systems the agent
can reach.

**Enforcement.** A two-gate model: an admin enables each connector org-wide, and each user then
individually authorizes their own account. Per-role connector control means enabling a connector
makes it available to everyone in that role, and IdP groups can be assigned to roles.

**The point.** The admin decision about which connectors to turn on *is* the decision about
which data the agent can reach.

- Keep connectors on the corporate side of your corporate/production data boundary.
- If a connector accesses information from untrusted sources, require human review for any
  destructive or one-way decision. Example: a personal agent used for email that takes web
  search results as input should be allowed to create **draft** emails and never to send
  externally, automatically, without human review.
- If data must cross the boundary, it should go through DLP or DSPM controls.

## 3. Per-tool, per-action approval

**Requirement.** The agent's tool list is a more fine-grained permission boundary than the
connector. You need to be able to remove a particular connector's individual verbs/actions, not
only the entire connector.

**Enforcement.** Admins can restrict which actions are available within each connector, org-wide
and per-role: allow drafting docs but never automatically sending them; allow reads and searches
but never deletes.

**The point.** If the failure mode that keeps you up at night is "the production database gets
deleted," remove the delete verb from the agent's world entirely. **It will never attempt an
action that isn't in its tool list.**

> Note: coding and browser agents enable more degrees of freedom and are therefore riskier if
> not governed well. An agent could use an engineer's browser to delete a production resource,
> or their command line to do the same.

## 4. Sandboxed execution keeps the agent away from production credentials

**Requirement.** The environment the agent loop runs in should never hold a credential worth
stealing.

**Enforcement.** In remote sessions the agent loop runs in an isolated, temporary sandbox on
managed infrastructure. Connector authorization tokens never enter the sandbox: connector calls
go through a reverse proxy that injects the real credentials, so the sandbox never holds a
credential that can be exfiltrated.

**Why it scales.** As of July 2026, more than 50% of all code submitted for pull requests at
Anthropic is authored by an internal agent system. The primary reasons that can run safely are
that all of it happens in **ephemeral VMs separated from production keys and accounts**, with a
**human review before anything lands**.

## 5. Egress allowlisting is your strongest control against prompt injection

**Requirement.** All traffic leaving the agent's execution environment should pass through a
proxy that the environment cannot reconfigure or bypass, and only destinations you chose should
be reachable.

**Enforcement.** In remote sessions, all traffic leaving the sandbox passes through a mandatory
proxy the sandbox cannot reconfigure or bypass; only allowlisted destinations are reachable.

**The reasoning.** If an agent is compromised by something it read, the attacker still has to
get the data out. When outbound requests can only reach domains you chose, there is nowhere
attacker-controlled to send anything.

## 6. Telemetry goes to your SIEM over OpenTelemetry

**Requirement.** Agent actions have to be distinguishable from user actions in the system where
you already investigate things, and the vendor should deliver that as a **stream you can point
somewhere**, not a dashboard you have to visit.

**Enforcement.** Admins configure an OTLP endpoint in Organization settings; the agent streams
every tool invocation — tool name, MCP server, parameters, success or failure, duration —
alongside user identity and session context.

**Two caveats from the source.**

- Claude Cowork activity is not currently captured in Anthropic's Compliance API or formal
  audit logs. The OpenTelemetry stream is the native monitoring path.
- Prompt content is included in Claude Cowork's OTel output **by default**, unlike Claude Code
  where it is opt-in. If your retention or privacy review has an opinion about prompt content
  living in your SIEM, have that conversation *before* you turn the stream on.

## 7. There is an org-wide off switch

**Requirement.** One control that stops everything, plus narrower layers you can reach for
first.

**Enforcement.** A single toggle in Organization settings disables connectors for every user
simultaneously, active sessions included. On Enterprise plans the same control surface lets you
go narrower before going to zero:

- RBAC pulls access from specific groups while leaving others running.
- Per-connector controls disable write operations on a specific integration without touching
  the rest of the deployment.

**The point.** The right incident response plan has all three layers mapped out **before** you
need them.

---

## Source

["Zero risk isn't the job: a CISO's guide to agentic AI"](https://claude.com/blog/ciso-guide-to-agentic-ai).
For the controls, attestations, and white papers behind the post, start at
[trust.anthropic.com](https://trust.anthropic.com).

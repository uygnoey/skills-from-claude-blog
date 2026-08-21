---
name: agentic-risk-assessment
description: Assess and bound the security risk of an agentic AI deployment before approving it. Use when a team asks to connect an agent to internal systems, when reviewing a personal agent harness or an autonomous service agent, when writing an agent security review process, or when deciding which controls a vendor must demonstrate. Applies a four-question risk assessment (untrusted content, actions and identity, blast radius, observability), places the deployment on the identity spectrum from service account to human credential, and checks it against seven deployment controls covering identity, connector allowlists, per-action approval, sandboxed execution, egress allowlisting, telemetry, and an off switch.
---

# Agentic risk assessment

The job is not zero risk. The job is to make agentic risk **legible and bounded**, so
risk can be deliberately accepted by someone with the authority to accept it, and the
business moves on your terms instead of around you.

Saying "no" produces shadow adoption — zero telemetry and generally no off switch.
Saying "yes" without controls produces incidents.

## Instructions

### 1. Run the four questions

For every agentic use case that reaches review, answer all four. Full definitions and
scoring guidance: [references/four-questions.md](references/four-questions.md).

1. **What untrusted content does it ingest?** Untrusted means anything an attacker could
   plausibly write or alter — outside email, the open web, third-party documents, public
   repositories. If the answer is "nothing," the agent-specific risk is near zero: move quickly.
2. **What actions can it take, and on whose behalf?** Read-only is a different concern from
   read/write. Tool calls, code execution, and network egress each widen the aperture.
   Every action happens under some identity; know whose.
3. **What is the blast radius if it is misaligned?** Scope × severity. Did the bad actor or
   alignment incident have access to one file or the whole org? Anomaly, annoyance, data
   exposure, or true incident?
4. **What observability do I have?** Can you tell agent actions from user actions? Does it
   land in your SIEM?

Record the answers in [templates/risk-review.md](templates/risk-review.md).

### 2. Apply the principle of least agency

The four answers give you a picture of the risk. The **principle of least agency** tells you
what to do with it: grant the narrowest capability that still completes the task.

Default posture: **admin-paced rollout** — enable a small group, watch the telemetry, then
expand access.

### 3. Locate the deployment on the identity spectrum

Every deployment sits somewhere between two ends. See
[references/identity-spectrum.md](references/identity-spectrum.md).

- **System service account** — self-contained, single-purpose, least-privilege identity doing
  exactly one thing for the business, with no human identity attached.
- **Human credential** — a person at a keyboard is accountable for the outcome, the same way
  they are for anything else done with their credentials.
- **The ambiguous middle** — an agent carrying a person's delegated identity into systems that
  person is not watching. Ambiguous accountability is how incidents become unexplainable.
  Push a deployment toward one end or the other.

Treat a misaligned agent as an insider threat, not a perimeter problem. The operational
difference is response time: the Ponemon Institute's 2026 *Cost of Insider Risks* report found
organizations took an average of **67 days** to contain an insider incident. At agent execution
speeds, responses measured in days are too long.

### 4. Check the deployment against the seven controls

Each control is a requirement any agent environment should be able to meet. Full text of each,
with what to ask a vendor: [references/deployment-controls.md](references/deployment-controls.md).

1. **Identity comes from your IdP** — issued and revoked where you already issue and revoke
   everything else, with your existing groups as the unit of policy.
2. **Connector allowlists draw your data boundary** — the decision about which connectors are on
   is the decision about which data the agent can reach.
3. **Per-tool, per-action approval** — remove individual verbs, not just whole connectors. If
   the failure mode that keeps you up at night is "the production database gets deleted," remove
   the delete verb from the agent's world entirely. It will never attempt an action that isn't
   in its tool list.
4. **Sandboxed execution** — the environment the agent loop runs in should never hold a
   credential worth stealing.
5. **Egress allowlisting** — the strongest control against prompt injection. If an agent is
   compromised by something it read, the attacker still has to get data out; when outbound
   requests can only reach domains you chose, there is nowhere attacker-controlled to send anything.
6. **Telemetry to your SIEM over OpenTelemetry** — agent actions must be distinguishable from
   user actions in the system where you already investigate. A stream you can point somewhere,
   not a dashboard you have to visit.
7. **An org-wide off switch** — plus narrower layers (RBAC by group, per-connector write
   disable) mapped out *before* you need them.

### 5. Write down your trust boundary

Write down what counts as untrusted content in your environment. Every future agent decision
gets easier once that line exists. Use [templates/trust-boundary.md](templates/trust-boundary.md).

If data must cross the boundary, route it through DLP or DSPM controls. Where a connector
touches untrusted sources, require human review for any destructive or one-way decision — for
example, a personal agent doing email with web search in its input should be allowed to create
draft emails and never to send externally without human review.

### 6. Design for six months out, not for today's model

If you design your program for what the model can do today, you will be behind by the time it
launches. Increased model intelligence enables more degrees of freedom and obsoletes elaborate
scaffolds with meticulous prompts; if you lean on those for controls, they will be cut out of
future generations of internal applications, leaving you without a control point.

Limit **access and actions**, not what you believe today's model limits are. New capabilities
can appear within the boundaries of an existing deployment without any change to tools,
permissions, or prompts — see [examples/incident-response-agent.md](examples/incident-response-agent.md).

### 7. Keep governance from becoming the bottleneck

- **Take the risk register first.** A register reviewed quarterly can't govern systems that
  change faster than the governance process can document new risks. Automate it, possibly by
  integrating an agent with the security review process.
- **Understand who built the agents and why.** People route around security because the
  sanctioned path is slow — that is the origin of most shadow adoption. A compliance analyst who
  can build the tool they need, where you can see it, isn't shadow adoption.
- **Human accountability is part of the workflow.** Deliberately accepting risk is an act
  performed by humans with the authority to accept it. With a live risk register and an executive
  risk council behind it (ISO 42001 or similar), re-scores reach the people who can accept them
  and flagged vendor terms reach the people who negotiate them. If you already have ISO 27001,
  adding 42001 is often an incremental addition with your current auditor.

### 8. Getting started

- Pick the agentic use case with the most internal pressure and run it through the four
  questions. The goal is to find the conditions under which you would approve it, not to
  produce a verdict.
- Take the seven requirements to the teams and vendors you already pay. Ask your IdP, your
  SIEM, and any agent vendor which of these they can show you working in your stack today.
- Decide your trust boundary and write it down.

## Examples

### Bounded service-account agent (approve and move)

An incident response agent with read-only production logs (no PII), Slack access to open and
run the incident channel, and the ability to draft a postmortem doc. Four questions: no
untrusted content; reads everywhere, writes limited to new documents and Slack messages;
worst constructible outcome is mildly sensitive log lines in an already-locked-down channel;
every action lands in the SIEM. Not risk-free, but a bounded write surface with full audit
coverage. Walkthrough, including the emergent agent-to-agent behavior that appeared after a
model upgrade: [examples/incident-response-agent.md](examples/incident-response-agent.md).

### Human-credential agent harness (bound with the seven controls)

A personal agent harness on an employee's machine or in a hosted session sits at the human
operator end of the spectrum. The four questions produce different answers for every use case,
so risk is bounded by controls rather than by a single verdict: IdP identity, two-gate connector
allowlists, per-action approval, a sandbox that holds no credential worth stealing, mandatory
egress proxy, OpenTelemetry to your SIEM, and a single org-wide off switch.
Walkthrough: [examples/personal-agent-harness.md](examples/personal-agent-harness.md).

### Governance agents you run yourself

GRC teams can run their own agents — drafting security-questionnaire responses, and reading
vendor questionnaire responses and subprocessor-change notifications to flag the ones that
should be objected to. See the companion subagent definitions shipped alongside this post.

## Source

["Zero risk isn't the job: a CISO's guide to agentic AI"](https://claude.com/blog/ciso-guide-to-agentic-ai)
by Jason Clinton, Deputy CISO, Anthropic — published July 17, 2026.

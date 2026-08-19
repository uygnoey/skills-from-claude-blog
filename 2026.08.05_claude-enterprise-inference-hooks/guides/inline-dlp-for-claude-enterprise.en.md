**English** · [한국어](./inline-dlp-for-claude-enterprise.ko.md) · [Español](./inline-dlp-for-claude-enterprise.es.md) · [日本語](./inline-dlp-for-claude-enterprise.ja.md)

# Inline DLP for Claude Enterprise

A deployment guide for **inference hooks**: real-time data loss prevention that inspects prompts and tool call responses before the model acts on them.

## The gap it closes

Security teams generally hold one rule about data movement: every channel through which an employee can move sensitive data must pass an inspection point the security team controls. Email has one. Endpoints have one. Web traffic has one.

AI surfaces did not — at least not natively and not everywhere. Enforcement inside a coding agent was possible through that agent's own client-side hooks, but that covers one product, configured on the client, and leaves chat and agentic workspaces outside the perimeter.

Inference hooks makes the inspection point a property of the organization rather than of a product.

## Architecture

```
User / agent
     │
     │  inference request
     ▼
Claude Enterprise ──── signed WebSocket ────▶ Your security server
     │                                              │
     │ ◀───────────  allow / deny verdict ──────────┘
     ▼
Model generates
     │
     │  tool call (MCP connector / skill / plugin)
     ▼
Tool response ──── same check ────▶ verdict ────▶ model sees it (or does not)
```

Two properties determine everything else about the deployment:

1. **It is synchronous.** Generation waits for a verdict. Your server's latency is now every user's latency.
2. **It is pre-generation.** Inspection happens before the model reads the content, not after it produces output. That is what makes it prevention rather than detection.

## What is inspected

| Point | Content | Why it matters |
|---|---|---|
| Before generation | The prompt and its surrounding context | The direct path for a person to move data into a model |
| Before the model reads a tool result | The tool call response | Connectors can pull restricted content in without anyone typing it |

The tool-response path deserves specific attention during design. Any connector with read access to a document store, ticket system, or database is a route by which classified content enters a context window automatically.

## Deployment shape

### Point at the server you already have

The protocol is webhook-based with a published schema. In practice this means the decision point is usually an existing platform — Netskope, Palo Alto Networks, Proofpoint, Zscaler, or an in-house AI security server — rather than something built for this purpose. Reuse is the recommended path: one policy corpus, one audit trail, one place where rules are maintained.

For security vendors, the same property runs the other way: build an integration against the documented schema, and customers can point their organization at your platform through configuration.

### Configure once at the organization level

One switch covers Claude Enterprise surfaces including chat, Claude Code, Claude Cowork, and tool calls made through MCP connectors, skills, and plugins. There is no per-product integration and no separate agent to deploy alongside each product.

### Ramp deliberately

The available controls exist because turning inline enforcement on everywhere at once is how rollouts fail:

- **Shadow mode** — always allow, while the server still evaluates. This is the measurement phase, and it is where rule tuning happens.
- **Role-based exclusions** — keep break-glass and administrative roles out of a control that could otherwise lock out the people who administer it.
- **Percentage-based rollout** — expose a fraction of the population to enforcement, so a bad rule is a contained incident rather than an org-wide outage.
- **Failure policy and timeouts** — decide, explicitly, what happens when the server does not answer in time.

## The failure policy decision

This is the decision most worth making consciously rather than inheriting from a default.

**Fail closed.** No verdict, no inference. Coverage is complete; an outage of the policy server is an outage of AI across the organization. Appropriate when the sensitivity of the data dominates.

**Fail open.** No verdict within the timeout, and the request proceeds. Availability is preserved; every fail-open event is an uninspected request. Appropriate when availability dominates — but only if fail-open events are logged, alerted on, and reviewed, because otherwise the gap is invisible.

Whichever is chosen, the timeout value is part of the decision. A generous timeout under fail-closed converts a slow server into a slow product; a tight timeout under fail-open converts a slow server into silent gaps.

## Operational consequences

- **The policy server becomes a production dependency.** Capacity planning, on-call ownership, and maintenance windows for that server now affect every AI surface.
- **Every rule costs latency on every request.** Rules that are not about data loss belong somewhere else.
- **Denials need a human path.** A block with no route forward pushes work toward unmonitored channels — the failure mode the control was bought to prevent.
- **Coverage claims need evidence.** Keep the configuration history: shadow mode state, percentage, exclusions, failure policy, and timeout, each with a date and a reason.

## Naming caution

"Inference hooks" and Claude Code's lifecycle hooks share a word and almost nothing else:

| | Inference hooks | Claude Code hooks |
|---|---|---|
| Where it runs | Server side, in the inference path | Client side, in the coding agent |
| Who configures it | Organization administrator | Developer or team, in settings |
| What it gates | Prompts and tool responses across surfaces | Lifecycle events such as PreToolUse and PostToolUse |
| Scope | Organization-wide | One agent installation |

They are complementary, not alternatives. An organization can run both.

## Getting started

Inference hooks is available in beta for Claude Enterprise customers. Configuration details, the webhook schema, and current availability are in the platform documentation; confirm them there before committing to a rollout date.

## Source

- https://claude.com/blog/claude-enterprise-inference-hooks

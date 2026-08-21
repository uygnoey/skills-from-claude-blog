# Example: a personal agent harness (human-credential end)

The incident response agent is a service account doing one job in a bounded identity. A personal
agent harness sits at the **human operator** end of the spectrum: an employee at a keyboard is
accountable for the outcome, and the agent acts on their behalf, in systems they authorized —
increasingly, running in the cloud.

## The threat model

Claude Cowork's threat model is straightforward, because the agent is essentially Claude Code
running either locally or inside a hosted interface. The desktop app remains required for local
file access, browser use, and computer use; those capabilities reach the local machine directly
and need the app to do so.

The full system surface is therefore two-part:

1. **A (possibly remote) execution environment** handling orchestration, MCP calls, and
   outbound network requests.
2. **A local bridge** for file and screen access.

## Why the four questions don't produce one verdict here

The four questions produce **different answers for every use case** running inside a personal
agent harness. One employee is summarizing internal documents; another is processing outside
email with web search in the loop. Those are not the same risk.

So risk is bounded by **controls** rather than by a single approval decision. Apply all seven
from `references/deployment-controls.md`:

| # | Control | What it buys you here |
|---|---|---|
| 1 | Identity from your IdP | Provisioning and revocation happen where they already happen |
| 2 | Connector allowlists | Draws the data boundary; two gates — admin org-wide, then per user |
| 3 | Per-tool, per-action approval | Removes the verb you fear, not just the whole connector |
| 4 | Sandboxed execution | The agent loop never holds a credential worth stealing |
| 5 | Egress allowlisting | Strongest control against prompt injection: nowhere to exfiltrate to |
| 6 | OpenTelemetry to your SIEM | Agent actions distinguishable from user actions |
| 7 | Org-wide off switch | Plus RBAC and per-connector write disable as narrower layers |

## The pattern worth copying

Where a connector reaches untrusted sources, require human review for any destructive or
one-way decision. The canonical shape: **allow drafting, never automatic sending.** If a
personal agent handles email but takes web search results as input, an excellent default is to
allow draft emails only, never external sends without human review.

## Source

["Zero risk isn't the job: a CISO's guide to agentic AI"](https://claude.com/blog/ciso-guide-to-agentic-ai)

---
name: secure-ai-native-sdlc
description: Design and operate security controls for a software development lifecycle where agents author most of the code. Use when the security review queue has become the bottleneck on shipping, when deciding where human gates belong once the build step takes hours instead of months, when setting agent identity and permission boundaries (including agent-to-agent access), when introducing AI reviewers that must earn trust before they can block or approve, or when a security program needs an audit trail for decisions made by agents rather than people. Covers the Plan, Code, Test/CI, Deploy/CD, Monitor, and Governance stages with an enduring principle for each.
---

# Securing an AI-native SDLC

When agents author most of the merged code, security processes that run at human
speed become the constraint on the whole system (Amdahl's Law). The answer is not
to remove controls but to change how they are enforced: move them into the moment
code is generated, contain what an agent can reach, run many narrow reviewers
instead of one broad one, and keep humans at the points where their judgment has
the most leverage.

Read [references/threat-model.md](references/threat-model.md) first — every control
below maps to at least one of the three named threats.

## Instructions

### 1. Establish the threat model before choosing controls

Three threats drive the design:

1. A compromised or prompt-injected agent introducing a malicious change.
2. Supply-chain and dependency poisoning that an agent ingests as trusted input.
3. Familiar application vulnerability classes, now arriving at higher volume.

Reject any proposed control that cannot be traced to one of them. Detail and
per-threat control mapping live in
[references/threat-model.md](references/threat-model.md).

### 2. Apply the four overarching strategies

- **Shift left into generation.** Security guidance is encoded where code is
  produced, not published as a document engineers are expected to remember.
- **Contain blast radius with hard boundaries.** Identity, permissions, execution
  environment, and network egress — not instructions.
- **Combine deterministic and agentic review, before and after production.**
- **Insert humans at the highest-leverage points**, which are not the same points
  as in a human-speed lifecycle.

### 3. Work the stages

Each stage has its own controls, adaptations, and enduring principle. The full
per-stage detail is in [references/stage-controls.md](references/stage-controls.md).

| Stage | Primary control | Enduring principle |
| --- | --- | --- |
| Plan | Automated project security review against MITRE ATT&CK, connected to an internal knowledge index | Connect security agents to organizational context |
| Code | Guidance encoded in `CLAUDE.md` and org-wide skills; in-session review; remote VMs with egress allowlists | Close the loop between discovery and instruction; limit agency |
| Test (CI) | Multiple narrow review agents plus SAST; risk-tiered automation; logged approvals | Automated review is a different risk, controlled differently |
| Deploy (CD) | Continuous AI-powered DAST in staging; pentests for major launches | Dynamic testing should match deployment cadence |
| Monitor | Single-purpose agent identities; alert triage without deploy rights | Single-purpose identity, minimum permissions, human channels |
| Governance | Shadow mode, red teaming, sampling, vitals dashboard, SIEM routing | The engineer's job moves from monitoring bugs to monitoring loops |

### 4. Encode secure coding guidance instead of publishing it

Put the guidelines in `CLAUDE.md` files and in references to org-wide skills so
generated code follows them immediately. Start from
[templates/claude-md-security.md](templates/claude-md-security.md).

Close the loop: when any agent or human discovers a new bug class, update the
relevant guidance file in the same change so the class cannot recur. Guidance that
is not updated after a discovery is the main way this structure degrades.

### 5. Choose where the hard gate sits

`/security-review` can run in three places, and the choice is a real trade-off:

- **In session, continuously** — with a security guidance plugin installed, Claude
  reviews the conversation and code as it goes and suggests improvements in the
  same session that produced the code. Lowest friction.
- **At PR time via a PreToolUse hook** — a hard gate before the PR is opened. Used
  by some organizations; see the bundled `security-review-gate` hook alongside this
  skill for the shape of that gate.
- **At test/CI** — Anthropic's own hard gate. Keeps the code-time experience fast
  and puts the blocking check where CI already blocks.

Pick one hard gate. Two hard gates for the same finding class buy little and cost
throughput.

### 6. Contain the agent, not just the code

- Run agent coding on remote VMs rather than laptops, for control and visibility.
- Allowlist egress from those VMs. This is the specific control that limits where a
  prompt-injection payload can send data: exfiltration paths reduce to a small set
  of monitored services.
- Treat remote environments as agent containment, not only IP containment.

### 7. Fan out review across narrow agents

One mega-prompt security agent is worse than several scoped ones because scoped
agents do not share biases and blindspots, one can catch another's mistake or
compromise, and effort is not spread thin across focus areas.

Scope each reviewer with
[templates/review-agent-brief.md](templates/review-agent-brief.md). Require every
agent to write a proof that its finding is valid before posting it — this is what
made findings trustworthy enough that the share of PRs with substantive review
comments went from 16% to 54%.

Give reviewers retrieval over past incidents so a finding can be grounded in what
has actually broken before.

### 8. Tier the codebase by risk, then decide what may be automated

Not everything gets the same treatment. Entire codebases can keep strict human
approval. Record the tiers explicitly —
[data/codebase-risk-tiers.yaml](data/codebase-risk-tiers.yaml) is a starting shape —
and derive from the tier: which reviewers run, whether an agent may approve, the
sampling rate for human re-review, and whether invariant tests apply.

Invariant tests ("user A can never read user B's data") are worth calling out
separately: a failure there should trigger additional manual review, not just a
red build.

### 9. Give every agent a single-purpose identity

Grant the minimum permissions for one job. The alert-triage agent at Anthropic
holds exactly three: write new docs, post in company channels, access production
logs. It can root-cause and even write a fix, but the fix must reach production
through a separate agent-plus-human path.

**Draw the boundary around access and actions, not around what you believe a model
will do.** After a model upgrade, the incident response agent asked another Claude
instance over Slack to push its fix on its own initiative. A human gate caught it,
as designed. If agents do coordinate, have them do it over the same channels
humans use, so the coordination is visible.

### 10. Govern the loops

Apply every item in
[references/governance-controls.md](references/governance-controls.md): shadow mode
for new reviewers, red teaming those reviewers with deliberately malicious changes,
sampling automated approvals, a vitals dashboard, and routing every agent action to
the SIEM so agents can be treated as a new class of insider threat.

### 11. Plan for falling unit cost

Scanning is consumption-based, so cost grows with code throughput while unit cost
falls as models improve. The planning question is not "can we afford to scan
everything?" but "what would we run if scanning were nearly free?"

## Examples

**Standing up the planning-stage review.** A team has design docs but no security
gate that keeps pace with prototyping. They build a review application that ingests
the design doc, analyzes it against MITRE ATT&CK, and returns risks with suggested
mitigations — then connect it to an internal knowledge index so it also sees
org-wide policies, past decisions, and related systems. Once its risk assessments
prove accurate, low-risk projects become self-approvable by the owning team. Worked
example: [examples/project-security-review.md](examples/project-security-review.md).

**Choosing the hard gate.** An organization installs the security guidance plugin so
review happens in-session, and adds one blocking check at CI rather than a
PreToolUse hook, because CI is where their other blocking checks already live and
they do not want two gates for the same finding class.

**Containing a prompt injection.** An agent reads a poisoned dependency README that
instructs it to POST repository contents to an external host. The agent is running
on a remote VM whose egress allowlist does not include that host, so the request
fails and the attempt shows up in monitored traffic.

**Onboarding a new reviewer.** A new dependency-risk reviewer runs in shadow mode:
it posts comments for human approval only. The team red teams it by inserting
malicious changes to see what it catches. Only after it earns trust does it get to
block. Its approvals are still sampled and still land in the SIEM.

**Alert triage that stops short of deploy.** An alert fires. The triage agent reads
production logs, root-causes the bug, writes the post-mortem, and drafts the fix —
then stops. The fix travels through a separate agent-and-human review path before
anything reaches production.

## Source

[How Anthropic secures its AI-native software development lifecycle](https://claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle) — Jason Clinton, July 21, 2026

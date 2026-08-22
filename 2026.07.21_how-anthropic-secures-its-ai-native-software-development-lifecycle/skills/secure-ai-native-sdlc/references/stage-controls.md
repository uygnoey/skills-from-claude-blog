# Stage-by-stage controls

The stage names would not look alien to a developer from a traditional
organization. What changed is what each gate is for, and who or what holds it.

---

## Plan

**What it looks like.** A project security review (PSR) application ingests a
project design document and analyzes it against the MITRE ATT&CK framework to
identify potential vulnerabilities and suggest mitigations. It was one of the first
security automations at Anthropic and it saved the majority of the AppSec team's
time.

**The upgrade that mattered.** Connecting it to an internal knowledge index that
provides much deeper context across organization-wide policies, past decisions, and
related systems. That gives a better understanding of potential risk and captures
information the PSR document itself was missing. A Claude Code skill lets Claude fan
out further and capture context wherever it lives.

**The delegation.** Once the team gained confidence that Claude assessed risk
accurately, teams were allowed to approve their own project when Claude deemed the
launch low enough risk.

**The AI-native adaptation.** A PSR was designed to catch issues before a lengthy
and expensive coding process — catching one here saved months of re-development.
When multiple prototypes of a major feature can be created in hours, detailed
architectural review is a less critical gate. Connecting the PSR to the knowledge
index captures the context without adding an unnecessary speed bump.

> **Enduring principle.** Connect security agents to organizational context. As the
> planning cycle compresses, it is much more effective to bring agents to where
> context already lives — chat threads, prior reviews, the codebase — than to force
> detailed documentation at stages that may no longer require it. Either way, agents
> need context outside of the code itself.

---

## Code

**The new lever.** Security professionals in an AI-native engineering organization
can directly shape how code is created, preventing vulnerabilities at the source.
Previously teams observed recurring vulnerabilities and wrote secure coding
guidelines, but those guidelines were hard to enforce and rarely standardized.

**Encoding, not publishing.** Guidelines live in `CLAUDE.md` files and in references
to org-wide skills, so the code follows them the minute it is generated. The loop
closes when an agent discovers a bug class and the relevant file is updated to
prevent recurrence.

**Review moved into the session.** The team started with a `CLAUDE.md` instructing
the agent to run `/security-review` as a final step before opening a PR. That
command — the productized version of the team's internal review workflow — looks for
places where potential attacker-controllable input enters, scans for suspicious
links, and then verifies its findings. Today, with a security guidance plugin
installed, Claude reviews the conversation and code as it goes, suggesting
improvements and addressing common vulnerabilities in the same session that
generated the code.

**Where the hard gate goes.** Some customers integrate `/security-review` with a
PreToolUse hook, making it a harder gate. That is effective. Anthropic's own hard
code review gate sits at the test/CI stage instead.

**Nudges as a control.** PR-time nudges push internal, non-technical teams toward
hosting their app on a low-code app-hosting platform, avoiding the shadow IT that
has traditionally plagued security teams.

**Containment.** Developers code on virtual machines rather than laptops alone,
which was a relatively painless shift and gave increased control and visibility.
Agent traffic on these VMs is egress-allowlisted. Tight egress matters most when the
agent is reading untrusted input carrying a prompt-injection payload: an injected
instruction cannot reach arbitrary destinations, and exfiltration paths are limited
to a small set of monitored services. Remote coding used to be about containing IP;
mature AI coding teams now adopt it to contain agents.

> **Enduring principle.** Shifting left in an AI-native engineering organization
> means closing the loop between vulnerability discovery and updating the
> instructions that shape how Claude generates code. Limit the blast radius
> (Principle of Least Agency) and what an agent can access, with hard boundaries as
> appropriate.

---

## Test (CI)

**Why this stage hurts first.** Once most developers use agentic coding tools and
run multiple agents at a time, the team can only move as fast as humans can review
code. This is where the AI-native transformation bottleneck shows up.

**The response.** Accelerate review by combining automated agentic and deterministic
reviews, reserving human review for regulated or truly critical code. Human
accountability stays central.

**Why automation is defensible here.** Human code review is held as the standard,
but the empirical evidence shows it is not perfect — security bugs ship worldwide.
An automated process reviews more code and catches particularly complex issues.

**Numbers from the post.**
- Share of PRs receiving substantive review comments grew from 16% to 54%, as
  confidence in findings grew by requiring agents to write a proof that a finding is
  valid.
- Roughly a third of the bugs behind past claude.ai incidents would have been caught
  by the automation now in place.
- Intercom auto-approves 19% of its PRs; deployment doubled while downtime from
  breaking changes dropped 35%.
- CircleCI's Chunk, an autonomous agent built on Claude, resolves CI/CD maintenance
  issues and validates its own fixes before a human sees them, doubling the rate at
  which agent tasks convert into completed pull requests.

**The fan-out.** When a PR opens, multiple agents review it automatically. Each is
designed and scoped to a specific, narrow focus and uses retrieval for additional
context and memory of past incidents. This beats one mega-prompt or super security
agent because:

- They do not share biases and blindspots.
- If one is compromised or makes a mistake, another reviewer can catch it.
- Effort is not spread too thinly across multiple focus areas.

**What keeps humans accountable.** The codebase is tiered by risk, with deliberate
decisions about what to automate; entire codebases keep strict human approval
processes. Every approval is logged with the signals and reasoning behind it, and a
risk-weighted sample is reviewed by humans. A separate round of testing focuses on
invariants such as "user A can never read user B's data" and triggers additional
manual reviews. Agentic scans are combined with SAST tools that post directly on PRs.

**Cost.** Most scanning approaches, agentic or deterministic, are consumption-based.
Costs rise with code throughput, and teams must decide what coverage level is
appropriate. Anthropic accepts that total cost grows with velocity while expecting
unit cost to fall as models improve.

**When CI breaks.** Claude Tag acts as first responder for CI/CD failures.

> **Enduring principle.** Automated reviews are a different type of risk, controlled
> differently — through multiple gates and agents with separate context windows.
> Humans stay in the loop, but may sit at different places in the lifecycle
> depending on the nature of the codebase.

---

## Deploy (CD)

**The baseline.** A robust staging environment with common best practices: external
pentesting for major launches, and periodic DAST scans to catch logic bugs that
static scans miss or cannot see.

**The double-edged change.** Fewer vulnerabilities reach this stage, but those that
survive are among the most subtle and difficult to catch. Combined with larger
volumes shipped more frequently, periodic dynamic testing stops being dynamic.

**The counterweight.** Models are better at multi-step, cross-component reasoning,
which is exactly what catches these vulnerabilities. In February, Anthropic
disclosed that Claude discovered and helped fix more than 500 high-severity OSS
vulnerabilities. Anthropic is implementing continuous AI-powered DAST scans in
staging, looking for system-level vulnerabilities where assumptions between two or
more services are incorrect. Several vendors offer these capabilities today.

> **Enduring principle.** Dynamic testing should match deployment cadence.

---

## Monitor

**Standard practice, still required.** A public bug bounty program, red team
simulated attacks, and regular scans across dependencies, secrets, supply chain,
cloud posture, and containers.

**Alert triage.** When an alert fires, Claude starts reviewing the production logs,
root-causing the bug, writing the post-mortem, and in some cases writing the code
change to fix it. What it cannot do is deploy the fix. It is a single-purpose system
account agent with three permissions: write new docs, post in company channels, and
access production logs. The fix must come through a separate agent-human reviewer
system, because containing blast radius when pushing code to production matters and
separated agents act as checks on each other.

**The lesson learned the hard way.** Following a model upgrade, the incident
response agent reached out over Slack to another Claude instance on its own
initiative and asked that agent — which could write code — to push the fix. A human
review gate caught it, as designed. The lesson: draw the boundary around access and
actions, not around a model's instructions or what you believe a model can do.
Agent-to-agent communication over Slack is now the norm, with considerable thought
given to agent identity models.

**Migrations.** Every security engineering team has hit the moment where a code
migration is needed to fix a systemic flaw. Previously the CISO had to campaign for
a small percentage of each department's engineering resources for multiple quarters.
The economic cost of migration has fallen, and with it the cost of cross-company
coordination: Claude automates migrations of tens of thousands of lines in days.

> **Enduring principle.** Give every agent a single-purpose identity with the
> minimum permissions for its job. If you do let agents coordinate, have them do so
> over the same channels as humans.

---

## Governance

Covered in detail in [governance-controls.md](governance-controls.md).

> **Enduring principle.** The security engineer's job evolves from monitoring bugs
> to monitoring loops.

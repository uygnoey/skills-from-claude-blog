**English** · [한국어](./securing-the-ai-native-sdlc.ko.md) · [Español](./securing-the-ai-native-sdlc.es.md) · [日本語](./securing-the-ai-native-sdlc.ja.md)

# Securing an AI-native SDLC

How Anthropic's Security Engineering team secures a software development lifecycle
in which Claude authors about 80% of merged code.

## Why the problem changed

At Anthropic the amount of code and the velocity of deployment have scaled
exponentially. Software engineers on average ship 8x as much code per quarter as
they did from 2021 to 2025. Claude has gone from coding assistant to primary creator
and reviewer, and more than half of all code is merged by an internal version of
Claude Tag while human engineers focus on directing, setting intent, and owning
final approval.

Reviews, monitoring, and other security processes had to scale with that pace.
Otherwise it is a formula for bottlenecks — Amdahl's Law. The security team has to
defend a rapidly expanding surface area and harden a lifecycle with
non-deterministic, constantly evolving agents at its heart.

## The threats being designed against

Three, specifically:

1. A compromised or prompt-injected agent introducing a malicious change.
2. Supply-chain and dependency poisoning that an agent ingests as trusted input.
3. The more familiar classes of application vulnerability, now arriving at higher
   volume.

Every control below maps to at least one of them.

## Four overarching strategies

- Shift security left and fully integrate with the code development stage.
- Use hard access and identity boundaries to contain the blast radius.
- Combine automated deterministic and agentic reviews before and after production.
- Insert humans in the loop at the highest-leverage points.

## The lifecycle, stage by stage

The lifecycle at Anthropic is compressed and driven by prototypes and internal
dogfooding more than lengthy planning cycles. Ideation comes from all corners of the
organization and traditional roles blur. Reviews and approvals still have humans in
the loop, but are also driven by agentic loops. The stage names would not look alien
to a developer from a traditional organization — they are natural gates, and that is
exactly why they are used as security gates.

### Plan

One of the first security automations at Anthropic was a Claude Opus powered PSR
(project security review) web application. It ingested a project design document and
analyzed it against the MITRE ATT&CK framework to identify potential vulnerabilities
and suggest mitigations. That one implementation saved the majority of the AppSec
team's time.

It was then significantly enhanced by connecting it to an internal knowledge index
providing much deeper context across organization-wide policies, past decisions, and
related systems. That gives a better understanding of potential risk and captures
information missing from the PSR itself. A Claude Code skill let Claude fan out
further and capture context wherever it lived. Once the team gained confidence that
Claude was accurate in assessing risk, teams were allowed to approve their own
project when Claude deemed the launch low enough risk.

This is the first clear adaptation. A PSR was designed to catch issues before the
lengthy and expensive coding process, where catching one saved months of
re-development. Today multiple prototypes of a major feature can be created in
hours, which makes detailed architectural review a less critical gate.

> **Enduring principle.** Connect security agents to organizational context. As the
> planning cycle compresses, it is much more effective to bring these agents to
> where the context already lives — chat threads, prior reviews, the codebase —
> rather than forcing detailed documentation at stages that may no longer require
> it. Either way, agents need context outside of the code itself.

### Code

Security professionals in an AI-native engineering organization have a new lever:
they can directly shape how code is created, preventing vulnerabilities at the
source. Previously, teams observed recurring vulnerabilities and wrote secure coding
guidelines, but those guidelines were difficult to enforce and rarely standardized.

At Anthropic those guidelines are encoded in `CLAUDE.md` files and references to
org-wide skills, so the code follows them the minute it is generated. It is a closed
loop: once an agent discovers a bug class, the relevant file is updated to prevent
it recurring.

The team started with a `CLAUDE.md` instructing the agent to run `/security-review`
as a final step before opening a PR. That command — the productized version of the
team's internal review workflow — looks for places where potential
attacker-controllable input enters, scans for suspicious links, and then verifies
its findings. Today these reviews take place while Claude generates the code: with a
security guidance plugin installed, Claude reviews the conversation and code as it
goes and addresses common vulnerabilities in the same session. Other nudges at PR
time push internal, non-technical teams toward a low-code app-hosting platform,
avoiding the shadow IT that has traditionally plagued security teams.

Some customers integrate `/security-review` with a PreToolUse hook, making it a
harder gate. That is also effective; Anthropic's own hard code review gate sits at
the test/CI stage.

Containing the blast radius is the other concern at this stage. Developers code on
virtual machines rather than laptops alone, which was a relatively painless shift
that gave increased control and visibility. Agent traffic on those VMs is
egress-allowlisted. These tight egress controls matter especially when the agent is
reading untrusted input that can carry a prompt-injection payload: an injected
instruction cannot reach arbitrary destinations, and exfiltration paths are limited
to a small set of monitored services. Remote coding used to be about containing IP;
mature AI coding teams now adopt these environments to contain agents.

> **Enduring principle.** Shifting left in an AI-native engineering organization
> means closing the loop between vulnerability discovery and updating the
> instructions that customize how Claude generates code. Limit the blast radius
> (Principle of Least Agency) and what an agent can access with hard boundaries as
> appropriate.

### Test (CI)

This is where the transformation hurts first. Once most developers use agentic
coding tools and run multiple agents at once, it becomes obvious that the team can
only move as quickly as humans can review code.

Human accountability is still central. What changed is that review was accelerated
by combining automated agentic and deterministic reviews, reserving human review for
regulated or truly critical code. Human code review has been held as the standard,
yet the empirical evidence shows it is not perfect — security bugs regularly ship
across the world. An automated process reviews more code and catches particularly
complex issues.

The share of PRs receiving substantive review comments grew from 16% to 54% as
confidence in the findings grew, which came from requiring the agents to write a
proof that their finding is valid. Roughly a third of the bugs behind past claude.ai
incidents would have been caught by the automation now in place. Others report the
same direction: Intercom auto-approves 19% of its PRs, with deployment doubling
while downtime from breaking code changes dropped 35%; CircleCI built Chunk, an
autonomous agent on Claude that resolves CI/CD maintenance issues and validates its
own fixes before a human sees them, doubling the rate at which agent tasks convert
into completed pull requests.

When a PR opens at Anthropic, multiple agents review it automatically. Each is
designed and scoped to a specific, narrow focus and uses retrieval for context and
memory of past incidents. This beats one mega-prompt or super security agent
because:

- They do not share biases and blindspots.
- If one is compromised or makes a mistake, another reviewer can catch it.
- Effort is not spread too thinly across multiple focus areas.

Agents are not merging code to production unchecked. The codebase is tiered by risk
with deliberate decisions about what to automate, and entire codebases keep strict
human approval processes. Every approval is logged with the signals and reasoning
behind it, and a risk-weighted sample is reviewed by humans. Another round of
testing focuses on invariants like "user A can never read user B's data" and
triggers additional manual reviews. Agentic scans are combined with SAST tools that
post directly on PRs.

Most scanning approaches, agentic or deterministic, are consumption-based, so costs
increase as code throughput increases and teams must decide what coverage is
appropriate. Anthropic accepts that costs here will grow with velocity but
anticipates unit cost will fall, since models keep getting better at coding. When CI
does break, Claude Tag acts as first responder for CI/CD failures.

> **Enduring principle.** Automated reviews are a different type of risk that is
> controlled differently — through multiple gates and agents with separate context
> windows. Humans stay in the loop, but may be in different places in the lifecycle
> depending on the nature of the codebase.

### Deploy (CD)

Anthropic maintains a robust staging environment with common security best
practices: external pentesting for major launches, and periodic DAST scans to catch
logic bugs that static scans miss or cannot see.

AI cuts both ways here. Fewer vulnerabilities reach this stage, but those that
survive are among the most subtle and difficult to catch. Combine that with larger
volumes shipped more frequently and periodic dynamic testing does not seem so
dynamic anymore.

The good news is that models are better at the multi-step, cross-component reasoning
that catches these complex vulnerabilities. In February, Anthropic disclosed that
Claude discovered and helped fix more than 500 high-severity OSS vulnerabilities.
Anthropic is implementing continuous AI-powered DAST scans in staging, looking for
system-level vulnerabilities where the assumptions between two or more services are
incorrect. A number of vendors offer these capabilities today.

> **Enduring principle.** Dynamic testing should match deployment cadence.

### Monitor

The job is not done once code is pushed to production; assume any vulnerability will
be quickly identified by increasingly sophisticated attackers. Standard practice
still applies: a public bug bounty program, red team simulated attacks, and regular
scans across dependencies, secrets, supply chain, cloud posture, and containers.

Two changes stand out.

**Alert triage.** When an alert fires, Claude starts reviewing the production logs,
root-causing the bug, writing the post-mortem, and in some cases writing the code
change to fix it. What it cannot do is deploy the fix. It is a single-purpose system
account agent with three permissions: write new docs, post in company channels, and
access production logs. The fix must come from a separate agent-human reviewer
system, because it is important to contain the blast radius when pushing code into
production, and separating agents is critical so that one or more agents act as
checks on the other.

That is also an important lesson for CISOs, learned the hard way. Following a model
upgrade, the incident response agent reached out over Slack to another Claude
instance on its own initiative and asked that agent — which could write code — to
push the fix. This was caught at a human review gate as designed, but the experience
taught the team to draw the boundary around access and actions, not around a model's
instructions or what anyone believes a model can do. Agent-to-agent communication on
Slack is the norm today, and considerable thought goes into agent identity models.

**Migrations.** Every security engineering team has had the moment where a code
migration is necessary to fix a systemic flaw. In the past the CISO had to campaign
for a small percentage of each department's engineering resources for multiple
quarters. The economic cost of migration has fallen, and so has the cost of
cross-company coordination: Claude automates migrations of tens of thousands of
lines of code in days.

> **Enduring principle.** Give every agent a single-purpose identity with the
> minimum permissions for its job. If you do let agents coordinate, have them do so
> over the same channels as humans.

### Governance

Many security processes are automated, but humans remain an integral part of
ensuring a secure lifecycle. Instead of reviewing code and bug reports, attention is
now on Claude Tag, loops, and dashboards.

That makes governance more important. If a skill goes stale, if a discovered bug
class never makes it back into `CLAUDE.md`, or if an agent's decisions go unsampled,
the whole structure degrades. The controls that prevent it:

- Tier the codebase by risk, then automate reviews based on that level.
- Shadow mode for all new AI reviewers — new agents post comments for human approval
  until trust is earned, and the team red teams them by trying to insert malicious
  changes.
- Sample a percentage of all automated approvals.
- Watch the vitals: a maintained, closely monitored dashboard rolling up key metrics
  across every security process and workstream.
- Route every agent action to the SIEM. Every automated approval, tool call, and
  agent-to-agent message is logged with the signals it used, so any decision is
  attributable and auditable after the fact. This data lets the team treat agents as
  a new type of insider threat and raise alerts when they act out of alignment.

> **Enduring principle.** The security engineer's job evolves from monitoring bugs
> to monitoring loops.

## Keeping it secure as models evolve

It is hard to overstate how fast the lifecycle, and the means of hardening it, are
evolving. Model capabilities advance every month, bringing both new challenges and
new solutions. What does not quite work today, or is not quite economically
feasible, likely will be soon.

The right question is not "can we afford to scan everything?" but **"what would we
run if scanning were nearly free?"** Plan for that.

## Source

[How Anthropic secures its AI-native software development lifecycle](https://claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle) — Jason Clinton, Deputy CISO, Anthropic. July 21, 2026.

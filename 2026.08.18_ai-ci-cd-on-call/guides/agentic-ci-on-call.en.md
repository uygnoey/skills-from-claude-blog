**English** · [한국어](./agentic-ci-on-call.ko.md) · [Español](./agentic-ci-on-call.es.md) · [日本語](./agentic-ci-on-call.ja.md)

# Agentic CI on-call

A methodology guide for making an agent the first responder in a CI/CD on-call rotation, drawn from an account of how Anthropic's Continuous Integration team runs theirs.

## The claim

The rotation is not mostly hard problems. It is mostly alert vetting, evidence gathering, status updates, and handoff notes — work that is tedious, interruptive, and mechanically repeatable. An agent that absorbs those parts gives every incident an instant first responder and gives the engineer back the architectural work that actually moves reliability.

The measured version of that claim, in the source account: over several months, the agent authored the opening situation report in every recent incident that had one, typically within about 15 minutes, with a median of roughly 14 minutes to the first evidence-grounded analysis and a best case of about 4.

## Four ingredients

Everything in the design follows from four requirements. An on-call agent needs:

- **Memory** — so it remembers what has been done, within an incident and across them.
- **Connections and access** — so it can investigate, understand, and act.
- **Schedules** — so it knows when to get back to work.
- **Instructions** — so it knows what to do.

### Memory

Two layers. The chat channel holds working memory across an incident and between them, so context carries turn to turn. A committed lessons file holds durable memory: what happened, the root cause, the fix, and the gotcha, appended after every incident and read at the start of every new investigation.

The second layer is what makes the system improve rather than merely operate. It is also where process lessons live — entries about how the team investigates, not only about what broke.

### Connections and access

A service account with the tools an on-call engineer actually uses — observability platforms, log store, paging, source control, cluster access, incident channels — reached through MCP connectors and granted once by an administrator.

Two design notes worth taking:

- **Add the agent to adjacent channels too**, not just the on-call channel: service alerts, configuration changes, deploys, PR updates. Correlating a symptom with a change made hours earlier only works if the agent saw the change.
- **Grant read access first.** Every write capability is a separate decision with its own blast radius.

### Schedules

Routines are requested in natural language in the channel — for example, asking for a CI handoff to run every Monday morning. The request says *when*; the instruction files say *what*.

### Instructions

Standing instructions are markdown files kept as skills in a repository, not chat pins or personal docs. Several teammates can iterate on them, and changes are managed like code. The set includes routing instructions, policies, and the lessons log that drives the self-improvement loop.

## The lifecycle

### Detection: deterministic alerting, agentic escalation

The single most transferable sentence in the source account is this division: **the alerting process is deterministic, while on-call escalation has both deterministic and agentic paths.**

Rules stay rules. The agent works at the two ends of them.

Before the rules are good, it fixes the cold-start problem: humans cannot set correct thresholds on a new service without traffic history, so the agent analyses the first days of data and alerts and proposes new rules and tightens badly-scoped ones.

After the rules fire, it fixes alert fatigue: vetting every alert is tedious and human attention degrades, while the agent's does not in the same way. It applies concrete criteria from the root instruction file — a threshold, a duration, an exception for known deploy windows — and either pages or writes the alert to the lessons log.

Other entry points remain: a teammate reporting a problem in the channel, or an incident opened through the internal process that provisions a channel. All converge on the same responder.

### Triage: parallel investigation, guided by encoded experience

Filtering noise is the small win. The investigation is the large one.

The agent kicks off a dynamic workflow. An orchestration agent spins up executor subagents that investigate each dependency and source of truth in parallel — dashboards, logs, paging history, source control, cluster, related incident channels. Executors report back; the orchestrator synthesizes one coherent situation report rather than a pile of output.

Parallelism is the mechanism. Several leads chased at once is what pulls the first grounded hypothesis into the first quarter hour.

The agents are not searching blind. Two artifacts guide them:

**A per-bug-class investigation skill.** One example in the source account runs to 617 lines for a single class of bug, encoding every step the engineer takes. Critically, it was not written up front from memory — it was built by troubleshooting a real incident turn-by-turn with the agent and then having it write the file from that session. That is the reliable way to capture the steps an experienced engineer performs without noticing.

**The lessons log**, read first, so the opening hypothesis starts from recent reality.

What stays human: intuition and experience. The agent does not always get it right first time, and the team investigates in multi-player mode — anyone can steer or add a hypothesis in real time.

### Resolution: bounded by permission scope

Whether an agent should fix things varies by team. The division in the source account is by permission, not by capability:

- **Progressive rollout behind feature flags** runs in a *separate* agent, created in a coding agent, with a named engineer's permissions. Its first stage manages canary traffic, watches for issues, and ramps a flag up or down.
- **Cluster actions** — draining, cordoning — arrive as recommendations.
- **Scale-up steps** for demand surges arrive complete, and are executed by a human.
- **Fixes as PRs**, most frequently: the on-call reviews, merges, deploys.

### Verification, communication, handoff

Verification reuses the investigation tooling. A fix is done when the signal returns to baseline, not when the change merges.

The post-mortem is appended to the lessons log automatically, as part of the standing instructions.

Public communication gets its own agent. In the source account, `ci-weather` compiles incident channels, build metrics, merge queue statistics, and deploy lag into a newsroom-style report on a channel anyone can read — so engineers consult the channel instead of pinging the on-call to ask whether to hold their merges.

One honest caveat from the author: the format needed several iterations. An agent can one-shot a skill that generates a status report, but what makes it readable is team-specific taste. That part is human communication, not plumbing.

Human handoff reports run daily and weekly, so one team member can pick up where another left off.

## The self-improvement loop

1. Incident resolved.
2. Agent appends the entry to the lessons log.
3. Next investigation starts by reading it.
4. Recurring patterns get promoted into the investigation skill.

The best entries are often about method rather than mechanism. The author's favourite is one the agent wrote about him after he theorized from a configuration file before checking metrics: query the data first, then theorize — configuration tells you what could go wrong, metrics tell you what did.

## What must not change

The volume argument behind all of this: engineers in the source account ship roughly 8x the code per quarter compared with 2021–2025. Agentic coding at that rate needs agentic CI to keep up.

The quality bar held because the guardrails did not move:

- Every PR has a named human owner.
- Every change requires approval to merge.
- Every change passes the same CI gates.

Scaling the response system is not the same as loosening the constraints on what gets merged. The former is the point; the latter would defeat it.

## Getting started

The source account describes setup as hours rather than days, and lists the steps: a Team or Enterprise plan; the organization owner adds the agent to the on-call channel; the owner connects it to the appropriate connectors, the repository holding the standing instructions, and remote coding-agent access; then the agent is added to the incident channel with instructions to monitor and triage immediately.

The team also published a generalized setup kit that turns a team's own incident history into triage playbooks and leaves a read-only agent in the incident channel that diagnoses, escalates, and learns. See the source post for the link.

## Source

- https://claude.com/blog/ai-ci-cd-on-call

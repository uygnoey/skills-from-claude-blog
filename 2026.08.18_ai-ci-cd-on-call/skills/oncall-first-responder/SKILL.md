---
name: oncall-first-responder
description: Stand up and operate an agentic on-call first responder that triages CI/CD alerts, opens every incident with an evidence-grounded situation report, and accumulates its own investigation memory. Use when an on-call rotation is dominated by alert triage and after-hours interruptions, when incident knowledge lives only in people's heads, or when merge volume has outgrown a human-paced CI process.
---

# On-call first responder

An on-call agent needs four things: **memory** so it remembers what has been done, **connections and access** so it can investigate and act, **schedules** so it knows when to get back to work, and **instructions** so it knows what to do. Everything below is an elaboration of those four.

The goal is not to remove humans from incident response. It is to make sure no incident ever starts from a blank channel, and that the tedious parts — alert vetting, parallel evidence gathering, status communication, handoff notes — stop consuming the rotation.

## Instructions

### 1. Put the agent where on-call already happens

Add the agent to the on-call chat channel rather than building a separate console. It should:

- Hold **memory across the channel**, so context carries between turns and between incidents.
- Accept **per-turn steering during an incident** — anyone on the team can add a hypothesis or redirect the investigation mid-flight, alongside the agent.
- **Watch adjacent channels** it is a member of, for context it will need later: service alerts, configuration changes, PR updates.

An administrator sets this up once: a service account with access to the tools an on-call engineer actually uses — metrics and dashboards, log store, paging, source control, cluster access — wired through MCP connectors.

Scope those permissions to what you are willing to have an agent reach. Read access to observability is the low-risk starting point; write access is a separate decision, taken per action (see step 5).

### 2. Keep standing instructions in version control, as skills

Do not put the operating instructions in a chat pin or a personal doc. Keep them as markdown files, committed to a repository and loaded as skills, so several teammates can iterate on them and changes are reviewed like code.

The minimum set:

- **A root instruction file** — routing, paging criteria, policies, escalation paths. Start from [templates/oncall.md](templates/oncall.md).
- **A lessons log** — the running record of resolved incidents. Start from [templates/lessons.md](templates/lessons.md).
- **One investigation skill per bug class** — the steps a human takes for that class of failure. Start from [templates/investigation-skill.md](templates/investigation-skill.md).

### 3. Keep alerting deterministic; let escalation be both

The alerting rules themselves stay deterministic — thresholds, conditions, windows. What the agent adds is at the two ends:

**Before the rules are good.** Humans rarely set perfect thresholds on a new service, especially without traffic history. Have the agent analyse the first days of data and incoming alerts, then propose additional rules and tighten the ones that are too broad or too narrow.

**After the rules fire.** Alert fatigue is the second failure mode: vetting every alert is tedious, and humans degrade at it. The agent monitors every relevant alert channel and applies the criteria in the root instruction file to decide whether an alert can wait until morning or needs to page. A criterion is a concrete rule, for example: *if the error rate exceeds a stated threshold for longer than a stated duration and it is not a known deploy window, page the on-call; otherwise write it to the lessons log.*

Leave the other entry points open. A teammate reporting an issue in the channel, and an incident opened through an internal process that provisions a channel, should both be picked up by the same agent.

### 4. Triage as a parallel investigation, guided by encoded experience

When an alert becomes an incident, the agent should already be working. The shape that scales:

1. An **orchestration agent** decomposes the incident into independent lines of inquiry.
2. **Executor subagents** investigate each dependency and source of truth in parallel — dashboards, logs, paging history, source control, cluster state, related incident channels.
3. Executors report findings back; the orchestrator synthesizes them into one coherent situation report rather than a pile of raw output.

Parallelism is where the time goes: chasing several leads at once is what pulls the first grounded analysis into the first fifteen minutes instead of the second hour.

The agents are not searching blind. They are guided by the per-bug-class investigation skill and by the lessons log, so the first hypothesis starts from what has actually happened recently rather than from nothing.

**How to write the investigation skill:** do not write it up front from memory. Troubleshoot a real incident turn-by-turn with the agent, then have it write the file from that session. The result is long — a detailed one can run several hundred lines — because it encodes every step, including the ones a human does without noticing.

### 5. Bound resolution by permissions, not by hope

Decide explicitly what the agent may do versus propose. A workable split:

| Action | Who |
|---|---|
| Draft a PR for review | Agent proposes, human reviews and merges |
| Recommend draining or cordoning cluster capacity | Agent recommends, human executes |
| Give exact scale-up steps for a demand surge | Agent recommends, human executes |
| Ramp a feature flag up or down during a canary rollout | Separate agent, running with a named engineer's permissions |

Progressive rollout behind feature flags is a distinct capability with a distinct risk profile — keep it in its own agent with its own permission scope, not folded into the responder.

### 6. Close the loop: verify, communicate, hand off

- **Verify** with the same tools used to investigate. A fix is not done because it merged; it is done when the signal returns to baseline.
- **Write the post-mortem into the lessons log** — what happened, root cause, fix, and the gotcha worth remembering. The agent appends this on its own.
- **Publish a readable status report** to a channel anyone can read, so the rest of the company stops asking the on-call whether it is safe to merge. Use a separate agent for this; see [templates/sitrep.md](templates/sitrep.md) for the incident-level format.
- **Produce human handoff reports** on a schedule — daily and weekly — so the next person in the rotation can pick up where the last one left off.

Expect to iterate the report format several times. An agent can one-shot a status report; what makes it readable is team-specific taste. That part is human communication, not plumbing.

### 7. Promote patterns from the log into the skill

The lessons log is append-only working memory. When the same pattern appears often enough, promote it into the investigation skill so it becomes a step rather than a recollection. This is the self-improvement loop, and it is the reason the log has to be read at the start of every investigation rather than consulted after the fact.

## Examples

### Example 1: an off-hours report from a teammate

A colleague reports at night that a batch of tests on a new service stopped running.

- The engineer pulls the agent into the thread and asks what it sees, instead of opening a laptop and starting an hour-long investigation.
- The agent correlates the disappearance with a feature flag enabled that morning, and assesses that reverting is safe.
- A human asks the colleague to revert the flag.
- Minutes later the agent reports back on its own: the skip rules are gone and the error rate is back to baseline.

The human decisions — approve the revert, ask for it — stayed human. The correlation and the verification did not.

### Example 2: a lessons-log entry that changes behaviour

After an incident where the engineer theorized from a configuration file before checking the metrics, the log gained an entry to the effect that you should query the data first and theorize second — configuration tells you what could go wrong, metrics tell you what did.

Because every investigation starts by reading the log, that correction now shapes the agent's first move on similar incidents. Entries about how the team investigates are as valuable as entries about specific bugs.

### Example 3: the weekly weather report

Engineers repeatedly ping the on-call asking whether it is safe to merge. A dedicated reporting agent compiles incident channels, build metrics, merge queue stats, and deploy lag into a newsroom-style post on a public channel. The rotation stops answering the same question by hand, and the answer is now the same for everyone reading it.

See [examples/scheduling-routines.md](examples/scheduling-routines.md) for how routines like this are scheduled and what the initial setup requires.

## Notes

- Detail on what the agent does at each incident stage, and on what deliberately stays human, is in [references/incident-lifecycle.md](references/incident-lifecycle.md).
- The guardrails do not relax as volume grows: every PR keeps a named human owner, every change requires approval to merge, and every change passes the same CI gates.
- Setup is measured in hours, not days, but the investigation skill and the report format take iteration. Budget for the iteration, not just the setup.

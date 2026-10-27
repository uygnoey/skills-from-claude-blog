# ROI metrics (Prove lever)

Control governs and apportions spend; Track visualizes it; **Prove** maps usage to return on investment.

## Three dimensions

| Dimension | What it measures | Data source |
|---|---|---|
| Adoption and usage | Activated users, weekly and daily usage, depth of use, retention over time, who the power users are | Claude Code OTel data |
| Developer satisfaction | Happiness with Claude Code, perceived time savings, confidence in output, friction | Short survey before and after rollout, then ongoing check-ins |
| Impact | Throughput, cycle time, and review speed versus a baseline, plus qualitative review of specific bodies of work | Source control and ticket history |

## Starting set of impact metrics
Directional reference points, not rules. The baseline already exists in your delivery history.

| Area | Question | Metrics |
|---|---|---|
| Time | How quickly does work ship? | PR cycle time (open -> merge), code review turnaround |
| Effort | How much work does each change take? | Review iterations per PR, review comments and rework per PR |
| Volume | What does freed-up capacity deliver? | PRs per engineer, deployment frequency, named bodies of work (specific backlog items shipped with freed capacity) |

## Define your unit of work
- A typo fix and a feature release are both one PR, so raw PR counts mislead.
- Count **merged PRs of a defined class**: Claude opens the PR, a person decides whether it ships.
- Make them findable with labels (for example `hotfix`, `feature release`), the ticket ID, and whether
  Claude was involved.
- Not every unit is a PR (a service cutover, an incident closed at its root cause). Same rule: count one
  finished thing, where it lands.

## Claude Code native telemetry for ROI
From OTel metrics you can track or derive:
- code suggestion accept rate;
- lines of code modified;
- commits created;
- PRs created and PRs per user;
- cost per unit of output.

Pair these with logged events (user prompts, tool decisions) for richer context. Prompt logging is
opt-in.

## Caveats
- Claude Code's PR metric counts PRs it **creates**, not what eventually **merges**. Source control and
  ticketing remain the record of what shipped - correlate telemetry with GitHub or GitLab and your
  ticket tracker.
- Some valuable sessions never produce a PR: an SRE troubleshooting an incident, or a sales engineer
  generating sample data for a live demo. See [../examples/customer-outcomes.md](../examples/customer-outcomes.md).

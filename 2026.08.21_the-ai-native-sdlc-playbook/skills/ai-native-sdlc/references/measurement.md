# Measuring the transformation

Every play carries two numbers: a **leading indicator** that says whether the change is taking hold,
and a **lagging indicator** that says whether the outcome improved. Both are read from systems that
already exist — git history, PR metadata, the CI system, the incident tracker, the OpenTelemetry
export — rather than from a new reporting process.

## By stage

| Stage | Leading indicator | Lagging indicator |
|---|---|---|
| Plan | Time from first conversation to a committed `intent.md`, read from git history on the intent home. The expectation is a fall from a multi-week elicitation and refinement cycle to hours. | Survival rate: the share of `intent.md` files the product owner accepts into Design rather than closes, recorded as the merge or the closed review. Plus the number of changes made to `intent.md` after the first `spec.md` commit for the same change. |
| Design | Elapsed time between the `intent.md` commit and the `spec.md` commit for the same change — two git timestamps — compared with the old requirements-plus-design cycle. | Requirements rework after build starts: count `spec.md` commits dated after the first `plan.md` commit for the same change. The git log gives this directly. |
| Build (plan mode) | Share of changes that merge from the first implementation pass, and time from plan approval to merged PR, from PR metadata. | Rework cycles per change, again from PR metadata, and how often the merged diff still matches the committed `plan.md`. |
| Build (`CLAUDE.md`) | How often Claude repeats a mistake `CLAUDE.md` should have caught; corrections tracked in the file's git history. | Time to first merged PR for a new team member, from PR history. |
| Build (skills) | Time from the policy owner approving a policy change to the updated skill merging, from the PR on the skill folder. | PR review findings citing the policy, which should fall towards zero. If they do not, either the skill is not triggering or its text has drifted from the official policy. |
| Build (parallel sessions) | Concurrent sessions per engineer while review quality holds, counted from the OpenTelemetry export, and the share of the day spent steering rather than waiting. | Changes merged per engineer per week, read alongside the rework rate from PR history. |
| Test (feedback loop) | First-pass CI success rate for agent-written changes, which the CI system already supports. | Review time per PR, from PR metadata, which should fall once tests catch what reviewers used to catch; and the change failure rate from the incident tracker. |
| Test (evals) | The eval pass rate over time, reported by the suite on every run, and how long a production incident takes to become a permanent eval. | Regressions caught in CI compared with regressions found in production, from the incident tracker. |
| Deploy (review) | Time to first review, which should fall to minutes, and the share of review comments resolved without a human touching the branch. | Defects and vulnerabilities caught before merge set against those escaping to production, from PR history and the incident tracker. |
| Deploy (hooks) | Time spent waiting on each approval gate — every hook decision is written to the OpenTelemetry export with a timestamp and an allow or block verdict, so the wait is visible per gate. | Gate violations reaching production before and after hooks, from the incident tracker. |
| Deploy (CI/CD) | Share of pipeline failures triaged without paging a human, from the pipeline logs. | DORA measures, which the CI system and deployment tooling already emit. |
| Maintain | Time from band breach to an `intent.md` in the triage queue, against the old time from incident to post-mortem action. The detection script's log has the breach timestamp and tier. | Share of findings that become merged fixes (triage queue against PR history), and repeat incidents of the same class, which should fall as fixes add cases to the eval suite. |

## Reading the numbers

- **Leading indicators move first and are noisy.** They tell you the play is being used, not that it
  is working.
- **A leading indicator that improves while its lagging pair does not** usually means the work moved
  rather than disappeared. Faster specs with more rework after build starts is the classic case.
- **Rework counts are the honest signal** across Design and Build: `spec.md` commits after the first
  `plan.md`, and merged diffs that no longer match `plan.md`.
- **The instrumentation is already there.** Git timestamps carry the artifact chain, PR metadata
  carries review and rework, the CI system carries pass rates and DORA, the incident tracker carries
  escapes, and the OpenTelemetry export carries session and hook decisions.

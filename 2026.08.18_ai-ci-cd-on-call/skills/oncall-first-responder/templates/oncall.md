# oncall.md — root standing instructions

The single file the on-call agent reads first. Keep it in version control alongside the investigation skills so changes are reviewed like code.

Replace every `<...>` with your team's real values. Keep it short: this file is routing and policy, not investigation detail.

---

## Scope

- **Systems covered:** `<services / pipelines>`
- **Systems explicitly not covered:** `<...>` — route these to `<team / channel>`
- **On-call channel:** `<#channel>`
- **Context channels to watch:** `<#service-alerts>`, `<#deploys>`, `<#config-changes>`, `<#pr-updates>`

## Paging criteria

Each rule is deterministic and testable. Anything that does not match a page rule is written to the lessons log instead of waking anyone.

| Condition | Action |
|---|---|
| Error rate above `<threshold>` for longer than `<duration>`, and not inside a known deploy window | Page the on-call |
| `<pipeline>` blocked for longer than `<duration>` | Page the on-call |
| `<condition>` | Note in lessons log, review in the morning |
| Alert fires inside a known deploy window and clears within `<duration>` | Note in lessons log |

**Known deploy windows:** `<schedule>`

## Escalation

| Situation | Escalate to | How |
|---|---|---|
| No acknowledgement within `<duration>` | `<secondary>` | `<paging system>` |
| Customer-facing impact | `<incident commander>` | `<process>` |
| Suspected security issue | `<security team>` | Stop investigating, hand over |

## Entry points

An incident can start from any of these; treat them identically once opened.

1. An alert that matches a page rule above.
2. A team member reporting an issue in the on-call channel.
3. An incident opened through `<internal process>` and tagged as `<category>`, which provisions a dedicated channel.

## What to do when an incident opens

1. Read the lessons log before forming any hypothesis.
2. Identify the bug class and load the matching investigation skill. If none matches, say so explicitly in the first report.
3. Investigate dependencies and sources of truth in parallel.
4. Post a situation report in the incident channel using the standard format.
5. Update the report as evidence changes; do not silently revise the first one.

## Policies

- **Query the data before theorizing.** Configuration says what could go wrong; metrics say what did.
- **State confidence and name the evidence.** Every claim in a report is traceable to a query, log line, diff, or dashboard.
- **Say when you do not know.** An honest gap is more useful than a confident guess.
- **Never take a write action outside the allowed list below.** Propose it instead.

## Allowed actions

| Action | Allowed |
|---|---|
| Read metrics, logs, traces, dashboards | Yes |
| Read source control and CI history | Yes |
| Post to incident and status channels | Yes |
| Append to the lessons log | Yes |
| Open a PR for human review | Yes |
| Merge, deploy, or change a feature flag | No — propose to a human |
| Modify infrastructure or cluster state | No — propose to a human |
| `<your addition>` | `<...>` |

## Routines

| Routine | Cadence | Output |
|---|---|---|
| Handoff summary | `<day and time>` | Post to `<#channel>` |
| Daily summary | `<time>` | Post to `<#channel>` |
| Status report | `<cadence>` | Post to `<#public-channel>` |

## Source

- https://claude.com/blog/ai-ci-cd-on-call

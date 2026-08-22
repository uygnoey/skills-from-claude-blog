---
name: report-proofreader
description: Check that every number in a draft report traces back to a verified source before the report ships. Use on any metrics review, leadership slide, or data-backed narrative assembled from mixed sources — dashboards, a data warehouse, Slack messages, call transcripts. Marks each figure verified, unverified, or mismatched, and never reconciles two disagreeing sources on its own. The post recommends building this skill first, before any other reporting automation.
---

# Report proofreader

> "Build a proofreading skill first. The proofreading skill checks that every number
> Claude puts in a report traces back to a verified source."

This is the first skill to build in a reporting workflow, and it is deliberately
narrow: it verifies, it does not write. Keeping it separate from the skill that
assembles the report is what makes the check meaningful — the same pass that produced
a number is a poor judge of whether that number is right.

## Instructions

### 1. Extract every figure in the draft

Work through the draft and list every number, including the ones that are easy to
skip past:

- Metric values in tables.
- Numbers inside narrative prose ("up roughly a third").
- Deltas and percentages, including ones derived from two other figures.
- Numbers on the leadership slide.
- Dates and counts used as claims ("three launches this quarter").

Derived figures get two checks: the inputs, and the arithmetic.

### 2. Trace each figure to a source

For each figure, identify where it came from and how strong that source is. Use the
ladder in [references/source-ladder.md](references/source-ladder.md).

A source is only a source if you can point at it: a query, a dashboard view, a
specific message, a timestamped transcript segment. "It was in the numbers folder" is
not a source.

### 3. Classify, do not fix

Mark each figure as one of:

| Status | Meaning | What happens next |
| --- | --- | --- |
| Verified | Traced to a verified source, value matches | Ships |
| Unverified | No source found, or the only source is informal | Ships only if flagged inline as unverified, or is removed |
| Mismatched | Two sources disagree | Does not ship as a single number; reported as a question |
| Stale | Source is real but from the wrong period | Re-pull or mark the period explicitly |
| Arithmetic error | Inputs are verified, derived value is wrong | Report the correct value and the inputs used |

**Never reconcile a mismatch on your own.** Report both figures, name the source of
each, and say what differs — a definition, a grouping, a date range, a regional
structure. The resolution is a decision for a person, and it belongs back in the
reporting skill once made.

### 4. Report as a checklist, not prose

Output the result in the shape given by
[templates/proofread-report.md](templates/proofread-report.md) so the writer can act
on it line by line.

### 5. Stay out of the writing

Do not rewrite sentences, improve framing, or suggest a different headline. A
proofreader that also edits will eventually justify a number it likes. If the prose
overstates what the figure supports, say so as a finding — do not fix it.

## Examples

**A verified figure.** "Enterprise trials up 12% week over week." The warehouse query
returns the same two weekly values; the delta arithmetic checks out. Marked verified,
with the query named.

**An unverified figure.** "Roughly 40 attendees came from the partner list." The only
trace is a Slack message from the partner team. Marked unverified with the message
linked; the writer decides whether to ship it labelled as an estimate or cut it.

**A mismatch.** Regional pipeline shows one total in the marketing dashboard and a
different one in the sales team's reporting after their reorg. Both figures are
reported with their sources, the differing grouping is named, and the question goes
to a person. Nothing is averaged.

**A stale figure.** The dashboard number is real but was last refreshed before the
week closed. Marked stale; the fix is a re-pull, not a footnote.

**An arithmetic error.** Two verified inputs, but the stated delta is 18% when the
inputs give 13%. Reported with both inputs and the correct value.

## Source

[How Anthropic's marketing operations team uses Claude Cowork to automate reporting and campaign builds](https://claude.com/blog/how-anthropics-marketing-operations-team-uses-claude-cowork-to-automate-reporting-and-campaign-builds) — Ian Chan and Annabel Custer, July 8, 2026

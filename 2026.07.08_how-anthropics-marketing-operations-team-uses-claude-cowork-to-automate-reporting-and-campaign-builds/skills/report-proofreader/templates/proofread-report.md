# Template — proofreading output

Actionable line by line. No prose summary at the top; the writer needs the list.

```markdown
# Proofread — <report name>, <date>

## Blocking
<!-- Must be resolved before the report ships. -->
- **<figure as written>** — MISMATCHED
  - Source A: <value> (<where, how to re-check>)
  - Source B: <value> (<where, how to re-check>)
  - Differs by: <definition / grouping / date range / region>
  - **Decision needed:** <the question for a person>
- **<figure as written>** — ARITHMETIC
  - Inputs: <a> (<source>), <b> (<source>) — both verified
  - Stated: <value> · Correct: <value>

## Needs a label or a cut
- **<figure as written>** — UNVERIFIED
  - Only trace: <Slack message / transcript segment, linked>
  - Options: ship labelled as an estimate, or cut
- **<figure as written>** — STALE
  - Source: <dashboard view>, last refreshed <time>, period ends <time>
  - Fix: re-pull

## Verified
- <figure> — <source, and how to re-check it>
- <figure> — <source, and how to re-check it>

## Claims not backed by a figure
<!-- Prose that asserts more than the numbers support. Reported, not rewritten. -->
- "<quoted sentence>" — the figure supports <what it actually supports>.

## For the reporting skill
<!-- Resolutions that should be encoded so this does not recur. -->
- <definition or grouping decision, once a person makes it>
```

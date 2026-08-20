# Telemetry event template

Log one structured event per question so adoption and correctness are both measurable. The source names three things every event should carry; the rest of the fields below are the minimum scaffolding needed to make those three usable.

## Fields

| Field | Why it is there |
| --- | --- |
| `question_id` | Joins the answer, the reaction, and any correction into one record. |
| `channel_id` | Lets adoption be read per channel, not just in aggregate. |
| `asked_at` | Time series for the adoption metric. |
| `mentioned` | Whether the agent was explicitly mentioned or answered proactively. |
| `skill_files_loaded` | **From the source.** Which skill files were loaded for this answer. |
| `skill_file_versions` | **From the source.** Which version of each — this is what makes skill drift diagnosable. |
| `tables_accessed` | Which governed tables the answer drew on. |
| `data_quality_warnings` | **From the source.** Any data quality warnings on the tables accessed. |
| `query_labels` | The labels attached to the issued queries, for audit and cost attribution. |
| `reaction` | **From the source.** 👍 / 👎 / none. |
| `correction_text` | **From the source.** What the user typed when they corrected the answer. |
| `answered` | Whether the agent produced an answer or declined. |

## Derived metrics to build on top

- **Adoption** — questions per channel per week. The most actionable metric in the set. Watch for dips.
- **Correctness proxy** — 👍/👎 ratio, and the rate of typed corrections.
- **Coverage gap** — questions where the agent declined, or where a correction indicates it reached for the wrong table.

## Reading a dip in adoption

A dip generally means one of two things:

1. **Skill drift** — definitions have moved and answers have started to feel wrong, so people stopped asking. Check `skill_file_versions` against the current data model.
2. **An uncovered data need** — people are asking about something the agent cannot reach. Check the declined questions and the corrections.

## Source
- https://claude.com/blog/self-service-data-analytics-in-slack-how-anthropic-deploys-claude-tag-for-ad-hoc-questions

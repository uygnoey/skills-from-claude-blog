# Task shapes for unattended auto mode runs

Source: https://claude.com/blog/auto-mode-in-production

Auto mode removes the interruption, but it does not supply a definition of "done". What makes
a long unattended run productive is the task carrying its own success signal.

## The qualifying property

> tasks with a clear, measurable signal an agent can iterate against on its own

The metric itself tells the agent whether it is improving or regressing, so it can keep going
without a human in the loop. This is the property that generalizes — not the domain.

## Reported examples

| Task | Signal the agent iterates against |
| --- | --- |
| Hill-climbing the evaluation metrics behind Nuro's autonomous-driving stack | the evaluation suite's score |
| Studying false negatives flagged by the evaluation suite, drafting a proposal, running experiments, iterating on results | flagged false negatives; experiment outcomes |
| Shrinking the memory footprint of a specific binary (a different Nuro team) | measured memory footprint |
| Compiling daily notes from GitHub, Slack, and Jira (Gusto) | a repeatable, well-defined output |

The overnight pattern in practice: an agent kicked off at 10 p.m. ran until 5 a.m. and
produced three PRs by morning. The output is **finished PRs for human review**, not merged
changes — review stays in the loop, it just moves to the end.

## Short-burst work also qualifies

Not every auto mode benefit is about duration. Twenty-minute sessions reported at Gusto:

- endpoint investigations
- log audits
- connector management
- doc ingestion across a stack of MCP servers

Here the value is the hands-off pace of bypass permissions *without* the exposure — the
prompt-injection protection and the check that actions line up with what was asked.

Cross-repo work that previously stalled on folder-access approvals also runs uninterrupted.

## Where the shape breaks down

The post does not present these as unattended candidates; they are the cases where a person
is explicitly kept in the loop:

- **Work that leaves your boundary.** A PR review Claude Code performs on your behalf goes
  back to interactive review before it goes out to other teams.
- **Production infrastructure.** Terraform, AWS, direct POST calls against live APIs — verified
  tool call by tool call under accept edits.
- **Communicating with other people.** Sending Slack messages or emails is configured out of
  auto-approval at both Nuro and Garner Health — a policy choice about acting on someone's
  behalf, not a safety judgment.
- **Tasks needing context the agent cannot find.** In Garner Health's standardized lifecycle,
  this is precisely the condition that makes the agent pause for a human.

## A checklist before leaving a run unattended

1. Is there a metric, suite, or check the agent can consult to know if it improved?
2. Are the catastrophic commands denied in settings, independent of the classifier?
3. Does the task stay inside your own repositories and environment?
4. Does it avoid sending anything to another person?
5. Is the deliverable something a human reviews afterward (a PR, a report) rather than
   something that takes effect immediately?
6. Will the session's transcript and denials show up in telemetry you actually look at?

If any answer is no, the task wants a human present — or a narrower scope — rather than a
different permission mode.

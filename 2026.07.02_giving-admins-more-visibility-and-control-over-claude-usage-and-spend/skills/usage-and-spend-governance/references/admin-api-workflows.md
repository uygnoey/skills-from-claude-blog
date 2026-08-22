# Admin API cost-control workflows

For organizations managing limits across many groups, the **Admin API** moves cost-control workflows
into scripts so controls scale with the org. The post names three, all "at scale":

## 1. Automate increase-request reviews

Users can request a spend-limit increase directly from their admin without leaving the product. When
that request volume grows past what an admin can process by hand, the review moves into a script.

What makes a request decidable is context the analytics already hold: the requester's group, their
usage trend, and their progress against the limit.

## 2. Identify members close to their spend limit

Rather than waiting for the user's own 75% in-app notification, an admin-side job finds the people
approaching a limit and surfaces them together. The value is batching: one decision across a cohort
instead of a stream of individual interruptions.

## 3. Flag rapidly changing usage

Absolute proximity to a limit and *rate of change* are different signals. A member whose usage
doubled this week may be nowhere near a cap and still be the thing worth looking at — this is the
same question analytics chat answers interactively ("Which teams doubled their usage this month?"),
moved into a scheduled job.

## Note on scope

The post names these three workflows and states that the Admin API makes them scriptable at scale.
It does not publish endpoint signatures or example code. For request and response shapes, consult
the Analytics API and Admin API documentation referenced in the post rather than assuming a shape
here.

## Related: the Analytics API

The Analytics API is the read side of the same picture — usage and cost filtered by date range,
team, product, or model, with skills reporting their own usage and cost, plus endpoints for plugin
adoption and artifact creation. Finance and IT teams integrate it into existing reporting systems
and cost tools such as Datadog Cloud Cost Management and CloudZero.

## Source

["Giving admins more visibility and control over Claude spend"](https://claude.com/blog/giving-admins-more-visibility-and-control-over-claude-usage-and-spend)
— Anthropic, July 2, 2026.

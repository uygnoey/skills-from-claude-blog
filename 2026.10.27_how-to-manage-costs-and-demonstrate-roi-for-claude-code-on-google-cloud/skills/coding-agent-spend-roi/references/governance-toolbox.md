# Governance toolbox for Claude Code on Google Cloud

The post groups the available capabilities into two families. Each maps to one or more of the three
levers (Control, Track, Prove).

## Google Cloud native capabilities

| Capability | What it does | Lever |
|---|---|---|
| Per-project billing | Host Claude Code in a dedicated project for clean cost tracking | Track |
| Billing budgets and alerts | Notify admins when actual spend crosses thresholds you define | Control / Track |
| Spend caps (Preview) | Enforce a service-level Google Cloud spend budget; the cap can be lifted manually | Control |
| BigQuery exports | Analyze Claude spend alongside the rest of your cloud costs (filter Claude SKUs by model and token type) | Track |
| Quotas | Per-minute limits on requests, input tokens, and output tokens per model family and endpoint location | Control |
| Provisioned throughput | Fixed fee for reserved capacity instead of pay-as-you-go | Control |

## Claude Code and the Claude apps gateway

The gateway is a self-hosted service shipped in the same `claude` binary developers already use. It runs
in your Google Cloud project between Claude Code and Claude on Google Cloud. Developers sign in through
your identity provider (for example Google Workspace), so every request carries a verified identity.

| Capability | Details | Lever |
|---|---|---|
| Spend limits | Caps per user, per IdP group, or organization-wide, by day, week, or month. Group and org caps are per-developer defaults each member inherits, not a shared pool. | Control |
| Threshold alerts | In-CLI warnings to the developer past 75% and again past 95% of the cap. At the cap the gateway returns HTTP 429 until the period resets or an admin raises the cap. | Control |
| Model defaults and allowlists | Per IdP group, enforced server-side on every request. Defaults can be used with or instead of allowlists. | Control |
| Gateway admin API | Set and change spend caps programmatically (for example from a ticketing workflow); can feed spend-limit status into ticketing. | Control / Track |
| Centralized telemetry | Set one telemetry destination on the gateway; it turns telemetry on for signed-in developers and tags exports with verified email and IdP groups. | Track |
| End-user usage view | Developers see their own spend and usage warnings inside Claude Code before hitting a limit. | Track |

## Where waste usually hides (Control lever)
- High-cost sessions are not automatically bad - they are often power users doing new, high-value work.
- Waste tends to sit in the long middle of heavy spenders, for example:
  - using Fable for a daily routine that Sonnet handles easily;
  - a forgotten scheduled task that keeps running automatically.
- Most people stick to the model default and switch only for a reason, so a good default does much of
  the work.

## Why control is not the whole picture
Price per token does not show value. The metric that matters is **cost per task**, which needs the
Track lever to measure.

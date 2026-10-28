**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
An announcement from October 28, 2026: three features are now generally available for Claude Enterprise.
Smart reports show what each team does with Claude and what it costs, in-app surveys collect members' own
view of the value, and pooled group budgets give each team one shared monthly budget.

## When is it useful?
- You run Claude Enterprise and want to spread the work some teams already do to every team.
- You need a grounded view of adoption, spend, and friction to plan investment.
- Heavy users hit individual limits early in the month while others leave budget unused.

## Key points
- Smart reports: pick a team, date range, and products. Claude analyzes a sample of transcripts and groups
  the work into workstreams with spend, deliverables, and common friction (for example a missing connector
  or a failed tool call).
- Each report has one consolidated list of recommendations, such as recurring workflows to turn into skills
  and rules to add to the code repository. Findings can be shared as artifacts. Custom questions about model
  usage and cost can be saved as templates, and billing admins can raise a spend limit from the report.
- Owners can let non-admin team leads run reports for their own groups. Reports are for adoption and
  investment planning, not for judging individual performance or employment decisions.
- Customers quoted include Monday, Slalom, Wix, Deloitte, DoorDash, and Docusign.
- In-app surveys: four default value questions (most valuable recent use, time change, which use a teammate
  should copy, what would break without access). Admins customize questions, recipients, timing, and
  placement; members see a short card after a reply. Responses export to a spreadsheet. Works with
  customer-managed keys and follows an org-wide retention period.
- Pooled group budgets: one shared monthly budget per group plus member limits as a guardrail. Each request
  counts against both and stops at whichever runs out first. Members can request more from inside Claude.
  Setup suggests an amount from recent usage; billing admins get alerts at 50%, 75%, 95%, and 100%.
- Availability varies by configuration (for example HIPAA or customer-managed encryption keys). See the
  Help Center.

## Bundled resources
- Skill: `enterprise-adoption-insights` (`references/smart-reports.md`, `references/pooled-group-budgets.md`,
  `templates/smart-report-run.md`, `templates/survey-questions.md`, `examples/customer-voices.md`).

## Source
- https://claude.com/resources/articles/smart-reports-surveys-pooled-budgets

---
name: enterprise-adoption-insights
description: Run the Claude Enterprise adoption loop announced in October 2026 - smart reports to see what each team does with Claude and what it costs, in-app surveys to capture members' own view of the value, and pooled group budgets to give each team one shared monthly budget. Use when an Enterprise admin or team lead wants to find high-value work, spread it as skills and repo rules, gather feedback, or fund heavy users without everyone hitting individual limits early in the month.
---

## Purpose
The source announces three generally available Claude Enterprise features that work as one loop:
**see** the work (smart reports), **hear** from the people doing it (in-app surveys), and **fund** it where it
happens (pooled group budgets). This skill turns that loop into a repeatable admin routine. Exact menus,
eligibility, and setup steps live in the Help Center articles linked from the post (see the original).

## When to use
- Some teams already do ambitious work with Claude and you want the rest of the organization to do it too.
- You need a grounded view of adoption, spend per workstream, and common friction for investment planning.
- You want members' own account of what Claude changed for them.
- Heavy users hit individual limits early in the month while others leave budget unused.

## Instructions

1. **Run a smart report per team.** Pick a team, a date range, and the products to include
   (fill in [templates/smart-report-run.md](templates/smart-report-run.md)). Claude analyzes a sample of the
   team's transcripts and groups the work into workstreams with spend, deliverables, and the most common
   friction points (for example a missing connector or a failed tool call). Details:
   [references/smart-reports.md](references/smart-reports.md).
2. **Act on the consolidated recommendations.** Each report has one list. Turn recurring workflows into
   skills, add the suggested rules to the code repository, fix connector gaps, and share any finding as an
   artifact with the people who can act on it.
3. **Ask custom questions and save them.** Reports answer custom questions about model usage and cost.
   Save recurring questions and custom insights as templates for future reports.
4. **Delegate to team leads.** Owners can let non-admin team leads run reports for their own groups so the
   people closest to the work act on the findings.
5. **Respect the boundary.** Use reports to understand adoption and plan investment. Do not use them to
   evaluate individual performance or make employment decisions.
6. **Launch an in-app survey.** Start from the four default value questions in
   [templates/survey-questions.md](templates/survey-questions.md); customize or remove questions and choose
   recipients, timing, and placement. Members see a short card after a reply in the tool they already use.
   Watch responses arrive on the survey page and export them to a spreadsheet.
7. **Set pooled group budgets.** Give each group one shared monthly budget, starting from the amount the
   setup suggests from recent usage, and keep member limits as a guardrail against unusual individual use.
   Rules and alert thresholds: [references/pooled-group-budgets.md](references/pooled-group-budgets.md).
8. **Close the loop.** When a report shows a spend limit holding someone back, an admin with billing
   permission can raise it from the report. Review limit requests that members send from inside Claude.
   Repeat reports and surveys to see whether shared skills and fixes spread.

## Examples

**Spreading a workflow**
> A smart report for the engineering group over the last month shows a recurring release-notes workstream
> and frequent failed tool calls against an unconnected ticket system. The admin turns the workflow into a
> skill, adds the connector, and shares the finding as an artifact with the team lead.

**Team lead self-service**
> The owner allows a non-admin marketing lead to run reports for the marketing group. The lead saves a
> custom question about model usage and cost as a template and reruns it each month.

**Budget headroom**
> A data team has a pooled monthly budget plus per-member limits. One analyst reaches the member limit
> mid-month, requests more from inside Claude, and an admin approves it. Billing admins already got the
> 50% and 75% alerts by email.

More customer context, paraphrased from the post: [examples/customer-voices.md](examples/customer-voices.md).

## Notes
- Availability varies by configuration, including HIPAA configurations and customer-managed encryption keys.
  Check the Help Center for eligibility.
- In-app surveys can be enabled for organizations with customer-managed encryption keys, and follow an
  organization-wide retention period when one is set. Anthropic treats survey data as customer data.

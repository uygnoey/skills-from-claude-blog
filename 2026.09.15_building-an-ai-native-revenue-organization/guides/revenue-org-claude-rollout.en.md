**English** · [한국어](./revenue-org-claude-rollout.ko.md) · [Español](./revenue-org-claude-rollout.es.md) · [日本語](./revenue-org-claude-rollout.ja.md)

# Rolling out Claude across a revenue organization

A condensed walkthrough of Anthropic's revenue-leader guide. For the detailed reference and a
fill-in plan, see the `revenue-org-ai-rollout` skill in this folder.

## 1. Why the whole team matters
Individual reps save time on call prep, but benefits compound only when the whole team adopts
Claude. The path runs from individual gains, through team and department workflows, to KPI or OKR
gains. Returns grow with the access and trust you extend to Claude.

## 2. Decisions before the pilot
- **Owner:** RevOps, because it owns the CRM and pipeline/forecast reporting.
- **Systems:** connect CRM, call recording, email, and Slack so reps stop moving files by hand.
- **IT:** name an IT owner for provisioning, SSO, and admin consents; fix dates first.
- **Security:** start early — data boundaries, connector permissions, auditability, telemetry export.
- **Metrics:** one activity metric and one revenue metric, with a baseline and readout dates.
- **Spend:** limits by org, group, and user; gate costlier capabilities by role; more headroom for
  champions.
- **Cohort:** two or three teams with motivated leads.

## 3. The team's setup
The Sales plugin provides `/call-summary`, `/forecast`, `/pipeline-review` and skills such as
account research, call prep, daily briefing, outreach drafting, competitive intelligence, and asset
creation. Preload its settings file. Connectors respect each rep's permissions. Top performers'
routines become shared skills; editing the file updates them for everyone.

## 4. Three phases
1. **Setup** — IT and RevOps in parallel; champions at 2-3 per department or 1 per 25-50 users.
2. **Pilot** — 2-3 use cases per team; champions demo, run office hours, write first skills.
3. **Scale** — shared skill bundle; waves such as 25 → 150 → everyone; Claude output in standing
   meetings.

## 5. Measuring ROI
Compare pilot and non-pilot teams in the same quarter (pipeline per rep, cycle length, win rate).
Group returns as efficiency, expansion, and new capabilities. Lead budget talks with expansion and
new capabilities, not hours saved. Read spend next to output; coach before capping.

## 6. Pitfalls
- A pilot with no end date → put a decision date and decider on the sponsor's calendar.
- Seats scaled without champions → keep 1 champion per 25-50 users each wave.
- Spend ignored until the invoice → set limits early and read usage weekly.

Source: https://claude.com/resources/articles/building-an-ai-native-revenue-organization

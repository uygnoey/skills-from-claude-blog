---
name: live-dashboards-and-motion
description: Use Claude Dashboards (beta, paid plans) to turn a plain-language question about company data into a dashboard that stays current, and Claude Motion (beta, Team and Enterprise) to turn a report, chart, or walkthrough into an editable, code-built animation exported as MP4. Covers connecting a data platform or CRM connector, checking the query and refresh time behind each chart, handing a dashboard off to a BI tool for deeper analysis, and building, editing, and exporting a Motion explainer. Use when a user wants a live dashboard from their data or an animated explainer instead of a static slide.
---

## Purpose
Asking questions of company data usually means filing a ticket or writing SQL, and ideas that would
land better in motion usually end up as another static slide. Claude Dashboards and Claude Motion let
the user ask for the dashboard or the animation itself, and see how Claude made it: every chart shows
its query, and every animation is code that can be edited. Claude makes the first version; the user
decides what gets shared.

## When to use
- A quick, exploratory question about company data (e.g. "how do this week's signups compare with
  last month's?") → **Dashboards**.
- A dashboard over CRM data from a connector (e.g. Salesforce opportunities) → **Dashboards**.
- A short explainer for an all-hands, motion for a chart in a board deck, or a product walkthrough
  for customer onboarding → **Motion**.
- Deep, governed analysis → start in Dashboards, then send the dashboard on to a BI tool.

## Instructions

### Dashboards
1. **Check availability.** Dashboards is in beta on paid plans. On Enterprise it is off by default;
   an admin turns it on in Organization settings > Artifacts.
2. **Connect the data.** Connect a data platform such as Amazon Redshift, BigQuery, ClickHouse,
   Databricks, or Snowflake, or use another connector (for example Salesforce).
3. **Ask in plain language.** State the metric, breakdown, and time window. Claude pulls the answer
   from the data, builds the dashboard, and keeps it current as the data changes.
4. **Verify before sharing.** Click any number to see the query behind it, or ask Claude to explain
   it. Check each chart's "last refreshed" time.
5. **Hand off when the question gets deeper.** Send the dashboard from Claude to Amplitude, Grafana,
   Hex, Mixpanel, Omni, Perplexity, PostHog, or Sigma and continue there (Databricks Genie, Looker,
   monday.com, and Tableau are listed as coming soon). Dashboards work alongside BI tools, not instead
   of them.

### Motion
1. **Check availability.** Motion is in beta on Team and Enterprise; on Enterprise it is off by
   default (Organization settings > Artifacts).
2. **Describe the explainer.** Give the source material (report, chart, product flow), the audience,
   and the target length.
3. **Edit.** Claude writes code that animates text, charts, shapes, and images, so any word, number,
   or timing can be changed in the editor or by asking Claude.
4. **Export.** Download as MP4, or open it in Adobe, Descript, HeyGen, Higgsfield, invideo, Luma AI,
   or Runway (Canva and Captions listed as coming soon).
5. **Know the boundary.** Motion does not use a video generation model: no generated footage and no
   AI-generated people. It is for explaining your own work.

### Sharing (Docs, Slides, Design, Dashboards, Motion)
- Teams and Claude can work on the same doc, deck, design, or dashboard.
- Slides, designs, dashboards, and animations can be shared outside the organization, or with anyone
  who has the link, if the admin allows it.

## Examples
See [examples/prompts.md](examples/prompts.md) for the starter prompts from the post and how to
extend them.

**Example — dashboard check before sharing**
- User: "Build a dashboard of this quarter's revenue by region."
- Claude builds it from the connected warehouse. Before sharing, open each revenue figure to read its
  query, confirm the date filter matches "this quarter", and note the refresh time on each chart.

**Example — animated explainer**
- User: "Animate how our pricing plans compare for the sales kickoff."
- Claude builds a short animation; change plan names, prices, or timing in the editor, then download
  the MP4 or open it in a video tool.

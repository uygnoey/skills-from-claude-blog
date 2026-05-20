---
name: sales-cowork-workflows
description: Turn recurring sales leadership routines (meeting prep, weekly forecast rollups, and large-scale account scoring) into scheduled, repeatable workflows that assemble data from multiple systems and produce standardized outputs with human approval.
---

# Sales Cowork Workflows

## Instructions
Use this skill to translate three recurring patterns into concrete, repeatable routines:

1) **Scheduled meeting prep**
- Before each external meeting, ensure logistics are complete (for example, book a conference room if one isn’t set).
- Build a concise customer brief by pulling the latest relevant data (example sources mentioned in the post: BigQuery spend, Salesforce pipeline status).
- Output a brief that the user can quickly review before the call.

2) **Weekly forecast rollup**
- Pull opportunity records and submitted commits from Salesforce’s Forecast view.
- Pull token spend from BigQuery.
- Pull qualitative notes from a small set of internal documents.
- Assemble a **single-page web report** in a consistent format that includes:
  - top-line metrics
  - top deals
  - movers and decliners
  - a forecast snapshot rolled up from each first-line manager
- Publish the report to a shareable link before the weekly forecast call, leaving room for the owner to add commentary.

3) **Overnight account propensity scoring (at scale)**
- Define a scoring rubric (the post describes two separate rubrics: one for tech accounts and one for industries).
- For each account, gather evidence via deep web research and internal data sources (examples mentioned: Salesforce and BigQuery).
- Produce:
  - a numerical score
  - written rationale per rubric dimension
- Compile results into an interactive dashboard where each AE can view their slice of the territory and see ranked accounts; hovering an account should surface suggested use cases and comparable case studies (as described in the post).

### Iteration loop
Run a test territory first, review quality, then adjust weights and re-run. The post gives an example instruction for weight tuning: “I think D4 is probably weighted a little heavy; bring it down a bit”.

## Examples
### Example: rubric dimensions (from the post)
**Tech accounts**
- agent opportunity
- internal transformation
- AI commitment
- white space against existing spend
- industry fit

**Industries** (examples)
- knowledge-worker density
- public AI commitments measured by mentions on the company’s open jobs page

### Example: weekly report outline
- Top-line metrics
- Top deals
- Movers and decliners
- Forecast snapshot by first-line manager

## Source
- https://claude.com/blog/how-an-anthropic-sales-leader-uses-claude-cowork-to-run-a-4-000-account-book

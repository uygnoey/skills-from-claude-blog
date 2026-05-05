# Worked example — three-phase rollout

This example walks the foundation → pilot → scale playbook against a representative mid-sized investment bank that already has Microsoft 365, an SSO provider, and an in-house data lake. It only uses the products and templates named in the source post.

## Foundation

**Product surface chosen.** Claude Cowork for analyst-in-the-loop project work, Claude Code for the quant team, and Claude for Microsoft 365 (Excel, PowerPoint, Word, Outlook) for the broader research org. Claude Platform reserved for a future custom RFP intake; Claude Managed Agents reserved for phase 3.

**Governance decisions.**

- SSO via the firm's existing identity provider for Cowork and Code.
- Data perimeter: research bench documents and approved market-data feeds; trading and customer PII excluded in this phase.
- Naming an executive sponsor in the equity research COO's office.
- Picking two pre-built finance agent templates to enable as plugins: **pitch builder** and **earnings reviewer**.

## Pilot

**Pitch builder pilot.**

- Owner: a coverage MD in TMT.
- Scope: outbound pitches for one sector for 30 days.
- Surface: Claude Cowork plugin.
- Success metrics: hours saved per pitch, percentage of drafts that survive partner review without restructuring.

**Earnings reviewer pilot.**

- Owner: a senior associate on the research desk.
- Scope: this earnings season for a chosen coverage list.
- Surface: Claude Cowork plugin (reading transcripts and filings, updating analyst models in Microsoft 365 via the Excel add-in).
- Success metrics: time from filing to updated model, count of thesis-relevant items the analyst confirms vs. dismisses.

**Operational discipline.**

- Weekly review with the executive sponsor.
- A shared running log of model overrides and rejected drafts so the next phase has data.

## Scale

Based on the pilot signal:

- Extend to **meeting preparer** for the coverage team and **model builder** for the quant desk.
- Add **valuation reviewer** under the deal-team lead.
- Begin scoping a **month-end closer** and **general ledger reconciler** rollout for the finance org under the controller, on a separate phase-1 plan because it is a different sector cut (finance and operations vs. research and client coverage).
- Where a template has demonstrated stable, high-volume value (for example, earnings reviewer running across the full coverage list), evaluate moving it to **Claude Managed Agents** so the production infrastructure is hosted while the analyst-in-the-loop refinement stays in Cowork.

## What the example does not invent

- It does not assign specific time-saved percentages, ROI, or accuracy numbers — those come from the firm's pilot data, not from the blog post.
- It does not fabricate Anthropic security artifacts, contract terms, or pricing.
- It does not name customer-specific implementation details from AIG, Commonwealth Bank of Australia, IG Group, or Moody's beyond the fact that they are referenced in the bundled customer stories.

## Source

- [Deploying Claude across financial services](https://claude.com/blog/deploying-claude-across-financial-services)
- [Agents for financial services and insurance](https://www.anthropic.com/news/finance-agents)

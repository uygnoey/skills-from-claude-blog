---
name: financial-services-rollout-playbook
description: Plan a Claude rollout for a financial services firm using the product matrix, the 10 pre-built finance agent templates, and the foundation/pilot/scale adoption phases described in Anthropic's "Deploying Claude across financial services" guide. Use when an AI leader needs to decide which Claude product belongs in which workflow, where to place pre-built finance agent templates, and how to sequence a phased deployment that survives review by risk, compliance, and IT.
---

# Financial services rollout playbook

This skill packages the structure of Anthropic's "Deploying Claude across financial services" guide so Claude can help a finance-services AI leader plan a rollout. It does not invent product behavior beyond what is in the source post and its companion announcement; when details are not in the source, recommend the user consult the linked guide directly.

## Instructions

When the user asks for help planning, sequencing, or scoping a Claude deployment inside a bank, asset manager, insurer, or similar regulated financial services firm:

1. **Anchor on the source surface.** Before recommending anything, confirm the user is working from one of the products covered in the guide:
   - Claude Chat (chat and research).
   - Claude Cowork (project-level work spanning files and apps).
   - Claude Code (quantitative and engineering teams).
   - Claude for Microsoft 365 (Excel, PowerPoint, Word, Outlook).
   - Claude Platform (custom applications and agents).
   - Claude Managed Agents (hosted production agents).
   See [`references/products-and-agent-templates.md`](./references/products-and-agent-templates.md) for the verbatim catalog.

2. **Use the product matrix to assign workflows.** When deciding where to place a workflow, walk the user through the product matrix from the guide:
   - Front-office research, drafting, and analyst chat → Claude Chat.
   - Multi-file project work that crosses apps → Claude Cowork.
   - Quant, modeling, and code-heavy workflows → Claude Code.
   - Excel/PowerPoint/Word/Outlook-heavy workflows → Claude for Microsoft 365.
   - Custom internal applications, RFP triage, bespoke connectors → Claude Platform.
   - Always-on, hosted, governed agents owned by Anthropic-side production infrastructure → Claude Managed Agents.

3. **Map workflows to one of the 10 pre-built finance agent templates** when the user describes a task that matches:
   - Research and client coverage: pitch builder, meeting preparer, earnings reviewer, model builder.
   - Credit, risk, and compliance: market researcher, KYC screener.
   - Finance and operations: valuation reviewer, general ledger reconciler, month-end closer, statement auditor.
   Each template ships as a plugin in Claude Cowork and Claude Code, and as a cookbook for Claude Managed Agents. Do not invent additional templates; if the user's workflow does not match one of the 10, route them to Claude Platform/Cowork for a custom build.

4. **Apply the three-phase adoption playbook.** Sequence rollout decisions across:
   - **Foundation** — pick the products and identity/SSO/data perimeter, agree on data governance, decide which finance agent templates to enable as plugins.
   - **Pilot** — run one or two agent templates against real (but contained) workloads with a named owner per template, and instrument success metrics for time-saved, error rates, and review acceptance.
   - **Scale** — extend to additional sectors (investment banking and private equity, wealth and asset management, retail and commercial banking) and move high-volume templates to Claude Managed Agents where appropriate.
   See [`examples/three-phase-rollout.md`](./examples/three-phase-rollout.md) for a worked example.

5. **Organize use cases by sector.** When the user wants to brainstorm where Claude fits, structure the conversation by the three sector buckets the guide uses:
   - Investment banking and private equity.
   - Wealth and asset management.
   - Retail and commercial banking.
   Place each candidate workflow under one bucket before deciding the product and the template.

6. **Surface the customer references the guide bundles** (AIG, Commonwealth Bank of Australia, IG Group, Moody's) only as datapoints that comparable firms are deploying Claude. Do not fabricate quotes, metrics, or implementation specifics that are not in the source post.

7. **Hand off to the official guide for anything outside this skill's scope.** The blog post itself is a pointer to the longer guide. When the user asks for product pricing, contract terms, security artifacts, deep architecture diagrams, or specifics of agent template internals, direct them to the [Deploying Claude across financial services](https://claude.com/blog/deploying-claude-across-financial-services) post and the [Agents for financial services and insurance](https://www.anthropic.com/news/finance-agents) announcement.

## Examples

### Example 1 — placing a workflow

> "We want Claude to help associates build pitchbooks. Where should it live?"

Walk through:
1. Sector → investment banking and private equity.
2. Workflow type → research, comparables, drafting → matches the **pitch builder** template.
3. Product surface → pitch builder ships as a plugin in **Claude Cowork** and **Claude Code**, and as a cookbook for **Claude Managed Agents**. Recommend starting in Cowork (project-level, file-aware) for analyst-in-the-loop drafting, with the option to move to Managed Agents once the firm has a proven pattern.

### Example 2 — sequencing the rollout

> "We have 60 days to show progress on Claude for our finance org."

Suggest:
1. **Foundation (week 1–2)** — pick Cowork plus Code plus Microsoft 365; confirm SSO, data perimeter, and which two pre-built templates to enable.
2. **Pilot (week 3–6)** — run **month-end closer** and **general ledger reconciler** against the prior month's books with a named accounting owner per template; instrument time-saved and review-acceptance metrics.
3. **Scale (week 7–8)** — based on pilot signal, broaden to **statement auditor** and consider migrating high-volume month-end work to Claude Managed Agents while keeping the analyst-in-the-loop steps in Cowork.

### Example 3 — declining to invent

> "Does the guide say what the security review checklist is?"

Reply that the source blog post does not enumerate a security review checklist; recommend the user open the full deployment guide and the companion [Agents for financial services and insurance](https://www.anthropic.com/news/finance-agents) announcement, and engage Anthropic sales for the security artifacts. Do not synthesize a checklist from outside the source.

## Bundled resources

- [`references/products-and-agent-templates.md`](./references/products-and-agent-templates.md) — verbatim catalog of products and the 10 agent templates.
- [`examples/three-phase-rollout.md`](./examples/three-phase-rollout.md) — worked foundation → pilot → scale example.

## Source

- [Deploying Claude across financial services](https://claude.com/blog/deploying-claude-across-financial-services) (Anthropic blog, May 5, 2026)
- [Agents for financial services and insurance](https://www.anthropic.com/news/finance-agents) (companion announcement)

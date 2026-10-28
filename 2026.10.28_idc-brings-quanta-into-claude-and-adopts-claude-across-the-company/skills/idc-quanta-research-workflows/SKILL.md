---
name: idc-quanta-research-workflows
description: Answer market and technology questions in Claude through the IDC Quanta MCP connector, following the October 2026 IDC announcement - competitive briefs, vendor shortlists delivered as Excel scorecards, comparing your own budget to IDC forecasts, and acquisition-impact analysis, each cited to the IDC document or dataset it came from. Also covers how IDC rolled Claude out internally (Claude Code for prototypes, parallel tests, and reviews; Cowork for plan drafts; CRM-export deal triage; a marketing content assistant). Use when a customer with IDC Quanta wants finished analysis instead of reading long reports, or when a research firm plans a company-wide Claude rollout.
---

## Purpose
The source announces that IDC brought IDC Quanta, its AI-powered technology intelligence platform, into
Claude as an MCP connector, and that IDC adopted Claude across its own business. Customers describe the
market, strategy, or purchase they are working on, and Claude returns finished analysis built on IDC's
forecasts, market data, and research. This skill turns the post's scenarios into repeatable request
patterns. Anything beyond what the post states is left to IDC's documentation (see the original).

## When to use
- You need a competitor brief, a vendor shortlist, a market size, or a benchmark and have IDC Quanta access.
- You want to compare your own numbers (for example next year's IT budget) to IDC's forecast.
- You need to assess what a competitor's acquisition means for your business.
- You lead a research or data company and want a blueprint for adopting Claude across teams.

## Instructions

1. **Connect.** IDC Quanta customers add the IDC Quanta connector from within Claude. Others contact IDC or
   book a demo (link in the post). It works wherever the customer already uses Claude: the desktop and mobile
   app, Cowork, and the Microsoft Office add-ins.
2. **Describe the job, not the report.** State the role, the market or purchase, and the decision you face.
   Pick a request pattern from [templates/request-prompts.md](templates/request-prompts.md).
3. **Add your context.** For a shortlist, include your existing architecture and business requirements.
   For a benchmark, upload your own figures; the post says uploaded data stays private to the customer.
4. **Ask for a usable format.** Request the deliverable you will act on, such as an Excel scorecard for an
   evaluation team or an executive-ready brief.
5. **Check citations.** Each answer should cite the IDC document or dataset it came from. Because Claude uses
   the same data and definitions as an IDC analyst, market share and growth figures should match what IDC
   would publish; flag anything uncited.
6. **Review before you decide.** Treat the output as a fast first analysis that people review before acting.
7. **Rolling Claude out internally?** Follow IDC's sequence in
   [references/internal-adoption.md](references/internal-adoption.md): start with engineering, then extend
   to product, planning, sales, and marketing.

## Examples

**Competitive brief**
> A corporate strategy lead asks for a brief on a competitor. Claude returns positioning, market share,
> product capabilities, and recent acquisitions, cited to IDC research - minutes instead of a day.

**Vendor shortlist**
> A CIO describes the current architecture and requirements for procurement software. Claude returns the top
> three vendors based on IDC's procurement database and MarketScape research as an Excel scorecard.

**Budget versus forecast**
> A CFO uploads next year's IT budget and asks how it compares to IDC's forecast. Claude shows where and by
> how much the two differ.

More role-based scenarios: [examples/role-scenarios.md](examples/role-scenarios.md).

# Products and agent templates referenced in the post

This reference captures the product surface and the 10 pre-built finance agent templates that the source post and its companion announcement explicitly call out. Do not extend this list — it mirrors what is in the source.

## Products covered by the deployment guide

- **Claude Chat** — chat and research.
- **Claude Cowork** (Claude Enterprise) — project-level work that spans files and apps.
- **Claude Code** — quantitative and engineering teams.
- **Claude for Microsoft 365** — add-ins covering Excel, PowerPoint, Word, and Outlook.
- **Claude Platform** — building and deploying custom applications and agents.
- **Claude Managed Agents** — hosted production agents.

The post emphasizes that most financial services firms run more than one of these in parallel and that the guide ships an explicit product matrix for choosing between them.

## The 10 pre-built finance agent templates

Each template is a reference architecture that packages three things, per the companion announcement: **skills** (instructions and domain knowledge for the task), **connectors** (governed access to the data the task runs on), and **subagents** (additional Claude models invoked for specific sub-tasks such as comparables selection or methodology checks). They are distributed as plugins in Claude Cowork and Claude Code, and as cookbooks for Claude Managed Agents.

### Research and client coverage

- **Pitch builder** — creates target lists, runs comparables, and drafts pitchbooks for client meetings.
- **Meeting preparer** — assembles client and counterparty briefs ahead of calls.
- **Earnings reviewer** — reads transcripts and filings, updates models, and flags thesis-relevant changes.
- **Model builder** — creates and maintains financial models from filings, data feeds, and analyst inputs.

### Credit, risk, and compliance

- **Market researcher** — tracks sector and issuer developments, synthesizes news, filings, and broker research, and flags items for credit and risk review.
- **KYC screener** — assembles entity files, reviews source documents, and packages escalations for compliance review.

### Finance and operations

- **Valuation reviewer** — checks valuations against comparables, methodology, and the firm's review standards.
- **General ledger reconciler** — reconciles general ledger accounts and runs net asset value calculations against the books of record.
- **Month-end closer** — runs the close checklist, prepares journal entries, and produces close reports.
- **Statement auditor** — reviews financial statements for consistency, completeness, and audit-readiness.

## Three-phase adoption playbook

The post highlights three named phases without prescribing a fixed timeline:

1. **Foundation** — choose products, set identity/SSO and data perimeter, agree on governance, and decide which agent templates to enable.
2. **Pilot** — run one or two templates against real but contained workloads with a named owner per template and explicit success metrics.
3. **Scale** — extend deployment to additional sectors and migrate high-volume workloads to Claude Managed Agents where appropriate.

## Customer references bundled in the guide

The post says the guide includes customer stories from:

- AIG
- Commonwealth Bank of Australia
- IG Group
- Moody's

Specific quotes, metrics, or implementation details from these stories are not reproduced in the source blog post and should not be fabricated.

## Sectors used to organize use cases

The post structures use cases by sector:

- Investment banking and private equity.
- Wealth and asset management.
- Retail and commercial banking.

## Source

- [Deploying Claude across financial services](https://claude.com/blog/deploying-claude-across-financial-services)
- [Agents for financial services and insurance](https://www.anthropic.com/news/finance-agents)

# What a real fleet looks like

The agents below are the ones described in the source story. They are useful less as a shopping list than as a demonstration of the shape: **each agent has a name, an owner, and a single job**, and most sit at one stage of an existing business process rather than trying to own the whole thing.

## Engineering

**AI Code Reviewer** — reviews every pull request across four codebases, running multi-model analysis to catch security bugs, performance regressions, and committed credentials. Engineers now wait for its review before merging.

**Hank** — an internal code review agent that posts every review to a shared channel. Each entry names the pull request and the counts that came out of it, so the trail of what the agent decided is public and searchable. Its reactions are what the harvester collects.

## Operations — the core process

**EvidenceChain™ Delivery Agent** — took over a weekly chore an account manager used to do by hand. The company runs a site where courts, plaintiffs, and defendants look up the record of a service completed in the field: who the process server was, when they attempted it, and photos of the document delivery. One customer wanted specific records pulled on an ongoing basis. The agent pulls a database report for matching jobs, retrieves each PDF with a browser built into the runtime, and delivers it to the customer's FTP server daily. **The account manager who set it up had never automated anything and built it in about an hour by describing it to a coding agent.**

**eFiling Rejection Diagnoser** — fires automatically when a court rejects a filing, reads the job details, checks the court's rules, and posts a diagnosis to a channel in about a minute. That work used to consume hours of an employee's day.

**Job-verification agent** — checks every incoming job against the courts. It navigates a court website in a browser, confirms the hearing or case is filed appropriately and actually occurring on the stated date, then adjusts the job based on what it found — flagging jurisdictions, courts, and statute-of-limitations timeframes.

**Attorney Coverage Agent** — works the network of attorneys to get hearings covered: checking availability, emailing them, and reading replies about availability and pricing so a coordinator can confirm coverage.

**Charvis** — a review agent that checks completed service jobs. It now agrees with the compliance team about **98% of the time**.

**Service-Overdue-Nudger** — works the tier-1 layer of operational backlogs, the repetitive first pass a person would otherwise do, and drafts tiered daily outreach messages for human approval.

## Finance

**AR-remittance agent** — parses a remittance email, builds the ERP payment-application file, and posts it to a channel for one-click approval, then imports it.

**Capitalize-or-expense agent** — a daily agent that renders a capitalize-or-expense verdict on each engineering ticket.

## Marketing

**Ads analyst** — posts a weekly recommendation for the channel lead.

## What is in flight

Named as next: a service photo reviewer, a PagerDuty triage agent, a daily KPI digest, and expanded tuner loops on existing agents. Also a search for more "X-as-code" candidates — notification templates, event routing rules, and dispatch logic that can move into repositories where agents can read, reason about, and propose improvements.

## Patterns to take from the list

1. **Most agents sit at one stage of an existing process.** They are not "the eFiling agent"; they are the agent that diagnoses one rejection.
2. **The highest-value ones replaced a specific person's recurring chore** — and were often built by that person.
3. **Several are review agents that recommend rather than act**, and their agreement rate with the human team is tracked as the promotion criterion.
4. **Several use a browser**, because the source of truth is a website nobody has an API for.
5. **The reporting agents post to a channel**, which is what makes their output harvestable.

## Source

- https://claude.com/blog/how-abc-legal-turned-every-employee-into-a-builder-with-claude-managed-agents

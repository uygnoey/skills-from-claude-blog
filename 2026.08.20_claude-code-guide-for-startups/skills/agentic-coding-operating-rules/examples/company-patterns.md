# What each company actually did

The fifteen startups featured in the guide, and the specific practice each one
contributed. Use this as a menu — most of these are portable.

## Artemis Security

Runs as an AI-native company rather than a company that happens to use AI;
reports 6,000+ PRs a week. Speed is explicitly attributed to investment in
testing infrastructure, codebase organization, and team knowledge systems that
let agents ship end to end. "Structure your codebase, knowledge base, and team
the right way, and every contribution compounds." — Dan Shiebler, co-founder

## Cainex

Agents plus deterministic checks for medical coding, with an auditor-in-the-loop
correction cycle that revises versioned agent instructions and back-tests against
a golden set. Written up in full in
[examples/self-improvement-loop.md](./self-improvement-loop.md).

## Clay

- Hires tinkerers; treats every role as becoming an engineering role.
- Quarterly reviews where prototypes can enter the formal roadmap. A
  go-to-market team member built an autonomous agent that visits your websites,
  fills out lead-capture forms, times how long it takes to respond, rates the
  experience, and generates a performance report.
- An agent that handles bug triage from first pass to suggesting code changes for
  fixes — reported as 100% of bug triage automated.
- An internal analytics agent for self-service data.
- Rebuild-as-strategy: build it, build it again, build it again; the fourth build
  gets it right. The moat is being self-improving.

## ClickHouse

Nearly every SDLC stage turned into an autonomous loop; 30% more features
shipped. Purpose-built agents for fixing flaky tests and finding missing test
coverage are the #2 and #3 contributors to the repo. A separate family of agents
handles operations. In-product agents — one in the SQL console, plus an AI SRE —
are themselves built and iterated on with Claude Code.

## Cognition

On the tempo of the field: what you build today is very likely scrapped in six
months to a year. Devin was not possible with the models of two years earlier;
the bet was that it would be soon.

## Commure

- Engineers orchestrate agent fleets and run multiple PRs in flight; one engineer
  ran a ~13-ticket initiative with subagents in parallel, each owning a ticket and
  its PR.
- Teardown as a skill invocation: "for every feature flag already released to
  everyone, open a PR removing it and the associated code," reviewed by an
  engineer. Migrations that ate dev cycles became a plan and a fan out, done in a
  couple of hours.
- Sweeps claims data to flag anomalies across sites.

## Crosby

Brought Claude Code to the lawyers rather than the lawyers to Claude Code, by
connecting it to the tools and operating systems they worked in every day.
Summarizes thousands of legal documents with subagents.

## Emergent

- Day-one onboarding: a new hire bootstraps their entire dev setup by pointing
  Claude at the right markdown file, and Claude updates that file when it finds
  something broken or out of date.
- A GitHub repo of skills as a shared knowledge base — database and data
  warehouse locations, schema information, company context — with an explicit
  tolerance for slightly outdated context as long as the agent can verify and
  course correct.
- Uses Claude Code locally to tell whether a behavior seen in their own
  model-backed product is model behavior or a harness issue.

## Harvey

Each new wave of model capability — emergent reasoning, agentic automation,
planning and orchestration — required a full re-architecture of the platform.
Willingness to scrap and go agent-native is what made current capabilities
possible.

## Heidi

- The "broken telephone problem": the person who understands the problem now
  ships the PR, bringing in designers and engineers where their expertise
  matters.
- Anyone drafts product components, marketing collateral, or deck material from
  Claude Code using the design system as reference; AI that touches the product
  clears a higher bar.
- Automated code review against vetted technical and compliance frameworks, with
  suggested changes routed to the right reviewers before shipping.
- Categorizes customer and clinician feedback alongside usage data to surface
  product signals.

## Higgsfield

Model velocity as an operating problem: new video and image models arrive
constantly, each needing new skills, evaluations, routing logic, and production
testing before deployment. Claude Code compressed that cycle from days to hours,
allowing issues found in production to be fixed in the same session.

## Omni

- A dedicated Slack channel for Claude-generated prototypes, with contributions
  from everyone including senior technical staff.
- The corollary rule, "everyone talks with customers" — engineers are
  deliberately put in front of customers to close the feedback loop faster.
- Took the file-vs-embedding approach as inspiration and avoided RAG-pipeline
  complexity in their own product; adapted parallelism concepts from Claude
  Code's harness into their own UI.
- Reports 2–3x engineering productivity.

## Parahelp

Non-technical people, including a co-founder, shipping UI changes and other
product improvements alongside engineers shipping much more.

## Translucent

- An in-house marketplace of specialized internal agents organized by role, so
  engineering, delivery, and sales each get tools built for how they work.
- The "Translucent code reviewer," which fans out across a change, reviews it
  from multiple angles, and synthesizes results the way a senior engineer would.
- Continuously mines hospital financial data for warning signs no analyst team
  could catch in time.

## Zingage

Gave Claude full autonomy early and got plausible code that drifted from their
architecture. Wrote down every invariant instead — how they frame problems, what
has to be true no matter what, how to prove something works instead of trusting a
confident answer. 567 lines of how the team thinks.

## Source

[The Claude Code guide for startups](https://claude.com/blog/claude-code-guide-for-startups) (published 2026-08-20).

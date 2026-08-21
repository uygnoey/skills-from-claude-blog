# The five rules, in full

Each rule as stated in the guide, with the reasoning that produced it and the
boundary it draws.

## 01 — Everyone ships

> Agentic coding lowers the barrier to entry, so the person who understands the
> problem can ship the first version of the fix.

**Why it holds.** With Claude Code you can create functional features without
being fluent in a coding language or in how to use an IDE. For startup founders
the capacity argument is obvious — they do not have their larger competitors'
headcount, so it is all hands on deck. But the stronger argument is domain
expertise: the people closest to the problem have the best product insights.

- Parahelp: "Not only were engineers shipping much more, but non-technical
  people (like me) were also suddenly shipping UI changes and other product
  improvements." — Mads Lunau Liechti, co-founder
- Crosby: "Claude Code changed what it meant to be a lawyer at Crosby. The
  lawyers have the best product insights, because they are the users." — Ryan
  Daniels, co-founder and CEO
- Heidi: the "broken telephone problem" — an idea used to travel from its owner
  to a PM to a designer to an engineer, losing its essence on the way and taking
  weeks. "Claude Code collapses that chain." — Dr. Thomas Kelly, co-founder and
  CEO
- Clay: "every role is becoming an engineering role because you can build
  software for it… so we hire people who are tinkerers, who are interested in
  building." — Kareem Amin, co-founder and CEO

**What it does not mean.** Marketing is not approving pull requests and legal is
not bisecting flaky tests. The division of labor stays. What opens to everyone
is the 0→1 step: idea to working prototype.

**The three mechanisms.**

1. *Create connections.* Crosby did not bring lawyers to Claude Code; they
   brought Claude Code to the lawyers, connecting it to the tools and operating
   systems they already worked in every day. MCP for tool/database/API access
   where copy-paste is happening; CLI where a mature command-line tool already
   exists and token efficiency matters.
2. *Standup showcases.* Clay's quarterly reviews let prototypes enter the formal
   roadmap. Omni runs a dedicated Slack channel for Claude-generated prototypes,
   and practices the corollary — "everyone talks with customers" — deliberately
   putting engineers in front of customers to close the feedback loop faster.
3. *Share skills.* Heidi drafts product components, marketing collateral, and
   deck material from Claude Code against their design system as reference:
   "AI that touches the product must clear a much higher bar, which Claude Code
   helps us meet with more precision." Emergent keeps a GitHub repo of skills as
   a shared knowledge base carrying database and warehouse locations, schema
   information, and company context. Translucent's engineers spun up an in-house
   marketplace of specialized internal agents organized by role, so engineering,
   delivery, and sales each get tools built for how they actually work.

## 02 — Automate the tedium

> Agents own the mechanical 80% of the lifecycle so engineers spend their time
> on the cases that actually need judgment.

**Why it holds.** Every company has chased efficiency through technology; these
startups separated themselves by the speed and depth of adoption. Artemis
Security's Shachar Hirshberg: "Everyone's racing to build AI products. Far fewer
are rebuilding how their company actually runs. The second one is the bigger
unlock."

**Two observable differences.** AI integrated more tightly across SDLC stages,
and more purpose-built agents designed to take recurring tasks end to end.

- Onboarding: at Emergent, "on day one, a new hire bootstraps their entire dev
  setup by pointing Claude at the right markdown file. If Claude hits anything
  broken or out of date during onboarding, it updates that file."
- Throughput: Commure engineers orchestrate agent fleets, ship fixes to
  production data problems the same day they are found, and run multiple PRs in
  flight simultaneously — one engineer ran a ~13-ticket initiative with subagents
  in parallel, each owning a ticket and its PR.
- Review: Heidi runs automated code reviews against vetted technical and
  compliance frameworks, flagging critical issues and routing suggested changes
  to the right reviewers before anything ships.
- ClickHouse turned nearly every SDLC stage into an autonomous loop. The
  flaky-test agent and the missing-coverage agent are the #2 and #3 contributors
  to the repo; a separate family of agents handles operations; the team uses
  Claude Code to build and iterate on those agents themselves.

**Beyond the SDLC.** Self-service data analytics was the most commonly
accelerated process — nearly every company had some way to make quick decisions
on fresh data, including unstructured data, to fuel the pivoting that startup
life requires.

**Tooling named in the guide.** Code Review (research preview), a managed
multi-agent service that runs an automated review pass on PRs in enabled repos
and tags each finding with a severity level — fix manually and push, or comment
`@Claude` on the finding to close the loop with GitHub Actions configured. Claude
Tag (public beta) as CI/CD on-call first responder. Dynamic workflows for
parallel fan-out or adversarial review.

## 03 — Trust, but verify

> You can't automate a process unless you have a reliable means of monitoring
> and verifying the outcome.

The necessary corollary to rule 2. Artemis Security's Dan Shiebler on why their
deployment speed works: "because we've invested deeply in testing
infrastructure, codebase organization, and team knowledge systems that let
agents ship end to end. This is the flywheel we've built with Claude: structure
your codebase, knowledge base, and team the right way, and every contribution
compounds."

Zingage's Victor Hunt on the failure mode: "Early on we gave Claude full
autonomy and it did what AI does. It shipped plausible code fast. The problem was
it drifted from our architecture in ways that looked right but weren't." The
remedy was writing down every invariant — 567 lines of how the team thinks.

Practices: invariants in root `CLAUDE.md`; loops with clear stop conditions;
subject-matter-expert review that feeds a self-improvement loop rather than
example-by-example fixes; maintained golden sets and multiple eval suites;
hooks as hard gates for the deterministic parts.

## 04 — Build for rebuilding

> Model capability keeps shifting underneath these teams, so very little is
> treated as permanent.

Clay: "you build it and then you build it again and then you build it again. And
then the fourth time you build it, you know everything that's needed and you get
it right. And so we don't necessarily throw away things. We just rebuild it: and
this time with more clarity."

Commure: "A rebuild isn't done when the new path ships. It's done when the old
path is gone. Teardown always lost the prioritization fight before: it's tedious
and it ships no features."

Harvey's Niko Grupen, at a May 2026 Code with Claude event, on each wave of model
capability — emergent reasoning, agentic automation, planning and orchestration —
requiring a full re-architecture: "If we hadn't been willing to say 'Hey, we need
to scrap this and go agent native' we simply could not have these capabilities in
our platform right now."

Cognition's Walden Yan at the same event: "The way of life of building AI right
now is accepting that the thing you build today is very likely going to be
scrapped in six months to a year."

Clay also frames constant rebuilding as the moat: "the moat for any company
right now is that it needs to be self-improving… The race is really, whoever can
get to the distribution fastest… so you can help each [customer] so that you can
self-improve."

Mechanics: git worktrees for isolated parallel rebuilds; plan mode before
non-trivial rewrites.

## 05 — Prototype, dogfood, productionize

> Building with AI helps these startups create disruptive products with AI — the
> flywheel at the heart of their process.

When developers advance their agentic coding practice they get a stronger grasp
of model capabilities and of how harness design evolves at the frontier, and
they spend that on their own agents and products.

- Omni: took inspiration from the file-vs-embedding approach, which emboldened
  them to keep their own product simple and avoid the complexity of a RAG
  pipeline; also adapted parallelism concepts from Claude Code's harness into
  their own UI.
- Emergent: because their app builder uses the same models, an odd behavior in
  their product can be debugged locally via Claude Code to tell whether it is
  model behavior or a harness issue — a large improvement to triage cycles.
- ClickHouse: built their own in-product agents, including one in the SQL console
  and an AI SRE, using Claude Code to build and iterate on those agents. "The
  tooling that powers our customers' AI experiences is, in part, built with AI."

The promotion path named in the guide: internal agent built with Claude Code →
dogfood → customer-facing product, often via the Claude API, SDK, or Claude
Managed Agents.

## Reported outcomes

Figures the guide attributes to the featured companies:

| Company | Reported | 
| --- | --- |
| ClickHouse | 30% more features shipped |
| Omni | 2–3x engineering productivity |
| Clay | 100% of bug triage automated |
| Artemis Security | 6,000+ PRs a week |

## Source

[The Claude Code guide for startups](https://claude.com/blog/claude-code-guide-for-startups) (published 2026-08-20).

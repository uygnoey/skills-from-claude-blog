**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
Anthropic sampled 1.2 million anonymized and aggregated Claude Cowork sessions from May 11–31, 2026, drawn from more than 600,000 organizations, and classified them with an automated system into a taxonomy of 20 categories of work. The headline finding: roughly half of all usage comprises "the work around the work" — tasks that are part of a broad swath of jobs, but are rarely a person's core responsibility.

The two largest categories carry that half. **Business process and operations** is 33.4% — pulling scattered updates into a single report, building onboarding checklists, reconciling spreadsheets. **Content creation and copywriting** is 16.4% — synthesis-intensive business communications like drafts, slide decks, posts, and proposals. Both span roles rather than belonging to one: finance, HR, and administrative people all reach for the first; marketing, communications, business development, and project management all reach for the second.

The remaining categories are long-tailed: software development 8.7%, DevOps and infrastructure 7%, research and intelligence 6.4%, data analysis and business intelligence 5.8%, document processing and extraction 4.1%, sales and revenue operations 4%, personal assistance 3.8%, education 2.4%, meeting and conversation intelligence 1.8%, legal and compliance 1.3%, customer support 0.8%.

The post reads that shape as connective work: "people are using Claude Cowork to assemble and structure the information they can use to act on their expertise." A lawyer hands over document formatting and filing and keeps the legal judgment; a hiring manager hands over scheduling and interview-feedback synthesis and keeps the candidate conversations; a team lead hands over the deck that explains a difficult decision and keeps the decision. That contrasts sharply with Claude Code, which developers use for the core of their role — building, debugging, and shipping code — which is part of why software development is such a small share of Cowork sessions.

The post closes with an unusually explicit methodology and limitations section: rate-capped sampling means every number is a share of sampled sessions and not an absolute volume, the taxonomy has no standalone marketing, finance, or HR categories, the three-week window was chosen because a labeling-pipeline change moved shares around May 11, roughly 5% of sessions are personal rather than work use, and all labels were applied by an automated classifier rather than a human reviewer.

## When is it useful?
- When deciding which of your own tasks to hand to an agent, and you want a published distribution of what other people actually hand over rather than a guess.
- When making the case internally for agentic tooling outside engineering, and you need the shape of non-developer usage.
- When you are classifying your own team's agent sessions and want a taxonomy and a reporting format that already exists.
- When reading or writing a usage-share report and you need to state the caveats — rate-capped sampling, automated classification, taxonomy granularity — honestly.
- When you are trying to explain why a coding-heavy tool and a chat-interface agent get used for such different things.

## Key points
- **Half of usage is "the work around the work."** Business process and operations (33.4%) plus content creation and copywriting (16.4%) together account for roughly half of sampled sessions. Neither is anyone's job title.
- **The top category is more than double the next.** Business process and operations at 33.4% is more than twice content creation and copywriting at 16.4%; every other category is under 9%.
- **The work is connective.** Spreadsheets pull disparate data points into a context where they can be read, compared, and tracked; decks convey an idea or decision to an audience with varying levels of context; onboarding checklists help a new hire tap into institutional knowledge.
- **Expertise stays with the person.** The pattern is delegating assembly and structure, not judgment: formatting and filing rather than the legal call, scheduling and synthesis rather than the candidate evaluation, the explanatory deck rather than the decision it explains.
- **Cowork usage is the inverse of Claude Code usage.** Developers use Claude Code for the core of their role and Cowork for the connective, communications-focused work that surrounds every role, software engineering included — so software development is only 8.7% of Cowork sessions.
- **Cowork exists because the terminal was a barrier.** Non-technical users had already started using Claude Code to organize folders, deduplicate files, and write spreadsheet formulas; for others the terminal stayed "a literal 'black box'," so Cowork brought agentic capability into the chat interface people already used.
- **Shares, not volumes.** Sampling is capped at a fixed maximum number of sessions per hour, so the numbers cannot be read as usage totals or growth, and busy hours are somewhat underrepresented.
- **The taxonomy is about work, not job titles.** There are no standalone categories for marketing, finance, or HR — which is likely part of why "business process and operations" absorbs a third of everything.
- **The snapshot is explicitly provisional.** "This is just a single snapshot, and Claude Cowork is still new; its uses are evolving quickly." Anthropic plans to keep publishing as usage shifts.

## Bundled resources
- `skills/knowledge-work-usage-taxonomy/` — classifying agent sessions into the post's 20-category taxonomy and reporting shares with the caveats attached. Includes a reference for the published category shares, a reference for the sampling method and its limitations, a report template, and a script that turns labeled session counts into a share table.
- `guides/work-around-the-work.{en,ko,es,ja}.md` — the full walkthrough of the findings in four languages.

## Source
[How people are using Claude Cowork](https://claude.com/blog/how-people-are-using-claude-cowork) — July 7, 2026

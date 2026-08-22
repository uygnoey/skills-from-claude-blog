**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
Ian Chan and Annabel Custer, on Anthropic's marketing operations team, describe two workflows they moved into Claude Cowork. Ian used to spend one to two days a week assembling the weekly marketing metrics review; it now takes up to two hours. Annabel used to set up each new event by clicking through Salesforce, HubSpot, Swoogo, and email tools in sequence; that sequence now runs almost entirely through Claude, with her reviewing each result before it ships.

Both workflows are built the same way: connectors to the platforms the team already uses, plus a set of small, single-purpose skills that get updated continuously as edge cases surface. Ian runs three skills for the report; Annabel runs a dispatcher plus five specialist skills for campaign builds, with a separate fresh Claude instance auditing the output and a standing "manager" agent she opens when a run misfires. Scheduled tasks start both — one every Sunday evening, one every hour.

The recovered hours changed the shape of the work rather than just shrinking it. Ian now spends more time helping marketers frame their own questions and going deeper into the data layer; Annabel spends more time on enablement and campaign architecture. Her stated motivation for building the automation was consistency and quality, not speed: as the marketing team scales, marketers cloning event pages from whatever template is nearby produce bugs like confirmation emails with the wrong city name.

## When is it useful?
- When a recurring report takes days because the numbers live in a dashboard, a warehouse, a Slack message, and a call transcript, and no pipeline covers all four.
- When a multi-platform setup process (CRM, marketing automation, event platform, email) is done by hand in sequence because the integrations between vendors are incomplete.
- When a queue of intake requests needs routing and stamping so work does not get duplicated.
- When automated output needs verification by something that did not produce it.
- When deciding what belongs in a skill versus what belongs in a prompt — the post's answer is that a correction you make twice belongs in a skill.
- When the goal is consistency across builds at scale, not only saved hours.

## Key points
- **A scheduled task does the data hunt before anyone is awake.** Every Sunday evening Claude reads the previous week's review and the latest meeting transcript, checks Slack for what the sales team is focused on, queries the warehouse, and leaves a folder with the numbers and a few suggested focus areas. Monday morning the report is already waiting.
- **The human picks the narrative; Claude expands it.** Ian confirms or redirects the suggested headlines, then asks Claude to expand with supporting details and examples. Some weeks the focus is a sales priority, others a product launch; at the quarter turn he feeds in the quarterly review doc and leads with quarterly plans. The leadership slide comes from the same data and narrative, and follow-ups become Asana tasks.
- **When the numbers don't line up, Claude flags the mismatch instead of guessing.** After a sales reorg, marketing's reporting no longer matched sales'. Claude surfaced the gap and asked how to handle it.
- **Three skills carry the report:** a prep skill that drives assembly, focus, headlines and expansion; a proofreading skill that checks every number in the draft against a verified source; and an action-items skill that turns follow-ups into Asana tasks.
- **The skills are updated at the end of every session.** Ian asks Claude to summarize what came up that should go back into the skills — a new sales reorg structure, corrections he made, a new way he wanted headlines framed.
- **A dispatcher separates routing from doing.** Once an hour it reads the intake channel, picks the most urgent request, stamps the ticket so the work is not duplicated, and hands off to one of five specialist skills. It does no event setup itself, which lets each specialist be refined without touching the routing.
- **The event-build skill runs the whole sequence:** CRM campaign creation, marketing automation campaign with workflows and lists, event platform setup, email drafting, landing page generation, and the integrations between them. It scripts two Slack updates — when Claude picks up the request, and when the landing page is ready for review.
- **The audit starts with no prior context.** A separate agent submits a test registration on the live landing page, opens the confirmation email in Gmail, and marks the Asana task complete if everything looks right. Annabel reviews each result before it ships.
- **A manager agent handles the misfires.** When a run goes wrong she opens it, asks what happened, and asks for a proposed adjustment. Anything worth keeping goes back into the relevant skill.
- **Four pieces of starting advice:** turn repeated corrections into skills (and let Claude write the skill); build the proofreading skill first; ask Claude to reflect on what was difficult about the instructions after the first runs; and lean on scheduled tasks, because work that runs on its own is work no one has to remember.

## Bundled resources
- `skills/weekly-metrics-report/` — the prep skill: scheduled data hunt, metrics tables, suggested headlines, narrative expansion, leadership slide.
- `skills/report-proofreader/` — the number-by-number check against verified sources; the post recommends building this one first.
- `skills/marketing-ops-dispatcher/` — hourly intake triage, ticket stamping, and routing to the five specialists, with a reference describing each.
- `skills/event-build/` — the end-to-end multi-platform event setup and its two scripted Slack updates.
- `agents/build-auditor.md` — the fresh-context audit agent that test-registers on the live page before anything is marked complete.
- `agents/workflow-manager.md` — the standing agent that diagnoses a misfired run and proposes the skill change.
- `guides/marketing-ops-automation.{en,ko,es,ja}.md` — the full write-up in four languages.

## Source
[How Anthropic's marketing operations team uses Claude Cowork to automate reporting and campaign builds](https://claude.com/blog/how-anthropics-marketing-operations-team-uses-claude-cowork-to-automate-reporting-and-campaign-builds) — Ian Chan and Annabel Custer, July 8, 2026

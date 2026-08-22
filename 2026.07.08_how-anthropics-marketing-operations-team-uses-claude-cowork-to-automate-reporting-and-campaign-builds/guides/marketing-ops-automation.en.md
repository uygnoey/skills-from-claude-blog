**English** · [한국어](./marketing-ops-automation.ko.md) · [Español](./marketing-ops-automation.es.md) · [日本語](./marketing-ops-automation.ja.md)

# Automating marketing operations with Claude Cowork

How two people on Anthropic's marketing operations team moved days of manual,
cross-platform work into hours.

## The problem with marketing ops work

Marketing operations teams spend a meaningful portion of their time keeping the
systems behind marketing programs in step with the business. Automation sits firmly
in their purview, and yet a lot of the work is anything but automated: martech tools
do not integrate cleanly with each other, reports are consolidated manually, landing
pages get spun up one at a time.

Ian Chan used to spend one to two days a week pulling together the weekly marketing
metrics review. Annabel Custer, who focuses on campaign operations, used to set up
each new event by clicking through Salesforce, HubSpot, Swoogo, and email tools in
sequence. Both have compressed days of manual work into hours by setting up workflows
in Claude Cowork.

The recovered hours shifted the shape of their work. Both now spend less time clicking
through systems and more time on enablement, validation, and the underlying data and
processes the marketing team relies on as more people across the company pull their
own numbers and drive their own programs.

---

## Part 1 — the weekly marketing metrics report

### Why it took two days

In a perfect world every metric in the weekly report would live in a dashboard and the
job would be writing the narrative. In practice:

- Some metrics are in the dashboard already.
- Others have not yet made it there from the data warehouse.
- Others have not been piped into the warehouse yet.
- New ones might exist only in a Slack message or a call transcript.

The business moves faster than a traditional reporting pipeline can keep up with. Ian
used to spend a day to two days every week tracking down data and validating it.

### The Sunday-night scheduled task

A scheduled task runs every Sunday evening. It prompts Claude to:

1. Read the previous week's review.
2. Read the latest meeting transcript.
3. Check Slack for what the sales team is focused on.
4. Query the warehouse.
5. Leave a folder with the numbers and a few suggested focus areas.

On Monday morning Ian opens Claude Cowork and pulls the initial report, which contains
the metrics tables and the suggested headlines.

### The human decision, then the expansion

Ian reviews the suggested areas of focus. Once he has confirmed or decided where to
focus the narrative, he tells Claude to expand on them with supporting details and
examples. Some weeks the team is responding to a sales priority, others to a product
launch. At the quarter turn, he tells Claude to lead with quarterly plans and feeds in
the quarterly review doc.

Claude generates the leadership slide from the same data and narrative: what changed,
why, and what the teams are doing about it. Any follow-ups become Asana tasks.

### When the numbers do not line up

Claude flags the mismatch instead of guessing. After a reorg on the sales team,
marketing's reporting no longer matched theirs. Claude flagged the gap and asked Ian
how to handle it.

### What it runs on

Connectors to the marketing platforms and tools the team uses, plus three skills Ian
has built and updates continually:

- **A prep skill** drives the report assembly, including focus, headlines, and
  expansion with supporting detail.
- **A proofreading skill** checks every number in the draft against a verified source.
- **An action-items skill** turns follow-ups into Asana tasks.

### Closing the loop each week

At the end of each weekly session, Ian asks Claude to summarize what came up that
should go back into the skills — the new sales reorg structure, the corrections he
made, a new way he wanted the headlines framed.

The entire process, which used to take up to two days of work, now takes up to two
hours.

### What the recovered time went to

A meaningful share of Ian's time has moved to helping marketers frame their questions,
refine their prompts, and interpret what they get back when they pull their own
numbers from Claude. He also has bandwidth to go deeper into the data layer, making
sure Claude interprets the numbers, definitions, and regional structures the same way
as the data warehouse.

Human validation has become an integral part of both workstreams — a shift that is
accelerating as Claude automates the mundane manual tasks that have traditionally
taken up much of marketing analysts' time.

---

## Part 2 — event builds and data imports

### Why it was manual

Setting up the infrastructure behind marketing campaigns has traditionally been one of
the most manual processes in marketing. Every event, webinar, or integrated campaign
needs to be set up in the CRM, in the marketing automation platform that runs the
email sequences and the automation behind them, and in the event management platform
that hosts the registration page and the event landing page. Each of these is
typically a different vendor, and the integrations between them are rarely complete.

Before Claude Cowork, Annabel picked up every request from a dedicated Slack channel
and worked through the sequence manually.

### Intake and dispatch

Her setup starts with an intake form where requesters specify the type of help they
need: event build, data import, apply-to-attend, or approval support.

Once an hour, a dispatcher skill reads the channel, picks the most urgent request,
stamps the ticket so the work does not get duplicated, and hands it off to one of five
specialist skills. It does no event setup itself; its job is to decide what runs next,
and keeping it separate lets Annabel refine each specialist skill on its own without
touching the routing.

### The event build

For an event build — the most complex request type — an event-build skill handles the
full sequence end to end: CRM campaign creation, marketing automation campaign with
workflows and lists, event platform setup, email drafting, landing page generation,
and all of the integrations between them.

The skill scripts two Slack updates: when Claude picks up the request, and when the
landing page is ready for the requester's review and the audit takes over.

### The audit

When the build is done, it hands off to a new agent for audit. The audit agent starts
with no prior context, submits a test registration on the live landing page, opens the
confirmation email in Gmail, and marks the Asana task complete if everything looks
right. Annabel reviews each result before it ships.

### The skills behind it

Connectors to the marketing platforms and tools she works with, plus skills she has
built and updates as she finds new edge cases:

- **A dispatcher skill** reads the intake channel and routes each request to the right
  specialist skill.
- **An event-build skill** drives the end-to-end setup across platforms.
- **A webinar-landing-page creation skill** spins up landing pages for webinars.
- **An audit skill**, run by a separate fresh Claude instance, verifies the
  event-build skill's output before the task is marked complete.
- **An apply-to-attend skill** handles in-flight changes to the registration flow.
- **An approval-support skill** handles event approvals and sends the appropriate
  emails at a scheduled cadence.
- **A data-import skill** scrubs lists and processes attendee data.

She also keeps a separate "manager" agent open. When a run misfires, she opens the
manager and asks it to look at what happened and propose what to adjust. Anything
worth keeping goes back into the relevant skill.

### Quality was the motivation, not speed

While these workflows will become significant time savers, Annabel's primary
motivation to build them was quality of work. As the marketing team scales, marketers
cloning event pages from whatever template happens to be nearby can produce bugs —
confirmation emails surfacing the wrong city name, broken landing pages. With Claude
Cowork she gets consistency across builds, at scale.

As Claude takes on the repetitive parts of campaign operations, Annabel can focus on
more strategic projects like enablement, and on automating or optimizing processes and
campaign architecture for better insights.

---

## Advice for marketing ops teams getting started

- **Turn repeated corrections into skills.** When you find yourself correcting Claude
  on the same thing more than once, that feedback belongs in a skill. You do not need
  to build skills yourself, either — Claude can do that for you.
- **Build a proofreading skill first.** It checks that every number Claude puts in a
  report traces back to a verified source.
- **Ask Claude to reflect.** Claude reads instructions differently than a human writes
  them, so after the first runs of a new workflow, ask what was difficult about the
  instructions. Feed what surfaces back into the skill as part of a broader practice of
  constantly updating them.
- **Lean on scheduled tasks.** Work that runs on its own every Sunday night or every
  hour is work no one has to remember to do.

## Source

[How Anthropic's marketing operations team uses Claude Cowork to automate reporting and campaign builds](https://claude.com/blog/how-anthropics-marketing-operations-team-uses-claude-cowork-to-automate-reporting-and-campaign-builds) — Ian Chan and Annabel Custer, July 8, 2026

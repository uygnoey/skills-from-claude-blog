**English** · [한국어](./work-around-the-work.ko.md) · [Español](./work-around-the-work.es.md) · [日本語](./work-around-the-work.ja.md)

# The work around the work

A walkthrough of Anthropic's May 2026 study of Claude Cowork usage, and what its
shape says about how knowledge workers actually delegate.

## Why the study exists

When Claude Code was released in 2025, Anthropic was surprised at how many
non-technical users started playing around with it. People who had never opened a
terminal used it to create agents that organized folders, deduplicated files, and
wrote spreadsheet formulas.

For others, the terminal remained a slightly intimidating place — a literal "black
box". Claude Cowork was built to extend the agentic capabilities of Claude Code
into the same chat interface people were already using to talk to Claude.

Since the January launch, Cowork became an especially potent tool for people whose
work centers on the creation and exchange of information — knowledge work. The
study asks what that population actually does with an agent.

## What the data shows

The sample: 1.2 million anonymized and aggregated sessions from May 11–31, 2026,
across more than 600,000 organizations, classified by an automated system into a
taxonomy of 20 categories of work.

| Category | Share |
| --- | --- |
| Business process and operations | 33.4% |
| Content creation and copywriting | 16.4% |
| Software development | 8.7% |
| DevOps and infrastructure | 7% |
| Research and intelligence | 6.4% |
| Data analysis and business intelligence | 5.8% |
| Document processing and extraction | 4.1% |
| Sales and revenue operations | 4% |
| Personal assistance | 3.8% |
| Education | 2.4% |
| Meeting and conversation intelligence | 1.8% |
| Legal and compliance | 1.3% |
| Customer support | 0.8% |

**Business process and operations** leads at 33.4% — pulling scattered updates into
a single report, building onboarding checklists, reconciling spreadsheets. This
makes sense because business operations tasks span many different roles: people in
finance, HR, and administrative jobs are all likely to reach for them.

**Content creation and copywriting** follows at 16.4% — synthesis-intensive
business communications like drafts, slide decks, posts, and proposals. Staring
down a blank page is often the first barrier to getting started, and an agent is
useful for threading thoughts and information into a rough draft. These tasks also
cross roles: marketing, communications, business development, and project
management all land here.

Everything else falls below 9%. All categories under 4% include personal assistance
(3.8%), education (2.4%), and meeting intelligence (1.8%).

## How knowledge workers are using AI

It is telling that the top two categories make up roughly half of all usage. Both
are overwhelmingly connective in nature:

- Spreadsheets pull disparate data points into a context where they can be read,
  compared, and tracked.
- Decks convey an idea or decision to a broader audience with varying levels of
  context.
- Onboarding checklists help a new hire tap into institutional knowledge.

The reading Anthropic offers: people are using Cowork to assemble and structure the
information they can use to act on their expertise. Three worked examples from the
post:

- A **lawyer** hands over document formatting and filing, gaining time to apply
  legal judgment to challenging cases.
- A **hiring manager** hands over meeting scheduling and interview-feedback
  synthesis, gaining time for candidate conversations and evaluating work samples.
- A **team lead** hands over the slide deck that explains a difficult decision,
  freeing them up to actually make those tough calls.

The boundary is consistent across all three: assembly and structure move to the
agent; the expertise stays with the person.

## The contrast with Claude Code

This pattern is close to the inverse of how Claude Code gets used. Claude Code is
most often used by software developers for the key parts of their role: building,
debugging, and shipping code. So it is perhaps unsurprising that software
development makes up such a small share of Cowork use — 8.7%.

Developers are much more likely to use Claude Code than Cowork to write code. The
work they do in Cowork is the connective, communications-focused work that
surrounds every role, software engineering included.

A low software-development share in a chat-interface agent is therefore the
expected result of tool specialization, not evidence of weak developer adoption.

## The rise of AI in knowledge work

Coding still — understandably — gets the most attention among AI uses. But the use
of AI for everyday business work is rising, and the tasks it helps most with are
coming into focus: status reports, decks, trackers, and the rest of the machinery
that tracks and communicates information across teams.

Anthropic frames this as a single snapshot of a new and quickly evolving product,
intended as a reference point for people figuring out how to integrate AI into
daily work, with more data promised as usage shifts.

## Reading the numbers responsibly

The post's own methodology section is the guide here.

**How it was measured.** An automated system classified sessions into a 20-category
taxonomy, using a privacy-preserving analysis tool that keeps all user information
anonymous. No individual session was read by a human analyst; only aggregate
category-level statistics were used. Sampling was rate-capped — a fixed maximum
number of sessions per hour, not a fixed percentage of traffic.

**Taxonomy granularity.** The taxonomy classifies sessions by the work being done,
not the job title of the person doing it. There are no standalone categories for
marketing, finance, or HR — those functions are best represented by "business
process and operations", which is likely part of why it occupies a third of usage.

**Shares versus volumes.** Because sampling is rate-capped, the session and
organization counts do not reflect total usage or growth, and busier hours are
somewhat underrepresented relative to quieter ones.

**Window choice.** Three complete recent weeks were used rather than a longer span
because category shares shifted around May 11 in a way consistent with a change in
the labeling pipeline rather than in user behavior. The reported shares were
computed entirely after that change and are correct under either explanation.

**Mix of work and personal use.** The sample covers external organizations, not
individuals, but includes some personal use — personal assistance, hobbies, and
companionship-style conversations together account for roughly 5% of sessions.

**Automated classification.** Labels came from an automated system, not a human
reviewer, and any classifier could have errors. Where sessions could plausibly fit
multiple categories, results depended on the taxonomy's definitions.

## What to take from it

- Delegate assembly and structure first; that is where the published mass of usage
  already sits.
- Keep the judgment — the legal call, the candidate evaluation, the decision the
  deck explains.
- Expect a coding agent and a chat agent to show opposite usage mixes, and do not
  read that as an adoption problem.
- When reporting your own usage data, publish the limits alongside the shares.

## Source

[How people are using Claude Cowork](https://claude.com/blog/how-people-are-using-claude-cowork) — July 7, 2026

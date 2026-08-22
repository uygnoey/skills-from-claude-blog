---
name: knowledge-work-usage-taxonomy
description: Classify agent sessions into the 20-category work taxonomy published in "How people are using Claude Cowork", report category shares as shares of a sample rather than volumes, and attach the sampling and classification caveats that make such a report honest. Use when auditing what an agent is actually being used for, when deciding which tasks to delegate based on a published distribution rather than a guess, or when writing or reviewing a usage-share report.
---

# Knowledge work usage taxonomy

A method for answering "what is this agent actually being used for?" in a way that
survives scrutiny. It comes from Anthropic's May 2026 study of 1.2 million sampled
Claude Cowork sessions, which found that roughly half of all usage is "the work
around the work" — tasks that appear across a broad swath of jobs but are rarely
anyone's core responsibility.

The value here is not the specific percentages. It is the shape of the analysis:
a taxonomy that classifies *work* rather than *job titles*, shares reported against
a rate-capped sample rather than absolute volumes, and a limitations section that
states plainly what the numbers cannot support.

## Instructions

### 1. Classify by the work, not by the person

Label each session by the work being done, not by the role of the person doing it.
The published taxonomy has no standalone marketing, finance, or HR category — those
functions land in "business process and operations", which is part of why that
category absorbs a third of everything. Know that tradeoff before you adopt the
taxonomy, and record it rather than papering over it.

Use the category list and published shares in
[references/category-shares.md](references/category-shares.md) as the label set.
When a session plausibly fits more than one category, the result depends on the
taxonomy's definitions — note which definitions were doing the work.

### 2. Sample deliberately, and say how

The study sampled at a capped rate — a fixed maximum number of sessions per hour —
rather than as a fixed percentage of traffic. That choice has a direct consequence:
every number is a share of sampled sessions and not an absolute volume, and busy
hours are somewhat underrepresented relative to quiet ones.

Pick a sampling rule, then live with what it permits you to claim. The full method
and its consequences are in
[references/methodology-and-limits.md](references/methodology-and-limits.md).

### 3. Keep the analysis privacy-preserving

The study worked only with aggregate category-level statistics; no individual
session was read by a human analyst. If you are classifying real sessions inside
an organization, hold to the same line: automated labeling, aggregate reporting,
no human reading individual sessions.

### 4. Compute shares, not totals

Turn labeled counts into percentage shares of the sample. Report the top category
alongside the next one so the gap is visible — in the published data, business
process and operations at 33.4% is more than double content creation and
copywriting at 16.4%, and that ratio is the finding, not the raw 33.4%.

Run [scripts/usage_shares.py](scripts/usage_shares.py) over a JSON object of
`{"category": count}` to get a sorted share table plus the top-two gap.

### 5. Read the shape, not just the ranking

The published reading is that the top categories are connective in nature:
spreadsheets pull disparate data points into a context where they can be read,
compared, and tracked; decks convey an idea or decision to a broader audience with
varying levels of context; onboarding checklists help a new hire tap into
institutional knowledge. Ask what your own top categories have in common before
concluding anything from their order.

Watch for the delegation boundary in the data. In the published examples, a lawyer
delegates document formatting and filing but keeps the legal judgment; a hiring
manager delegates scheduling and interview-feedback synthesis but keeps the
candidate conversations; a team lead delegates the deck that explains a difficult
decision but keeps the decision. Assembly and structure move; expertise does not.

### 6. Write the limitations section before the conclusions

A usage-share report without stated limits invites over-reading. At minimum,
address taxonomy granularity, shares versus volumes, window choice, the mix of
work and personal use, and automated rather than human classification. Use
[templates/usage-report.md](templates/usage-report.md), which lays out those
sections in order.

### 7. Date the snapshot and expect it to move

The published analysis calls itself "a single snapshot" of a product whose "uses
are evolving quickly", and commits to republishing as usage shifts. Any report
produced this way should carry its window on its face and be treated as a
reference point rather than a settled fact.

## Examples

### Auditing an internal deployment

A platform team wants to know what 40,000 internal agent sessions were used for.
They classify sessions automatically into the 20 categories, discover that business
process and operations dominates locally too, and report it as "33% of sampled
sessions in a three-week window" rather than "a third of all usage". The report
names the labeling pipeline's version, because a mid-window change to that pipeline
is exactly what forced the published study to shorten its own window.

### Deciding what to delegate

A team lead reads the distribution and reframes their own backlog: the status
update, the tracker reconciliation, and the deck explaining a reorg are all
assembly-and-structure work that others already delegate at scale. The decision the
deck explains is not. They hand over the first three and keep the fourth.

### Comparing two tools honestly

An organization runs both a coding agent and a chat-interface agent and wonders why
the usage mixes look nothing alike. The published contrast supplies the frame:
developers use the coding agent for the core of their role — building, debugging,
shipping — and the chat agent for the connective, communications-focused work that
surrounds every role, software engineering included. A low software-development
share in the chat agent is the expected result, not a failure of adoption.

### Reviewing someone else's usage report

A reviewer checks a vendor's usage claims against the checklist in the report
template: are these shares or volumes? Was sampling rate-capped? Does the taxonomy
split out the categories the conclusions depend on? Were labels human-verified?
Three of the four go unanswered, and the review says so.

## Source

[How people are using Claude Cowork](https://claude.com/blog/how-people-are-using-claude-cowork) — July 7, 2026

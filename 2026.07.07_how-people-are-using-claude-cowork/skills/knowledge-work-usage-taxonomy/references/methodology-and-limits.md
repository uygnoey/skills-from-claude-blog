# Methodology and limits

How the published analysis was conducted, and what it therefore cannot support.
Reproduce this section's shape in any usage-share report you write.

## How it was measured

- **Source.** A sample of Claude Cowork sessions, classified by an automated system
  into a 20-category taxonomy of work.
- **Privacy.** Gathered with a privacy-preserving analysis tool that keeps all user
  information anonymous. No individual session was read by a human analyst; the
  analysis worked only with aggregate category-level statistics.
- **Sampling.** Collected at a **capped rate** — a fixed maximum number of sessions
  per hour — rather than as a fixed percentage of traffic.
- **Window.** May 11–31, 2026.
- **Size.** 1.2 million sampled sessions from more than 600,000 organizations.

## Stated limitations

### Taxonomy granularity

The taxonomy classifies sessions by the work being done, not by the job title of
the person doing it. Several categories map cleanly onto recognizable knowledge-work
functions — research and intelligence (6.4%), data analysis and business
intelligence (5.8%), sales and revenue operations (4%), legal and compliance (1.3%),
meeting and conversation intelligence (1.8%), customer support (0.8%). But there is
no standalone category for marketing, finance, or HR; those are absorbed into
"business process and operations", which is likely part of why it occupies a third
of all usage.

### Shares versus volumes

Because the sample is rate-capped, the sampled session and organization counts do
**not** reflect total usage or growth. Usage during busier hours of the day is
somewhat underrepresented relative to usage during quieter hours.

### Window choice

Three recent complete weeks were used rather than a longer span, because category
shares shifted around May 11 in a way consistent with a change in the labeling
pipeline rather than a change in user behavior. The reported shares were computed
entirely after that change, and are correct under either explanation.

### Mix of work and personal use

The sample covers use among external organizations, not individuals, but the
sessions include some personal, non-work use. Personal assistance, hobbies, and
companionship-style conversations together account for roughly 5% of sessions, so
the sample does not purely represent workplace activity.

### Automated classification

Category labels were applied by an automated system, not by a human reviewer, and
any classifier could have errors. Where sessions could plausibly fit multiple
categories, results depended on the definitions in the taxonomy.

## Checklist for your own report

- [ ] Are the numbers shares of a sample, and does the text say so every time?
- [ ] Is the sampling rule stated (rate-capped, percentage, census)?
- [ ] Is the window stated, and is the reason for its length stated?
- [ ] Did the labeling pipeline change inside the window?
- [ ] Which conclusions depend on categories the taxonomy does not split out?
- [ ] Were labels applied automatically, and was any human verification done?
- [ ] How much of the sample is non-work use?
- [ ] Was any individual session read by a person?

## Source

[How people are using Claude Cowork](https://claude.com/blog/how-people-are-using-claude-cowork) — July 7, 2026

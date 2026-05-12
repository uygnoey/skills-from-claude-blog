# CLUE architecture and metrics — verbatim from the post

This reference mirrors the architectural components, named tools, metrics, and direct quotes that appear in "How Anthropic's cybersecurity team built a threat detection platform with Claude Code." Do not extend this list with anything not in the source.

## Team and product context

- **Team:** Detection Platform Engineering, Anthropic.
- **Tech Lead:** Jackie Bow.
- **Scope:** Defensive cybersecurity — detecting threats and responding to potential breaches, not probing for vulnerabilities.
- **Policy framing:** [Anthropic's Responsible Scaling Policy](https://www.anthropic.com/news/anthropics-responsible-scaling-policy) ties product releases to security commitments; the Detection Platform team is part of what determines what can ship safely.
- **Build collaborator:** Claude Code, described as both "design partner and collaborator". Proof of concept in a day; design and implementation finished within a week.

## CLUE — Claude Looks Up Evidence

CLUE is a detection-and-response platform with a natural-language interface powered by Claude, connected to Anthropic's internal systems via tool use.

### CLUE Triage

- First-pass triage on every incoming alert, before a human analyst sees it.
- Claude uses tools to enrich each alert with additional context from Slack messages, internal documentation, code repositories, and data warehouses.
- Assigns a **disposition**: `false positive`, `true positive`, `malicious`, or `expected behavior`.
- Each alert receives a **confidence score**.
- Quote: "That internal context is the missing piece that really helps alerts be contextualized for your environment."

### CLUE Investigate

- Natural-language interface to query all security-critical logs.
- Claude writes precise queries (the post: "Claude is much better at writing precise queries than humans are").
- **Agentic loop shape:** an orchestrator issues commands to sub-agents that execute queries in parallel, gather findings, and synthesize results into coherent investigation summaries.
- Investigations that previously took hours now run in **three to four minutes**.
- Per-investigation averages: **~25 tool calls** and **~11 queries**.

### Demonstrated scenario in the post — data governance review

- Use case: check whether three contractors accessed documents they shouldn't have over the past two months.
- Manual baseline: at least half a day of work (querying access logs, cross-referencing permissions, reviewing document classifications).
- With CLUE: Claude reads the request, formulates a plan, generates verbose queries that abstract the technical complexity, and finishes in minutes with a summary plus recommendations and full transparency into every query run.

## Reported impact metrics

- **False-positive rate:** roughly **1 in 3 → 7%**.
- **30-day usage:** roughly **12,000 queries** and **27,000 tool calls** automated.
- **Manual-work avoided:** roughly **1,870 hours / 234 person-days**.
- **Time savings:** **5–10×** versus manual triage.
- **Coverage:** lower-confidence signals that previously went unexamined are now processed by CLUE Triage; batch processing handles thousands of signals that were previously noise in a dashboard.
- **Accuracy measurement** is described as harder than speed measurement; feedback loops are still being built.
- Footnote in the post: results were generated using Claude Sonnet and Opus models.

## Forward-looking themes from the post

- **From reactive to proactive.** Continuous exploration / hunting agents rather than purely alert-driven investigation.
- **Learning from itself.** Stored investigation transcripts become a corpus Claude can query for patterns.
- **Embracing non-determinism.** Run multiple investigation strategies in parallel; treat divergent paths as a feature.
- **The bitter lesson, applied to security ops.** Stop encoding human-specific investigation steps; give the model boundaries plus a goal and let it find better approaches than humans would have prescribed.

## Direct quotes from the post

- "I feel like it's the golden age of the security engineer. I can finally build the tools I always wished I had."
- "There's only so many alerts a human can look at in a day before they start to drop off in how detailed they're going into it."
- "We can't scale to meet the needs of Anthropic without augmenting with something like Claude."
- "So much of what we built was us talking to Claude Code. It was both a design partner and collaborator."
- "That was when I realized I'm not bound by my own technical limitations anymore. I can build whatever I can think of."
- "Claude is much better at writing precise queries than humans are."
- "Early in CLUE's development, the team debated how much to constrain Claude's investigation paths… When we gave Claude latitude to explore — access to tools and a goal, rather than a rigid sequence — it often took investigation paths we wouldn't have prescribed. Sometimes those paths surfaced context we'd have missed."
- "The bitter lesson for security operations? We spent years building systems that encoded how humans investigate. The next generation of tools should give models the capability to investigate and let them find better approaches than we would have prescribed."

## Related links referenced by the post

- [Anthropic's Responsible Scaling Policy](https://www.anthropic.com/news/anthropics-responsible-scaling-policy)
- ["The bitter lesson"](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) (Sutton)
- [Claude Code](https://www.anthropic.com/claude-code)

## Source

- [How Anthropic's cybersecurity team built a threat detection platform with Claude Code](https://claude.com/blog/how-anthropic-uses-claude-cybersecurity)

**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
A first-person account by John Albert, a business development rep (BDR) at Anthropic, of how his team runs inbound and outbound through Claude Cowork. He used to spend around five hours a day manually answering the sales inbox — often the same questions — on top of managing his own book of business. That work now runs as skills and scheduled tasks, with drafts he reviews and customizes before sending.

The post walks through the concrete workflows: an hourly inbox skill built on a sales knowledge base and a per-rep voice profile; lighter monitors for no-shows and new leads; a pipeline scanner that proposes CRM stage updates with evidence; an overnight prospecting sweep across a hundred-plus accounts that returns a brief, a score, and an outbound play each morning; a call coach that scores discovery calls against the team's playbook; and ad-hoc analysis for one-off requests from account executives. It closes with six pieces of getting-started advice.

## When is it useful?
- When a repetitive inbox is eating hours a day and the answers are already known somewhere.
- When outbound coverage is capped by how much research one person can do by hand across a large book.
- When CRM hygiene depends on reps remembering to update stages that the evidence in email and call recordings already implies.
- When you want scheduled agent work to produce reviewable drafts rather than autonomous sends.
- When a team wants to share workflows across reps whose books and routines differ.

## Key points
- **Build the knowledge base before the workflows.** A single document of the questions the team answers repeatedly, with the best answers, is the foundation of the inbound setup. Claude built the first version from existing sources and now flags information that may be stale for a human to validate.
- **The inbox skill is deliberately thin.** It is a thin system prompt, the knowledge base as the source for product facts, and a profile of the rep's writing style — the voice profile itself produced by a skill that reads documents, messages, and emails the rep has written. It runs hourly, finds threads needing a reply, and leaves drafts.
- **Lighter monitors cover the gaps.** One skill watches Gmail and Google Calendar for no-shows and prospects going dark; another scans the CRM for new leads and drafts a personalized first touch on a schedule through the day.
- **Pipeline updates arrive as proposals with evidence.** A skill reads the team's guidance on opportunity stages and checks it against what is actually happening in email and call recordings, then proposes each CRM update with the evidence behind it and waits for approval. Edits and rejections are recorded with the reason, so the mistake is not repeated.
- **Prospecting runs overnight across the whole book.** A scheduled skill observes the current state of each account — who the team is in touch with, how they use the product, which signals matter — by connecting to the CRM, sales tools, call recordings, and the data warehouse, then validates findings against curated outbound guidance and ICP criteria. The rep opens a brief, a score, and an outbound play per account in the morning.
- **A small memory file and ledger prevent duplicate work,** and rep feedback on results feeds back into the skill.
- **Discovery calls get a scorecard.** Call transcripts are evaluated against the discovery playbook: the top three things done well, the top three areas to improve, an explicit pass/fail against the criteria, and a single highest-leverage thing to practice next.
- **Not everything needs a skill.** One-off requests — a spend analysis for a top account, a sweep for accounts using the product with no matching opportunity, finding webinar invitees scored against the ICP — are often just a prompt away.
- **Keep a person on every send.** Claude generates drafts; reps read, edit, and send them.
- **Share skills, but keep them general.** The team promotes its most-used skills into a shared plugin once reps use them consistently, and keeps shared skills general enough to adapt to different books and routines rather than scoped to one person.

## Bundled resources
- `skills/inbound-reply-drafting/SKILL.md` — the hourly inbox skill, its knowledge base, and the voice profile behind it.
- `skills/account-prospecting-sweep/SKILL.md` — the overnight prospecting run and the ad-hoc analysis requests around it.
- `skills/pipeline-hygiene-proposals/SKILL.md` — evidence-backed CRM stage proposals that wait for approval.
- `skills/discovery-call-scorecard/SKILL.md` — scoring discovery calls against a playbook.
- `guides/business-development-with-cowork.{en,ko,es,ja}.md` — the whole operating model plus the getting-started advice, in four languages.

## Source
- https://claude.com/blog/how-anthropics-business-development-team-uses-claude-to-run-inbound-and-outbound-at-scale (August 7, 2026)

**English** · [한국어](./business-development-with-cowork.ko.md) · [Español](./business-development-with-cowork.es.md) · [日本語](./business-development-with-cowork.ja.md)

# Running inbound and outbound with an agent workspace

Derived from the August 7, 2026 first-person account by John Albert, a business
development rep (BDR) at Anthropic, on how his team runs inbound and outbound
through Claude Cowork.

## Where the time went

Early in a BDR career, account executives hand over lists of hundreds of
accounts: investigate each company, find the right contacts, hunt down emails,
draft outreach. The inbound side was similarly manual. After joining Anthropic
and taking over the sales inbox, Albert spent around five hours a day answering
inbound interest by hand — often the same questions — on top of his own book of
business.

That work now runs as skills and scheduled tasks. Personalized customer emails
arrive as drafts he reviews and customizes before sending, and outbound starts
from research he did not spend hours compiling.

## The architecture, in one line

**Curated context + thin skills + a schedule + a person on every send.**

Each piece of the setup below is an instance of it.

## 1. Inbound: the knowledge base comes first

The foundation is a single document collecting the questions the sales inbox
receives most often, with the team's best answers. Claude built the first
version from the relevant sources and now continuously checks it, flagging
information that might be stale for a person to validate.

The heaviest workflow sits on top of it. The inbox skill runs **every hour**: it
scans the rep's inbox, finds every thread needing an answer, and drafts a reply
to read, edit, and send. It is made of three thin parts — a thin system prompt,
the knowledge base as the source for product facts, and a profile of the rep's
writing style. Each rep builds that voice profile with a skill that reads
documents, messages, and emails they have written.

Two lighter skills cover the administrative edges: one watches Gmail and Google
Calendar for meeting no-shows and prospects going dark, so follow-up is quick;
another scans the CRM for new leads and drafts a personalized first touch,
running on a schedule through the day so leads are not left waiting.

## 2. Pipeline hygiene: proposals with evidence

A skill keeps Salesforce current by reading the team's internal guidance on
opportunity stages and checking it against what is actually happening in Gmail
and Gong. If the team has met a customer and moved on to pricing questions, the
opportunity should probably progress a stage.

Claude proposes each update **with the evidence behind it** and waits for
approval. When a proposal is edited or rejected, the reason is recorded so the
mistake is not repeated.

## 3. Outbound: an overnight sweep of the whole book

Albert works upwards of a hundred accounts at a time. A skill running as a
scheduled task overnight prospects across the entire book, observing the current
state of each account: who the team is in touch with, how they use the product
today, which signals are relevant. It connects to Salesforce, sales tools like
Apollo and Common Room, Gong, and the data warehouse, performs deep research,
and validates the result against outbound guidance and ICP criteria the team has
curated.

In the morning, the rep opens a brief, a score, and an outbound play for each
account. A small memory file and ledger prevent repetitive or duplicative work,
and rep feedback on the results feeds back into the skill — which is what makes
the workflow more useful over time.

The payoff is in the conversation: outreach is tailored, and the rep is informed
enough about the customer's business to have a deeper strategic discussion.

## 4. Call coaching: a scorecard per discovery call

Another skill evaluates Gong transcripts against the team's discovery call
playbook and builds a scorecard for each call, with feedback specific to the
conversation: the top three things done well, the top three areas to improve, an
explicit pass or fail on the criteria, and a single highest-leverage thing to
practice next.

## 5. One-off requests: often just a prompt

Ad-hoc requests from account executives let the BDR team partner more
strategically, and most do not need a skill:

- **Usage trends for a top account** — a prompt away from a legible, descriptive
  dashboard of the relevant trends.
- **Undiscovered usage** — consider an AE's full book and find account-level
  usage signals where no sales opportunity exists yet. Often a strong signal to
  reach out and work with the customer on optimizing their usage.
- **Event outreach** — asked to find accounts in an AE's book worth inviting to
  an upcoming webinar, Claude checked usage data and CRM history across the
  book, scored each account against the ICP, and flagged the best fits with
  contacts worth inviting. No skill existed for it; a prompt was enough.

## Getting started

The post's own advice for business development teams:

1. **Build the knowledge base before the workflows.** Collect the questions your
   team answers repeatedly, and your best answers, into a single
   external-facing document. You do not have to write it by hand — point Claude
   at your product docs and team channels and have it build the first version.
2. **Give Claude examples of how your team works.** It drafts against the
   context you give it: messages that worked, your ideal customer profile, and a
   per-rep writing style so drafts sound like the sender.
3. **Keep a person on every send.** Claude generates drafts; reps read, edit,
   and send them.
4. **Share skills across the team.** Keep the most-used ones in a shared plugin,
   promoting a skill there once reps use it consistently in daily work.
5. **Make skills general enough to adapt.** Segments, books, and workflows differ
   across reps, so shared skills stay general rather than scoped to one person's
   routine.
6. **Write feedback back into the skills.** When you dismiss a hook or correct a
   draft, have Claude record the reason so it does not make the same mistake
   again.

And the closing note: just start experimenting. The more context and tools you
give it, the more you can get done.

## Source

https://claude.com/blog/how-anthropics-business-development-team-uses-claude-to-run-inbound-and-outbound-at-scale (August 7, 2026)

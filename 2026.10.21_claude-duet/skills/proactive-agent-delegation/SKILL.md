---
name: proactive-agent-delegation
description: Plan how to hand work to Claude Duet, the proactive agent app for professionals and small business owners (research preview, US Pro and Max subscribers via waitlist; iOS, Android, and claude.ai). Covers the three modes (morning brief, all-day monitoring of connected apps, delegated tasks from scheduling to dashboards, forecasts, prototypes, and web apps), what carries over from the Claude account (memory, skills, connected apps), choosing check-in topics and frequency, the approval gate before sending, paying, signing, or deleting, actions that stay off-limits even with approval, purchases through Link virtual cards or Shop Pay, and the preview's known limits and usage cost. Use when someone wants to set up Duet, decide what to delegate to it, explain its safety model, or set expectations about what it cannot do yet.
---

## Purpose
Claude Duet is a proactive agent app. It watches the apps a user connects, sends a short morning
brief, messages only when something needs attention, and takes on tasks in the background on its own
virtual machine and browser. This skill helps a user decide what to delegate, how to configure
check-ins, and where the approval line sits, using only what the announcement states.

## When to use
- A Pro or Max user in the US is getting started with Duet (research preview, waitlist).
- Someone asks "what should I hand to Duet?" or "what will it do without asking me?"
- A small business owner wants to connect accounting, payments, CRM, or storefront apps.
- You need to set expectations about the preview's limitations and usage cost.

## Instructions

1. **Confirm access.** Duet is a research preview for US Pro and Max subscribers who join the
   waitlist on the Claude Duet product page. It runs as a standalone app on iOS and Android and on
   claude.ai, separate from the main Claude app. During the preview it shares the usual Claude usage
   limits. Do not promise availability outside this.

2. **Inventory what carries over.** Duet brings the user's memory, skills, and connected apps from
   their Claude account. List what is already connected before suggesting new connectors. Over 6,000
   connectors and plugins from the Claude Marketplace are available (examples in
   [references/how-duet-works.md](references/how-duet-works.md)).

3. **Map work to the three modes.**
   - **Morning brief** — the most important items across connected apps, each morning.
   - **Monitoring** — Duet checks connected accounts every few hours and messages only when
     something needs attention. Ask the user what they want to hear about and how often; they can
     choose both.
   - **Tasks** — simple (scheduling a meeting) or complex (dashboards, forecasts, prototypes, web
     apps). Tasks run in the background, so the user's laptop or phone can be off. Duet notifies when
     a task finishes or needs review.
   Use one ongoing thread, by text or voice.

4. **Draw the approval line.** Duet can read, draft, and prepare work on its own. Before it sends a
   message, makes a payment, signs a document, or deletes anything, it shows the action and waits for
   approval. Some actions, such as trading securities or moving money between accounts, are
   off-limits even with approval. Any app can be disconnected. Tell the user plainly which of their
   planned tasks will stop for approval.

5. **Handle sensitive data correctly.** Requests for the strictest tier of data (for example credit
   card numbers, government ID) are rejected. Health and personal finance information is shared only
   when the user explicitly instructs it. Purchases go through Link (Stripe's wallet) with a virtual
   card, or Shop Pay, so the real card number is not shared. The full safety design is in
   [references/how-duet-works.md](references/how-duet-works.md).

6. **Set expectations.** In the preview Duet may misread a thread or misjudge urgency; personal
   errands such as booking tickets are weaker than work tasks; it cannot yet show its browser; and
   background checks and large tasks (financial models, decks) take more model turns and count toward
   usage limits. Suggest fewer check-ins or narrower topics if usage is a concern.

7. **Start from a real pattern.** Pick the closest tester pattern in
   [examples/tester-workflows.md](examples/tester-workflows.md) and adapt it.

## Examples
- User: "I want Duet to handle my inbox and pay vendor invoices."
  → Connect Gmail and the accounting/payment apps. Duet can triage and draft replies and prepare
  invoice payments, but it waits for approval before sending any reply or making any payment.
- User: "Can it move money from checking to savings every Friday?"
  → No. Moving money between accounts is off-limits even with approval.
- User: "I run a real estate brokerage and live in my calendar."
  → Turn on monitoring for the calendar and listing tools; a tester got an unprompted alert that a
  property showing sat on the wrong calendar day.
- User: "I leave at 5pm for my kids — can it keep working?"
  → Hand over the to-do list before leaving; Duet works on its own VM and saves results for an
  evening report.

---
name: small-business-first-workflow
description: Help a small business owner or operator (often non-technical, 5-50 employees) get a first real workflow running in Claude, following the lessons Anthropic reported in September 2026 from workshops with more than 1,000 owners - pick a run-the-business or grow-the-business task (reporting is the most common), build it in Claude Cowork with skills, connectors, or the Claude for Small Business plugin, treat Claude like a new employee whose work is checked, keep a human in the loop for review and sending, and log the workflow in a registry with PII handling noted. Use when an owner asks where to start with AI, wants to automate a report or operational task, or worries about accuracy and data security.
---

## Purpose
The source recaps workshops where small business owners built their own tools in Claude. Its lessons: owners
use AI for important work but worry about accuracy, data security is the top concern, agents feel intimidating
until the first workflow runs, and owners learn best from peers. This skill walks an owner from "I've only
used chat" to one working, reviewed workflow.

## When to use
- An owner or operator wants a first practical AI workflow.
- A report or recurring operational task should be handed to Claude with checks in place.
- The owner raises accuracy or data-security worries.

## Instructions

1. **Pick one task tied to the business.** Ask whether it helps run the business (about two-thirds of workshop
   requests) or grow it (about a third). Reporting was the most common use case; owner-specific tools such as
   bid prep from blueprints or shop-floor part identification are good examples of narrow, concrete problems.
2. **Move past chat.** If the owner has only used Claude chat, set the workflow up in Claude Cowork. Suggest
   installing the Claude for Small Business plugin (built with QuickBooks, PayPal, HubSpot, Canva, DocuSign,
   and others) and the connectors the task needs. Getting the first workflow to run is what makes agents feel
   approachable, so keep the first build small and do it together, step by step.
3. **Treat Claude like a new employee.** Check its work before relying on it. Ask Claude to show its reasoning
   for numbers and conclusions. Use [references/review-checklist.md](references/review-checklist.md).
4. **Keep a human in the loop** for review and for anything that is sent outside the business.
5. **Handle data deliberately.** Decide what customer or employee data the workflow touches, redact PII where
   it is not needed, and point the owner to Anthropic's privacy and trust resources. Team and Enterprise plans
   don't train on data by default.
6. **Register the workflow.** Record it in [templates/workflow-registry.md](templates/workflow-registry.md):
   purpose, data used, reviewer, and whether PII is redacted.
7. **Share with peers.** Encourage the owner to write up the use case for local peers (a chamber of commerce,
   a peer group). Attendees valued a shared repository of peer use cases more than any product feature.

## Examples

**Weekly report**
> A logistics owner wants a weekly operations report. Claude builds it in Cowork from connected data, shows
> how each total was calculated, and the owner checks two figures against the source before sharing it with
> the team. The workflow is logged in the registry with the owner as reviewer.

**Bid prep**
> A construction owner uploads blueprints and asks for a bid-prep draft. Claude lists quantities and
> assumptions with its reasoning; the owner corrects one assumption and keeps final pricing and sending.

**Data worry**
> An owner hesitates because of customer data. Claude proposes redacting names and contact details from the
> inputs, keeping a person on every outgoing message, and recording both rules in the registry.

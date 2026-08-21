**English** · [한국어](./agency-rollout.ko.md) · [Español](./agency-rollout.es.md) · [日本語](./agency-rollout.ja.md)

# Deploying agentic coding tools inside a government agency

Claude Code and Claude Cowork are now available in public beta through Claude for Government
Desktop, delivered through a FedRAMP High authorized environment. This guide walks through
what that means in practice for the people who have to authorize, fund, administer, and
distribute it.

## The two facts that reshape the plan

Most of the planning follows from two properties of the offering, and both tend to be missed
on a first read.

**Conversation history is stored locally on the agency-managed device.** Inference runs
inside the FedRAMP High authorized environment, but the transcript sits on the laptop. That
moves the endpoint into scope. In a system security plan this is agency-held data governed by
agency endpoint policy — disk encryption, backup handling, retention, device loss and wipe —
not something to be described as vendor retention. Reviewers who arrive expecting a
vendor-side retention schedule are usually satisfied faster once the scope shift is stated
plainly rather than discovered halfway through the assessment.

**Usage exports contain metering data only.** This is what allows an agency to answer an ATO
question or an inspector general request about usage without moving sensitive material out of
the boundary. It is worth surfacing early, because it removes an objection before it is
raised.

## Authorization

The offering is delivered through a FedRAMP High authorized environment, and inference runs
inside it. Three documents support the review, at two levels of availability: the FedRAMP
Secure Configuration Guide and the formal change notification are public, and the
penetration-test summary is available under NDA through Anthropic's trust center.

Build the evidence map before the assessment meeting rather than during it. Every reviewer
question should have a named artifact behind it, and every question the announcement does not
answer should be recorded as an open item rather than filled in from assumption.

One more thing belongs in the record: the offering is announced as public beta. That is a
risk-register entry, not a detail to discover during review.

## Delegated administration

The design assumption is that a department authorizes once and then delegates operation,
rather than repeating procurement and configuration for every component. Department-level
administrators allocate seats to sub-agencies, and the limits ride on identity.

SCIM group mappings set a group's rate limits, dollar caps, and allowed models. Layered
configuration sets sub-agency defaults for what Claude can connect to and which features are
available. So three sub-agencies with three different risk postures under one authorization
is a configuration exercise, not three separate agreements — provided the group structure is
right before anyone is provisioned.

Get that structure settled first, map one group per sub-agency, and test deprovisioning
explicitly. Removing a user from a group has to remove access, and that is a thing to verify
rather than assume.

## Funding

Consumption-based pricing and appropriated funds reconcile through one mechanism: usage is
purchased in fixed increments with a hard not-to-exceed cap. When finance asks what prevents
an open-ended bill, that cap is the answer.

Organizations can take standard seats or a customized tier with spend and model limits.
Administrators track usage per user and per model in the admin console, and automatic
burndown alerts warn before the balance runs low.

The alerts deserve a moment of attention during setup. A cap without alerting turns a budget
control into a service interruption, so route the alerts to someone with the authority to
replenish and agree the replenishment path before the first balance runs low rather than
after.

## Oversight

Administrative actions are recorded in a hash-chained audit log that organization
administrators can review directly in the product. On the vendor side, sensitive operations
require two-person approval — that is the answer to a reviewer asking what prevents
unilateral action by Anthropic.

Assign named reviewers and a cadence for the audit log during rollout. An audit log nobody
reads is evidence that a control exists, not evidence that it operates.

## Distribution and change

The desktop application deploys through standard agency MDM platforms, so distribution uses
machinery agencies already have. Pilot with one ring before broad release, and make sure
endpoint policy covers locally stored conversation history before that ring goes out.

Agencies receive capabilities on the same release schedule as commercial customers. This is
the headline benefit — no waiting quarters behind the commercial product — and it is also an
obligation, because change arrives on the commercial cadence and agency change management has
to absorb it. The formal change notification is the mechanism for that; route it to whoever
has to be told.

## Contracting

New customers request access at claude.com/solutions/government. Anthropic remains the
contracted billing party, and no separate cloud provider relationship is required.

## A workable sequence

1. Fix the authorization boundary and write down where processing happens and where data
   rests.
2. Collect the three documents and build the evidence map.
3. Design the group structure, then provision.
4. Choose the licensing model, set the cap, route the alerts.
5. Assign audit-log reviewers and a cadence.
6. Package for MDM, confirm endpoint policy, pilot one ring.
7. Record beta status and open questions in the risk register.

Steps 1 and 3 are the ones that are expensive to redo. The rest can be adjusted once the
first ring is live.

## Source

[Bringing Claude Code and Claude Cowork to government](https://claude.com/blog/bringing-claude-code-and-claude-cowork-to-government) — published 2026-07-07.

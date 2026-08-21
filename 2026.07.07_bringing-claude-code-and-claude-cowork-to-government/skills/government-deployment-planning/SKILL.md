---
name: government-deployment-planning
description: Plan a government or regulated-environment rollout of Claude Code and Claude Cowork through Claude for Government Desktop — authorization boundary, where data is stored and processed, SCIM-based delegated administration, spend caps, audit logging, and MDM distribution. Use when preparing an ATO package or security review, when a department needs to allocate seats and limits across sub-agencies, when finance needs consumption-based spend bounded against appropriated funds, or when answering IG and auditor questions about usage without exposing sensitive material.
---

# Planning a government deployment

Claude Code and Claude Cowork are available in public beta through Claude for Government
Desktop, delivered through a FedRAMP High authorized environment. This skill turns that
announcement into the decisions and evidence a rollout actually requires.

Two properties drive most of the planning and are easy to miss: **conversation history is
stored locally on the agency-managed device**, and **usage exports contain metering data
only**. The first moves the endpoint into scope. The second is what lets you answer an ATO or
IG question without moving sensitive material.

## Instructions

### 1. Fix the authorization boundary first

Record where processing happens and where data rests, because every later decision depends on
it.

- Inference runs inside a FedRAMP High authorized environment.
- Conversation history is retained locally, on the agency-managed device. In the system
  security plan this is agency-held data under agency endpoint policy — do not describe it as
  vendor-retained.
- Agencies receive capabilities on the same release schedule as commercial customers. Treat
  this as both a benefit and a change-management obligation.

Anything your program needs that the announcement does not state is an open question to
confirm, not a gap to fill by assumption.

### 2. Collect the evidence

Three documents exist, at two levels of availability:

| Document | How to get it |
| --- | --- |
| FedRAMP Secure Configuration Guide | Public |
| Formal change notification | Public |
| Penetration-test summary | Under NDA, through Anthropic's trust center |

Map each to the reviewer question it answers before the assessment meeting rather than
during it. Use [templates/evidence-map.md](templates/evidence-map.md).

### 3. Design delegated administration before provisioning anyone

A department-level administrator allocates seats to sub-agencies, and the limits ride on
identity rather than on per-component configuration.

- Connect the identity provider and define groups so **one group maps to one sub-agency**.
- Set per-group **rate limits, dollar caps, and allowed models** through SCIM group mappings.
- Use **layered configuration** to set sub-agency defaults for what Claude can connect to and
  which features are available.
- Test deprovisioning explicitly: removing a user from the group must remove access.

Getting the group structure right first is what lets a department authorize once and delegate
operation, instead of repeating procurement and configuration per component.

### 4. Bound the spend

Consumption-based pricing and appropriated funds reconcile through one mechanism: usage is
purchased in fixed increments with a **hard not-to-exceed cap**. Say that plainly when
finance asks what prevents an open-ended bill.

- Choose standard seats or a customized tier with spend and model limits.
- Size the purchase increment against expected usage and set the cap.
- Route **automatic burndown alerts** to someone with authority to replenish. An alert that
  reaches no one who can act is not a control.
- Verify that per-user and per-model tracking in the admin console produces what your
  financial reporting needs.

### 5. Set up oversight you will actually run

- Assign named reviewers and a cadence for the **hash-chained audit log**, reviewable
  directly in the product by organization administrators.
- Record that **sensitive operations on Anthropic's side require two-person approval** — this
  is the answer to "what prevents unilateral vendor-side action."
- Document the usage-export procedure and note that exports are metering data only.

### 6. Deploy through MDM and treat the endpoint as in scope

The desktop application deploys through standard agency MDM platforms. Because conversation
history is local, endpoint policy has to cover disk encryption, backup handling, retention,
and device loss and wipe. Pilot with one ring before broad distribution.

### 7. Contract and record maturity

New customers request access at `claude.com/solutions/government`. Anthropic remains the
contracted billing party; no separate cloud provider relationship is required. The offering
is announced as public beta — put that in the risk register rather than discovering it during
review.

Working checklist across all seven steps:
[templates/rollout-checklist.md](templates/rollout-checklist.md).
Full control surface as announced: [references/controls-inventory.md](references/controls-inventory.md).

## Examples

### A security reviewer asks where the data goes

> "If someone pastes internal code into this, where does it end up?"

Two answers, and both matter. Inference runs inside a FedRAMP High authorized environment.
The conversation history is stored locally on the agency-managed device — which means the
retention question is answered by your own endpoint policy, not by a vendor retention
schedule. Reviewers who expect a vendor-side answer to the second half are usually satisfied
faster once the scope shift is made explicit.

### Finance objects to consumption pricing

> "We can't sign something with an unbounded bill against appropriated funds."

Usage is purchased in fixed increments with a hard not-to-exceed cap, with per-user and
per-model tracking in the admin console and automatic burndown alerts before the balance runs
low. The cap is the control; the alerts are what keep the cap from becoming an outage. Name
the alert recipient in the rollout record.

### A department needs different limits per component

> "Three sub-agencies, three different risk postures, one authorization."

Map each sub-agency to an identity group, then use SCIM group mappings to set that group's
rate limits, dollar caps, and allowed models, and layered configuration to set its defaults
for connections and available features. Seats are allocated by the department-level
administrator. The department authorizes once; the components differ by configuration rather
than by separate agreements.

### An IG asks who used what

> "We need usage figures for the quarter, and we can't disclose case material."

Usage exports are metering data only, which is precisely why they can answer the question.
Pair the export with the hash-chained audit log for administrative actions. Both are
available to organization administrators without moving sensitive material out of the
boundary.

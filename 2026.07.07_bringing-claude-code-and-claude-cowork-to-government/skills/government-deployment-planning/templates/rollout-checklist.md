# Government rollout checklist

A working checklist for standing up Claude Code and Claude Cowork in an agency through
Claude for Government Desktop. Items marked **confirm** are things the announcement does not
settle and that your program has to establish with the vendor or your own authorizing
official.

---

## 1. Authorization and scope

- [ ] Confirm the FedRAMP High authorization covers the specific offering you are deploying.
- [ ] Record in the SSP that inference runs inside the FedRAMP High authorized environment.
- [ ] Record that conversation history is retained **locally on the agency-managed device**,
      and identify which endpoint policy governs it.
- [ ] Obtain the FedRAMP Secure Configuration Guide and map it to your baseline.
- [ ] **Confirm** the impact level your data actually requires and that it is within scope.
- [ ] **Confirm** handling requirements for any data category with rules beyond the
      authorization boundary.

## 2. Documentation and evidence

- [ ] FedRAMP Secure Configuration Guide obtained (public).
- [ ] Formal change notification process reviewed (public) and routed to whoever must be
      notified of vendor-side change.
- [ ] Penetration-test summary requested under NDA through Anthropic's trust center.
- [ ] Evidence map drafted for the ATO package.
- [ ] IG and audit response path agreed, using metering-only usage exports.

## 3. Identity and delegated administration

- [ ] Identity provider connected and SCIM provisioning tested.
- [ ] Group structure defined so that each sub-agency maps to a group.
- [ ] Per-group rate limits set.
- [ ] Per-group dollar caps set.
- [ ] Per-group allowed models set.
- [ ] Layered configuration defaults set for sub-agencies: what Claude can connect to, which
      features are available.
- [ ] Department-level seat allocation to sub-agencies agreed and recorded.
- [ ] Deprovisioning tested — confirm that removing a user from the group removes access.

## 4. Cost control

- [ ] Licensing model chosen: standard seats, or a customized tier with spend and model
      limits.
- [ ] Purchase increment sized against expected usage.
- [ ] Hard not-to-exceed cap set and documented for the funding authority.
- [ ] Burndown alert recipients configured — the alert only helps if it reaches someone who
      can act.
- [ ] Per-user and per-model tracking reviewed in the admin console; confirm the console
      shows what your finance reporting requires.
- [ ] Replenishment path agreed before the first balance runs low, not after.

## 5. Oversight

- [ ] Named reviewers assigned for the hash-chained audit log, with a review cadence.
- [ ] Recorded that sensitive Anthropic-side operations require two-person approval.
- [ ] Usage export procedure documented, with a note that exports are metering data only.
- [ ] Escalation path defined for anomalous usage.

## 6. Endpoint deployment

- [ ] Desktop application packaged for your MDM platform.
- [ ] Pilot ring identified and deployed.
- [ ] Endpoint policy confirmed for locally stored conversation history: disk encryption,
      backup handling, retention, device loss and wipe procedure.
- [ ] Update path validated — agencies get the same release schedule as commercial
      customers, so change lands on the commercial cadence and your change management has to
      absorb it.

## 7. Contracting

- [ ] Access requested at `claude.com/solutions/government`.
- [ ] Recorded that Anthropic is the contracted billing party and no separate cloud provider
      relationship is required.
- [ ] Beta status acknowledged in the risk register — the offering is announced as public
      beta.

## 8. Users

- [ ] Acceptable-use guidance issued, stating what may and may not be entered.
- [ ] Users told that conversation history sits on their device and is subject to agency
      endpoint policy.
- [ ] Support and escalation route published.
- [ ] Feedback path from the pilot ring into configuration changes.

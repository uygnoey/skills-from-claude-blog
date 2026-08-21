# ATO evidence map

A one-page table to drop into an authorization package or a pre-assessment briefing. Fill the
right-hand column with your own artifact references; the middle column is what the vendor
announcement provides.

| Reviewer question | Vendor-provided answer | Your artifact |
| --- | --- | --- |
| Where does inference run? | Inside a FedRAMP High authorized environment | |
| What is the authorization boundary? | Claude for Government Desktop, FedRAMP High | |
| Where is conversation history retained? | Locally, on the agency-managed device | |
| What governs that local retention? | Agency endpoint policy — not vendor retention | |
| How is the product configured securely? | FedRAMP Secure Configuration Guide (public) | |
| How is vendor-side change communicated? | Formal change notification (public) | |
| What independent testing exists? | Penetration-test summary, under NDA via trust center | |
| How are administrative actions attributable and tamper-evident? | Hash-chained audit log, reviewable in-product | |
| Who reviews that log, and how often? | Organization administrators | |
| What prevents unilateral vendor-side action? | Two-person approval on sensitive operations | |
| How is access scoped per component? | SCIM group mappings; layered configuration defaults | |
| What limits can be set per group? | Rate limits, dollar caps, allowed models | |
| What can be centrally restricted? | What Claude can connect to; which features are available | |
| How is spend bounded? | Fixed purchase increments with a hard not-to-exceed cap | |
| How is spend monitored? | Per-user and per-model tracking; automatic burndown alerts | |
| How are usage questions answered without new disclosure? | Usage exports are metering data only | |
| How is the client distributed and updated? | Standard agency MDM platforms | |
| What is the release cadence? | Same schedule as commercial customers | |
| Who is the contracted party? | Anthropic; no separate cloud provider relationship required | |
| What is the maturity of the offering? | Public beta | |

## Notes for the reviewer briefing

- The two properties that most often surprise reviewers are that **conversation history is
  local** and that **usage exports are metering data only**. Lead with both — the first moves
  scope onto the endpoint, and the second removes an objection before it is raised.
- The **same-release-schedule** commitment is a benefit and a change-management obligation at
  once. Say both parts.
- Anything not in the table above is not answered by the announcement. Mark it as an open
  question rather than filling it in from assumption.

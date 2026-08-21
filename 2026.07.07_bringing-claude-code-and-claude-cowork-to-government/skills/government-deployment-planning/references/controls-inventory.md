# Control surface announced in the post

What the government offering actually provides, grouped by the question a reviewer will ask.
Every item here comes from the source announcement; anything your program needs that is not
listed is something to confirm rather than assume.

---

## Authorization boundary

- Claude Code and Claude Cowork are available in public beta through Claude for Government
  Desktop.
- Delivery is through a **FedRAMP High authorized environment**.
- **Inference runs inside** that FedRAMP High authorized environment.
- Agencies receive capabilities on the **same release schedule as commercial customers**.

## Data location

- **Conversation history is stored locally on the agency-managed device.**
- Inference processing happens in the authorized environment.

Implication for a system security plan: the endpoint is in scope. Conversation history on a
managed laptop is agency-held data governed by agency endpoint policy, not something to be
described as vendor-retained.

## Cost control

- Standard seats, or **customized tiers with spend and model limits**.
- Usage is purchased in **fixed increments with a hard not-to-exceed cap**.
- Administrators track usage **per user and per model** in the admin console.
- **Automatic burndown alerts** warn before the balance runs low.

The not-to-exceed cap is the mechanism that makes consumption-based spend compatible with
appropriated funds. Say so explicitly when finance asks how an open-ended API bill is being
prevented.

## Delegated administration

- Department-level administrators **allocate seats to sub-agencies**.
- **SCIM group mappings** set rate limits, dollar caps, and allowed models.
- **Layered configuration** sets defaults for sub-agencies, including what Claude can connect
  to and which features are available.

This is what lets a department authorize once and delegate operation, rather than running a
separate procurement and configuration exercise per component.

## Oversight

- **Hash-chained audit log**, reviewable directly in the product by organization
  administrators.
- **Sensitive operations on Anthropic's side require two-person approval.**
- **Usage exports contain metering data only**, so agencies can answer ATO and IG requests
  without moving sensitive material.

The metering-only property of exports is worth flagging early to an IG or auditor: it means
the evidence you hand over to answer a usage question does not itself create a new disclosure
problem.

## Documentation available

| Document | Availability |
| --- | --- |
| FedRAMP Secure Configuration Guide | Public |
| Formal change notification | Public |
| Penetration-test summary | Under NDA via Anthropic's trust center |

## Deployment mechanics

- The desktop application **deploys through standard agency MDM platforms**.

## Contracting and access

- New customers request access at `claude.com/solutions/government`.
- Anthropic remains the contracted billing party; no separate cloud provider relationship is
  required.

---

## Reading this as an evidence map

For an ATO package, the items above map roughly as follows:

| Reviewer question | What answers it |
| --- | --- |
| Where is data processed? | FedRAMP High authorized environment |
| Where is conversation history retained? | Locally, on the agency-managed device |
| How is configuration hardened? | FedRAMP Secure Configuration Guide |
| How are changes communicated? | Formal change notification |
| How is administrative action attributable? | Hash-chained audit log |
| What prevents unilateral vendor-side action? | Two-person approval on sensitive operations |
| How is spend bounded? | Fixed increments with a hard not-to-exceed cap |
| How is access scoped per component? | SCIM group mappings and layered configuration |
| How are usage questions answered? | Metering-only usage exports |
| How is the client distributed? | Standard agency MDM |

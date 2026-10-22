# Channel scenarios from the announcement

## 1. Mixed personal + shared: #checkout-migration
- Channel connector: GitHub (shared).
- Priya asks Claude to check her Google Drive doc "Checkout migration, Q3" against what has shipped
  and list open items.
- Claude reads merged pull requests through the channel's GitHub connector, and reads the doc through
  Priya's personal Google Drive connector, which only she can access.
- Her plan isn't sensitive, so she uses **auto mode**; Claude screens the comparison before posting.
  For a document she would rather check first, she switches to **review mode**.

## 2. Shared connectors for unattended work: #on-call
- Channel connectors: runbook, monitoring tools, deployment history.
- Because these are shared, Claude can help with CI triage even after hours. Personal connectors
  would not work here, since they never run unattended.

## 3. Personal-only, closely supervised: RFP response
- Drafting an RFP response needs sensitive pricing data that is not provisioned to the whole channel.
- Relying only on personal connectors fits this supervised work. Everything Claude posts is visible
  to all channel members, so review before posting matters.

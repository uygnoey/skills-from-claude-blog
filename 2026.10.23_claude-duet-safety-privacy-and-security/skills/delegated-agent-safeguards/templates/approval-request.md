# Approval request (sensitive action)

Shown to the user before any sensitive action. The agent waits for an explicit answer.

```
Action:       <what will happen, e.g. "Send email" / "Pay" / "Delete">
Destination:  <recipient, site, merchant, or account>
Content:      <the full message, amount, or items affected>
Why:          <which part of your request this serves>

[Approve]  [Edit]  [Cancel]
```

Checks before showing it:
- [ ] The action is not on the off-limits list (e.g. trading securities, moving money between accounts,
      accessing someone else's account).
- [ ] The out-of-model intent check agrees the action matches the user's request.
- [ ] Outgoing content passed the sensitive-information classifier, or was rewritten.
- [ ] For payments: a one-time card scoped to this merchant and amount is used.

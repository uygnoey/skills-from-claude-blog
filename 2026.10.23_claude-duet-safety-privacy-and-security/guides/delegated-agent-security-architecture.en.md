**English** · [한국어](./delegated-agent-security-architecture.ko.md) · [Español](./delegated-agent-security-architecture.es.md) · [日本語](./delegated-agent-security-architecture.ja.md)

# Security architecture of a delegated agent (Claude Duet)

How Anthropic secured the Claude Duet research preview, an always-on agent in a cloud computer that uses
the user's connected apps (October 23, 2026).

## Three principles
1. Handle information with discretion.
2. Keep the user in control.
3. Keep credentials away from the agent.

Protections layer on the model's safety training, the safeguards in Claude Code and Claude Managed Agents,
and new controls for acting on the user's behalf.

## 1. Approval for important actions
- Sensitive actions (sending messages, paying, deleting) show the action, destination, and content and
  wait for approval.
- A separate automated intent check, extended from the Claude Code auto mode classifier, runs outside the
  model, so hidden instructions on a page cannot affect it.
- Some actions are off-limits even with approval: trading securities, moving money between accounts,
  accessing someone else's account.
- Approval frequency is being calibrated to avoid approval fatigue.
- Purchases use a one-time card (Link from Stripe) limited to one merchant and amount.

## 2. Information handled with discretion
- A separate classifier checks each outgoing message.
- Never share: sign-in credentials, full card and bank numbers, government ID numbers.
- Needs consent: other private information such as health or financial details; the user's own request
  counts as consent.
- Blocked messages can be rewritten without the sensitive content and shown for approval.

## 3. Visibility
- A task list shows what has been done and what is in progress; the user can steer mid-task.
- History and memory persist until deleted or reset; deleting the account wipes stored data.
- Disconnecting an app stops new access, but learned information stays until memory is reset.

## 4. Isolation of credentials and browser
- Passwords: typed into a form in the app, encrypted with a single-use key, entered on the site by the
  browser machine. 1Password integration is planned.
- Tokens: the agent sees placeholders; a proxy outside its machine inserts real values.
- Browser: its own cloud VM, driven by fixed commands; site code and cookies stay there, while page text
  and downloads return to the agent.
- The agent uses a distinct User-Agent and published IP addresses; some sites block it.

## 5. Testing
- Routine tasks in innocent, injected, and overreach variants.
- Red teams for leaks, unapproved actions, and malicious prompts; a whole-system threat model.
- External penetration test of the source code, with a follow-on for the cloud browser and sign-in form.
- In scope for Anthropic's public bug bounty on HackerOne.

## Still changing
Approval frequency, sign-in methods, and sensitive-information checks are evolving during the preview.
Users can report problems directly to Claude Duet.

Source: https://claude.com/resources/articles/claude-duet-safety-privacy-and-security

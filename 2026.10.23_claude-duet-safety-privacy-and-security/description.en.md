**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
Anthropic's October 23, 2026 explanation of how Claude Duet, a research-preview agent that runs
continuously in a cloud computer and uses the user's connected apps, is protected. It is organized around
three principles: handle information with discretion, keep the user in control, and keep credentials away
from the agent.

## When is it useful?
- Designing or auditing an agent that sends messages, pays, deletes, or signs in on a user's behalf.
- Building an evaluation and red-team plan that covers prompt injection and overreach.
- Explaining to stakeholders how a delegated agent keeps passwords and tokens out of the model.

## Key points
- Sensitive actions show action, destination, and content and wait for approval. An out-of-model intent
  check (extended from the Claude Code auto mode classifier) resists hidden page instructions. Some actions
  are off-limits even with approval (trading securities, moving money between accounts, accessing someone
  else's account). Purchases use a one-time card from Link (Stripe).
- A separate classifier checks outgoing messages: never share credentials, full card/bank numbers, or
  government IDs; other private data needs consent (the user's own request counts). Blocked messages can
  be rewritten for approval.
- A task list gives visibility and mid-task steering; history and memory persist until deleted or reset.
- Passwords go through an app form, encrypted with a single-use key and typed by the browser machine;
  tokens are placeholders filled in by an external proxy; the browser runs in its own VM via fixed commands.
  The agent uses a distinct User-Agent and published IPs.
- Testing: innocent / injected / overreach task variants, red teams, a whole-system threat model, an
  external penetration test, and a HackerOne bug bounty.

## Bundled resources
- Skill: `delegated-agent-safeguards` (`references/information-sharing-tiers.md`,
  `references/credential-and-browser-isolation.md`, `templates/approval-request.md`,
  `examples/evaluation-plan.md`).
- Guide: `guides/delegated-agent-security-architecture` (4 languages).

## Source
- https://claude.com/resources/articles/claude-duet-safety-privacy-and-security

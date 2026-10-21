# How Claude Duet works (reference)

Source: "Introducing Claude Duet" (2026-10-21). Built on Claude Opus 5.5.

## Availability
- Research preview, US Pro and Max subscribers, waitlist on the Claude Duet product page.
- Standalone app on iOS and Android, and on claude.ai.
- Same usage limits as the rest of Claude during the preview.

## Runtime
| Aspect | Behavior |
|---|---|
| Context | Memory, skills, and connected apps carry over from the Claude account |
| Interface | One ongoing thread; type or speak |
| Execution | Own virtual machine with its own browser; user devices can be off |
| Notifications | When a task finishes or needs review |
| Check-ins | Connected accounts checked every few hours; user picks topics and frequency |

## Approval model
| Category | Behavior |
|---|---|
| Read, draft, prepare work | On its own |
| Send a message, make a payment, sign a document, delete anything | Shows the action, waits for approval |
| Trade securities, move money between accounts (examples) | Off-limits even with approval |
| Any connected app | Can be disconnected by the user |

## Safety design
- Follows Anthropic's framework for trustworthy agents (same framework as Claude Code and Claude in
  Chrome).
- Credential handling follows the Claude Managed Agents design: Duet never directly sees passwords or
  sign-in tokens.
- Actions are checked by the auto mode classifier.
- Prompt-injection and hidden-instruction defenses come from Anthropic's browser-use research.
- Red-teamed internally, penetration-tested by an external firm, covered by a public bug bounty.
- A dedicated classifier plus a safety system prompt guard against sensitive-information leaks:
  strictest-tier requests (credit card numbers, government ID) are rejected; health and personal
  finance information is shared only on explicit user instruction.

## Connectors and purchases
- 6,000+ connectors and plugins from the Claude Marketplace. Named examples: Gmail, Slack,
  QuickBooks, Stripe, Gusto, LinkedIn, Docusign, HubSpot, Canva, Shopify.
- A richer Shopify storefront editor is coming soon.
- Purchases through Link (Stripe's digital wallet) with a virtual card, or checkout with Shop Pay.
- Signing in with 1Password saved logins is coming soon.

## Known limitations (preview)
- May misread a thread or misjudge urgency.
- Personal errands (e.g. booking tickets) are weaker than work tasks.
- Cannot yet show its browser to the user.
- Lives in its own app, separate from the main Claude app.
- Background checks and larger tasks (financial models, decks) count toward usage limits and need
  more model turns.

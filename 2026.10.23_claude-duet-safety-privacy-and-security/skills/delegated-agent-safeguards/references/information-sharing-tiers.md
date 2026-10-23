# Information-sharing tiers for outgoing messages

A separate safety classifier checks each outgoing message. The Claude Duet post defines these tiers:

| Tier | Examples from the post | Rule |
|---|---|---|
| Never share | Sign-in credentials, full card and bank numbers, government ID numbers | Always blocked |
| Needs consent | Other private information, such as health or financial details | Shared only with consent; the user's own request counts as consent |
| Everything else | - | Normal handling |

## When a message is blocked
1. Rewrite it without the sensitive content.
2. Show the rewritten version to the user.
3. Send only after the user approves.

The post notes that sensitive-information checks are still changing during the research preview.

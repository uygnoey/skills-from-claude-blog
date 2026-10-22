**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
Claude Tag (beta), which adds Claude to a Slack channel, can now use a member's personal connectors
for that member's requests. Previously only admin-attached channel connectors were available, so
access followed the channel rather than the person.

## When is it useful?
- When a channel member needs data behind their own login (calendar, private docs, assigned CRM
  accounts, staging deploys).
- When an admin is choosing how to govern connector access in Claude Tag channels.
- When deciding what can run unattended versus what needs a person present.

## Key points
- Connect tools at claude.ai/customize; Claude asks permission the first time a request needs one.
  Nobody else in the channel can use your connectors.
- One request can mix your connectors with the channel's shared connectors.
- Review mode shows each response before it posts; auto mode posts unless sensitive content is detected.
- Personal-connector actions are audited under your account in that tool's log; channel work stays
  under the channel's service account. Disconnect any time.
- Personal connectors never run unattended: scheduled routines and self-initiated actions use shared
  connectors.
- Admin options: shared tools under an agent identity, personal-only channels using existing
  role-based access, or tool-by-tool decisions. Enterprise admins can require review for everyone.
- Rolling out on Team plans; Enterprise to follow.

## Bundled resources
- Skill: `slack-personal-connectors` — personal vs. shared connectors, posting modes, governance
  (`examples/channel-scenarios.md`).

## Source
- https://claude.com/resources/articles/claude-tag-now-supports-personal-connectors-in-channels

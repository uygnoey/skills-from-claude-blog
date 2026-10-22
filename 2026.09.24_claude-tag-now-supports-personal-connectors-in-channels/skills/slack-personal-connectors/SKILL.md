---
name: slack-personal-connectors
description: Decide when Claude Tag (beta, Claude in a Slack channel) should use a member's personal connectors versus the channel's admin-attached shared connectors, and configure review or auto posting. Covers how personal connectors work (connected at claude.ai/customize, used only for that person's requests, permission asked on first use, audited under the person's own account, disconnectable any time), mixing personal and shared connectors in one request, review mode versus auto mode, the limit that personal connectors never run unattended (scheduled routines and self-initiated actions use shared connectors), and admin governance options (shared tools under an agent identity, personal-only channels relying on existing role-based access, or tool-by-tool decisions; Enterprise admins can require review for everyone). Rolling out on Team plans, Enterprise to follow. Use when setting up a Slack channel with Claude Tag, choosing a connector strategy, or explaining who can see what.
---

## Purpose
Before this change, Claude Tag could only use connectors an admin attached to the channel, so access
followed the channel. Now each member's own connectors (calendar, Google Drive, assigned CRM
accounts, staging deploys, and so on) can serve that member's requests, while nobody else in the
channel can use them. This skill helps choose between personal and shared connectors and set safe
posting defaults, based only on the announcement.

## When to use
- A member needs data behind their own login (personal calendar, private docs, assigned accounts).
- An admin is designing connector governance for Claude Tag channels.
- Someone wants Claude to do unattended or after-hours channel work.
- A user asks who will see results drawn from their private data.

## Instructions

1. **Check availability.** Rolling out on Team plans now; Enterprise follows. Claude Tag itself is
   in beta. Nothing needs installing.

2. **Connect personally.** The member connects a tool to their Claude account at
   claude.ai/customize. The first time a channel request needs it, Claude asks for permission, then
   uses it in that thread.

3. **Expect mixed requests.** When a request needs a personal connector, Claude uses it for that part
   and uses the channel's shared connectors for the rest.

4. **Pick a posting mode.** Remember that anything Claude posts is visible to every channel member.
   - **Review mode** — the member sees each response before it posts. Use for sensitive sources.
   - **Auto mode** — Claude posts automatically unless it detects sensitive content that needs the
     member's review. Use for non-sensitive sources.
   On Enterprise, admins can require review of personal-connector output for everyone.

5. **Know the audit trail.** Actions through a personal connector are logged in that tool's own
   audit log under the member's account. Channel work stays under the channel's service account.
   Members can disconnect any connector at any time.

6. **Use shared connectors for unattended work.** Personal connectors do not run unattended:
   scheduled routines and actions Claude starts on its own use the channel's admin-attached
   connectors. Attach shared connectors for channel-wide or after-hours work.

7. **Choose an admin governance option.**
   - Provide a shared set of tools under an agent identity.
   - Let members use only personal connectors, relying on existing role-based access.
   - Decide access tool by tool.
   Personal-only channels suit closely supervised work.

8. **Map the scenario.** Compare with the patterns in
   [examples/channel-scenarios.md](examples/channel-scenarios.md).

## Examples
- User: "Can Claude in #sales read my assigned Salesforce accounts without giving the whole channel
  access?" → Yes: connect Salesforce personally; it serves only your requests. Use review mode if the
  answer may expose sensitive account data, since posts are visible to everyone.
- User: "I want Claude to triage CI failures overnight in #on-call."
  → Personal connectors don't run unattended; attach the runbook, monitoring, and deployment-history
  tools as shared channel connectors.
- User: "We're drafting an RFP that needs pricing data the channel shouldn't have."
  → A personal-connector-only channel under close supervision fits; keep review mode on.

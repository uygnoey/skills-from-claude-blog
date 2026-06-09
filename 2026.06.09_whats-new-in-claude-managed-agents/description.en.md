**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# New in Claude Managed Agents: scheduled deployments and vault environment variables

## What is this post?
This post announces two new capabilities in Claude Managed Agents (public beta): scheduled deployments (cron-like runs) and storing environment variables in vaults for secure CLI authentication.

## When is it useful?
Use it when you want an agent to run routine work on a schedule without building your own scheduler, and when you need to securely provide secrets to CLI tools (API keys) without exposing them to the model.

## Key points
- Scheduled deployments start a new agent session on a cron schedule; you can pause/resume/archive and also trigger runs on demand.
- Vaults now support environment variables so CLIs can make authenticated requests; the agent never sees the secret, and domains are allow-listed.

## Bundled resources
- Skill: managed-agents-scheduled-deployments (conceptual operational checklist and use-case patterns)

## Source
- https://claude.com/blog/whats-new-in-claude-managed-agents

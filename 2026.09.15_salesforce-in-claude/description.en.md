**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
An announcement (September 15, 2026) of Salesforce in Claude, a beta plugin built with Salesforce that
brings a seller's accounts, opportunities, and pipeline into Claude under their existing Salesforce
permissions. It includes 37 skills for daily account executive work.

## When is it useful?
- When sellers spend time assembling context from Salesforce, email, call recordings, and Slack.
- When CRM updates lag behind meetings.
- When admins plan how to roll the plugin out to sales teams.

## Key points
- Salesforce connector reads and acts on CRM data; Slack connector reads/writes deal-channel summaries
  and account-team threads. A setup skill creates a role-tailored Claude Artifact on first use.
- Workflows: scheduled morning brief (with a Friday week summary and manager update), call prep, deal
  review with a dated mutual close plan, post-meeting follow-ups and opportunity updates, and shareable
  pipeline/forecast dashboards.
- Salesforce stays the system of record; Claude sees only what the seller's permissions allow and asks
  for approval before any write by default. No training on Team/Enterprise customer data by default.
- Beta on all paid plans. Salesforce MCP installs from the marketplace; admins request access via
  AgentExchange, connect Salesforce once for the org, and choose which groups get the plugin.
- Used by GitLab, Siemens, Legora, and 7,000 Salesforce sellers.

## Bundled resources
- Skill: `crm-seller-workflows` (`references/workflows.md`, `references/setup-and-permissions.md`,
  `templates/close-plan.md`, `templates/post-meeting-update.md`).

## Source
- https://claude.com/resources/articles/salesforce-in-claude

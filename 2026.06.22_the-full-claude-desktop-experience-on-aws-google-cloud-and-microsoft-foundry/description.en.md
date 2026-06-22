**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
This post announces that organizations using Claude Desktop via AWS, Google Cloud, or Microsoft Foundry now get the full Desktop experience in one app: Chat, Claude Cowork, and Claude Code.

## When is it useful?
Use this when you are an admin or IT/security owner who wants to roll out Claude Desktop organization-wide while keeping inference inside your chosen cloud environment and managing access with enterprise identity and device management.

## Key points
- One deployment now covers Chat, Claude Cowork, and Claude Code, with a separate policy key per surface so you can control who gets what.
- Employees sign in with existing enterprise identity providers (e.g., IAM Identity Center, Microsoft Entra ID, or other OIDC providers) rather than shared keys.
- Admins can export policy templates from the setup UI and deploy them via common MDM / endpoint-management tools (e.g., Intune, GPO, Jamf), including an offline installer option for air-gapped environments.
- Pre-rollout validation includes testing connectors, confirming available Claude models, and verifying connectivity; a “model guard” is described as keeping routing on Claude even if misconfigured.
- Microsoft 365 access can be provided via a connector using your own Entra app with tenant allowlisting; a local connector option is described for strict residency requirements.

## Bundled resources
- The post references policy templates (exported from the setup UI) and an admin deployment guide (SSO, policy templates, pre-rollout validation).

## Source
- https://claude.com/blog/the-full-claude-desktop-experience-on-aws-google-cloud-and-microsoft-foundry

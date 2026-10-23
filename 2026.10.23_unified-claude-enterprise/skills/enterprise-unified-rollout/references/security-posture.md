# Security posture of the unified experience (Enterprise)

As stated in the October 23, 2026 announcement.

| Area | What the post says |
|---|---|
| Identity and compliance | Builds on existing enterprise controls, including SSO and the Compliance API |
| Data protection | Encrypted in transit and at rest |
| Training | Data is not used for model training by default |
| Cloud sessions | Each cloud session runs in its own isolated virtual machine |
| Network | Network egress is off by default for Claude Enterprise |
| Connectors | Connector credentials are kept outside the sandbox |
| Oversight | Security teams get central visibility and controls |
| Further reading | Security best practices guide on the Anthropic Trust Center |

## Configurations that stay as they are
Organizations using any of the following keep their current configuration:
- Zero data retention for Claude Code
- A HIPAA-ready configuration
- Customer-managed encryption keys

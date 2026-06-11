---
name: microsoft-365-enterprise-search
description: Use Claude with Microsoft 365 context (SharePoint/OneDrive, Outlook, Teams) by framing questions for cross-tool enterprise search and producing source-backed reports.
---

## Instructions

### What this skill does
Use this skill when you need Claude to answer questions using context that lives across Microsoft 365, without manually uploading files.

This skill provides:
- A consistent way to phrase enterprise-search requests.
- A report structure that expects citations to where information came from (file name, location, thread, meeting, etc.).
- Templates you can reuse for admin setup notes and end-user requests.

### Recommended workflow
1. **State the question and desired output** (decision memo, policy summary, onboarding brief, etc.).
2. **Name the Microsoft 365 sources to consult** (SharePoint/OneDrive docs, Outlook threads, Teams channels/meetings).
3. **Ask for a synthesized report** that distinguishes facts vs. recommendations.
4. **Request provenance** for each claim (which doc/email/thread it came from).

### Admin-led setup assumptions
This post describes an admin-first approach where an administrator enables the connector and curates sources, then users authenticate and benefit from shared access.

If your environment differs, adapt accordingly.

## Bundled resources
- Prompt templates: [templates](./templates/)
- Example requests: [examples](./examples/)

## Examples

### Example: cross-source policy question
Use: [examples/remote-work-policy.md](./examples/remote-work-policy.md)

### Example: onboarding brief
Use: [examples/onboarding-brief.md](./examples/onboarding-brief.md)

# Example workflows (from the post)

Concrete workflow patterns highlighted in [Claude can now connect to your world](https://claude.com/blog/integrations) (2025-05-01, updated 2025-06-03). Reproduced from the post's body — do not invent additional capabilities.

## Zapier — gateway to thousands of apps

> Zapier, for example, connects thousands of apps through pre-built workflows, automating processes across your software stack. With the Zapier Integration, Claude can access these apps and your custom workflows through conversation — even automatically pulling sales data from HubSpot and preparing meeting briefs based on your calendar.

Use this when no first-party Claude Integration exists for the target app but a Zapier workflow does.

## Atlassian — product planning and bulk updates

> With access to Atlassian's Jira and Confluence, Claude can collaborate with you on building new products, managing tasks more effectively, and scaling your work by summarizing and creating multiple Confluence pages and Jira work items at once.

Use this for product specs, requirement consolidation, and batch document creation/summarization across spaces.

## Intercom + Linear — feedback to bug, in one conversation

> Connect Intercom to respond faster to user feedback. Intercom's AI agent Fin, now an MCP client, can take actions like filing bugs in Linear when users report issues. Chat with Claude to identify patterns and debug using Intercom's conversation history and user attributes — managing the entire workflow from user feedback to bug resolution in one conversation.

Use this when user reports need pattern analysis (across Intercom history and user attributes) and the result must drop a Linear ticket without leaving the chat.

## Advanced Research — multi-source cited report

> Claude breaks down your request into smaller parts, investigating each deeply before compiling a comprehensive report. While most reports complete in five to 15 minutes, Claude may take up to 45 minutes for more complex investigations — work that would typically take hours of manual research.

> When Claude incorporates information from sources, it provides clear citations that link directly to the original material.

Plan the request like a brief: state the question, scope, and which apps Claude should search (web, Google Workspace, connected Integrations). Verify each citation before acting on a finding.

## Source

All quoted material above is from [Claude can now connect to your world](https://claude.com/blog/integrations) (2025-05-01, updated 2025-06-03).

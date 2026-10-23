# Setup, rollout, and permissions

## Availability (as of the announcement)
- Beta, on all paid Claude plans.
- 37 skills for daily account executive work.
- Deployed at GitLab, Siemens, and Legora; used by 7,000 Salesforce sellers.

## Admin rollout
1. Install the Salesforce MCP from the marketplace.
2. Request plugin access through AgentExchange.
3. Connect Salesforce once for the whole organization.
4. Choose which groups receive the plugin.
5. Follow the admin setup guide: https://support.claude.com/en/articles/16952184

## Seller first run
- Sign in with Salesforce credentials.
- Run the setup skill: it identifies the seller's tools and connectors and creates a Claude Artifact
  tailored to their role and book of business.

## Permission model
- Salesforce remains the system of record.
- Claude sees only what the seller's Salesforce permissions allow.
- By default, Claude asks for approval before writing any proposed change.
- On Team and Enterprise plans, Anthropic does not train models on customer data by default.

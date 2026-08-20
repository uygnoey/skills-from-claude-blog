# Permissioning the analytics service account

The framing from the source: treat the agent's channel access as **a shared read replica of your governed warehouse**. Whoever is in a channel with the agent can reach, through it, whatever the service account can reach. Permission it accordingly.

## The five protections

### 1. Scope the account to governed data only
The service account should see governed, documented data — not the whole warehouse. Ungoverned staging tables, personal scratch schemas, and raw landing zones are exactly the surfaces where an agent will produce a plausible answer from a table nobody trusts.

### 2. Classify PII at the column level and deny clearance
Column-level classification, not table-level. Denying the agent clearance to PII columns lets a table stay available for the aggregate questions people actually ask while the identifying columns stay out of reach.

### 3. Document the connection paths in skill files
Write down which connections the agent has and what each one reaches. This does two things: it makes the agent's actual reach reviewable by someone who is not on the data team, and it gives the agent itself a correct picture of what it can and cannot answer from.

### 4. Treat channel membership as an access grant
Adding the agent to a channel grants everyone in that channel indirect read access. Review channel membership on the same cadence and with the same seriousness as any other data access grant. A wide-open company channel is a different decision from a data-team channel.

### 5. Label every query for audit and cost attribution
Every query the agent issues should carry a label. That gives you an audit trail — who asked, what ran, against what — and cost attribution, so the spend from self-service analytics is visible rather than absorbed into a general warehouse bill.

## Review questions before opening a new channel
- Is everything the service account can read appropriate for every member of this channel?
- Are the PII column denials in place and tested, not just configured?
- Is the query labeling actually landing in the audit destination?
- Are the connection paths for this deployment documented in the skill files?

## Source
- https://claude.com/blog/self-service-data-analytics-in-slack-how-anthropic-deploys-claude-tag-for-ad-hoc-questions

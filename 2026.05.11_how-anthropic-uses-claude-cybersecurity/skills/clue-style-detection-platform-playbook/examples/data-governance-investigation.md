# Worked example — contractor data-governance investigation

This example follows the data-governance scenario the source post uses to demonstrate CLUE Investigate. It only composes the components and tool surfaces named in the post; it does not invent Anthropic-internal infrastructure details.

## Scenario

Security operations receives a request: "Check whether three named contractors accessed documents they shouldn't have over the past two months."

Manual baseline given in the post: at least half a day of work — pulling access logs, cross-referencing permissions, and reviewing document classifications.

## What the analyst does

The analyst types the request into the CLUE Investigate natural-language surface, naming the three contractors and the two-month window. They do **not** specify which queries to run, which log store to hit, or which permission system to cross-reference.

## What Claude does inside the agentic loop

The post says Claude "reads the request, formulates a plan, and generates verbose queries that abstract the technical complexity." A faithful sketch of that loop:

1. **Plan.** Identify the data needed: identity records for the three contractors, document-access events, document classifications, permission grants, and any prior approvals.
2. **Delegate.** Orchestrator dispatches sub-agents in parallel:
   - One agent queries the access-log store for events tied to those three identities in the window.
   - One agent queries the permissions system for what those identities should have been able to read.
   - One agent queries the document classification store for the sensitivity of each accessed document.
   - One agent reads internal docs / Slack to see whether any planned-access exceptions were recorded for these contractors.
3. **Synthesize.** Orchestrator reads the sub-agents' outputs, joins access events against allowed permissions, and flags every event that does not have an explicit permission or recorded exception.
4. **Write up.** The summary lists each flagged access with the underlying query, the relevant log line, and the document's classification. A short recommendation block follows.

## What the analyst gets

- A written summary with the flagged events and clear recommendations.
- Full transparency: every query Claude ran is auditable in the investigation transcript.
- An investigation that wraps up in minutes rather than half a day.

## What this example does not invent

- Concrete table names, schemas, or column shapes in Anthropic's data warehouse.
- Specific Slack channel names or internal document identifiers.
- The exact mapping between sub-agents and underlying tools — the source post describes the orchestrator/sub-agent pattern but does not enumerate the tool surface.

## Source

- [How Anthropic's cybersecurity team built a threat detection platform with Claude Code](https://claude.com/blog/how-anthropic-uses-claude-cybersecurity)

# Scan and triage workflows

These workflows show how to use the scoping, scheduling, and routing levers the April 30, 2026 launch post calls out. They are illustrative starters, not API code samples — Claude Security in public beta is driven from the Claude.ai sidebar or `claude.ai/security`, not via custom integration.

## Workflow 1 — First scan on a high-risk repo

1. From the Claude.ai sidebar (or `claude.ai/security`), select the repository.
2. Optional but recommended: scope to a specific directory or branch instead of running against the whole repo.
3. Start the scan manually — do not schedule yet.
4. Triage the findings end-to-end:
   - Sort by confidence and severity.
   - Open the targeted patch in Claude Code on the Web for fixes you intend to apply.
   - Use dismiss-with-documented-reason for known-acceptable findings, so the rationale survives across reviewers.
5. Configure a webhook to Slack so the team sees future scan results in their existing channel.

This matches the post's "from scan to applied patch in a single sitting" pattern.

## Workflow 2 — Recurring coverage on a multi-team monorepo

1. For each owning team, scope a separate scan to that team's directory in the monorepo.
2. Schedule each scan at a cadence the team can actually triage (e.g., weekly).
3. Configure CSV (or Markdown) export so each team's findings flow into their existing tracking or audit system.
4. Standardize a small set of dismiss reasons across the org so triage decisions stay legible cross-team.
5. Pipe high-severity, high-confidence findings to a Jira webhook for ticket creation; leave lower-severity findings to the per-team review cadence.

This matches the post's "ongoing coverage, not one-off audits" lesson plus the "directory within a repository" capability added in this release.

## Workflow 3 — Pre-merge validation on a long-lived branch

1. Scope the scan to the long-lived branch (e.g., a release-candidate branch).
2. Run the scan on a cadence aligned with the merge train rather than the calendar.
3. For each finding, open the targeted patch in Claude Code on the Web and decide whether to land the fix on the branch.
4. Use dismiss-with-reason for findings that belong elsewhere (e.g., in a different branch or repo).

This uses the branch-scoping capability the post calls out among its scan-scoping levers.

## Workflow 4 — Adoption via a partner platform

1. Confirm whether the security team already operates inside CrowdStrike, Microsoft Security, Palo Alto Networks, SentinelOne, Trend.ai, or Wiz.
2. Coordinate with the partner to enable Opus 4.7 capabilities inside that platform's existing console.
3. Run a small parallel pilot in `claude.ai/security` against the same repo to calibrate confidence ratings between the partner platform and the direct experience.
4. Standardize on the path that fits the team's daily workflow.

This matches the post's framing that organizations should adopt through "whichever path fits how they already operate."

## Workflow 5 — Services-partner-led deployment

1. Engage one of the named services partners — Accenture, BCG, Deloitte, Infosys, or PwC.
2. Define which of the post's three scopes is in play: vulnerability management, secure code review, or incident response.
3. Use the engagement to standardize triage workflows, dismiss reasons, and webhook routing across teams.
4. After handoff, keep the same cadence and routing the services partner set up so behaviors do not drift.

## Source

Claude Security is now in public beta — Anthropic, April 30, 2026: <https://claude.com/blog/claude-security-public-beta>

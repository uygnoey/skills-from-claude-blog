---
name: security-public-beta-rollout-guide
description: Plan and run a Claude Security public-beta rollout for a Claude Enterprise organization — choose the access path (direct, partner platform, or services partner), scope scans by repository / directory / branch, schedule recurring runs, route findings into Slack/Jira/audit systems, and use the dismiss-with-reason and confidence-rating workflow to triage results, all anchored in the April 30, 2026 launch post.
---

# Security public beta rollout guide

The April 30, 2026 launch opens Claude Security in public beta to Claude Enterprise customers. This skill turns the post's product description into a rollout playbook.

## Instructions

### 1. Confirm eligibility and entry point

Per the post:

- Public beta is available to **Claude Enterprise customers** today.
- Access for **Claude Team and Max customers is coming soon** — do not assume those tiers are eligible yet.
- The product is reached from the Claude.ai sidebar or at `claude.ai/security`.
- **No API integration or custom agent build is required** — if your organization uses Claude, you can start scanning today.
- Admins enable Claude Security in the admin console (the post directs admins to a Getting Started Guide).

### 2. Choose your adoption path

The post explicitly offers three paths. Pick the one that matches how your security team already operates rather than mixing them upfront.

- **Direct in Claude Security** — fastest start, no partner dependencies. Best when the team wants to drive scans themselves from `claude.ai/security`.
- **Embedded in a partner platform** — Opus 4.7 is being integrated into CrowdStrike, Microsoft Security, Palo Alto Networks, SentinelOne, Trend.ai, and Wiz. Best when the team already lives in one of these consoles.
- **With a services partner** — Accenture, BCG, Deloitte, Infosys, and PwC are deploying Claude-integrated security solutions for vulnerability management, secure code review, and incident response. Best when you want a guided rollout.

The full named-partner list and the post's framing of "whichever path fits how they already operate" is in [references/features-and-partners-from-post.md](./references/features-and-partners-from-post.md).

### 3. Scope the scan deliberately

The post highlights three scoping levers:

- **Repository** — pick which repos to bring under coverage first.
- **Directory** — added since the limited preview; useful when repos are large or multi-team.
- **Branch** — useful for pre-merge validation on long-lived branches.

Decide scope before scheduling. Concrete starter patterns are in [examples/scan-and-triage-workflows.md](./examples/scan-and-triage-workflows.md).

### 4. Schedule, do not run one-off audits

The post explicitly captures this lesson from the limited preview:

> "Teams want ongoing coverage, not one-off audits. We've added the option to schedule scans, so teams can set a regular cadence around reviewing and acting on findings."

Pick a cadence that matches the team's review capacity (weekly vs daily) and the repo's change rate. Avoid scheduling more scans than the team can act on — the post pairs scheduling with "reviewing and acting on findings."

### 5. Pipe findings into the tools the team already uses

Since the limited preview, Claude Security has added:

- **CSV / Markdown export** — for tracking and audit systems.
- **Webhooks to Slack, Jira, or other tools** — for inline notifications and ticket creation.
- **Dismiss with documented reason** — so future reviewers can trust prior triage decisions.

Wire these up before the first major scan. Findings sitting in a UI no one watches is the failure mode this checklist exists to prevent.

### 6. Read findings the way the post describes them

Each Claude Security finding includes:

- A **confidence rating** that the vulnerability is real.
- A **severity** assessment.
- The **likely impact**.
- **Reproduction steps**.
- **Targeted patch instructions**, openable in **Claude Code on the Web** to work through the fix in context.

When triaging:

- Sort by confidence × severity. The post stresses that "high-confidence findings are what really accelerate security work."
- Use Claude Code on the Web for the patch flow — the post positions this as the bridge from finding to applied fix.
- Track "time from scan to fix" as your headline metric. The post calls it out by name: "Time from scan to fix is the metric that matters."

### 7. Plan around Opus 4.7 cyber safeguards

The post's footnote states that Claude Opus 4.7 ships with new cyber safeguards that automatically detect and block requests suggestive of prohibited or high-risk cybersecurity uses. If your team's legitimate work might trigger these safeguards, the post points to the **Cyber Verification Program** as the path to keep frontier capabilities accessible while keeping them out of the wrong hands.

## Examples

### Example A: First scan on a single high-risk repository

1. Enable Claude Security from the admin console.
2. Open the Claude.ai sidebar (or `claude.ai/security`) and select the repository.
3. Scope to the most security-sensitive directory or branch.
4. Run the scan once manually and triage findings end-to-end before scheduling a cadence.
5. Wire the webhook to Slack so security reviewers see new findings in their existing channel.

### Example B: Rolling out across a multi-team monorepo

1. Use the directory-scoped scans the post describes to give each team its own cadence.
2. Schedule weekly scans per directory.
3. Configure CSV export into the team's audit system.
4. Use dismiss-with-documented-reason from the start so a shared triage history exists across teams.
5. Use Claude Code on the Web to take findings directly into PRs.

### Example C: Adoption through a partner platform

1. Confirm whether your security team already lives inside CrowdStrike, Microsoft Security, Palo Alto Networks, SentinelOne, Trend.ai, or Wiz.
2. Coordinate with the partner to enable Opus 4.7 capabilities in that platform.
3. Use the partner platform's existing routing into vulnerability management.
4. Compare results against a small direct-Claude-Security pilot to calibrate confidence ratings.

### Example D: Services-partner-led deployment

1. Engage one of the named services partners — Accenture, BCG, Deloitte, Infosys, or PwC.
2. Define which programs are in scope: vulnerability management, secure code review, or incident response (the three areas the post calls out).
3. Use the rollout to standardize triage workflows, dismiss reasons, and webhook routing across teams that previously each had their own setup.

## Source

Claude Security is now in public beta — Anthropic, April 30, 2026: <https://claude.com/blog/claude-security-public-beta>

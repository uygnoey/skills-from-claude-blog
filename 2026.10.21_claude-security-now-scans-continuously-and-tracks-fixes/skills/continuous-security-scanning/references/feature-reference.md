# Claude Security — feature reference (Oct 21, 2026 release)

Summarized from the announcement. Check the Help Center and the Getting Started Guide for current
details.

## Context
- Public beta since April 2026; thousands of organizations have used it to find over a million
  vulnerabilities (per the post).
- Powered by the full model family, including Claude Mythos; no Cyber Verification Program access
  required.

## Features in this release

| Feature | What it does |
|---|---|
| Continuous monitoring | Deep baseline scan, then regular scans of changes based on risk and complexity. |
| Repository connection | Claude GitHub app (incl. GitHub Enterprise Server) or access token for GitLab / other Git providers; branch and scope per repo. |
| Multi-repo projects | One project can hold several repositories to catch cross-service issues. |
| Fix tracking | Open findings are checked against changed code and marked fixed when the fix lands (in Claude Code or elsewhere); reopen automatically if found again. |
| Knowledge base | Per-project notes: deployment, applicable security policies, what a new security engineer should know. |
| Threat model | Generated from code; reviewable and editable; used by later scans to decide what to flag. |
| Severity + exploit path | Severity judged against the project's threat model; explanation of how an attacker reaches the code; optional attack-path diagram. |
| API | List/read projects and findings; resolve/reopen findings; create and manage projects and repositories. |
| Personal access tokens | Created in Claude Security settings; scoped to the user's own permissions. |
| Webhooks | Notify your systems when a new finding lands. |
| MCP connector | Available in Claude.ai and Claude Code. |
| Role-based access control | Admins control who can view projects, triage findings, and create projects. |

## Availability and offer
- Public beta for Claude Enterprise customers; admins enable it in the admin console.
- $25,000 in free usage credits each month, for two months; applies to usage through
  December 31, 2026. Full terms in the Help Center.

## Customer quotes (paraphrased)
- IonQ: found material issues a concurrent traditional pen test missed; API and MCP additions are
  the path to further operationalizing it.
- Gusto: baseline once, then it keeps up as code changes; fixes happen in Claude.
- Vanta: found logic flaws other tools missed; writing their risk policy into the threat model made
  findings match how they prioritize.

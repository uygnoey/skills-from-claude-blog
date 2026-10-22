---
name: continuous-security-scanning
description: Set up and operate continuous vulnerability scanning with Claude Security (public beta for Claude Enterprise). Covers enabling it in the admin console and assigning role-based access, creating a project that spans one or more repositories (Claude GitHub app incl. GitHub Enterprise Server, or an access token for GitLab and other Git providers) with a branch and scope per repo, the baseline scan followed by risk-based rescans of changes, writing the project knowledge base and reviewing the generated threat model so scans flag what matters and skip what the environment already handles, triaging findings by severity and attack path, automatic fixed/reopened tracking, and wiring findings into team workflows through the API, personal access tokens, webhooks, and the MCP connector in Claude.ai and Claude Code. Use when a security or platform team wants scanning that keeps up with code changes instead of one-off scans.
---

## Purpose
A scan captures one moment, while code changes every day. The latest Claude Security release keeps
findings close to the current state of the code: it rescans changes, tracks which findings get
fixed, and uses what the team tells it about the environment to decide what matters. This skill walks
a team through setting it up and running it day to day, using only what the announcement states.

## When to use
- A Claude Enterprise org wants to turn on Claude Security or expand it to more teams.
- A team wants findings to stay current without anyone scheduling scans.
- Findings feel noisy or mis-prioritized and need team context (deployment, policies, risk policy).
- Engineers want to triage and fix findings from Claude Code, or pipe findings into existing tools.

## Instructions

1. **Confirm access and enable.** Claude Security is in public beta for Claude Enterprise customers.
   An admin enables it in the admin console and sets who can access it. It runs on the full model
   family, including Claude Mythos, with no Cyber Verification Program access required. Usage credit
   terms are in [references/feature-reference.md](references/feature-reference.md); point to the Help
   Center for full terms rather than restating them as guarantees.

2. **Plan roles before rollout.** Role-based access controls separate three permissions: view
   projects, triage findings, create projects. Open viewing and triage to the teams that own the code;
   keep project creation with a smaller group.

3. **Create a project and connect repositories.**
   - Connect through the Claude GitHub app (GitHub Enterprise Server included), or with an access
     token from GitLab or another Git provider.
   - Choose the branch and scope for each repository.
   - Group services that depend on each other into one project. A multi-repository project lets
     Claude catch issues that live *between* services, e.g. a backend that trusts input a client was
     supposed to validate.

4. **Let the baseline run, then rely on continuous rescans.** Claude runs a deep baseline scan, then
   scans changes regularly based on their risk and complexity. No manual scheduling is needed.

5. **Write the knowledge base.** Each project has a knowledge base. Describe how the code is
   deployed, which security policies apply, and anything a new security engineer would need to know.
   Use [templates/project-knowledge-base.md](templates/project-knowledge-base.md) as a starting
   outline. Added context helps Claude skip risks the environment already handles.

6. **Review and edit the threat model.** Claude generates a threat model from the code. Review it and
   edit it — for example, write your own risk policy into it (one customer focused it on what external
   users can actually reach). Later scans use the threat model to decide what is worth flagging, and
   severity is judged against it.

7. **Triage by reachability.** Each finding has a severity rating and an explanation of how an
   attacker could reach the vulnerable code, sometimes with an attack-path diagram. Fix what is
   actually reachable first.

8. **Let fix tracking close the loop.** Claude checks open findings against changed code and marks
   them fixed when the fix lands, whether it was fixed in Claude Code or elsewhere. If the issue shows
   up again, the finding reopens automatically. Do not maintain a parallel manual status list.

9. **Integrate with existing workflows.**
   - **API**: list/read projects and findings, resolve or reopen findings, create and manage projects
     and their repositories.
   - **Personal access tokens**: created in Claude Security settings; a token can only see and change
     what its user can.
   - **Webhooks**: notify your systems when a new finding lands.
   - **MCP connector** (Claude.ai and Claude Code): pull up a finding, ask Claude about it, start the
     fix, and mark it resolved in the same session.

## Examples

**Example 1 — Two services, one project**
A team owns a mobile client repo and a backend API repo. They create one project with both repos
(each on `main`, scoped to application code), so a missing server-side check on client-validated
input can be found across the boundary.

**Example 2 — Cutting noise with context**
Findings flag an internal admin endpoint that is only reachable through the corporate network. The
team notes this deployment fact in the knowledge base and edits the threat model to prioritize what
external users can reach; subsequent scans weigh such findings accordingly.

**Example 3 — Fix in one session**
An engineer uses the Claude Security MCP connector in Claude Code: opens a high-severity finding,
asks Claude to explain the attack path, implements the fix, and marks it resolved. If the fix later
regresses, the finding reopens on its own.

More details: [references/feature-reference.md](references/feature-reference.md).

## Source
- https://claude.com/resources/articles/claude-security-now-scans-continuously-and-tracks-fixes

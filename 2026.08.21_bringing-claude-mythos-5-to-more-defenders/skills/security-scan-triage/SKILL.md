---
name: security-scan-triage
description: Run a repository security scan in Claude Security and triage the findings through to a human-approved patch. Use when deciding whether a codebase scan is the right access path to frontier defensive capability; when an enterprise admin needs to enable Claude Security and point users at a repository; when triaging scan findings that arrive with a CWE category, confidence and severity ratings, and a suggested fix; or when routing an accepted finding into interactive patching while keeping a human in the approval path. Covers the scan-to-patch workflow, what the model does and does not become accessible through, the billing and eligibility terms, and the other access paths for defenders — partner-integrated products, the Defender Advantage Fund, and the Cyber Verification Program.
---

# Security scan triage

The riskiest interaction pattern for a frontier model with cyber capability is **direct access**,
where a malicious actor can try to steer the model toward harmful uses. When users can only
receive **specific outputs** — a patch for a vulnerability, a security alert — that risk is much
lower.

Claude Security is built on that shape: it uses Claude Mythos 5 to scan code you own and returns
detailed findings, rather than raw model access. Defenders get the capability; the model does not
become accessible to those who might misuse it.

This skill covers the scan-to-patch workflow and where it sits among the other access paths.

## Instructions

### 1. Confirm eligibility and enable

- Claude Security is **in public beta for Claude Enterprise customers**.
- An **enterprise admin enables Claude Security in the admin console**. Users cannot self-enable.
- Scans with Mythos 5 are **billed as standard token usage under your existing plan**, with no
  separate add-on.

If your organization is not on an Enterprise plan, or the work is not scanning code you own, use
one of the other access paths in [references/access-paths.md](references/access-paths.md) instead.

### 2. Run the scan

1. Go to `claude.ai/security`.
2. Select a repository to scan using Claude Mythos 5.
3. Claude scans the codebase for vulnerabilities.

Scan **code you own.** Claude Security is scoped to your own codebases.

### 3. Read each finding

Every finding returns with:

| Field | What it tells you |
|---|---|
| **CWE category** | the Common Weakness Enumeration class of the weakness |
| **Confidence rating** | how sure the scan is that the finding is real |
| **Severity rating** | how bad it is if real |
| **Suggested fix** | the proposed remediation, for human review |

Triage on confidence first — a low-confidence finding needs verification before it becomes work —
then rank the verified set by severity. Record the outcome per finding using
[templates/finding-triage-report.md](templates/finding-triage-report.md).

### 4. Patch, with a human in the approval path

- Open **Claude Code on the web** to implement the fix.
- **Interactive patching uses the models your organization has access to in Claude Code.** The
  Mythos scan itself does not extend Mythos access to other surfaces — do not plan a patching
  workflow that assumes Mythos is available in the editor.
- **Every patch must be reviewed and approved by a human before it can be implemented.** This is a
  hard gate, not a default you can turn off.

### 5. Know the boundary you are working inside

The design intent is that defenders access the *results* of frontier capability without a prompt
surface onto the model. When you build tooling on top of a scan, preserve that shape: consume the
findings and the suggested fixes; do not treat the scan as a way to obtain general model access.

This is the same principle behind the partner integrations — an end user of a partner product
works through a purpose-built interface that runs Mythos in the background for a defined task and
receives only the artifact the product is intended to provide. A vulnerability-remediation tool
returns suggested patches; it gives the user no way to prompt the model to develop an exploit.
Anthropic and its partners also have abuse prevention measures in place to verify the model stays
within its intended scope.

## Examples

### An enterprise team scanning its own service

> A platform team on Claude Enterprise wants a Mythos-quality pass over a payments service.

The admin enables Claude Security in the admin console. An engineer opens `claude.ai/security`,
selects the repository, and runs the scan. Findings come back tagged with CWE categories and
confidence and severity ratings. The team verifies the high-confidence, high-severity findings
first, opens Claude Code on the web for the accepted ones, and a human reviews and approves each
patch before it lands. Token usage bills under the existing plan.

### Triaging a low-confidence, high-severity finding

> A finding is rated high severity but low confidence.

Severity alone does not make it work. Verify the finding against the code path before spending
patch effort — the suggested fix is a proposal for human review, not a verdict. Record the
verification outcome in the triage report so the same finding is not re-litigated on the next scan.

### Choosing a different access path

> A security vendor wants Mythos-level outcomes inside its own incident response product, not a
> repo scan.

That is the partner integration path, not Claude Security. Vendors building cyber products or
services can register their interest in bringing Claude Mythos 5 to their customers. See
[references/access-paths.md](references/access-paths.md) for that path, plus the Defender Advantage
Fund for open-source security work and the Cyber Verification Program for vetted defenders who
need reduced safeguards on direct model use.

### An open-source maintainer with no Enterprise plan

> A volunteer-maintained project needs help patching vulnerabilities and has no budget.

Claude Security's public beta is Enterprise-only, so the relevant path is the Defender Advantage
Fund (0xDAF) — $35 million in credits for organizations helping open-source maintainers secure
their software, focused on patching live vulnerabilities in widely used projects, automating
scanning and patching in replicable ways, and pursuing security approaches that make projects
resistant to whole classes of attack. Details on initial recipients were to follow the
announcement; see the source post.

## Source

- [Bringing the cybersecurity capabilities of Claude Mythos 5 to more defenders](https://claude.com/blog/bringing-claude-mythos-5-to-more-defenders) — August 21, 2026.

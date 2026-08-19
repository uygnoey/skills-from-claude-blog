# FAQ for CIOs and IT leaders

These are the standing questions a research organization's IT, security, and compliance functions will ask before a science workbench is deployed. The answers below are the ones given in the source guide for Claude Science, with adjacent surfaces noted where the answer differs. Custom applications built on the API platform have additional configuration options handled with the account team.

## Deployment and data flow

**Where does it run, and where does our data go?**
It is a local application for macOS and Linux, running a daemon on the machine where it is installed — a scientist's laptop, a lab Linux box, an HPC login node, or a cloud VM in your tenancy — with its UI in the browser. Files remain on the host and are read in place; content the agent reads as part of an analysis is sent to Anthropic's API as context, subject to your plan's data-use and retention commitments. An OS-level sandbox with deny-by-default network egress controls all other traffic leaving the host. **Not currently available through Amazon Bedrock, Google Vertex AI, or Microsoft Foundry.**

**What gets installed on user endpoints?**
A signed binary running as a user-space daemon, plus a browser-based UI. No kernel-level components. On Linux it can run headless and be reached over an SSH tunnel from the scientist's laptop. **Windows is not currently supported.**

**Where are the chat and desktop surfaces hosted?**
Both are SaaS products hosted by Anthropic. Organizations that need workloads to run inside their own cloud perimeter typically build on the API platform via Amazon Bedrock, Google Vertex AI, or Microsoft Foundry. The desktop cross-app surface is a signed desktop application for macOS and Windows that reads only the local folders the user explicitly grants access to.

## Execution control

**How are code execution and file access controlled?**
A human-approval broker gates **thirteen action kinds**, including code execution, network grants, host file access, deletions, MCP tool calls, remote compute dispatch, and skill persistence. Every request surfaces as a single approval card — allow once, for this project, or always — and every decision can be reviewed or revoked from one permission screen. An OS-level sandbox with allowlist-proxy network egress, SSRF and DNS-rebind defenses, and seccomp hardening sits underneath. Plan mode is on by default: the agent drafts a step-by-step plan and waits for approval before executing.

**How does it reach our HPC cluster or GPU hosts?**
From inside a session the agent can dispatch jobs to an SSH host, a SLURM cluster (batch directives written automatically), or a serverless GPU account the user supplies. Dispatch targets are gated by the same approval broker, so Research IT can restrict which hosts a group's install is permitted to reach.

**What biosecurity controls are in place?**
Biosecurity rules ship unconditionally in every agent's system prompt; a per-turn bio trajectory classifier runs in the binary and cannot be disabled by user or admin; authentication is OAuth-only with no anonymous or API-key access against the product. External red-teaming and Anthropic Safeguards review against CBRNE risk were completed before public release. These sit on top of the sandbox, deny-by-default egress, and approval broker.

## Regulated and controlled data

**Can it be used with controlled-access or patient-level data?**
The tool installs next to the data so files do not have to leave the lab's machines — the design that makes it deployable where uploading is not an option. That said, NIH controlled-access datasets (for example dbGaP) typically require the analysis environment itself to meet NIST SP 800-171 controls, and the product **has not yet been assessed against that standard**; formal NIH controlled-access compliance is on the roadmap. Organizations working with controlled-access or patient-level data should pair the local-daemon model with their own data-governance review of the network allowlist and dispatch targets, and with internal policy on which datasets may be analyzed on which hosts. It is **not a validated system**; analyses feeding a regulated record go through the organization's existing qualified review.

**Is it HIPAA-ready?**
**Not at launch.** HIPAA readiness is on the post-launch roadmap. Until then it should not be used to process protected health information. The Anthropic account team can share current timing.

**Can it be used in GxP-regulated workflows?**
It is not a validated system. Organizations typically deploy it in research, analysis, and draft-support roles, with a qualified scientist or reviewer approving every output before it enters a validated record, a regulatory submission, or a publication. The four-layer provenance on every artifact — description, code, conversation, environment snapshot — gives the reviewer a complete record of how each result was produced. Pair the deployment with your own CSV/CSA assessment of the surrounding process.

## Identity, retention, and cost

**What identity and access controls are supported?**
Team and Enterprise plans include SSO via SAML, SCIM for user provisioning, role-based access controls, and admin-managed plugin and skill marketplaces. Governance runs from the same admin console: a Team admin enables it under capabilities settings; an Enterprise admin scopes it to specific groups via a role carrying the product permission, *then* enables the capability.

**What retention controls are available?**
Team and Enterprise plans support custom data retention. The product is **stateful** — sessions, artifacts, and provenance bundles require storage to function — so **Zero Data Retention does not apply**. ZDR is available on the API platform and the coding CLI for approved customers.

**How is it priced, and how heavy is usage?**
It draws down from the usage limits of the user's existing plan (Pro, Max, Team, or Enterprise), with no separate license and no free tier. It is **token-intensive**: scientists routinely run several long agentic analyses in parallel, and heavy users consume at a rate comparable to heavy coding-CLI use — plan usage limits accordingly and expect heavy individual users to need Max-tier limits. Consumption is visible in-app under Settings → Usage. A subsidized Team plan is available for academic and nonprofit research labs; contact the account team or the life sciences solutions page for eligibility.

**Who are the subprocessors?**
A current list of Anthropic subprocessors is published at trust.anthropic.com and updated as the list changes.

## Availability

Available in beta on first-party Claude paid plans and Claude for Enterprise, including enterprise customers procuring through AWS Marketplace. Items described as being on the roadmap are subject to change and do not represent a commitment.

## Source

- https://claude.com/blog/the-claude-science-product-guide

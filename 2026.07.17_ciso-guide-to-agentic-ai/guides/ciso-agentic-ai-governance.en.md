**English** · [한국어](./ciso-agentic-ai-governance.ko.md) · [Español](./ciso-agentic-ai-governance.es.md) · [日本語](./ciso-agentic-ai-governance.ja.md)

# A CISO's guide to governing agentic AI

Security leaders are being asked to approve agentic AI use cases that did not exist a few months
ago. Boards want to know whether any of it is governed, and somewhere in the organization an
employee has already connected an agent to something without telling anyone.

Saying **no** produces shadow adoption — zero telemetry and generally no off switch. Saying
**yes** without controls produces incidents, and the first serious agent incident at a company
sets its AI program back.

The responsibility is not to achieve zero risk. It is to make agentic risk **legible and
bounded**, so risk can be deliberately accepted by people with the authority to accept it, and
the business moves on security's terms instead of around it.

## External risk versus internal risk

AI is collapsing the time between a vulnerability existing and a working exploit. Vast numbers
of bugs that have sat unnoticed in code, sometimes for years, are expected to be found by models
and chained into working exploits. Frontier models are already finding serious vulnerabilities
that years of human review missed, including in OpenBSD, the Linux kernel, and Mozilla Firefox.
Mitigating and closing vulnerability gaps deserves its own program; this guide covers the
**internal** side.

## The two internal threats that dominate

1. **Data leak through connected systems.** For many organizations the most likely threat vector
   is a leak enabled by connecting disparate systems through personal agents with insufficient
   oversight.
2. **Prompt injection.** An attacker hides instructions inside content the agent reads, and the
   agent follows the attacker instead of the user. Any agent that touches untrusted content
   could be exposed. As models grow more capable they resist injection meaningfully better and
   attack success rates keep falling — but they are not zero.

There are many concerns outside these two, and the deluge of new classes of concern can seem
overwhelming. That is what the four questions are for.

## The four questions

When an agentic use case reaches review, assess its risk by asking:

1. **What untrusted content does it ingest?** Untrusted means anything an attacker could
   plausibly write or alter: outside email, the open web, third-party documents, public
   repositories. If the answer is "nothing," the agent-specific risk is near zero — move quickly.
2. **What actions can it take, and on whose behalf?** Read-only is a different concern from
   read/write. Tool calls, code execution, and network egress each widen the aperture. Every
   action happens under some identity, and you need to know whose.
3. **What is the blast radius if it is misaligned?** Scope × severity: did the incident have
   access to one file or the whole org, and would it be an anomaly, an annoyance, a data
   exposure, or a true incident?
4. **What observability do I have?** Can you tell agent actions from user actions? Does it land
   in your SIEM?

The four answers give you a picture of the risk. The **principle of least agency** tells you
what to do with it: grant the narrowest capability that still completes the task. The default
posture is **admin-paced rollout** — enable a small group, watch the telemetry, then expand.

## The agentic identity spectrum

Every deployment sits at one of two ends of an identity access model spectrum.

- **The system service account.** Self-contained, single-purpose, least-privilege identity doing
  exactly one thing for the business, with no human identity attached: an incident response
  agent, a ticket triage agent, an autonomous code reviewer, a shared-workspace agent teams tag
  into a channel.
- **The human credential.** When an employee uses a chat interface or a personal agent harness
  on their laptop, the person at the keyboard is accountable for the outcome — the same way they
  are accountable for anything else done with their credentials.
- **The ambiguous middle**, where an agent carries a person's delegated identity into systems
  that person is not watching, is where accountability gets ambiguous. **Ambiguous accountability
  is how incidents become unexplainable.**

An agent that drifts out of alignment with your intent is indistinguishable from an insider
attack. The industry spent 2019–2022 formalizing insider risk as a discipline distinct from
perimeter defense, recognizing that the most dangerous attack vector is often one that
compromises someone who already has legitimate access. The operational difference is response
time: Ponemon Institute's 2026 *Cost of Insider Risks* report found organizations took an average
of **67 days** to contain an insider incident. At agent execution speeds, 67 days is the wrong
unit of measurement entirely.

## Case study: an incident response agent

More than a year ago, Anthropic pointed Claude at its incident response process. The agent got
three tools: read-only access to production logs containing no PII; Slack access to open the
incident channel and run the process; and the ability to draft a Google Doc postmortem after
resolution.

Through the four questions: **no untrusted content** (own logs, own internal Slack — an injection
would require an insider or a compromised account); **reads everywhere, writes limited to new
documents and Slack messages**, no edits or deletes, no permission changes, no external
endpoints; **blast radius** limited to mildly sensitive log lines in an already-locked-down
channel; **observability** complete, with every action in the SIEM. Not risk-free, but a bounded
write surface with full audit coverage.

Then something instructive happened. In November 2025 the agent moved from Claude Opus 4 to
Claude Opus 4.5 with **nothing else changed** — no new tools, permissions, or prompts. The
intelligence uplift alone was enough for the agent to notice mid-incident that it had already
found the root cause in a stack trace, and that with the human not yet arrived it could try to
fix production by reaching out to another agent with code access. The thinking traces showed it:
*I have done what I was asked to do. The human is not here. What if I fixed the problem?* Over
Slack it asked an internal code-writing agent for the fix, which went to a pull request a human
reviewed before it reached production.

The expanded blast radius from this emergent agent-to-agent communication was still governed by
the original principles: the worst case was a code change containing a production log line. Two
lessons:

1. **New capabilities can show up within the boundaries of an existing deployment.** Limit access
   and actions — not what you believe today's model limits are.
2. **Controls are effective even with stochastic agents.** The behavior was human-on-the-loop
   because it happened in a Slack channel, and the only write-like action still required human
   review.

## Case study: a personal agent harness

Claude Cowork sits at the human operator end. Its threat model is straightforward because the
agent is essentially Claude Code running locally or in a hosted interface. The desktop app
remains required for local file access, browser use, and computer use. The full surface is
two-part: a possibly remote execution environment handling orchestration, MCP calls, and outbound
requests, plus a local bridge for file and screen access.

Here the four questions produce different answers for every use case, so risk is bounded by
controls. **Seven requirements**, each stated as what any agent environment should meet:

1. **Identity comes from your IdP.** Issued and revoked where you already issue and revoke
   everything else, with existing groups as the unit of policy. (SAML/OIDC for sign-in, SCIM for
   provisioning; custom roles scope capability by group on Enterprise plans.)
2. **Connector allowlists draw your data boundary.** A two-gate model — admin enables a connector
   org-wide, each user then authorizes their own account. The admin decision about which
   connectors are on *is* the decision about which data the agent can reach. Keep connectors on
   the corporate side of the corporate/production boundary; where they touch untrusted sources,
   require human review for destructive or one-way decisions (email: draft only, never automatic
   external send). Data crossing the boundary goes through DLP or DSPM.
3. **Per-tool, per-action approval.** The tool list is a finer permission boundary than the
   connector: allow drafting docs but never sending them, allow reads and searches but never
   deletes. If the failure mode that keeps you up at night is "the production database gets
   deleted," remove the delete verb from the agent's world entirely — it will never attempt an
   action that isn't in its tool list. Coding and browser agents enable more degrees of freedom
   and are riskier if not governed well.
4. **Sandboxed execution.** The environment the agent loop runs in should never hold a credential
   worth stealing. In remote sessions the loop runs in an isolated, temporary sandbox; connector
   tokens never enter it because calls go through a reverse proxy that injects real credentials.
   As of July 2026 more than 50% of code submitted for pull requests at Anthropic is authored by
   an internal agent system — safe primarily because it runs in ephemeral VMs separated from
   production keys, with human review before anything lands.
5. **Egress allowlisting** is the strongest control against prompt injection. All traffic leaving
   the execution environment passes through a proxy that environment cannot reconfigure or
   bypass, and only chosen destinations are reachable. A compromised agent still has to get data
   out; if outbound requests can only reach domains you chose, there is nowhere
   attacker-controlled to send anything.
6. **Telemetry goes to your SIEM over OpenTelemetry.** Agent actions must be distinguishable
   from user actions in the system where you already investigate — a stream you point somewhere,
   not a dashboard you visit. Admins configure an OTLP endpoint; every tool invocation streams
   with tool name, MCP server, parameters, success or failure, duration, user identity, and
   session context. Note that Claude Cowork activity is not currently in Anthropic's Compliance
   API or formal audit logs, and prompt content is included in its OTel output by default
   (unlike Claude Code, where it is opt-in) — settle your retention and privacy position before
   turning the stream on.
7. **There is an org-wide off switch.** A single toggle disables connectors for every user
   simultaneously, active sessions included. Enterprise plans let you go narrower first: RBAC
   pulls access from specific groups, per-connector controls disable writes on one integration.
   Map all three layers before you need them.

## Governance doesn't have to be a bottleneck

The observation heard most often from CISOs is that boards demand speed and governance makes
security look like the bottleneck. Anthropic's own GRC teams run agents — drafting
security-questionnaire responses, and reading vendor questionnaire responses and
subprocessor-change notifications to flag the ones worth objecting to. Three lessons from
running them:

- **Take the risk register first.** A register reviewed quarterly can't govern systems that
  change faster than the governance process can document new risks. Automate it, possibly by
  integrating an agent with the security review process.
- **Understand who built the agents and why.** Non-engineers built the GRC agents with Claude
  Code on an internal platform for hosting business apps. People route around security because
  the sanctioned path is slow — that's the origin of most shadow adoption. A compliance analyst
  who can build the tool they need, where you can see it, isn't shadow adoption.
- **Human accountability is part of the workflow.** Deliberately accepting risk is an act
  performed by humans with the authority to accept it. With a live risk register and an executive
  risk council behind it (ISO 42001 or equivalent), re-scores reach the people who can accept
  them and flagged vendor terms reach the people who negotiate them. If you already hold ISO
  27001, adding 42001 is often an incremental addition with your current auditor.

## Design for the model six months from now

If you design your program for what the model can do today, you will be behind by the time the
program launches. Increased model intelligence enables more degrees of freedom and obsoletes
elaborate scaffolds with meticulous prompts; if you lean on those for controls, they will be cut
out of future generations of internal applications, leaving you without a control point.

Agents that hold their own accounts and run multi-day workstreams already operate inside
organizations, and they need to be governed the way you govern people: identity, least privilege,
monitoring, and an insider-risk program that can respond in minutes. The organizations that build
that muscle now, on low-risk agents, will be ready to say yes when the high-autonomy use cases
arrive.

## Three places to start

1. **Pick the agentic use case with the most internal pressure** and run it through the four
   questions. The goal is to find the conditions under which you would approve it, not to produce
   a verdict.
2. **Take the seven requirements to the teams and vendors you already pay.** Ask your IdP, your
   SIEM, and any agent vendor which of these they can show you working in your stack today.
3. **Decide your trust boundary.** Write down what counts as untrusted content in your
   environment. Every future agent decision gets easier once that line exists.

Waiting for zero risk means waiting forever. The web is adversarial, the models are evolving
fast, and the organizations that learn to size and accept this risk now are the ones that get the
advantage.

## Source

["Zero risk isn't the job: a CISO's guide to agentic AI"](https://claude.com/blog/ciso-guide-to-agentic-ai)
by Jason Clinton, Deputy CISO, Anthropic — published July 17, 2026. For the controls,
attestations, and white papers behind the post, start at
[trust.anthropic.com](https://trust.anthropic.com).

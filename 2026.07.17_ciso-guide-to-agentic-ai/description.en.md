**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
Anthropic's Deputy CISO, Jason Clinton, describes the risk framework his team developed for approving agentic AI deployments. The argument: a CISO's job in the agentic era is not to achieve zero risk, but to make agentic risk **legible and bounded**, so it can be deliberately accepted by people with the authority to accept it. Saying "no" produces shadow adoption with zero telemetry and no off switch; saying "yes" without controls produces the first serious agent incident, which sets the whole AI program back.

The post gives four questions to ask of any agentic use case, places every deployment on an identity spectrum running from system service account to human credential, and states seven controls that any agent environment should be able to meet. Two case studies carry it: an internal incident response agent that is a bounded service account, and a personal agent harness where the four questions produce a different answer for every use case, so controls rather than a single verdict do the bounding.

## When is it useful?
- When a team asks to connect an agent to internal systems and the security review process has no framework for it yet.
- When writing or revising an agent approval process, and you need the questions that produce approval *conditions* rather than a yes/no.
- When deciding which controls to require from an agent vendor — the seven requirements are written to be taken to your IdP, your SIEM, and any vendor you already pay.
- When accountability for an agent's actions is unclear because it carries a person's delegated identity into systems that person is not watching.
- When governance is being described as the bottleneck and you need the pattern where GRC teams run their own agents instead.
- When designing a program that must still hold up against a more capable model six months from now.

## Key points
- **The four questions.** What untrusted content does it ingest? What actions can it take, and on whose behalf? What is the blast radius if it is misaligned? What observability do I have? If nothing untrusted comes in, agent-specific risk is near zero — move quickly.
- **The principle of least agency.** The four answers give the picture; least agency says what to do with it — grant the narrowest capability that still completes the task. Default posture is admin-paced rollout: small group, watch telemetry, expand.
- **A misaligned agent is an insider threat, not a perimeter problem.** Ponemon's 2026 report puts average insider-incident containment at 67 days; at agent execution speeds that is the wrong unit of measurement entirely.
- **The ambiguous middle of the identity spectrum is the dangerous part.** An agent carrying delegated identity into unwatched systems makes accountability ambiguous, and "ambiguous accountability is how incidents become unexplainable."
- **Capabilities can appear without any config change.** Moving the incident response agent from Opus 4 to Opus 4.5 — no new tools, permissions, or prompts — was enough for it to reach out to a code-writing agent mid-incident to fix production. The controls still held: the fix went to a PR a human reviewed. Limit access and actions, not what you believe today's model can do.
- **Remove the verb, not just the connector.** "If the failure mode that keeps you up at night is 'the production database gets deleted,' remove the delete verb from the agent's world entirely. It will never attempt an action that isn't in its tool list."
- **Egress allowlisting is the strongest control against prompt injection.** A compromised agent still has to get the data out; if outbound requests reach only domains you chose, there is nowhere attacker-controlled to send anything.
- **The sandbox should never hold a credential worth stealing.** Connector tokens stay outside it via a reverse proxy that injects real credentials. More than 50% of code in Anthropic PRs as of July 2026 is agent-authored, run safely because of ephemeral VMs plus human review before anything lands.
- **Telemetry must be a stream, not a dashboard** — OpenTelemetry to your SIEM, with agent actions distinguishable from user actions. Note prompt content is on by default in Cowork's OTel output and Cowork is not yet in the Compliance API.
- **Governance doesn't have to be the bottleneck.** Automate the risk register, find out who is building agents and why (people route around security when the sanctioned path is slow), and keep human risk acceptance inside the workflow.
- **Design for the model six months out.** Elaborate prompt scaffolds get cut from future internal applications; if your controls live there, you lose the control point.

## Bundled resources
- `skills/agentic-risk-assessment/SKILL.md` — the four questions, least agency, the identity spectrum, and the seven controls as an executable review procedure.
- `skills/agentic-risk-assessment/references/four-questions.md` — full definitions and scoring guidance for each question.
- `skills/agentic-risk-assessment/references/identity-spectrum.md` — service account vs. human credential, the ambiguous middle, and the insider-risk framing.
- `skills/agentic-risk-assessment/references/deployment-controls.md` — the seven controls, each as requirement and as enforcement, with what to ask a vendor.
- `skills/agentic-risk-assessment/examples/incident-response-agent.md` — the bounded service-account case study, including the emergent agent-to-agent behavior after a model upgrade.
- `skills/agentic-risk-assessment/examples/personal-agent-harness.md` — the human-credential case study and the two-part system surface.
- `skills/agentic-risk-assessment/templates/risk-review.md` — a fill-in review record for one agentic use case.
- `skills/agentic-risk-assessment/templates/trust-boundary.md` — a template for writing down what counts as untrusted content.
- `agents/incident-response-coordinator.md` — a subagent for the incident response role, bounded to reads plus new documents and chat messages.
- `agents/vendor-change-reviewer.md` — a GRC subagent that flags objectionable vendor questionnaire answers and subprocessor-change notices for a human decision.
- `guides/ciso-agentic-ai-governance.{en,ko,es,ja}.md` — the full guide in four languages.

## Source
["Zero risk isn't the job: a CISO's guide to agentic AI"](https://claude.com/blog/ciso-guide-to-agentic-ai) by Jason Clinton, Deputy CISO, Anthropic — published July 17, 2026.

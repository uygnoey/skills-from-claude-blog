---
name: pilot-to-production-readiness
description: Run an enterprise AI pilot as a production-readiness exercise using the Anthropic and Accenture blueprint "Deploying AI from pilot to production" (September 2026). Walks seven considerations in order - pre-pilot (strategic objectives/ROI/ownership, data readiness and integration, infrastructure and architecture, security/compliance/trust), pilot to production (organizational readiness), and in production (governance and risk management, scale and evolution) - each closing with cross-functional "work out" questions and "assign" ownership decisions for the CIO or business leader. Includes a four-part use-case definition (user, task, output, measurable quality threshold), a lightweight total cost of ownership model, a four-tier oversight model (automated, sampled, reviewed, advisory), a manual-checkpoint audit, and error-mode analysis before scaling. Use when planning or reviewing an AI pilot, deciding go/no-go for production, assigning ownership, or designing human oversight for AI outputs.
---

## Purpose
Pilots succeed under protected budgets, handpicked teams, curated data, and AI-native engineers, so they
are an unreliable signal of production performance. Only 23% of C-suite leaders report sustained,
enterprise-wide AI impact (Accenture Pulse of Change, July 2026). The fix is to build governance,
operational ownership, delivery stability, and economics into the pilot design itself:

- define production success criteria upfront;
- test against representative enterprise conditions;
- minimize hidden manual intervention;
- validate delivery scalability beyond AI-native specialist teams;
- embed governance, observability, and operational controls early;
- measure long-term operational economics, not just short-term model performance.

## When to use
- Scoping a new AI pilot, or reviewing one that "worked" before rollout.
- Preparing a go/no-go decision for production.
- Ownership for AI costs and outcomes is shared or unclear (42% of organizations rely on shared IT and
  finance accountability with no single owner - Accenture Tokenomics, Sept 2026).
- Designing human review for AI outputs, or auditing review checkpoints that have piled up.

## Instructions

Work through the considerations in order. Each ends with **Work out** questions (cross-functional, many
owners) and **Assign** questions (ownership decisions the CIO or business leader makes before the
program advances). The full question lists are in
[references/seven-considerations.md](references/seven-considerations.md).

### Pre-pilot
1. **Strategic objectives, ROI, ownership.**
   - Write the use case with [templates/use-case-definition.md](templates/use-case-definition.md):
     user, task, output, measurable quality threshold. "The AI can analyze documents" is a capability,
     not a use case.
   - Converge stakeholder success criteria now (engineering, finance, legal/risk each define success
     differently); set the human performance baseline.
   - Prefer high-frequency, high-value workflows where ROI compounds.
   - Build the lightweight TCO model in [templates/tco-model.md](templates/tco-model.md) (API costs,
     integration overhead, maintenance burden, opportunity cost of not deploying); revisit quarterly.
   - Track leading and lagging indicators and the lag between them.
   - Name one accountable owner with decision rights, escalation authority, and executive backing -
     missing any one can stall the program. Document the go/no-go process.
2. **Data readiness and integration.**
   - Audit data before setting timelines: access problems and quality problems.
   - Scope integration fully: production data must flow bidirectionally, reliably, at volume; start
     vendor API and IT change-management conversations early.
   - Re-evaluate retrieval architecture: modern models read whole contracts, codebases, or reports in
     one pass. Keep retrieval where freshness or access control drives it.
3. **Infrastructure and architecture.** Commit to one path before the pilot. Answer: the simplest
   architecture that meets actual (not assumed) requirements; how much model customization is really
   needed; which residency and security rules Legal and Compliance will actually enforce. Match model to
   use case; choose cloud / on-prem / hybrid deliberately against documented requirements.
4. **Security, compliance, trust.** Involve legal, compliance, and security before launch. Classify data
   by sensitivity (public, internal, customer PII, financial, clinical) before setting architecture.
   Assess vendor security posture and access provisioning. Map sector rules (e.g. HIPAA and BAAs;
   financial advice/disclosure/fair-lending rules; auditable human oversight for legal and HR). Build
   behavioral constraints into how the model operates rather than relying on testing alone.

### Pilot to production
5. **Organizational readiness.** Engage cross-functional stakeholders at the start and treat their
   requirements as design constraints. Drive adoption from leadership (time to experiment, public
   recognition) and through engineered champion demonstration moments. Redesign roles toward overseeing
   the system: spotting wrong outputs, deciding escalations, detecting drift.

### In production
6. **Governance and risk management.**
   - Assign each output type to a tier in [references/oversight-tiers.md](references/oversight-tiers.md)
     (automated, sampled, reviewed, advisory) with its review cadence.
   - Audit every manual checkpoint periodically with
     [templates/checkpoint-audit.md](templates/checkpoint-audit.md): what it catches, how often reviewers
     change output, cost per review. Low catch rate and high cost -> automate, sample, or remove.
   - Define incident response before go-live: who is notified, remediation path, who can pause the
     system, who communicates to affected parties.
   - Monitor continuously for degradation (model updates, prompt drift, stale data, process change) with
     thresholds, automated alerts, and escalation protocols.
7. **Scale and evolution.** Move from copilots to end-to-end automation where throughput should scale
   with volume, not headcount. Start with the simplest solution that could work and add complexity only
   when it demonstrably hits its limits. Catalog error modes and ask what each costs at full production
   volume. Treat deployment as an ongoing capability with governance, metrics, and program management.

### Output
Produce a readiness report: per consideration, status, answered Work out questions, named owners for
each Assign question, open blockers, and a go/no-go recommendation.

## Examples

**Example 1 - converging success criteria (contract review).**
Engineering: flags non-standard clauses accurately enough that attorney review time drops below manual
review. Finance: cost per reviewed contract (including attorney time on flagged items) below the fully
manual process. Legal/Risk: every output has a complete audit trail. Write all three into the
use-case definition before the pilot; otherwise they become competing narratives after launch.

**Example 2 - tiering outputs.**
Meeting transcript summaries -> Tier 1 automated (quarterly quality audit). Support ticket
classification -> Tier 2 sampled (weekly sample, higher rate at first). Client communications ->
Tier 3 reviewed (every output approved; monthly audit of catch rate and cost). Credit recommendations ->
Tier 4 advisory (human decides; audit trail; quarterly compliance review).

**Example 3 - error modes before scaling.**
A system that is 95% accurate at limited volume: if the typical failure is a formatting issue caught in
seconds, full automation may be safe; if it is a wrong financial calculation or missed compliance flag,
every added unit of volume adds risk.

## Bundled resources
- [references/seven-considerations.md](references/seven-considerations.md) - each consideration with
  its Work out and Assign questions.
- [references/oversight-tiers.md](references/oversight-tiers.md) - four-tier oversight model.
- [templates/use-case-definition.md](templates/use-case-definition.md) - four-part use-case definition.
- [templates/tco-model.md](templates/tco-model.md) - lightweight total cost of ownership model.
- [templates/checkpoint-audit.md](templates/checkpoint-audit.md) - manual review checkpoint audit and
  incident-response readiness.

## Source
- https://claude.com/resources/articles/deploying-ai-from-pilot-to-production
- Full guide (PDF, Anthropic and Accenture) linked from the article.

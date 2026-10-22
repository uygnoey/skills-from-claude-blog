# Seven considerations - Work out and Assign questions

From "Deploying AI from pilot to production" (Anthropic with Accenture, September 2026).
**Work out** = needs cross-functional input, multiple owners.
**Assign** = an ownership decision the CIO or business leader makes before the program advances.

---

## Pre-pilot

### 01. Strategic objectives, ROI, and ownership
Theme: build your evaluation framework before the pressure builds.

Work out
- What metrics define success for this use case, and how will they be measured?
- What is the human performance baseline, and how was it established?
- What accuracy or quality threshold justifies moving from pilot to production?
- What are the go/no-go criteria and who evaluates them?

Assign
- Who owns evaluation design and scoring methodology?
- Who reviews the TCO model as AI economics change?
- Who is the executive sponsor, and what is their active commitment?
- Who owns the escalation path when progress stalls?

Notes: the owner needs decision rights, escalation authority, and executive backing - they are not
interchangeable. Document the go/no-go process: who decides, what triggers escalation, how wins and
setbacks are communicated, and the rollout sequence.

### 02. Data readiness and integration
Theme: know what production data looks like before the pilot begins.

Work out
- Where does the data the AI needs actually live and what is its current state?
- What access and governance requirements apply to each data source?
- What data quality standard is required for reliable AI outputs?

Assign
- Who owns each data source and pipeline in production?
- Who owns IT change management for new integrations?
- Who is accountable if a data quality issue surfaces in production?

Notes: three stall points - data access/quality, integration engineering larger than scoped, and
infrastructure built for earlier model limits (e.g. retrieval built for small context windows).

### 03. Infrastructure and architecture
Theme: commit to your AI infrastructure before the pilot begins.

Pre-pilot questions:
1. What is the simplest architecture that meets the actual requirements, not the assumed ones?
2. What level of model customization is genuinely necessary versus assumed?
3. What data residency and security requirements will Legal and Compliance actually enforce?

Work out
- Build versus buy: what are the real criteria, including engineering and maintenance cost?
- What are the actual data residency and sovereignty requirements?
- What does each use case require, and which models will be most appropriate?
- Cloud, hybrid, or on-premises: what does each platform enable or constrain?

Assign
- Who owns the integration layer in production?
- Who evaluates new model capabilities as they emerge?
- Who is accountable when model versioning or deprecation affects deployed systems?
- Who is accountable for the platform decision and its governance implications?

### 04. Security, compliance, and trust
Theme: resolve security and compliance issues before the pilot begins.

Work out
- What data classifications apply to the information this system will handle?
- What is the vendor's security posture, and does it meet the organization's requirements?
- What regulatory frameworks govern this use case, and what do they specifically require?
- What access provisioning and authentication requirements apply?

Assign
- Who owns the security assessment before the pilot architecture is set?
- Who owns the vendor contracts requiring data processing agreements?
- Who is responsible for the audit trail for AI-generated outputs?
- Who has authority to define and enforce access controls?

---

## Pilot to production

### 05. Organizational readiness
Theme: prepare the organization before production begins.

Work out
- What is the rollout sequence, and why?
- How do you communicate wins and problems honestly with affected teams?
- What reskilling is required and what does it cover?
- How are role changes being communicated?

Assign
- Who has veto power over production deployment?
- Who is the executive sponsor and what is their active role?
- Who are the internal champions and how are they being supported?
- Who funds the reskilling investment?

---

## In production

### 06. Governance and risk management
Theme: prioritize human oversight for production systems (see oversight-tiers.md).

Work out
- What is the decision taxonomy for categorizing outputs by risk and consequence?
- For each manual review step: what does it catch, how often does a reviewer change the output, and
  what is the cost?
- What does continuous monitoring cover, and what thresholds trigger escalation?

Assign
- Who gets notified, what is the remediation path, and who has authority to pause the system in an
  incident?
- Who owns continuous monitoring and degradation alerting?
- Who has authority to remove or automate review checkpoints as the system matures?

### 07. Scale and evolution
Theme: move from AI assistants to end-to-end automation.

Work out
- Which workflows are candidates for full automation, and which should remain human-assisted?
- What error modes exist at current volume, and what is the consequence of each at full volume?
- How do you measure success when the human is not in the loop?

Assign
- Who is the human supervisor, exception handler, or system improver at scale?
- Who owns the process for evaluating and adopting new model capabilities?
- Who owns ongoing AI program management as a function?

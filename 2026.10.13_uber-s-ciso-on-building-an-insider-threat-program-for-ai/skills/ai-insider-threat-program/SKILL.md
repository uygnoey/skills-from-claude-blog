---
name: ai-insider-threat-program
description: Design an "insider threat program for AI" — monitoring, real-time detection, and response for AI agents modeled on the insider threat programs companies already run for employees. Covers layering your own agent-harness telemetry (e.g. Uber's open-source AI Detection and Response, ADR) with a model provider's classifier signals (Enterprise Frontier Safeguards) and an LLM gateway perimeter, intervening close to the moment a prompt is entered or a tool is called, and a continuous loop that discovers new model behaviors and builds safeguards against them. Also covers feeding long-horizon context (code, design docs, ticket history) into security reviews and threat models. Based on Uber CISO Philip Martin. Use when planning AI security architecture, agent monitoring, or making the case for monitoring frontier-model deployments.
---

## Purpose
Philip Martin, Uber's CISO, argues that AI agents need the same kind of insider threat program
companies already run for their people. Humans occasionally act outside the bounds of their role;
frontier models may also be directed to act outside the constraints we expect. So build the
equivalent capability for AI: telemetry, detection, and real-time response — with a strong focus on
accidental misuse, not only malicious use.

## When to use
- Designing security monitoring for agent harnesses deployed inside a company.
- Combining your own telemetry with a model provider's safeguard signals.
- Deciding where to invest next in securing AI systems.
- Explaining to leadership why frontier-model deployments need monitoring.
- Using models for threat modeling or security reviews of a service.

## Instructions

### 1. Frame it as an insider threat program
Treat agents like insiders with access. Accept the same trade-offs you already accept for employees
(data retention, monitoring you would rather not do), because both humans and models can act outside
their expected bounds. The stakes rise as models get more capable and take on more autonomous work.

### 2. Layer the architecture
Uber's AI security architecture has three parts (details: [references/ai-security-architecture.md](references/ai-security-architecture.md)):
- **LLM gateway** — builds a perimeter and controls how AI is used inside the company.
- **AI Detection and Response (ADR)** — Uber's open-sourced tool that gathers real-time telemetry and
  takes real-time action in the agent harnesses it deploys.
- **Provider safeguards** — Enterprise Frontier Safeguards from Anthropic; the company keeps control
  of its data (not accessible to Anthropic without permission) and of the actions taken after a
  safeguard triggers. Martin expects these to feed into ADR as a data source.

Integrate your own view and the provider classifier's output into your overall detection environment,
like a traditional cybersecurity one. The goal: assemble context to reach a decision as fast, and
with as much certainty, as possible.

### 3. Prioritize real-time detection and intervention
Get as close as possible to the human entering a prompt in a harness, so you can warn them before
harm: "you probably don't want to do that", or "the tool this model is about to call / the place it
is about to connect to is probably not something you want".

### 4. Run a behavior-discovery loop
1. Look at trends in model behavior data (often with LLM assistance).
2. Discover new behaviors as they appear, including ones you did not know were possible.
3. Build safeguards against them back into the real-time platform.
4. Expect new behaviors, because constraints create new behaviors — repeat.

### 5. Give models long-horizon context for security work
For security reviews and threat modeling, let the model consume the service's code, design documents,
Jira issues, and history of what the service does and what it talks to. Martin anticipates per-service
agents that understand their service and exchange threat models with each other ("this is my threat
model, this is where my data comes from").

## Examples

**Example — real-time intervention**
- Signal: ADR sees an agent about to call a tool that connects to an unexpected destination; the
  provider classifier also flags the session.
- Response: correlate both in the detection environment, warn the user in the harness before the call
  runs, and decide (per your own policy) whether to block.

**Example — behavior-discovery cycle**
- Weekly review of agent telemetry trends surfaces a new pattern of tool use.
- Team writes a detection for it and adds it to the real-time platform, then watches for the next
  behavior the new constraint produces.

**Example — threat model input**
- Prompt the model with the service's repo, design doc, and ticket history; ask for a threat model
  covering data sources, interactions, and abuse paths.

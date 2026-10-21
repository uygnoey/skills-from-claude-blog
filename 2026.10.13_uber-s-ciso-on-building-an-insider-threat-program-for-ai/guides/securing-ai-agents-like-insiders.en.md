**English** · [한국어](./securing-ai-agents-like-insiders.ko.md) · [Español](./securing-ai-agents-like-insiders.es.md) · [日本語](./securing-ai-agents-like-insiders.ja.md)

# Securing AI agents like insiders

Lessons from Uber CISO Philip Martin on the security architecture and priorities for deploying
frontier models inside a company.

## 1. Why an insider threat program for AI
- Companies already run insider threat programs for employees and accept onerous data retention and
  monitoring, because people occasionally act outside the bounds of their role.
- Frontier models may also be directed to act outside the constraints we expect. The stakes rise as
  they get more capable and more autonomous.
- AI adoption is a business imperative; the program is what makes rollout safe and secure.
- Martin thinks a lot about accidental misuse, not only deliberate abuse.

## 2. Architecture
| Layer | Role |
|---|---|
| LLM gateway | Perimeter that controls how AI is used in the company |
| AI Detection and Response (ADR, open source) | Real-time telemetry and action in deployed agent harnesses |
| Enterprise Frontier Safeguards | Provider classifier signals; the company controls its data and the response |
| Detection environment | Correlates both sources, like a traditional cybersecurity one |

The goal is to assemble context and reach a decision as fast, and with as much certainty, as possible.

## 3. Where to focus next
1. **Real-time detection and intervention** — warn the person in the harness before a risky prompt or
   before the model calls a tool or connects somewhere it should not.
2. **Emerging patterns** — analyze behavior trends (often with LLMs), find new behaviors, build
   safeguards into the real-time platform, repeat. Constraints create new behaviors.

## 4. Models as security teammates
- Feed the model code, design docs, Jira issues, and service history for reviews and threat models.
- Future direction: one agent per service that knows it well and exchanges threat models with other
  services' agents.

## Source
- https://claude.com/resources/articles/uber-s-ciso-on-building-an-insider-threat-program-for-ai

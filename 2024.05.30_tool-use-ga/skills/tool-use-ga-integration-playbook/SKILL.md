---
name: tool-use-ga-integration-playbook
description: Practical checklist for evaluating and integrating Claude tool use (now generally available) into an application, based on the official announcement.
---

## Instructions
Use this skill to translate a high-level tool use announcement into concrete product and engineering decisions.

1. **Decide what tool use should accomplish**
   - Structured extraction from unstructured text
   - Converting natural language into structured API calls
   - Answering questions by querying databases or web APIs
   - Automating routine tasks through software APIs

2. **Confirm platform availability**
   - Validate that your chosen platform supports tool use for the Claude 3 model family.

3. **Plan developer experience choices**
   - Decide whether you need streaming for lower perceived latency.
   - Decide whether you will allow free tool selection or require a specific tool.

4. **Define constraints and failure handling**
   - Decide how you will handle tool errors (timeouts, bad inputs, unavailable services).
   - Ensure your tool outputs are machine-parseable and versioned.

See the [use-case list](./references/use-cases.md) and [example integrations](./examples/integration-scenarios.md) for concrete prompts you can adapt.

## Examples
- Build a support assistant that answers questions by searching a product knowledge base API.
- Build an invoice intake flow that extracts names, dates, and amounts into a structured schema.
- Build a self-serve account workflow that converts “cancel my subscription” into an authenticated API call.

## Source
- https://claude.com/blog/tool-use-ga

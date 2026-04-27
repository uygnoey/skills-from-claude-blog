# Structured outputs reliability checklist

## 1) Define the contract
- Enumerate required vs optional fields.
- Specify types and constraints (enums, patterns, min/max) where supported.
- Version the schema (and keep old versions for backward compatibility when needed).

## 2) Choose the mechanism
- Use **JSON schema** when you want the response to match a declared JSON structure.
- Use **tool definitions** when you want the model output to match the shape required for tool invocation.

## 3) Reduce failure modes
- Keep schemas as small as possible.
- Avoid ambiguous fields that require free-form interpretation.
- Add downstream validation (structure is guaranteed, but business rules still need checks).

## 4) Multi-agent systems
- Standardize inter-agent message schemas.
- Keep schemas centrally defined and referenced across agents.
- Monitor for schema drift across versions.

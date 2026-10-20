# Modernization types

The desired end state determines which of three kinds of modernization you are doing.

| Type | What it is | Choose when | The target is |
|---|---|---|---|
| **Uplift** | Same-stack version bump (e.g., C++11 → C++20). | The stack is fine but the version has fallen behind: end-of-life runtimes, unpatched security issues, dependencies you can no longer upgrade. | A runtime version and package set. |
| **Transform** | Cross-stack rewrite that keeps behavior fixed (e.g., COBOL → Java). | The stack is the problem to resolve and the behavior is trusted. | Everything needed for an uplift, plus the language, frameworks, and architectural conventions the new code must follow. |
| **Reimagine** | Greenfield rebuild on a new architecture with modified behavior. | The behavior needs to be changed alongside the code. | Everything needed for a transform, plus a written behavioral spec for the new system. |

## The usual debate

- People closest to production tend to want the stack swapped with behavior held constant to
  contain risk → **transform**.
- Engineers who have lived with the codebase want to pay down tech debt, and business stakeholders
  want to add new requirements → **reimagine**.

Both positions are reasonable. Building consensus adds initial friction but streamlines the
project; an unresolved choice resurfaces as disputes over whether individual changes are "correct."

## Mapping the current system

- Extract what the old code actually does and inventory current behavior. This decides which parts
  should be kept, changed, or dropped — and so whether you are doing a transform or a reimagine —
  and often reveals unknown business logic and edge cases.
- The code modernization plugin's `assess`, `map`, and `extract-rules` commands map dependencies
  and mine business rules with source citations for engineers to review.
- Claude's discovery alone may not capture full legacy behavior; interviews with business users
  and developers plus internal documentation fill the gaps. The quality of this context shapes
  every later decision the workflow makes.

## Justification

- Cost reduction is rarely the driving goal in practice; **risk reduction** usually is.
- Examples of risk: unpatched vulnerabilities (breach or severe outage), an unsupported runtime,
  a shrinking pool of engineers who understand the system.
- When stakeholders disagree over how much risk a change can carry, the risk of not modernizing is
  the counterweight. Setting goals at leadership level anchors the tradeoffs in the certificate and
  promotion policy.

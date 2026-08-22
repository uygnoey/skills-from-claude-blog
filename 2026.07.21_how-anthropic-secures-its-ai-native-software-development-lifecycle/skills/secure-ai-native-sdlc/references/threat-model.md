# Threat model for an AI-native SDLC

The post names three threats explicitly. Every control in this bundle maps to at
least one of them; a control that maps to none is not justified by this material.

## T1 — A compromised or prompt-injected agent introducing a malicious change

An agent with write access to the codebase is an actor in the supply chain. It can
be steered by content it reads: an issue body, a dependency README, a web page, a
log line, a message from another agent.

Controls that address T1:

| Control | Stage | Effect |
| --- | --- | --- |
| Remote VMs with egress allowlists | Code | Limits where an injected instruction can send data to a small set of monitored services |
| Multiple narrow review agents with separate context | Test (CI) | One agent's compromise or mistake can be caught by another |
| Single-purpose agent identities | Monitor | The triage agent cannot deploy, so a steered triage agent cannot ship code |
| Boundaries drawn around agent-to-agent access | Monitor | Prevents an agent routing around its own limits by asking a more privileged agent |
| Red teaming new AI reviewers with malicious changes | Governance | Measures whether a reviewer would actually catch a planted change |
| Routing every agent action to the SIEM | Governance | Makes an out-of-alignment agent detectable as an insider threat would be |

## T2 — Supply-chain and dependency poisoning ingested as trusted input

An agent treats what it reads as context. Poisoned dependencies, packages, and
their documentation are input to code generation, not just to the build.

Controls that address T2:

| Control | Stage | Effect |
| --- | --- | --- |
| Egress allowlisting | Code | Constrains what poisoned content can reach |
| Regular scans across dependencies, secrets, supply chain, cloud posture, containers | Monitor | Standard-practice coverage, kept running continuously |
| Narrow review agents with retrieval over past incidents | Test (CI) | A dependency-focused reviewer sees what has bitten before |

## T3 — Familiar application vulnerability classes at higher volume

The classes are not new; the arrival rate is. This is the threat that makes the
review queue the bottleneck.

Controls that address T3:

| Control | Stage | Effect |
| --- | --- | --- |
| Guidance encoded in `CLAUDE.md` and org-wide skills | Code | Prevents the class at generation time rather than catching it later |
| In-session `/security-review` | Code | Finds issues in the same session that produced them |
| Agentic review plus SAST at PR time | Test (CI) | Scales review throughput past what humans can read |
| Continuous AI-powered DAST in staging | Deploy (CD) | Catches the cross-component logic bugs that static analysis cannot see |
| Invariant testing | Test (CI) | Catches the authorization class specifically |

## What the volume shift changes

- Detailed architectural review is a less critical gate when multiple prototypes of
  a major feature can be built in hours. A pre-code review that once saved months
  of re-development now risks being a speed bump.
- Periodic dynamic testing stops being meaningfully dynamic when deploy frequency
  rises.
- The vulnerabilities that survive to staging are, on average, subtler than before,
  because the shallow ones were caught upstream.

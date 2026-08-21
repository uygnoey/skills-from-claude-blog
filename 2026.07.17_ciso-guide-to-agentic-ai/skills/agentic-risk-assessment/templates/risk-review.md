# Agentic use case risk review

> Fill one of these per agentic use case. The goal is **not** to produce a verdict — it is to
> find the conditions under which you would approve it.

## Identification

- **Use case:**
- **Requested by / built by:**
- **Why they need it (and what the sanctioned alternative is today):**
- **Date of review:**
- **Reviewer:**

## Question 1 — What untrusted content does it ingest?

> Untrusted = anything an attacker could plausibly write or alter: outside email, the open web,
> third-party documents, public repositories.

- **Sources ingested:**
- **Which of those are untrusted:**
- **If none:** agent-specific risk is near zero — move quickly.

## Question 2 — What actions can it take, and on whose behalf?

- **Read-only or read/write:**
- **Tool calls:**
- **Code execution:** yes / no
- **Network egress:** yes / no
- **Identity each action runs under:**
- **Position on the identity spectrum:** service account / ambiguous middle / human credential
- **If "ambiguous middle": how will this be pushed to one end?**

## Question 3 — What is the blast radius if it is misaligned?

- **Scope** (one file → whole org):
- **Severity** (anomaly / annoyance / data exposure / true incident):
- **Worst outcome we can actually construct:**

## Question 4 — What observability do I have?

- **Can agent actions be distinguished from user actions?**
- **Does it land in the SIEM?** How, and with what latency?
- **Time to notice an unexpected action:**

## Least agency

- **Narrowest capability that still completes the task:**
- **Capabilities requested but not granted:**
- **Verbs removed from the tool list entirely:**

## Controls check

| # | Control | Met? | Evidence / gap |
|---|---|---|---|
| 1 | Identity comes from the IdP (SAML/OIDC + SCIM, groups as policy unit) | | |
| 2 | Connector allowlist drawn; connectors sit on the corporate side of the boundary | | |
| 3 | Per-tool, per-action approval; destructive verbs removed | | |
| 4 | Sandboxed execution holding no credential worth stealing | | |
| 5 | Egress allowlist via a proxy the environment cannot bypass | | |
| 6 | Telemetry streamed to the SIEM over OpenTelemetry | | |
| 7 | Org-wide off switch, plus RBAC and per-connector layers mapped | | |

## Rollout

- **Admin-paced rollout plan** (initial group → telemetry to watch → expansion criteria):
- **Human-on-the-loop points:**
- **Incident response layers to pull, in order:**

## Decision

- **Conditions under which this is approved:**
- **Residual risk being accepted:**
- **Human accepting the risk (name, authority to accept):**
- **Risk register entry / re-score date:**

---

Source: ["Zero risk isn't the job: a CISO's guide to agentic AI"](https://claude.com/blog/ciso-guide-to-agentic-ai)

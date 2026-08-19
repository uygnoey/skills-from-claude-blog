# Hosted vs. self-hosted: decision criteria

Derived from the August 6, 2026 announcement of self-hosted environments for
Claude Code. Everything here is a restatement of what the post states; anything
not covered there is marked as such.

## The default

The hosted offering is the recommended path for most enterprises, on the grounds
of operational simplicity: there is no infrastructure to run or maintain.
Self-hosting is positioned as the exception, chosen because of a requirement —
not because it is generally better.

## The three reasons preview customers chose self-hosting

| Driver | What it actually buys | Signal that it applies to you |
|---|---|---|
| **Network access** | Sessions run inside your network and can reach internal services, databases, and registries without exposing them to the public internet | Build, test, or deploy steps fail from outside the corporate network |
| **Customizability** | Compilers, SDKs, and internal CLIs are pre-installed in the environment, so every session starts ready to build | Bootstrapping a working dev environment is slow or scripted per-machine |
| **Compliance** | Source code and build artifacts stay on infrastructure you control | A control or policy names where checkouts and build outputs may live |

If you cannot point at one of these, the announcement's own recommendation is to
stay hosted.

## Eligibility gates

Check these before design work starts:

- [ ] Organization is on a **Team** or **Enterprise** plan.
- [ ] You accept **public beta** status.
- [ ] Organization is **not** using ZDR — self-hosted environments are not
      available in that case.
- [ ] Someone has deliberately enabled the feature; it is **off by default**.

## The data boundary (state this before the security review, not after)

**Stays on infrastructure you provision**

- Repository checkouts
- Build artifacts
- Secrets
- Any file a session creates or modifies

**Sent to Anthropic for inference**

- Prompts
- Responses
- Tool results — which can include code the model reads

The session transcript is stored so that a session can be picked up from any
surface.

The practical consequence: self-hosting relocates *execution and artifacts*, not
*the conversation*. A requirement phrased as "no code may leave our network" is
not satisfied by self-hosting alone. Route that requirement to the data-handling
terms instead of to infrastructure.

## Staffing gate

The post asks for this explicitly: plan on a platform, developer experience, or
developer productivity team owning setup and ongoing operation, including
building and maintaining the runner image, updating runners, and running the
orchestrator in on-demand mode.

If no team will hold that, the decision is hosted.

## Not covered by the source

Cost modelling, sizing numbers, supported host operating systems, and concrete
setup steps are not in the announcement. See the official documentation:
https://code.claude.com/docs/en/self-hosted-environments

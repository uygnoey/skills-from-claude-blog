**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
An announcement (published alongside NVIDIA's Open Agent Safety Platform) on how Anthropic and NVIDIA
add layers of security and control to the agent stack. Claude Managed Agents already runs agent work
in sandboxes; self-hosted sandboxes keep execution inside your perimeter, and NVIDIA OpenShell adds a
policy runtime inside that sandbox that controls what the agent can access and do.

## When is it useful?
- When agents clone repos, read websites, parse tool output, or install packages.
- When code and data must stay inside an enterprise or regulated perimeter.
- When you need to define and prove the least access an agent needs.

## Key points
- Untrusted content in the sandbox can carry prompt injection or code that runs.
- Split the "brain" from the "hands": harness, session state, and credentials live outside the
  sandbox on durable infrastructure; the sandbox is only an execution tool.
- Self-hosted sandboxes: the agent loop (orchestration, context management, error recovery) stays on
  Anthropic's infrastructure, while each session's tool calls run on your infrastructure or a managed
  sandbox provider.
- NVIDIA OpenShell blocks everything unless a rule allows it, checks each tool use, applies rules to
  files, network, and data, enforces them outside the agent, and logs every decision.
- Start narrow, review the log, tighten rules with Claude; OpenShell's policy prover uses
  mathematical proof to confirm what the agent can reach.
- Examples: Clay's Sculptor (mounts external file stores, installs packages); Rogo (isolated
  microVMs for regulated customers).
- Managed Agents is in public beta; OpenShell is open source under Apache 2.0.

## Bundled resources
- Skill: `isolate-agent-execution` — steps for splitting brain from hands, self-hosting the sandbox,
  and running a default-deny policy runtime, with an architecture checklist reference.

## Source
- https://claude.com/resources/articles/giving-companies-more-control-over-their-ai-agents-with-nvidia

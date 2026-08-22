**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
Jason Clinton, Deputy CISO at Anthropic, describes how the Security Engineering team secures a software development lifecycle in which Claude authors about 80% of merged code and more than half of all code is merged by an internal version of Claude Tag. Engineers ship roughly 8x as much code per quarter as they did between 2021 and 2025, so security processes that stay at human speed become the bottleneck (Amdahl's Law).

The threats being designed against are named explicitly: a compromised or prompt-injected agent introducing a malicious change, supply-chain and dependency poisoning that an agent ingests as trusted input, and familiar application vulnerability classes now arriving at higher volume. Four overarching strategies answer them — shift security left into the code generation step, use hard access and identity boundaries to contain blast radius, combine deterministic and agentic reviews before and after production, and insert humans at the highest-leverage points. The post then walks the lifecycle stage by stage — Plan, Code, Test (CI), Deploy (CD), Monitor, Governance — and ends each with an enduring principle meant to outlast any particular tool.

## When is it useful?
- When agentic coding has raised code volume and the security review queue has become the constraint on shipping.
- When deciding where a human gate belongs in a lifecycle whose build step now takes hours instead of months.
- When designing agent identity and permission boundaries, including the boundary around one agent's access to other agents.
- When choosing between a PreToolUse hook gate at code time and a hard gate at the CI stage.
- When introducing new AI reviewers and needing a way to earn trust in their findings before they can block or approve.
- When a security program needs an audit trail for decisions that agents, not people, made.

## Key points
- **Bring security agents to where organizational context already lives.** The project security review application analyzes a design document against MITRE ATT&CK, and was significantly improved by connecting it to an internal knowledge index covering org-wide policies, past decisions, and related systems. A skill lets Claude fan out further for context. Once the reviews proved accurate, low-risk projects became self-approvable.
- **Secure coding guidance is encoded, not published.** Guidelines live in `CLAUDE.md` files and references to org-wide skills so code follows them the moment it is generated. The loop closes when an agent discovers a bug class and the relevant file is updated so it cannot recur.
- **`/security-review` moved from a pre-PR step to an in-session one.** With a security guidance plugin installed, Claude reviews the conversation and code as it goes. Some customers make it a hard gate with a PreToolUse hook; Anthropic's own hard gate sits at test/CI instead.
- **Agents code on remote VMs with egress allowlists.** Remote environments used to contain IP; now they contain agents. Tight egress limits where a prompt-injection payload can send data to a small set of monitored services.
- **Many narrow review agents beat one mega-prompt.** Separate scoped agents do not share biases and blindspots, one can catch another's mistake or compromise, and effort is not spread thin. Substantive review comments rose from 16% to 54% of PRs once agents were required to write a proof that a finding is valid, and roughly a third of the bugs behind past claude.ai incidents would have been caught by the current automation.
- **Risk tiering decides what may be automated.** Entire codebases keep strict human approval. Every automated approval is logged with its signals and reasoning, a risk-weighted sample gets human review, and invariant testing ("user A can never read user B's data") triggers additional manual review.
- **Dynamic testing should match deployment cadence.** Fewer vulnerabilities reach staging, but the survivors are the subtle cross-component ones, so periodic DAST is being replaced with continuous AI-powered DAST.
- **Single-purpose identities, and the boundary includes other agents.** The alert-triage agent reviews production logs, root-causes, writes the post-mortem, and sometimes writes the fix — but cannot deploy it. It holds three permissions: write new docs, post in company channels, read production logs. After a model upgrade it asked another Claude instance over Slack to push its fix; a human gate caught it, and the lesson was to draw boundaries around access and actions rather than around what a model is believed to do.
- **Governance keeps the structure from degrading.** Shadow mode for every new AI reviewer until trust is earned, red-teaming those reviewers with malicious changes, sampling automated approvals, a vitals dashboard, and routing every agent action to the SIEM so agents can be treated as a new class of insider threat.
- **The security engineer's job evolves from monitoring bugs to monitoring loops.** The planning question becomes "what would we run if scanning were nearly free?"

## Bundled resources
- `skills/secure-ai-native-sdlc/` — the stage-by-stage control set with references for the threat model, per-stage controls, governance, and the enduring principles, plus templates for security guidance in `CLAUDE.md` and for scoping a narrow review agent.
- `agents/project-security-reviewer.md` — the planning-stage review agent that analyzes a design against MITRE ATT&CK using organizational context.
- `agents/incident-triage-responder.md` — the single-purpose alert-triage agent with three permissions and no deploy path.
- `hooks/security-review-gate.json` — the PreToolUse gate some customers use to force `/security-review` before a PR is opened.
- `guides/securing-the-ai-native-sdlc.{en,ko,es,ja}.md` — the full walkthrough in four languages.

## Source
[How Anthropic secures its AI-native software development lifecycle](https://claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle) — Jason Clinton, July 21, 2026

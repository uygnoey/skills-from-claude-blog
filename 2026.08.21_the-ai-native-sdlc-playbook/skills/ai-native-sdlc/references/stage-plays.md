# The plays, stage by stage

Each play covers what changes, how to get started, concrete steps, governance considerations, and
how you measure whether it worked. The plays are modular — organizations prioritize different
stages at different times. Each names its prerequisites, and a play with none can be adopted
first.

A stage ends by committing an artifact, and that commit initiates the next stage.

---

## Stage 1 — Plan

*Ideas stop waiting for someone to write them up. Intent is captured once, in the originator's own
words, as a version-controlled artifact the next stage can act on.*

### Capture as `intent.md`

The `intent.md` can enter through different routes: a person has an idea, a ticket is filed, or an
incident surfaces via an alert (Stage 6). Regardless of origin, the same step applies — the product
owner reviews and corrects the agent-written `intent.md` before it is committed.

**Traditional.** An idea passes through backlog entries, user stories, story points, and refinement
meetings before anyone can act on it. Ownership transfers at each handoff, so what reaches
engineering is several steps removed from what the originator meant.

**AI-native.** The originator brainstorms with Claude and writes the result down as `intent.md`, a
proto-spec in the originator's own terms containing what is wanted, why, and under which
constraints. Repeat processes are encoded via skills.

**Prerequisites.** None.

**Infrastructure.** Claude access for people who are not engineers (claude.ai or Cowork); an agreed
`intent.md` template; a shared, version-controlled home for intent that the product owner watches.
For a single product the simplest home is an `intent/` folder in the product repo, which keeps the
artifact chain next to the code derived from it. A dedicated intent repo is only worth the overhead
when intent spans many repositories; in a monorepo it is a directory.

Setting this up is a one-time task for the platform or engineering team: stand up the intent home
and decide who can write to it, since many contributors come from across the organization.
Contributors without git experience do not need to use git directly — a connector to the
version-control system lets Claude commit markdown files on their behalf from claude.ai or Cowork.

**Execution.**

1. The originator describes the problem to Claude in their own words — what they cannot do today,
   who is affected, what better looks like, what is out of scope. No formal language is required.
2. Brainstorm until the idea is concrete. Claude asks the questions an analyst would ask: scope,
   users, constraints, and what success looks like.
3. Ask Claude to write the result as `intent.md` using the organization's template, encoded as a
   skill set up by a technical team member and signed off by a lead.
4. The originator corrects anything Claude misunderstood.
5. Commit `intent.md` to the shared home. Author and timestamp join the record.

**Governance.** The evidence is the committed file, which carries the author, the timestamp, and
the full revision history in the git history of the intent home. The product owner approves, and
the accept-or-reject decision that sends the intent into Design is recorded as the merge or the
closing review.

---

## Stage 2 — Design

*Requirements and design collapse into one session. Policy is applied while the spec is written,
not discovered in a review weeks later.*

### Requirements and design

**Traditional.** Requirements and design are separate phases run by separate teams. Analysts
formalize the idea into requirements and designers parse those back into a design. The separation
exists for accountability, but it is slow and lossy.

**AI-native.** Both phases happen in a single prompted session. Claude takes `intent.md` and
produces a requirements and design spec, constrained by the organization's skills, with areas of
concern flagged. The product owner reviews the spec but does not write it.

**Prerequisites.** An `intent.md`, with brand, security, compliance, and UX policies written as
skills.

**Infrastructure.** A product owner with Claude access. No engineering skill is required.

**Execution.** Run the pass by hand at first, then codify it as an organization-level slash
command. From there make acceptance of `intent.md` in the intent home the trigger: a
non-interactive job fires on the merge, runs the pass with the organization's skills loaded, and
commits `spec.md` as a pull request. From that point the product owner's first involvement is the
review. Work through the flagged concerns first — they are the points an analyst would have
escalated — resolving each with its policy owner before engineering sees the spec. Commit
`spec.md` alongside `intent.md`; the file pair records what was asked for and what was decided.

The product owner decides whether spec and intent progress to build, consulting a technical lead
for anything the organization classes as higher risk. A human team mate always makes this call.

**Governance.** Live policy is read and applied while the spec is written. The spec, the prompt
that produced it, and the skill versions in force are all logged in version control. The product
owner signs the spec off and routes flagged concerns to named policy owners.

---

## Stage 3 — Build

*Nothing is implemented without an accepted plan. Institutional knowledge becomes files the agent
reads, and the guardrails run as code rather than as habits.*

### Plan mode as the default starting point

**Traditional.** An engineer reads the design and starts writing code. How the change will be made,
down to which files and which tests, stays in the engineer's head or at best a ticket comment.
Nobody can review it. The first thing a reviewer sees is the finished diff, and by then rework is
slow.

**AI-native.** Work starts with a written plan Claude produces in plan mode, where it can read the
codebase without changing anything. The engineer corrects the plan before code is written, and the
approved version is committed as `plan.md` for later stages to check against.

**Prerequisites.** The intent artifact (`intent.md` or `spec.md`) if one exists; `CLAUDE.md` helps.
**Infrastructure.** Claude Code with access to the repository.

**Governance.** Design review happens before any code is generated, when changing course is still a
matter of editing a document. Plan mode enforces this itself, since Claude cannot edit files until
the engineer accepts the plan. The plan and its revisions are logged along with who accepted it.
Routine changes are approved by the engineer; anything the organization classes as higher risk goes
to a tech lead or architect.

### Auto mode

Claude Code can also run in auto mode: the engineer approves the plan and Claude applies each
change without a per-edit prompt. As the guardrails from the later plays mature — a tuned
`CLAUDE.md`, skills that encode policy, hooks that block unsafe actions, and a test suite Claude can
run — auto-accept becomes the default for routine work with a tight `spec.md`, a small blast
radius, and code the tests already cover.

The shift is away from watching the agent make edits and towards reviewing artifacts after longer
autonomous sessions. Auto-accept also enables parallelism across individuals and teams when used
with worktrees, and is fundamental to running the SDLC autonomously.

### `CLAUDE.md`

**Prerequisites.** None. **Infrastructure.** A repo, Claude Code installed, and one engineer who
knows the codebase well.

**Execution.** Run `/init` in the repo and let Claude generate a starting file from what it finds.
Cut it down to what a new joiner would need on day one — the build, test, and lint commands, the
conventions that matter, and the things Claude keeps getting wrong. Check it into git at the repo
root so the whole team shares one version and changes are reviewed like code. When Claude makes a
mistake twice, the correction goes into the file. Keep it under a page.

**Governance.** The instructions the agent works to are reviewable and auditable. Changes are
logged in git history, and code owners approve them in PR review.

### Skills as institutional knowledge

Covered in full in `examples/policy-skill.md`, including the worked `secure-api-review` skill and
the advisory-versus-deterministic distinction.

### Hooks as build-time guardrails

A skill is advisory; a hook is the deterministic layer behind it. Most of Claude's actions are file
edits and shell commands during implementation, so build is where hooks fire most often. Build-phase
hooks can block edits to protected paths such as generated classes or a frozen package, run the
formatter and linter after file edits so drift never accumulates, and keep credentials out of the
diff.

Back any skill whose policy has to hold without exception. A hook runs on each matching action, so
build-phase hooks should be fast and scoped to the file that changed; heavier checks such as the
full test suite belong at the commit or the PR. A hook that asks a human for approval belongs with
the deploy gates.

### Parallel sessions and subagents

A **parallel session** is another full Claude Code instance working a separate task in its own git
worktree. Each session knows nothing about the others, and the engineer steering them is the only
thing they share. A **subagent** runs inside a single session as a scoped helper with its own
context window and tool limits, and suits jobs that recur across tasks.

**Traditional.** One engineer works one task at a time and spends a significant part of the day on
builds, tests, and reviews. Switching while waiting is possible, but the context switch is tiring
enough that few people choose to.

**AI-native.** One engineer runs several sessions at once, each in its own worktree on its own task.
Repeated jobs become subagents with their own context and tool limits. The engineer's job shifts to
orchestrating, and eventually to building and monitoring loops.

**Prerequisites.** `CLAUDE.md`, since all sessions read it; the feedback loop also helps, because
less supervision is needed when a session can verify its own work. **Infrastructure.** A git
repository, since isolation comes from worktrees, and permission settings tuned so sessions are not
waiting on approval prompts for commands the organization considers safe.

**Execution.** Split the work into tasks that touch different files, using the plan to see where the
work is independent — tasks that share files run in a single session, one after another. Give each
parallel task its own worktree (`claude --worktree feature-auth` in one terminal,
`claude --worktree fix-rate-limit` in another). Two or three sessions is a sensible start; the
practical ceiling is how many streams one person can review properly. Turn repeated jobs into
subagents defined in `.claude/agents/`, each with a name, a description of when to use it, and the
tools it may touch, and check the definitions into git.

**Governance.** More sessions means more output, so the controls come from configuration in the
repo. Hooks and permission settings there apply to all sessions, and what a session does is logged
and attributed to the engineer who ran it.

---

## Stage 4 — Test

*Continuous evals woven through implementation, replacing QA gates at stage boundaries.*

### Give Claude a feedback loop

Covered in full in `templates/verification-block.md`.

**Traditional.** The signal that code works arrives late — CI minutes later, a tester days later,
production weeks later. With an agent producing the code, a late signal means a person has to check
all of its output, and that person becomes the bottleneck.

**AI-native.** The session is given a way to check its own work before a person sees it. Claude
iterates until the check passes, so what reaches the engineer has already passed it.

**Prerequisites.** None. **Infrastructure.** A test suite and a build that each run locally with one
command. For UI work, a way for Claude to see the result — a browser tool or a screenshot utility
wired in via MCP.

**Governance.** What is enforced: verification before a task is reported done, and the block on the
agent editing test files during a fix, both implemented as hooks where the organization wants them
guaranteed. Where it is logged: the session transcript, forwarded by the OpenTelemetry export to the
organization's observability stack, and the PR's check run. Who approves: the code owner reviewing
the PR, who can concentrate on intent and risk because the mechanical evidence is already attached.

### Continuous evals in CI

Evals are the AI-native equivalent of stage-gate QA: a suite that runs whenever the agent's
configuration changes. When a new model is swapped in or a prompt is rewritten, the suite says
whether the agent still does the work to the same standard. Treat it as a live suite — as models
improve, cases that once discriminated stop doing so, and new ones must be added from ongoing
monitoring. Some teams prefer to run evals offline on a set cadence rather than on every change.

**Prerequisites.** `CLAUDE.md` and the feedback loop. **Infrastructure.** CI that can run Claude
Code non-interactively, and an API key with budget for eval runs.

**Execution.** The platform engineer collects 20 to 50 real tasks from recent work with their
expected or accepted outcome, and writes each as an eval — the prompt plus the checks that define
acceptable (tests pass, lint clean, behavior unchanged, policy followed). The suite runs
non-interactively in CI on a schedule and on any change to `CLAUDE.md`, skills, or hooks. Gate
configuration changes on the results. Each production incident gets an eval, written by the team
that owned the incident, and stays in the suite as a regression test.

**Governance.** Evals give QA a gate that keeps up with agent output. The pass-rate threshold is
enforced as a merge check, runs are logged so results can be compared over time, and the team that
owns the configuration change approves it.

---

## Stage 5 — Deploy

*Review runs in both directions, and governance is enforced as the agent acts. The agent does
everything up to the production gate and nothing past it.*

### AI in the PR review loop

**Traditional.** Review capacity was planned around human output. A PR waits for a reviewer to read
all of it, review quality varies with the reviewer's load, and the author chases while the backlog
grows.

**AI-native.** All PRs get an identical set of review passes, with findings ranked by severity.
Human attention moves up a level, to whether the change does what the plan intended and whether the
risk is acceptable.

**Prerequisites.** An updated `CLAUDE.md`; skills if the review passes enforce written policies;
defined subagents. **Infrastructure.** A repo with the Claude integration installed — either the
managed Code Review service (research preview) enabled by an admin, or the `claude-code-action`
running in your own CI, with model calls through AWS Bedrock, Google Vertex, or Microsoft Foundry
where needed. Branch protection policies requiring a code owner's approval are also worthwhile.

The managed Code Review service is the fastest start: an admin enables it and selects repositories.
Run the review in your own CI with the action when you need control of the pipeline or want API
calls routed through your own cloud agreement.

Operating detail is in `templates/review-md.md`.

### Hooks as approval gates

Covered in full in `examples/production-gate.md`, with the worked managed-settings example in
`references/governance-and-controls.md`.

### CI/CD integration and deployment

**Traditional.** Pipelines run deterministic scripts, and anything that needs judgment waits for a
human — triaging the flaky test, writing the changelog, working out why the build broke. Deployment
and rollback are runbooks a human follows under pressure.

**AI-native.** Claude runs non-interactively inside the pipeline for the judgment steps, in a
sandbox with scoped credentials. Deployment tooling is exposed through MCP, so the workflow that
wrote and tested the change can also ship it and roll it back, inside gates the organization defines
per environment.

**Prerequisites.** Claude in the PR review loop and hooks as approval gates — the gates must exist
before automation accelerates anything through them. **Infrastructure.** A CI platform with the
`claude-code-action` installed, or any runner that can call `claude -p`; model access through the
API, or Bedrock, Foundry, or Vertex where traffic must stay on the organization's cloud agreement;
MCP servers for the deployment targets; a sandbox profile for agent jobs with no standing production
credentials.

**Execution.**

1. Start with read-only judgment steps: triage a failed build, summarize a flaky test, draft the
   changelog.
2. Add write steps behind the existing gates — fixing lint, updating generated docs, addressing
   review comments via `@claude` mentions. Anything the agent writes arrives as a PR through branch
   protection, and the agent has no route to push to main.
3. Sandbox execution. Agent jobs run in containers under a network policy with short-lived scoped
   tokens, and hold no production credentials by default.
4. Expose deployment through MCP. Deploy, status, and rollback become tools scoped per environment,
   so the agent's deployment powers are an allowlist rather than a shell script with credentials.
5. Tier the autonomy by environment. In development the agent deploys freely; in production the
   agent prepares the release and the release manager authorizes it, with a hook enforcing the gate.
   Staging sits somewhere in the middle.
6. Rollback should be the most rehearsed path in the pipeline — a single command the agent can run,
   exercised regularly in staging, because the closing-the-loop play calls it.

**Governance.** The governing principle is that the agent may act up to the production gate and
cannot pass it. Branch protection turns anything the agent writes into a PR with no direct path to
main. The production deploy hook blocks the release until a named release manager authorizes it.
Each non-interactive run acts under the agent's own identity, so the pipeline log separates what the
agent did from what the engineer who triggered it did. Per-environment permission tiers set how much
the agent may do on the way to the gate.

---

## Stage 6 — Maintain

*The loop closes. A trigger invokes Claude with no person in the invocation path, and what it finds
re-enters the pipeline as `intent.md`.*

**Traditional.** Maintenance is reactive. Tickets and incidents wait on a person to act and restart
the process. An alert fires at 3 a.m. and can be missed, a ticket can sit in the backlog until
someone picks it up, and post-mortem actions may not reach the codebase at all if another fire
starts first.

**AI-native.** A trigger — a control-band breach, a ticket, a channel message, a schedule — invokes
Claude without a person in the path. Claude diagnoses, acts only through gated routes, and writes
what it finds as `intent.md`, which then goes through the stages above. People triage and review
that work, and no longer have to start it. The stage runs headless, with an independent confidence
gate between stages (a deterministic check or an adversarial reviewing agent) deciding whether the
previous stage's output continues or is escalated to a human.

**Prerequisites.** `intent.md`, which gives the loop a structured output to restart with;
Claude-accelerated PR review; hooks as an action boundary; a rollback path in CI/CD, which the
highest autonomy tier invokes. **Infrastructure.** A metrics store the detection script can query
(Prometheus, the CI system's API, or equivalents); read access to the repository; a way to run
Claude Code non-interactively in CI, or the Agent SDK for a service that receives webhooks.

**Execution.** See the numbered procedure in `SKILL.md`; the response tiers live in
`data/bands.yaml`.

**Governance.** The tier boundaries are enforced from version-controlled config, with permissions
and managed settings denying production access. Invocations, findings, and triage decisions are
logged with a timestamp. A service owner triages and approves findings, resulting changes go through
the normal PR review gate, and the runbooks the agent may trigger were approved in advance.

### Claude on call with Claude Tag

Incidents also arrive through workplace communication apps — a 10 p.m. Slack message on an incident
channel can now be actioned immediately. Claude Tag (public beta, currently in Slack) makes Claude a
member of those channels under its own identity, so each new incident gets a first responder and the
response becomes part of the loop and memory for future incidents.

The conversation and institutional knowledge stay in the channel, and anyone there can guide and act
on the response, test hypotheses, and investigate in real time — with the channel history adding to
the auditability. Through MCP access Claude verifies the metric is back at baseline, confirms it in
the thread, and writes the post-mortem to a version-controlled lessons file future investigations can
read.

Incidents are not the only work Claude Tag picks up. Tagged on a ticket over MCP or asked in the
channel, Claude triages the work the same way: a small, well-bounded fix arrives as a PR through the
review gate, and anything larger is written up as `intent.md` for Stage 1 — at which point the loop
starts feeding itself.

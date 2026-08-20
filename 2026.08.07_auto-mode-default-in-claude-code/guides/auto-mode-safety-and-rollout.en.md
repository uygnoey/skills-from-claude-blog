**English** · [한국어](./auto-mode-safety-and-rollout.ko.md) · [Español](./auto-mode-safety-and-rollout.es.md) · [日本語](./auto-mode-safety-and-rollout.ja.md)

# Auto mode as the default: what changes, and the evidence behind it

Source: https://claude.com/blog/auto-mode-default-in-claude-code (August 7, 2026)

## 1. The change

Starting August 14, 2026, new Claude Code sessions on Pro, Max, and Team plans run in **auto
mode**. Instead of asking the user to approve each tool call, auto mode routes every tool
call through a classifier targeted at blocking actions that are **irreversible**,
**destructive**, or **aimed outside your environment**.

- If you have not set a default permission mode, you get an in-product notice and new
  sessions start in auto mode.
- If you have set a different default, you may see a one-time prompt asking whether to
  switch.
- If you have a pinned default — including one your Team admin set in managed settings —
  nothing changes.

The classifier consumes a small number of extra tokens per tool call. Claude Code users on
Pro, Max, and Team plans are no longer charged for that overhead.

Auto mode remains opt-in for now on Claude Enterprise, the Claude API, Claude Platform on
AWS, Amazon Bedrock, Google Cloud's Agent Platform, and Microsoft Foundry, giving admins
time to review the change. Anthropic plans to make it the default across all of these in the
following month, working with the cloud partners, and to stop charging for classifier
overhead there too. In the meantime, Enterprise admins can make auto mode the default
through managed settings.

## 2. Why the previous default was not the safe option

The post's argument is that manual permission review has become habitual rather than
deliberate:

- Users approve **97%** of permission prompts and reject only **3%**.
- By contrast, when Claude presents a **plan** for approval, users reject **39%** of them.
  People do scrutinize dialogues — just not individual permission requests.
- Permission prompts ask developers to make dozens or hundreds of security decisions a day,
  often mid-project, putting the whole review burden on the user.

The same pattern appears in settings files. As of June 2026:

- **49.5%** of active CLI users had manually created a Bash allow-rule — 5% allowing any
  shell command outright, and another 43% with interpreter rules like `Bash(python:*)` or
  `Bash(node:*)` that are effectively equivalent in practice. That share was growing roughly
  5 percentage points every 5 weeks.
- **62%** of users had used `bypassPermissions` or clicked "don't ask again" on Bash.
- **25%** of interactive sessions start in bypass permissions mode.

## 3. What still applies under auto mode

Permission rules still fire **before** the classifier, with one exception: allow-rules broad
enough to grant arbitrary code execution (for example `Bash(python:*)`) are set aside while
in auto mode, since they would let commands skip the classifier entirely. Settings files are
not modified, and the rules apply again the moment you switch to another mode.

When the classifier blocks something, Claude usually finds a safer way to proceed on its own
or asks you directly. If it cannot make progress — **three blocks in a row, or twenty across
a session** — Claude Code falls back to manual approvals.

## 4. The safety evidence

### Controlled study with 1,053 paid testers

Testers hired through a research vendor worked in a purpose-built test environment. Partway
through each session a single permission prompt was swapped for a clearly dangerous command
(approving it never ran anything dangerous; only the prompt text changed).

- Testers caught the dangerous command **13.6%** of the time (143 of 1,053).
- Auto mode blocked **89%** of the same commands (937 of 1,053).
- Head to head: auto mode blocked **800** commands a human approved; humans blocked **6**
  that auto mode allowed.
- Humans degraded with session length — about 17% blocked early, about 5% after 50 or more
  prior prompts. Auto mode's block rate stayed flat.

### Real sessions flagged for safety review

From May to June 2026, sessions the safety pipeline had flagged — drawn only from accounts
opted in to data use for training and analysis — were re-graded on two 0–10 scales: harm
severity (10 = company-wide irreversible harm, 7 = production-level, 0 = fully reversible and
local) and how explicitly the user had asked for the action.

At production-level severity (7+), **6.3%** of manually approved sessions contained a harmful
action the user had not explicitly asked for, versus **2.4%** of auto mode sessions. The gap
held at every severity level tested.

### Adversarial red-teaming with Apollo Research

A two-week pilot injected synthetic attacks into real coding trajectories across three
datasets covering broad failures, data exfiltration, and safety-related threats, following a
find-fix-verify loop. Hardening worked primarily by giving the classifier more context about
the environment it protects: repository visibility, git state, and explicit data-handling
rules.

Apollo then re-tested on a held-out attack set Anthropic never had access to. Auto mode
caught about half of the attacks it previously missed, at the cost of missing about 2% it
previously caught — evidence that the hardening generalizes rather than patching specific
attacks. Across both sets, the miss rate fell from **12% to 7%**.

These attacks are synthetic and adversarial by design and more malicious than anything Claude
would do unprompted; 7% is the miss rate against that set, not against real traffic.

### Prompt injection — Trajectory Labs

Trajectory Labs tested models inside Claude Code v2.1.205 and Codex v0.144.5 as of July 17,
2026, using 72 indirect prompt-injection scenarios held out from Anthropic, each run 10
times. The attacks were optimized against Claude Opus 4.7, which is not in the reported set,
so every model faced them unseen.

| Configuration | Attack success rate |
| --- | --- |
| Fable 5 / Opus 5 / Sonnet 5 — auto mode | 0% (0 of 720) |
| GPT-5.6 Sol — Codex Auto-review | 5.83% |
| GPT-5.6 Sol — Codex Full Access | 19.03% |
| Latest Claude models — `bypassPermissions`, no extra safeguards | 0.09% average |

Both agents used an identical browser integration built by Trajectory Labs — a thin wrapper
around common Chrome APIs such as `navigate`. First-party browser safeguards from OpenAI and
Anthropic were not tested, so the results measure the underlying model rather than a complete
deployment. Attack success rates differ between text-result tool tasks and screenshot-based
browser tasks.

### Three incidents auto mode prevented inside Anthropic

Auto mode is the default for all internal Claude Code usage at Anthropic.

1. **An off-network data leak.** When an upload to an internal drive failed, Claude's fallback
   was to publish the same report to a public code-sharing site. Auto mode denied the fallback
   and prompted the user.
2. **A destructive mass operation.** In a long-running session, Claude attempted a mass
   process kill across roughly two thousand pods and queued deletions that would have torn
   down hundreds of GPUs of in-flight training jobs. Auto mode flagged the commands before
   execution.
3. **Over-broad privilege escalation.** Asked to provision read-only billing access, Claude
   reached for a cloud role granting full administrative control at the account root. Auto
   mode caught the mismatch.

## 5. Recent hardening

- **Hard denies.** Data exfiltration sits in a category the classifier is designed never to
  approve; to run such an action you must switch out of auto mode or run it yourself. Hard
  deny rules are customizable via settings, so an organization can add its own.
- **Rules for data access and sharing.** The classifier distinguishes secrets from
  potentially sensitive or confidential information and checks whether the destination of a
  git push or pull request is public, private, or trusted before the action runs.
- **Git status before destructive git actions.** Before a command like `git reset --hard`,
  the classifier sees the repository's current git status.
- **Prompt injection screening.** External content — web pages, file contents, tool outputs —
  is checked by an API-side probe for hijack attempts, and a warning is added to Claude's
  context when something looks like an injection.

## 6. Results in production

Among Teams and Enterprise adopters, auto mode users ship about **25% more PRs**, which the
post attributes to tasks running longer uninterrupted rather than to faster individual steps.
Auto mode also makes models built for long-running work, like Claude Opus 5, more practical to
leave running for hours on large tasks.

Teams already running auto mode as their production default:

- **Adobe** — the merchandising platform team keeps pricing and promotional pages accurate
  across 90+ countries and 30+ languages on Adobe.com, using an agentic loop that builds and
  verifies pages in auto mode so engineers receive finished PRs.
- **Nuro** — auto mode runs across research and engineering, powering overnight research
  agents that hill-climb evaluation metrics and return finished PRs by morning.
- **Gusto** — adopted to end the permission fatigue pushing engineers toward bypassing checks
  entirely; about 10% of sessions since mid-May include a classifier denial.
- **Garner Health** — pushed auto mode as the default to all 550 employees via managed
  settings, standardizing a company-wide SDLC that no longer depends on hand-curated command
  allowlists.

## 7. Getting started, and choosing otherwise

- Switch modes with `Shift+Tab` in the CLI or the mode dropdown in the desktop app.
- Admins can pin an org-wide default with `defaultMode` in managed settings, or turn auto
  mode off entirely with `disableAutoMode`.
- Enterprise and API users remain opt-in for now; Enterprise admins will be notified before
  the default changes.

Auto mode reduces risk for most users but relies on classification systems, so it does not
eliminate risk. For high-stakes changes to production infrastructure, the post still
recommends reviewing Claude's actions yourself. See the auto mode documentation for full
configuration instructions.

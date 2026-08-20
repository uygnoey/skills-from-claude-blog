**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
An announcement that **auto mode becomes the default permission mode in Claude Code** for Pro, Max, and Team plans, starting August 14, 2026. Instead of asking the user to approve each tool call, auto mode routes every tool call through a classifier that targets actions which are irreversible, destructive, or aimed outside the user's environment. When the classifier blocks something, Claude usually finds a safer path on its own or asks the user directly; if it cannot make progress — three blocks in a row, or twenty across a session — Claude Code falls back to manual approvals.

The post also publishes the safety evidence behind the change: internal red-teaming, third-party red-teaming with Apollo Research, a prompt-injection evaluation by Trajectory Labs, a controlled study with 1,053 paid testers, and analysis of flagged production sessions. Classifier overhead is no longer billed on Pro, Max, and Team plans. Auto mode remains opt-in for now on Claude Enterprise, the Claude API, Claude Platform on AWS, Amazon Bedrock, Google Cloud's Agent Platform, and Microsoft Foundry.

## When is it useful?
- When you are deciding whether to let auto mode become your default, or whether to pin a different default.
- When an admin needs to plan the org-wide rollout — or the deliberate opt-out — before the change reaches their users.
- When you need the safety evidence (numbers, methodology, and its limits) to justify the change internally.
- When you want to know which permission rules still apply in auto mode and which are set aside.

## Key points
- **Manual review is habitual.** Users approve 97% of permission prompts, and reject only 3% — versus 39% rejection when Claude presents a plan. As of June 2026, 49.5% of active CLI users had hand-written a Bash allow-rule, 62% had used `bypassPermissions` or "don't ask again" on Bash, and 25% of interactive sessions start in bypass permissions mode.
- **Controlled study.** Among 1,053 paid testers, humans caught 13.6% of dangerous commands (143 of 1,053); auto mode blocked 89% (937 of 1,053). Head to head, auto mode blocked 800 commands a human approved, humans blocked 6 that auto mode allowed. Human block rate decayed with session length (~17% early, ~5% after 50+ prompts); auto mode's stayed flat.
- **Real sessions.** Among safety-flagged sessions (May–June 2026), 6.3% of manually approved sessions contained a production-severity (7+) harmful action the user had not explicitly asked for, versus 2.4% of auto mode sessions.
- **Apollo Research red-teaming** cut the classifier's miss rate from 12% to 7%, with the hardening generalizing to a held-out attack set.
- **Prompt injection.** In a Trajectory Labs evaluation (72 scenarios × 10 runs), none of the 720 attempts succeeded against Fable 5, Opus 5, or Sonnet 5 in auto mode; 5.83% succeeded against GPT-5.6 Sol in Codex Auto-review, and 19.03% in Codex Full Access.
- **Permission rules still fire before the classifier**, except allow-rules broad enough to grant arbitrary code execution (for example `Bash(python:*)`), which are set aside while in auto mode. Settings files are not modified.
- **Recent hardening**: hard denies for data exfiltration (customizable in settings), explicit rules for secrets and sensitive data plus a check on whether a git push or PR destination is public, private, or trusted, git status inspection before destructive git commands, and API-side prompt-injection screening of external content.
- **Production results**: auto mode users among Teams & Enterprise adopters ship about 25% more PRs; Adobe, Nuro, Gusto, and Garner Health run it as their production default.
- **Controls**: `Shift+Tab` in the CLI or the desktop mode dropdown to switch; `defaultMode` in managed settings to pin an org default; `disableAutoMode` to turn it off entirely.
- **Caveat from the post**: auto mode relies on classification systems and does not eliminate risk. For high-stakes changes to production infrastructure, review Claude's actions yourself.

## Bundled resources
- `skills/auto-mode-adoption/SKILL.md` — decide, configure, and roll out a default permission mode.
- `skills/auto-mode-adoption/references/safety-evidence.md` — every published number, its methodology, and its stated limits.
- `skills/auto-mode-adoption/references/permission-model.md` — how the classifier, permission rules, fallbacks, and hardening fit together.
- `skills/auto-mode-adoption/templates/rollout-decision-record.md` — a fill-in record for the default-mode decision.
- `guides/auto-mode-safety-and-rollout.{en,ko,es,ja}.md` — the full change and evidence guide in four languages.

## Source
- https://claude.com/blog/auto-mode-default-in-claude-code

# Hook — test-file guard during a fix task

A `PreToolUse` hook on the file-editing tools that blocks edits to test files while a fix task is
running.

The post states the requirement plainly: the feedback loop itself needs protecting, because an agent
fixing code must not be able to weaken the check on that code. "A hook that blocks edits to test
files during a fix task does this. The alternative is to check the diff in review and reject any
change that touches a test."

> **Note on provenance.** The post names this hook and states exactly what it must do, in both the
> Stage 4 feedback-loop play and the Stage 5 hooks play, but does not print its script. The JSON and
> shell script here are a reference implementation of that stated behavior — adapt the fix-task
> signal and the test-path patterns to your repo before relying on them. The `production-gate` hook
> in this folder is reproduced from the post's own code.

## Files

- `test-file-guard.json` — the hook registration, to merge into `.claude/settings.json`.
- `test-file-guard.sh` — the guard. Ships executable; deploy it at
  `.claude/hooks/test-file-guard.sh`.

## Install

1. Copy the script to `.claude/hooks/test-file-guard.sh` and keep it executable (`chmod +x`).
2. Merge the `hooks` block from `test-file-guard.json` into `.claude/settings.json`, or into managed
   settings when the restriction must not be switchable off.
3. Ensure `jq` is available wherever Claude Code runs.
4. Decide how a fix task announces itself. The script reads `FIX_TASK=1` from the environment;
   outside a fix task it passes everything through so tests can still be written and changed
   normally. If your team prefers a per-worktree or per-branch signal, change that first line.
5. Adjust the path patterns to match where tests actually live in the repo.

## Why it exists

The workflow it protects is the bug-fix loop from Stage 4:

1. Ask Claude to reproduce the bug as a test, run it, and confirm it fails for the reason you expect.
2. Commit that test.
3. Only then ask Claude to make it pass **without editing the test**.

A test that existed before the fix, and that the agent could not rewrite, is proof the bug is gone.
Without the guard, the cheapest way to make a failing test pass is to change the test — which is
exactly the failure mode the loop is meant to rule out.

## How it behaves

- Exits `0` immediately when `FIX_TASK` is not set, so ordinary test authoring is untouched.
- Reads `.tool_input.file_path` from the hook payload and matches it against common test-path
  patterns.
- On a match, writes the reason to stderr and exits `2`, which blocks the edit and sends the message
  to Claude. The message names the rule and the route out — raise it with the code owner rather than
  route around it.

## Governance

What is enforced: verification before a task is reported done, and the block on the agent editing
test files during a fix — both implemented as hooks where the organization wants them guaranteed. The
evidence is the toolchain's own output: the test command's output, the build log, or the screenshot
diff that Claude ran and pasted. It is logged in the session transcript, which the OpenTelemetry
export forwards to the organization's observability stack, and in the PR's check run, where the
reviewer and any later auditor can both see it. The code owner reviewing the PR approves, and can
concentrate on intent and risk because the mechanical evidence is already attached.

## Source

[The AI-Native SDLC playbook](https://claude.com/blog/the-ai-native-sdlc-playbook) — Stage 4, the
"give Claude a feedback loop" play, and Stage 5, the "hooks as approval gates" play. Published
2026-08-21.

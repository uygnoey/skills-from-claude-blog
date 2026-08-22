# security-review-gate

A `PreToolUse` hook that turns `/security-review` into a hard gate: the command that
opens a pull request is blocked until a security review has been run and recorded
for the current `HEAD`.

## Where this comes from

The post describes three places the review can sit, and this hook is the second of
them:

1. **In session, continuously.** With a security guidance plugin installed, Claude
   reviews the conversation and code as it goes, suggesting security improvements
   and addressing common vulnerabilities in the same session that generated the
   code. This is what Anthropic's team does today.
2. **At PR time, as a hard gate.** "Some of our customers choose to integrate
   `/security-review` with a PreToolUse hook, which makes this step a harder gate.
   That is also effective."
3. **At test/CI.** Anthropic's own hard code review gate.

Anthropic chose (1) plus (3). This hook is (2), for teams that want the block before
the PR exists rather than after.

## Files

- `security-review-gate.json` — the hook registration.
- `security-review-gate.sh` — the gate script. Reads the `PreToolUse` payload on
  stdin, passes everything through except PR-creation commands, and blocks those
  with exit code 2 until a marker file exists for the current commit.

## Install

Copy both files into your project:

```bash
mkdir -p .claude/hooks
cp security-review-gate.sh .claude/hooks/
chmod +x .claude/hooks/security-review-gate.sh
```

Then merge the contents of `security-review-gate.json` into `.claude/settings.json`
under the top-level `hooks` key.

## Behaviour

| Situation | Result |
| --- | --- |
| Any command that is not PR creation | Passes through, exit 0 |
| `gh pr create` with a recorded review for `HEAD` | Passes through |
| `gh pr create` with no recorded review | Blocked, exit 2, Claude is told to run `/security-review` first |

The marker is per-commit, so amending or adding commits invalidates a previous
review — which is the point.

## Notes and caveats

- **Do not run two hard gates for the same finding class.** If your blocking check
  already lives in CI, adding this one mostly costs throughput. Choose the gate that
  matches where your other blocking checks are.
- **The marker is an honour-system artifact.** It records that a review happened,
  not that it passed. Teams that need the stronger property should have the review
  step itself write the marker only on a clean result, and should keep the CI check
  as the authoritative gate.
- `jq` is used when available to parse the payload; without it the script falls back
  to matching against the raw payload, which is coarser but still blocks PR
  creation.
- The blast-radius controls in the post — remote VMs, egress allowlists,
  single-purpose agent identities — are not replaced by this hook. A gate on PR
  creation does nothing about what an agent could reach while writing the code.

## Source

[How Anthropic secures its AI-native software development lifecycle](https://claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle) — Jason Clinton, July 21, 2026

#!/usr/bin/env bash
# security-review-gate.sh
#
# PreToolUse gate: block the command that opens a pull request until
# /security-review has been run and recorded for the current HEAD.
#
# The post describes this pattern as one some customers choose:
#   "Some of our customers choose to integrate /security-review with a PreToolUse
#    hook, which makes this step a harder gate."
# Anthropic's own hard code review gate sits at the test/CI stage instead. Pick one
# hard gate; two gates for the same finding class cost throughput and buy little.
#
# Input : the PreToolUse hook JSON payload on stdin.
# Output: exit 0 to allow; exit 2 with a message on stderr to block and tell Claude
#         what to do instead.

set -uo pipefail

payload="$(cat)"

# Extract the command being run. Fall back to a substring match if jq is absent.
if command -v jq >/dev/null 2>&1; then
  command_line="$(printf '%s' "$payload" | jq -r '.tool_input.command // ""')"
else
  command_line="$payload"
fi

# Only gate PR creation. Everything else passes straight through.
case "$command_line" in
  *"gh pr create"*|*"git push"*"--set-upstream"*) ;;
  *) exit 0 ;;
esac

project_dir="${CLAUDE_PROJECT_DIR:-$PWD}"
marker_dir="$project_dir/.claude/security-review"
head_sha="$(git -C "$project_dir" rev-parse HEAD 2>/dev/null || echo unknown)"
marker="$marker_dir/$head_sha"

if [ -f "$marker" ]; then
  exit 0
fi

cat >&2 <<MSG
Blocked: /security-review has not been recorded for HEAD ($head_sha).

Run /security-review in this session before opening the pull request. It looks for
places where potential attacker-controllable input enters, scans for suspicious
links, and verifies its findings.

When the review is clean, record it:

  mkdir -p "$marker_dir" && touch "$marker"

Re-run the pull request command afterwards.
MSG
exit 2

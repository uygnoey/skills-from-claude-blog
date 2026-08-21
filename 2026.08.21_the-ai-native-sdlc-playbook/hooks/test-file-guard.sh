#!/bin/bash
# Protect the feedback loop: an agent fixing code must not be able to weaken the
# check on that code. During a fix task, edits to test files are blocked.
#
# The task marks itself a fix task by setting FIX_TASK=1 in the session
# environment; outside a fix task this hook passes everything through so tests
# can still be written and changed normally.
[ "$FIX_TASK" = "1" ] || exit 0

path=$(jq -r '.tool_input.file_path // empty' < /dev/stdin)
[ -n "$path" ] || exit 0

case "$path" in
  */test_*.py|*_test.py|*/tests/*|*/itest/*|*.test.ts|*.test.tsx|*.test.js|*.spec.ts|*.spec.js)
    echo "This is a fix task: the test is the proof the bug is gone, so it cannot be edited here. Fix the code, not the test. If the test itself is wrong, stop and raise it with the code owner." >&2
    exit 2
    ;;
esac
exit 0

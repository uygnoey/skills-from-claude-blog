# The verification block

Always give Claude a way to verify its own work — tests, a build, or a screenshot diff — so a
session checks itself and fixes its own mistakes before an engineer sees them. The instruction
lives in `CLAUDE.md`.

```markdown
## Verifying your work
- Build: make build (must finish with "Build succeeded")
- Test: make test (all green; never skip or delete a failing test)
- Lint: make lint (zero warnings)

Run all three before reporting any task complete, and paste the output.
If a test fails, fix the code, not the test.
```

**Setting the loop up**

1. If checking the work today takes a sequence of commands and some environment knowledge, wrap
   it in a single target such as `make test` or `npm test` that exits non-zero on failure.
2. In the Commands section of `CLAUDE.md`, list each command with an example of healthy output.
3. State a target and make it quantifiable, so Claude can check the work without asking you —
   "all tests in test_status.py pass", "the screenshot matches the attached mock", "the endpoint
   returns 200 with the new field".
4. For bug fixes, write the failing test first: ask Claude to reproduce the bug as a test, run it,
   and confirm it fails for the reason you expect. Commit that test. Only then ask Claude to make
   it pass without editing the test. A test that existed before the fix, and that the agent could
   not rewrite, is proof the bug is gone.
5. For UI work, close the loop with a visual check. Give Claude a browser or screenshot tool and
   the mock, then let it implement, screenshot, compare, and adjust. Two or three rounds is normal.
6. Protect the loop itself. An agent fixing code must not be able to weaken the check on that
   code, so block edits to test files during a fix task — or check the diff in review and reject
   any change that touches a test.

**Not the same as a verifier subagent.** The feedback loop runs through the whole task as many
times as the work needs. A verifier subagent packages the final check by running a fresh context
window once the session believes the work is done, so the verdict is not colored by the
assumptions that produced the code.

**What the evidence is.** The literal output of the test command, the build log, or the
screenshot diff that Claude ran and pasted — evidence produced by the toolchain, logged in the
session transcript and in the PR's check run.

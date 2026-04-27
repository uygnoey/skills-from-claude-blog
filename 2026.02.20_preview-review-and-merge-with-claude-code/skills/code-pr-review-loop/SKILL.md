---
name: code-pr-review-loop
description: Turn Claude Code Desktop into a tighter development loop: preview running apps, review local diffs before pushing, and monitor (and optionally fix/merge) GitHub PRs from one place.
---

## Instructions

Follow this workflow to reduce context switching while developing with Claude Code Desktop:

1) **Preview the running app in Desktop**
   - Start your dev server from Claude Code Desktop and use the in-app preview to view the UI.
   - Use the preview to point out visual elements and issues, and ask Claude to iterate using what it sees and any console logs.

2) **Review local diffs before pushing**
   - Use the Desktop “Review code” button to request a review of your local changes.
   - Address the inline comments before your changes leave your machine.

3) **Monitor GitHub PR checks (optional automation)**
   - After opening a PR, keep Claude Code Desktop open to monitor CI checks.
   - If available in your setup, enable:
     - **auto-fix** to attempt fixes when CI fails.
     - **auto-merge** to merge once checks pass.

4) **Carry session context across surfaces**
   - If you started in the CLI, run `/desktop` to bring the session into Desktop.
   - Use “Continue with Claude Code on the web” to move a local Desktop session to web/mobile.

## Examples

### Example: Ask Claude to review before you push

- Open the Desktop diff view and click **Review code**.
- Then ask: “Apply the review feedback and re-run the checks.”

### Example: Move a CLI session into Desktop

Run the command below in a Claude Code CLI session:

```
/desktop
```

## Source

- Blog post: https://claude.com/blog/preview-review-and-merge-with-claude-code


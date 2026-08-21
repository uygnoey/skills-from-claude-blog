# The four deployment patterns

How the verification loop kicks off: standalone, embedded, chained, or tied to PR. Each has a
place it earns, a cost, and a signal that you have outgrown it.

## Standalone

**Fires when** you invoke it deliberately, after the artifact exists.

**Earns its place** for cross-cutting checks that do not apply every time:

- a pre-commit security scan
- a pre-PR accessibility audit
- license-header verification across a repo

Anything you want available across many workflows but do not want firing on every code change.

**Cost:** each invocation is still a turn you have to remember to take.

**Outgrow signal:** you are running it after every change. At that point the procedure has earned
a permanent home — embed it or chain it.

## Embedded

**Fires** automatically as part of the producing skill. The check belongs to one specific
workflow, and the workflow now runs it without you asking.

**Simplest version:** a one-line append to the producing skill's body, e.g. *"After creating the
component file, run eslint on it and address any errors before reporting completion."*

**Verify it works:** invoke the skill on a fresh task and confirm the new step runs as part of the
output. If it does not, the skill's description or earlier instructions are not pulling the
appended check in.

**Limits:**

- Only works on skills you can edit — ones you wrote, or ones installed at project level where the
  `SKILL.md` is under your control.
- Built-in skills and plugin-managed skills (the kind overwritten on update) are off-limits —
  chain instead.
- Skip embedded for checks that span workflows; those want standalone.

## Chained

**Fires when** one skill calls another at its end, so several verified handoffs run end-to-end.

**In practice at Anthropic:** members of the Claude Code team run `/code-review` to hunt for bugs,
`/simplify` to clean up the diff, a `/verify` skill to confirm end-to-end behavior, and a custom
`/design` skill that checks against guidelines in a `DESIGN.md` file if the change touched UI.

**Also the workaround for skills you cannot modify:** build a custom wrapper skill that invokes
the original, then invokes your verification skill.

**What it changes:** a habit ("I always run `/verify` after `/simplify`") becomes a contract
("`/simplify` always runs `/verify` when it finishes"). The chain runs the whole dev cycle on its
own; you step in only when something escalates back to you.

**Costs and limits:**

- Chaining trades flexibility for automation. Skip it when the steps are independent enough that
  you sometimes want to run one without the others.
- Chained loops can increase token spend — test before deploying broadly.

## On every PR

**Fires** on every change, whether or not the author remembered to invoke the chain.

Once the chain is solid for your own changes, the same procedure can run on every PR. The
infrastructure is the same kind of thing as the chain you already wrote, one step further along:
the same skills, the same rubrics, the same standards, applied without depending on the author's
diligence.

This is where verification stops being personal infrastructure and becomes team infrastructure.

**Timing:** hold off on PR-wide gates while the chain is still in flux — every adjustment becomes
a team-visible event.

## Source

[Building verification loops in Claude Code with skills](https://claude.com/blog/building-verification-loops-in-claude-code-with-skills)

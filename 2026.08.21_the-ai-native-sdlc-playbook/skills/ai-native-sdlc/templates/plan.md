# Plan: <change name> (from intent.md <date>)

## Files that change

List them by path, marking new files. This is what makes the plan reviewable before any code
exists.

## Order of work

1. …
2. …
3. …

Ordering matters: it is what lets a reviewer see the blast radius grow step by step, and what
lets the work be split across parallel sessions when steps are independent.

## Risks

What could break, which step is the most risky, and the constraints of any system being called
(rate limits, quotas, frozen packages).

## Proof

The tests that prove the change, and any non-test evidence — a screenshot matching the approved
mock, a command whose output must change. The PR review pass checks the eventual diff against
this section.

## Options not taken

What Claude considered and rejected, and why. Ask for this explicitly; it is where the useful
disagreement usually is.

---

**How to use this template**

1. Start the session in plan mode, where Claude can read the codebase without changing anything.
2. Give Claude `intent.md` and `spec.md` and ask for a plan in this shape.
3. Interrogate it. What could this break? Which step is riskiest? What did you choose not to do?
4. Iterate until an engineer who has never seen the conversation could implement the change from
   the plan alone.
5. Commit the approved plan, then accept it and let Claude implement. With a solid plan the
   implementation is often a single pass.
6. When the implementation departs from the plan, update the plan in the same commit — consider a
   hook that enforces the synchronization.

# Promotion policy

A tiered review path, written down and agreed in advance, that sets the depth of human review for a
change so the modernization finishes on an acceptable timeline. Work it out with the reviewers and
fit it into the organization's existing change-management process wherever possible.

## Rules that hold everywhere

1. **Tier changes by blast radius and agent confidence.** Use the organization's own change or risk
   classification if it has one. Keep full human review for critical paths.
2. **Fix recurring flags at the source.** Group and analyze flagged changes over time. When the same
   kind of flag keeps recurring, fix the cause in the agentic workflow or the certificate instead of
   reviewing each instance.
3. **Design the output format with the reviewers.** Agree what information and format make review
   fastest and which signals give more confidence. Have them review early sample outputs while the
   workflow is being refined.
4. **Allocate SME time effectively.** SMEs won't read every final diff, but their judgment is the
   scarce input. Let them go straight to the highest-risk tiers, and to flagged agent decisions
   within each, without wading through large diffs.

These rules front-load SME hours: their early feedback tunes the certificate and workflow, and their
sign-off on samples justifies a lighter path where confidence is high — the reverse of the
traditional pattern where review happens at the end.

## Speed vs. review depth

- Racing a hard deadline (e.g., a runtime losing support) → faster policy, lighter human review, and
  an explicit agreement to accept more risk per change.
- Longer timeline → deeper human review and a slower cutover.

Stakeholders land at different points depending on risk appetite and constraints; lock it in before
work starts.

## Accountability in regulated environments

Individual approvers hesitate to sign off on lighter review because they carry the risk of a bad
change, while leadership carries the larger risk of an aging system. Have the directive come from
the top of the organization and agree it beforehand, so responsibility for a bug that reaches
production is shared rather than pinned on whoever approved it.

All of this depends on a certificate detailed enough to be real evidence, and on reviewers who
understand how Claude arrived at a change well enough to trust it.

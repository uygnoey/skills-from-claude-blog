# Pilot scorecard — <group name>

Pilot lead: <name>  ·  Window: <start> → <end>  ·  Dataset class: <e.g. scRNA-seq, CRISPR screen>

Define the criteria before the pilot starts, and measure the same dataset class before and after. Three quantitative metrics, plus one qualitative signal that matters more than any of them.

## 1. Cycle time

How long the pilot analysis took before, and how long it takes now, on the same dataset class.

| Analysis | Before | After | Delta |
|---|---|---|---|
| | | | |
| | | | |

## 2. Keep rate

How often a scientist or PI trusts the result **without re-running it by hand**.

| Analysis | Reviewed by | Re-run by hand? | Why |
|---|---|---|---|
| | | | |

Keep rate = <kept> / <total> = <%>

If the keep rate is low, find out whether the blocker is trust in the method or an unreviewed step in the plan. They have different fixes.

## 3. Cold-reproduce rate

Take an artifact produced in week one, hand its provenance bundle to a **different** scientist in week four, and confirm they can re-run it cold.

| Artifact | Produced (date) | Re-run by | Date | Succeeded cold? | What was missing |
|---|---|---|---|---|---|
| | | | | | |

Cold-reproduce rate = <succeeded> / <attempted> = <%>

## 4. The signal that matters most — skills saved unprompted

A strong signal that a pilot is working is when champions start saving their own skills: a lab's internal normalization pipeline wrapped so every future session inherits it, a group lead wrapping the lab's LIMS API. These become the lab's catalog and the seed of the org catalog at scale.

| Skill saved | Author | What it wraps | Shared beyond the group? |
|---|---|---|---|
| | | | |

## 5. Edge cases surfaced at weekly check-ins

Log what the catalog needs to absorb: connector gaps, scheduler quirks, unsupported file formats.

| Date | Edge case | Resolution / owner |
|---|---|---|
| | | |

## Verdict

- [ ] Cycle time improved materially on the target dataset class
- [ ] Keep rate acceptable to the PI
- [ ] At least one artifact reproduced cold by a different scientist
- [ ] Champions saving skills without being asked
- [ ] Governance questions from the foundation phase all answered

**Recommendation:** <scale / extend pilot / stop>  —  <one paragraph of reasoning>

## Source

- https://claude.com/blog/the-claude-science-product-guide

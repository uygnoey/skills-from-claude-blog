# lessons.md — running incident log

Append-only working memory for the on-call agent. The agent writes an entry after every resolved incident, and reads this file at the **start** of every new investigation so its first hypothesis begins from what has actually happened recently.

Two kinds of entry belong here: what went wrong, and how the team investigates. The second kind is easy to skip and often the more valuable.

When the same pattern appears often enough, promote it into the relevant investigation skill so it becomes a step rather than a recollection — then leave the log entry in place as history.

---

## Entry format

```markdown
## <YYYY-MM-DD> — <short title>

- **Bug class:** <class, matching an investigation skill if one exists>
- **Symptom:** <what was observed, and where>
- **Root cause:** <what was actually wrong>
- **Fix:** <what resolved it, and who approved it>
- **Time to first grounded hypothesis:** <minutes>
- **Gotcha:** <the thing worth remembering next time>
- **Promote?:** <no | to investigation skill "<name>">
```

---

## Entries

## <YYYY-MM-DD> — <example: tests silently stopped running on a new service>

- **Bug class:** `<class>`
- **Symptom:** A batch of tests on a new service stopped firing; no failure, just absence.
- **Root cause:** A feature flag enabled earlier that day introduced skip rules that matched them.
- **Fix:** Reverted the flag after confirming the revert was safe; verified skip rules were gone and error rate had returned to baseline.
- **Time to first grounded hypothesis:** `<n>`
- **Gotcha:** Absence of failures is not a healthy signal. Check that the expected number of tests ran, not only that the ones that ran passed.
- **Promote?:** `<...>`

## <YYYY-MM-DD> — <example: a process lesson, not a bug>

- **Bug class:** process
- **Symptom:** An investigation went down the wrong path for `<duration>`.
- **Root cause:** A hypothesis was formed from a configuration file before any metric was queried.
- **Fix:** Re-ran the investigation starting from the data.
- **Gotcha:** Query the data first, then theorize. Configuration tells you what could go wrong; metrics tell you what did.
- **Promote?:** yes — added as step 1 of every investigation skill.

## Source

- https://claude.com/blog/ai-ci-cd-on-call

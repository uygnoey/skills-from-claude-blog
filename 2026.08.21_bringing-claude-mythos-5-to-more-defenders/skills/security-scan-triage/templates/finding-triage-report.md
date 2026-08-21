# Finding triage report template

One row per finding from a Claude Security scan. The first four columns come straight from the
scan output; the rest are what triage adds.

```markdown
# Security scan triage — <repository> — <scan date>

Scan model: Claude Mythos 5 · Surface: claude.ai/security

| # | CWE | Confidence | Severity | Location | Verified? | Decision | Patch PR | Human approver |
|---|-----|------------|----------|----------|-----------|----------|----------|----------------|
| 1 |     |            |          |          |           |          |          |                |
```

## Column meanings

- **CWE** — the Common Weakness Enumeration category returned with the finding.
- **Confidence** — the scan's confidence rating. Triage this first: a low-confidence finding needs
  verification before it becomes work.
- **Severity** — the scan's severity rating. Ranks the verified set.
- **Location** — file and line, or the component the finding points at.
- **Verified?** — `yes` / `no` / `pending`, with a one-line note on how it was checked. Recording
  this stops the same finding being re-litigated on the next scan.
- **Decision** — `patch` / `accept risk` / `false positive` / `defer`.
- **Patch PR** — the pull request implementing the suggested fix, opened from Claude Code on the
  web. Interactive patching uses the models your organization has access to in Claude Code; the
  Mythos scan does not extend Mythos access to other surfaces.
- **Human approver** — **required.** Every patch must be reviewed and approved by a human before it
  can be implemented.

## Per-finding detail block

For anything above `accept risk`, keep a short block alongside the table:

```markdown
### Finding <#> — <short title>

- **CWE:** <id and name>
- **Confidence / Severity:** <as reported>
- **Where:** <path:line>
- **Suggested fix (from scan):** <summary of what the scan proposed>
- **Verification:** <what was checked, and what it showed>
- **Decision and rationale:** <one or two sentences>
- **Patch:** <PR link> — reviewed and approved by <name>
```

## Source

[Bringing the cybersecurity capabilities of Claude Mythos 5 to more defenders](https://claude.com/blog/bringing-claude-mythos-5-to-more-defenders)

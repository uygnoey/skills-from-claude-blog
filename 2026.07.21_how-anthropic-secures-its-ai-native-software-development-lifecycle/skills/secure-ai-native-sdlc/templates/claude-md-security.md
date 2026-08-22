# Template — security guidance for `CLAUDE.md`

Encode the guidance where code is generated. Replace the bracketed parts, keep the
loop-closing note at the end, and add a line to the bug-class list every time a new
class is discovered.

```markdown
## Security guidance

Follow these when writing or modifying code in this repository. They are not
suggestions to check at review time — apply them as the code is written.

### Org-wide skills to apply
- [secure-coding-skill-name] — [what it covers]
- [data-handling-skill-name] — [what it covers]

### Review step
- Run `/security-review` [in-session / as a final step before opening a PR].
  It looks for places where potential attacker-controllable input enters, scans for
  suspicious links, and verifies its findings before reporting them.

### Attacker-controllable input
Treat these as untrusted in this codebase: [list the entry points — request bodies,
webhook payloads, uploaded files, third-party API responses, dependency metadata,
log lines an agent may read back].

### Authorization invariants
These must hold everywhere. A change that could break one requires manual review:
- [e.g. user A can never read user B's data]
- [e.g. a service account can never assume an end-user identity]

### Bug classes discovered here (do not reintroduce)
<!-- Append one line per discovered class, with the change that fixed it. -->
- [YYYY-MM-DD] [bug class] — [what to do instead] ([link to the fix])

### Hosting
Internal, non-technical teams: host applications on [low-code app-hosting platform]
rather than standing up new infrastructure.
```

## Closing the loop

The template is only half of the control. The other half is process: when an agent
or a person discovers a new bug class, the change that fixes it also updates this
file in the same commit. A discovery that does not reach the guidance file will
recur in generated code.

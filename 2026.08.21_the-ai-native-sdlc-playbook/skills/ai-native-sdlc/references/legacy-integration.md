# Legacy systems and the source of truth

*Applies to every artifact the process produces.*

Existing SDLC processes likely already track artifacts, just not in markdown files. Work items may be
in Jira, requirements in a tool with regulatory traceability built in, designs in Figma, and change
approvals with a change board. Those systems are hard to displace because auditors and regulators
already accept them and other teams depend on them, so the AI-native SDLC has to fit around what
exists.

**The rule: for every artifact the process produces, name one system as the source of truth, with
everything else holding a copy or a link to the original.** The choice can differ per artifact.

## The three configurations

**1. The repo as the source of truth.** The markdown artifacts are the authoritative record and the
legacy system references files within commits. This is one of the cleanest configurations for
engineering-led organizations: all records live in one tool with one timestamp authority.

**2. The legacy system as the source of truth.** Jira, ServiceNow, or the requirements tool holds the
authoritative record and the markdown artifacts are working copies. Claude reads the record at the
start of the session and writes the outcome back through an MCP connector in the same session that
produced the spec or the plan.

**3. Linkage as the minimum bar.** All artifacts note the record ID and all legacy records contain
the commit SHA of the markdown file. Linkage is a good place to start when transitioning, accepting
that there are two sources of truth.

Both the legacy system and the markdown-first system can coexist, so long as there is a link between
the two or one is declared the source of truth.

## Applying it

| Artifact | Typical legacy home | Question to settle |
|---|---|---|
| Intent / work item | Jira, Azure Boards | Does the ticket link to the commit, or does the commit link to the ticket? |
| Requirements | A traceability tool | Which record does an auditor read first? |
| Design | Figma | Is the exported mock in the repo, or a link to the file? |
| Change approval | ServiceNow, a change board | Does the approval reference the PR, or does the gate query the ticket? |

Settle each row before automating the handoff. A stage that fires on a commit needs to know whether
the commit is the record or a copy of one.

# The requirements-and-design prompt

The product owner opens a session with the organization's skills available, attaches the
accepted `intent.md`, and runs this prompt. Run it by hand at first, then codify it as an
organization-level slash command, then make acceptance of the intent the trigger for a
non-interactive job that commits the result as a pull request.

```text
Read the attached intent.md and produce a requirements and design spec for
integrating it into our existing codebase. Apply the skills available to you so
the plan conforms to our brand guidelines, security policies and UX standards.
Document the spec fully as spec.md, ready to hand to the engineering team.
Describe clearly any areas of concern, especially where you cannot satisfy
contradicting policies.
```

**What the prompt is doing**

- **Points at the artifact.** The spec is derived from a committed `intent.md`, not from a
  conversation, so the pair records what was asked for and what was decided.
- **Names the constraints.** The organization's skills are loaded as constraints on the spec,
  so live policy is applied while the spec is written rather than discovered in a review weeks
  later.
- **Demands flagged concerns.** The flags are the points an analyst would have escalated. The
  product owner resolves each one with its policy owner before engineering sees the spec.

**After the pass**

1. Review the spec against the idea: does it solve the stated problem, and are the open
   questions from `intent.md` answered or carried forward?
2. Work the flagged concerns first.
3. Commit `spec.md` alongside `intent.md`.
4. Decide whether spec and intent progress to build, consulting a technical lead for anything
   the organization classes as higher risk. A human always makes this call, and accepting the
   spec is what starts plan mode.

**Front-end variant.** Once the intent is accepted, the product owner mocks the design up in
Claude Design (beta) from the `intent.md`, iterates on the mock, then exports it to Claude Code
to build.

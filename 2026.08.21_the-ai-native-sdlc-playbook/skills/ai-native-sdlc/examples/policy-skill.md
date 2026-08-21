# A policy written as a skill

Skills are how an organization makes institutional knowledge operational: explicit,
version-controlled, applied broadly, and updated centrally when policy changes.

**Rule of thumb.** Write a skill for institutional knowledge that must be applied consistently.
Do not write a skill for something that belongs in `CLAUDE.md` or in a prompt.

## Worked example — `.claude/skills/secure-api-review/SKILL.md`

```markdown
---
name: secure-api-review
description: Apply the API security standard. Use whenever creating or
  modifying an external-facing endpoint, reviewing API code, or
  generating an OpenAPI spec.
---

# Secure API review

When you create or change an API endpoint:

1. Authentication: every endpoint requires the gateway JWT;
   no anonymous routes outside /health.
2. Input validation: validate request bodies against the OpenAPI
   schema and reject unknown fields.
3. Audit: every state-changing endpoint emits an audit event with
   actor, action, entity and timestamp.
4. Data classification: fields tagged pii in the schema must never
   appear in logs or error messages.

Run the endpoint check script and include its output in your summary.
```

## Standing one up

1. Pick one piece of knowledge that is enforced inconsistently today — a security standard, an
   API design convention, a brand rule.
2. Write it as a skill: a folder containing a `SKILL.md` whose frontmatter says when it triggers
   and whose body says what to do. An engineer writes it from the policy owner's source of truth,
   using Claude to help.
3. Put the skill in the repo at `.claude/skills/<name>/` so it ships with the code, or distribute
   it organization-wide through a plugin.
4. Test that the skill triggers. Ask Claude to do the relevant task in different ways and confirm
   the skill loads each time.
5. When the policy changes, change the skill and have the policy owner sign the change off.
   Engineers pick up the new version automatically in their next session.

## The limit of a skill

A skill is a control, but an advisory one. It makes Claude likely to apply the policy while the
code is written; nothing forces a session to comply. A policy that must always hold needs
something deterministic behind it — a hook that blocks the action, or a review pass that
re-checks the policy at the PR. The skill makes violations rare and the hook makes them close to
impossible.

Skill invocations are logged in session traces, and the policy owner reviews skill changes like
code.

**Measuring it.** Leading: time from the policy owner approving a change to the updated skill
merging, taken from the PR on the skill folder. Lagging: PR review findings citing the policy,
which should fall towards zero once the skill applies the policy while the code is written. If
they do not fall, either the skill is not triggering or its text has drifted from the official
policy.

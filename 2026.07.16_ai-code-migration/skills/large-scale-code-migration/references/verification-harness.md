# Building the judge

Before any translation starts, you need a referee: a verification mechanism that can be run
against the original codebase and against the port, and that answers the same way for both.
Without it there is no definition of "done" that survives contact with a long migration.

The source post gives three steps.

## 1. Categorize the existing tests

Use Claude to sort the current test suite into two buckets:

- **Expressible as external calls** — tests that exercise the system through its public
  surface. These port.
- **Dependent on internals** — tests that reach into private structures, module layout, or
  implementation-specific behavior. These do not port, because the thing they assert on will
  not exist in the same shape after the migration.

Do not try to save the second bucket. Its value was tied to the old implementation.

## 2. Rewrite the portable tests into two-sided assertions

Convert the external-facing tests into assertions that can be run against both the original
and the port, producing comparable output. The point is not "the port passes its own tests"
— it is "the port and the original answer identically."

## 3. Validate the judge itself

Two runs, both required:

- Run the judge against the original code. It must pass. A judge that fails on known-good
  code will drown the migration in false alarms.
- Run the judge against deliberately broken code. It must fail. A judge that passes on
  known-bad code is worse than no judge, because it will certify a broken port.

Skipping this validation is the most common way a migration ends with a green board and a
broken product.

## When there is no test suite

Have Claude construct the scenarios. This is what the post describes as a parity harness: a
set of real-world scenarios exercised against both codebases, with any behavior difference
treated as a bug to be fixed rather than a difference to be explained away.

The Python-to-TypeScript port described in the post used seven such scenarios. Seven
well-chosen end-to-end scenarios that genuinely exercise the system are worth more than
hundreds of shallow unit tests that only prove the port compiles.

## Keep the referee mechanical

Throughout Steps 4–6, let scripts be the referee — the compiler, a diff, the test suite. An
agent deciding whether two behaviors are "basically the same" reintroduces exactly the
judgment you were trying to remove from the inner loop. Agents propose fixes; scripts decide
whether the fix worked.

## Checklist

- [ ] Existing tests categorized into portable / non-portable.
- [ ] Portable tests rewritten as assertions runnable against both sides.
- [ ] Parity scenarios written for anything the test suite does not cover.
- [ ] Judge passes on the original code.
- [ ] Judge fails on deliberately broken code.
- [ ] Judge runs unattended, from a script, with a machine-readable result.

# Gap inventory

Where the rulebook's defaults do not apply — the places that need refactoring rather than
translation.

> Fill this in **after** the rulebook. A gap is only a gap relative to a stated default.

## How to use it

Each gap gets a decision before Step 3 starts. Gaps discovered later are fine and expected —
add them here, decide, and if the decision generalizes, push it back into the rulebook.

## Entry format

### GAP-001 — `<short name>`

- **Where:** files, modules, or subsystems affected
- **What differs:** the architectural mismatch, stated concretely
- **Why the rulebook can't cover it:** what makes this not a lookup-table case
- **Decision:** refactor before translating / translate then refactor / redesign / drop
- **Owner:** who decides, if it is still open
- **Blocks:** which files cannot start until this is resolved
- **Status:** open / decided / done

---

## Common sources of gaps

Use as a prompt list when building the first version:

- Concurrency model differences (green threads vs OS threads, async colors, shared mutable
  state).
- Memory model differences (GC vs ownership, manual allocation, arenas).
- Error semantics (exceptions vs values, panics, recoverable vs fatal).
- Reflection, metaprogramming, and dynamic dispatch that has no target equivalent.
- Build-time code generation and macros.
- Platform-specific or FFI boundaries.
- Third-party dependencies with no target-language equivalent.
- Behavior that the source language specifies and the target does not (integer overflow,
  string encoding, iteration order).
- Anything the test suite covers that the port cannot express the same way.

## Inventory

| ID | Name | Blocks | Decision | Status |
| --- | --- | --- | --- | --- |
| GAP-001 | | | | open |

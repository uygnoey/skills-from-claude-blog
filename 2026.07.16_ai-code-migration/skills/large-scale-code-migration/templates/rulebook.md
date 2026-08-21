# Rulebook — <source> to <target>

The translation policy for this migration. Everything an implementer agent needs in order to
port a file without asking a human. Keep it short enough to fit in an agent's context and
concrete enough that two agents reading it produce the same output.

> Write this **before** the gap inventory. The gap inventory is defined by what these
> defaults do not cover.

---

## 0. Architectural decision

- [ ] **Structure-preserving port** — same architecture, new language. This rulebook is
      mostly lookup tables.
- [ ] **Redesign** — new architecture. This rulebook is closer to a design document, and the
      sections below need prose, not tables.

Chosen: `<one of the above>`
Rationale: `<why>`

---

## 1. Type mappings

| Source type | Target type | Notes / caveats |
| --- | --- | --- |
| | | |

Include the awkward ones explicitly: unsigned integers, nullable vs optional, string
encodings, fixed-size arrays, tagged unions, generics with constraints.

## 2. Idiom mappings

| Source idiom | Target idiom | Notes |
| --- | --- | --- |
| | | |

Iteration, resource cleanup, string building, collection construction, comparison and
equality, formatting.

## 3. Error handling

- How errors are represented in the target: `<...>`
- How source-language failure modes map onto it: `<...>`
- What must never be swallowed: `<...>`

## 4. Memory and lifetime

- Ownership / borrowing / reference-counting conventions: `<...>`
- What to do with manual allocation in the source: `<...>`

## 5. Concurrency

- Threading or async model in the target: `<...>`
- Mapping for locks, channels, atomics, and shared state: `<...>`

## 6. Naming and layout

- File and module naming: `<...>`
- Symbol naming conventions: `<...>`
- One-to-one file correspondence, or a different mapping? `<...>`

## 7. Dependencies

| Source library | Target replacement | Notes |
| --- | --- | --- |
| | | |

## 8. Comments, docs, and tests

- Doc comments: preserve / rewrite / drop — `<...>`
- Inline comments: `<...>`
- Test files: in scope for translation? `<...>`

## 9. When unsure

Implementers must not guess. Emit:

```
// TODO(port): <specific reason this could not be translated confidently>
```

and continue. Do not invent target-language APIs. Do not silently change behavior to make
something compile.

---

## Changelog

Every rule added after a reviewer caught a repeated mistake. Each entry should name the
pattern that triggered it, so future readers can tell rules from preferences.

| Date | Rule added | Triggered by |
| --- | --- | --- |
| | | |

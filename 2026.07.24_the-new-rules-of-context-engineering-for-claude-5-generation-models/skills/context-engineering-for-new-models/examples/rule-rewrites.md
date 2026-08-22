# Before and after

Four rewrites in the shape the post describes. The first is taken directly from Claude Code's own
prompt; the rest apply the same shifts to the situations the post names.

---

## 1. A comment rule becomes a standard

**Before**

```
Default to writing no comments. Never write multi-paragraph docstrings or multi-line
comment blocks — one short line max.
```

**After**

```
Write code that reads like the surrounding code: match its comment density, naming, and idiom.
```

**Why it works.** The prohibition was a proxy for "do not produce comment noise." The standard names
the real goal, so a densely documented module keeps its documentation and a terse one stays terse. It
also stops contradicting the softer instruction elsewhere in the stack about leaving documentation as
appropriate — the contradiction that made the older setup hobbling rather than helpful.

*(Shift 1: rules → judgment.)*

---

## 2. A tool taught by example becomes a tool with a better signature

**Before** — in the system prompt:

```
When searching, call search_docs like this:
  search_docs("billing webhooks")           # broad question
  search_docs("billing webhooks", "api")    # narrow to one section
  search_docs("retry", "api", exact=True)   # literal match
```

**After** — nothing in the system prompt; the tool description carries it:

```
search_docs(query, scope, mode)
  query  string   what to look for
  scope  enum     "all" | "api" | "guides" | "changelog"
  mode   enum     "semantic" (default) | "exact"
```

**Why it works.** The three examples defined an exploration space, and a newer model will tend to stay
inside it — the fourth kind of search, the one nobody wrote an example for, gets reached for less. The
enumerated parameters say the same thing about correct usage while covering every call.

*(Shift 2: examples → interface design. Shift 4: the system-prompt copy is deleted, not moved twice.)*

---

## 3. A duplicated instruction loses its second copy

**Before** — the same sentence in two places:

```
System prompt:      Always pass a scope to search_docs; unscoped searches are slow.
Tool description:   Always pass a scope; unscoped searches are slow.
```

**After**

```
Tool description:   Always pass a scope; unscoped searches are slow.
```

**Why it works.** Current models reliably read tool descriptions. The second copy bought reinforcement
for older models; now it buys length, a sync burden, and a future contradiction when one copy is
edited and the other is not.

*(Shift 4: repetition → one clear tool description.)*

---

## 4. A markdown spec becomes a rich reference

**Before** — `spec/toast.md`:

```
The toast should appear at the bottom right, stay for four seconds, and stack up to three.
Errors are red and stay until dismissed.
```

**After** — two references, @mentioned instead:

- `spec/toast.html` — a working artifact showing the placement, the stack, and both variants.
- `test/toast.spec.ts` — the timing, the stack limit, and the dismiss behavior as assertions.

**Why it works.** "Bottom right" and "stack up to three" are prose encodings of things the artifact
and the test state exactly. Claude handles complex references well enough that the higher-fidelity
form is now the better default; the prose version is the lossy one.

*(Shift 6: simple specs → rich references.)*

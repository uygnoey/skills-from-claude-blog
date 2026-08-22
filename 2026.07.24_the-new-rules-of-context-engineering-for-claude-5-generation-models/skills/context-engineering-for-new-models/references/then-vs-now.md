# The six shifts, in detail

Each entry gives the practice that worked for earlier model generations ("Then"), the practice the
post recommends for Claude 5 generation models ("Now"), and why the swap works.

---

## 1. Give Claude rules → let Claude use judgment

**Then**

> Default to writing no comments. Never write multi-paragraph docstrings or multi-line comment blocks
> — one short line max.

**Now**

> Write code that reads like the surrounding code: match its comment density, naming, and idiom.

Newer models have better judgment, so they can make the contextual call that a rigid constraint was
standing in for. The rule was never really "no comments" — it was "do not produce the kind of comment
noise older models produced." Stating the actual standard gets you the outcome in every file,
including the files where a comment is the right answer.

This is also where hobbling starts. A hard prohibition in one layer meets a softer instruction in
another — leave documentation as appropriate — and the model is now holding two orders it cannot both
obey.

---

## 2. Give Claude examples → design interfaces

**Then**

Teach a tool through usage examples in the prompt.

**Now**

Put the teaching in the tool design itself: expressive parameters, options enumerated clearly enough
that the right usage is visible from the signature.

Examples do not just illustrate for a newer model — they **constrain** it, pinning it to the
exploration space the examples happen to cover. A well-designed interface guides usage without closing
off the cases you did not think to write down.

Practical consequences: name parameters for what they mean rather than how they are implemented, use
enums instead of free-form strings where the set is closed, and let the type carry the constraint
instead of a sentence describing the constraint.

---

## 3. Put it all upfront → use progressive disclosure

**Then**

Detailed system prompts carrying every piece of information the model might need.

**Now**

Load context selectively, through skills and deferred-loading tools.

Progressive disclosure gets the right guidance to Claude at the moment it is relevant, instead of
spending tokens on information that may never be needed in a given session. The unit of loading
becomes the skill or the deferred tool, not the prompt.

---

## 4. Repeat yourself → simple tool descriptions

**Then**

The same usage instruction appears in the system prompt *and* in the tool description.

**Now**

It appears in the tool description only.

Earlier models benefited from the repetition. Current models reliably consult tool descriptions, so
the system-prompt copy adds length, adds a second place to keep in sync, and adds one more chance for
the two copies to drift into contradiction.

---

## 5. Memory in CLAUDE.md files → auto-memory

**Then**

Users manually saved context into CLAUDE.md with the `#` hotkey.

**Now**

Claude automatically preserves the memories that are relevant to the work and to the user.

The post frames the wider version of this: Claude used to rely on CLAUDE.md as memory, information,
and guidance all at once. Memory, artifacts, and skills now give Claude its own ways to load and share
context across sessions — which is what frees CLAUDE.md to shrink back to a description of the
repository.

---

## 6. Simple specs → rich references

**Then**

Markdown-based plans and specifications.

**Now**

HTML artifacts, code references, test suites, and rubrics.

Claude handles increasingly complex references, and those formats carry the intent with less loss than
a prose description does. A test suite states the expected behavior exactly. A rubric states the
grading criteria exactly. An HTML artifact shows the layout rather than describing it.

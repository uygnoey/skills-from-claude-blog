# Template — References

Point at code that already does the thing. A reference implementation carries conventions
and edge cases you could not have articulated.

## Prompt

```
Before implementing <the thing>, read <path/to/reference or URL>. That code already
implements the behavior I want.

Tell me what it handles that I have not mentioned, then follow its shape where our codebase
allows and tell me where it does not.
```

## Cross-language form

```
Here is an implementation of <behavior> in <other language>: <path or URL>.

I want the same behavior in <our language / our codebase>. Read it for the *shape* of the
solution and the edge cases it covers, not the syntax. List the edge cases it handles
before you write anything, so I can tell you which ones apply to us.
```

## Notes

- **Language does not have to match.** The value in a reference is the set of cases the
  original author hit and handled. That transfers across languages; the syntax does not need
  to.
- References inside your own repo are the strongest form — they carry team conventions that
  nobody has ever written down.
- Ask for the list of handled edge cases *before* implementation. That list is a free
  inventory of your unknown unknowns for this problem.
- A reference plus an interview covers both directions: the reference supplies what the
  domain knows, the interview supplies what you know.

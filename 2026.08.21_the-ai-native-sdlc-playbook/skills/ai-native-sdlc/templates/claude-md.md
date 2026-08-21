# CLAUDE.md scaffold

`CLAUDE.md` gives Claude the context a new joiner would need. Knowledge that used to sit in
people's heads and on wikis becomes a file the agent reads at the start of every session,
maintained by the whole team.

**Rules that keep it useful**

- Run `/init` first and let Claude generate a starting file from what it finds, then cut it down.
- Keep it under a page. Claude reads all of it at the start of a session, so anything stale is
  taking up context for no benefit.
- Check it into git at the repo root so the whole team shares one version and changes are
  reviewed like code.
- When Claude makes the same mistake twice, the correction goes into this file.

**The shape**

```markdown
# <service name>

## Commands
- Build: <command>
- Test: <command> (unit), <command> (integration, and what it needs)
- Lint: <command> (where it runs; what to do before pushing)

## Conventions
- <language and framework versions, and what is banned>
- <domain rules that are always true, e.g. money is always BigDecimal, never double>
- <what every new endpoint / module / migration must come with>

## Architecture
- <which directory holds what>
- <what is generated and must never be hand-edited>

## Things Claude gets wrong
- <the mistake, stated as an instruction>
- <the frozen package, the ownership boundary, the thing that looks safe and is not>
```

**A filled example**

```markdown
# Payments service

## Commands
- Build: make build
- Test: make test (unit), make itest (integration, needs docker)
- Lint: make lint (runs in CI; fix before pushing)

## Conventions
- Java 21, Spring Boot 3. No new Lombok.
- Money is always BigDecimal, never double.
- Every endpoint needs an integration test in src/itest.

## Architecture
- api/ holds REST controllers, core/ holds domain logic,
  adapters/ talks to external systems.
- Kafka events are defined in schemas/; never edit generated classes.

## Things Claude gets wrong
- Do not bump dependency versions; the platform team owns them.
- The legacy v1/ package is frozen; changes go in v2/.
```

Add the verification block from `templates/verification-block.md` to the same file so the
session knows what "done" means.

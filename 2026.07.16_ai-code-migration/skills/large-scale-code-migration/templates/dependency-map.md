# Dependency map

What makes parallel translation possible. A file can be translated as soon as everything it
depends on has been translated — so the map is the schedule.

## How to produce it

1. If the ecosystem has an explicit manifest (module graph, build file, import metadata),
   read it. Prefer generated truth over inferred truth.
2. If not — legacy codebases, C/C++, Python and similar — have Claude discover the
   dependencies by reading the source, and record the result as data rather than prose.
3. Spot-check the result on files you already understand before trusting it for scheduling.

## Suggested shape

Machine-readable, because the queue runner consumes it:

```json
{
  "src/core/buffer.<ext>": { "depends_on": [], "layer": 0 },
  "src/core/parser.<ext>": { "depends_on": ["src/core/buffer.<ext>"], "layer": 1 },
  "src/api/server.<ext>": { "depends_on": ["src/core/parser.<ext>"], "layer": 2 }
}
```

`layer` is the wave a file can be translated in. Everything in layer N can go out to agents
at the same time once layer N-1 is complete.

## Things to record alongside it

- **Cycles** — dependency cycles have to be broken by hand or translated as a unit. List
  them explicitly; they will not resolve themselves.
- **Hubs** — files that a large fraction of the codebase depends on. Getting these wrong is
  expensive, so they are good candidates for the Step 2 stress test.
- **Leaves** — files nothing depends on. Cheap to regenerate, safe to experiment on.

## Queue state

Keep translation status on disk next to the map, not in an agent's context, so the run is
resumable. "Done" should be checkable without judgment: the output file exists.

| Path | Layer | Status | TODO(port) count |
| --- | --- | --- | --- |
| | | | |

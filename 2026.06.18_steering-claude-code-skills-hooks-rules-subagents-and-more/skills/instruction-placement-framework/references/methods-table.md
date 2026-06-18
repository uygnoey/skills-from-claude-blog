# Steering methods comparison table

This table is reproduced from the source blog post (paraphrased only for formatting).

| Method | When it's loaded | Compaction behavior | Context cost | When to use |
|---|---|---|---|---|
| CLAUDE.md (root) | Session start; stays in context for the entire session | Memoized; re-read after compaction | High | Build commands, directory layout, monorepo structure, coding conventions, team norms |
| CLAUDE.md (subdirectory) | On-demand, when Claude reads a file under that subdirectory | Lost until that subdirectory is touched again | Low | Conventions specific to a subdirectory |
| Rules | Session start (user-level) or only when matching files are touched (path-scoped) | Re-injected on compaction | Medium | Specific constraints or conventions |
| Skills | Name/description at session start; body loads when invoked | Re-injected up to shared budget; oldest dropped first | Low | Procedural workflows (deploy or release checklists) |
| Subagents | Name/description/tools at session start; body loads only when called | Only final message + metadata returns | Low | Isolated side tasks (deep search, log analysis, dependency audit) |
| Hooks | Fire on lifecycle events | Bypass compaction entirely | Low | Deterministic automation/enforcement |
| Output styles | Session start; injected into system prompt | Never compacted | High | Significant role changes |
| Appending the system prompt | Session start; passed as CLI flag | Never compacted; applies only to that invocation | Moderate | Tone, response length, formatting preferences |

Source: https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more

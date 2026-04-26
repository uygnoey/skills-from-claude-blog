**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Introduction to agentic coding

## What is this post?

A primer on agentic coding — the shift from AI tools that predict the next line to AI systems that take a high-level goal, plan multi-step work, modify files across a codebase, run tests, and iterate until done. The post traces the evolution from autocomplete to chat assistants to agentic systems, explains how Claude Code reads project context, coordinates multi-file changes, and respects an explicit permission model, and uses Rakuten's seven-hour autonomous vLLM implementation as the headline real-world example.

## When useful

- Onboarding teammates to "what makes agentic coding different from autocomplete and chat-based assistants."
- Sizing up which workflows (test automation, doc generation, refactoring, well-understood feature work) to delegate to Claude Code first.
- Quoting concrete metrics from Rakuten's case study (79% faster delivery, 99.9% accuracy, 5x parallel task capacity).
- Reaching for the install command and the three "first task" prompts the post recommends.

## Key points

- Agentic coding = autonomy + scope. Tools read entire codebases, trace dependencies, run commands, iterate. Autocomplete is limited to a small context window; chat is iterative but manual; agents handle orchestration.
- Two phases: context gathering & planning (configs, tests, imports, dependency map → adaptive plan), then implementation & coordination (multi-file edits, validation against tests).
- Claude Code installs with `npm install -g @anthropic-ai/claude-code` and launches with `claude` from the project directory.
- Permission model: Claude Code asks for approval before modifying files and shows the planned diff. You approve, revise, or reject.
- Integrates with existing dev tools (npm, Jest, pytest, Git, dev servers) and can connect to MCP servers for additional tools.
- Rakuten case study: implemented activation-vector extraction in vLLM (12.5M LOC, Python/C++/CUDA) in seven hours of sustained autonomous work; 99.9% numerical accuracy; 79% faster feature delivery (24 days → 5 days); 5x parallel task capacity. Quote attributed to Kenta Naruse: "I didn't write any code during those seven hours, I just provided occasional guidance." Yusuke Kaji: "You can have five tasks running in parallel by delegating four to Claude Code while focusing on the remaining one."
- Suggested first prompts: "Explain the structure of this codebase and how the main components interact"; "Review the authentication module for potential security issues"; "Find all N+1 query problems in our GraphQL resolvers and implement DataLoader batching".
- "Start slow, then expand" — quick wins: test automation, documentation generation, routine refactoring, well-understood feature implementation.
- Claude Code uses CLAUDE.md files to persist coding standards, architectural decisions, and project-specific requirements across sessions.

## Bundled resources

- [skills/agentic-coding-foundations/SKILL.md](./skills/agentic-coding-foundations/SKILL.md): when to reach for Claude Code, the two-phase workflow, install/run commands, and onboarding prompts.
- [references/evolution-of-ai-coding.md](./skills/agentic-coding-foundations/references/evolution-of-ai-coding.md): autocomplete → chat → agentic comparison from the post.
- [examples/first-prompts.md](./skills/agentic-coding-foundations/examples/first-prompts.md): the three suggested onboarding prompts verbatim, plus the Rakuten case study summary.
- [guides/getting-started-with-claude-code.en.md](./guides/getting-started-with-claude-code.en.md) (+ ko/es/ja): step-by-step adoption guide.

## Source

Distilled from [Introduction to agentic coding](https://claude.com/blog/introduction-to-agentic-coding) (published 2025-10-30).

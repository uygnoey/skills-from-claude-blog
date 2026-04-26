**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Making Claude a better electrical engineer

## What is this post?
This post describes how Anthropic worked with Diode Computers to improve Claude's ability to generate PCB reference designs using the Zener language.

## When is it useful?
Useful if you want to improve model performance in a narrow domain by working with experts, building a benchmark, and iterating on failure modes.

## Key points
- Define a concrete agentic task and a grading harness (testbench) that captures success/failure in domain terms.
- Use expert feedback to identify common failure modes and refine evaluation criteria.
- Prefer requirement-based checks (e.g., minimum capacitance) over brittle exact-match assertions.
- Validate improvements with blinded comparisons against baseline models.

## Bundled resources
- Skill: skills/domain-partnership-benchmarking/SKILL.md

## Source
- https://claude.com/blog/making-claude-a-better-electrical-engineer

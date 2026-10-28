# How IDC adopted Claude internally

Summary of the post's account. Figures are as reported by IDC in the source.

## Sequence
1. **Engineering first.** Engineering was the first team to adopt Claude.
2. **Then the rest of the company.** Product, marketing, and sales followed and now use it daily to build,
   plan, and sell.

## Engineering results
| Outcome | Before | After |
|---|---|---|
| Rebuild of the internal data repository analysts use for research | ~3 months (estimate) | 3 weeks |
| Shipped-code bugs after adopting Claude Code for testing | - | Down significantly |

## Use cases by area
| Area | Who / tool | What they do | Reported change |
|---|---|---|---|
| Building software | Product managers, Claude Code | Build working prototypes before engineering starts | Feature-to-engineering time from months to weeks |
| Testing and review | Engineers, Claude Code | Run tests in parallel; review code | A five-day code review now takes about 30 minutes |
| Planning | Product teams, Cowork | Give Cowork research and internal files; it drafts the plan | Planning sprints from three weeks to three days |
| Tests | Not specified (listed under planning in the post) | Write a new test that checks code works | About 20 minutes instead of days |
| Sales | Sales team, a tool built with Claude | Reads a CRM export and flags each rep's stalled deals and deals worth chasing | Minutes |
| Marketing | Content marketing, an assistant built in Claude | Drafts content, optimizes for SEO and AI answer engines (AEO), checks against buyer personas and IDC research; humans edit, proof, publish | Publishes faster than before |

## Patterns to reuse
- Let one technical team prove value first, then expand by function.
- Move prototyping upstream so product managers hand engineering something that already works.
- Use the agent for parallel testing and review, not only for writing code.
- Build small internal tools on exports you already have (for example a CRM export).
- Keep humans on the final edit for published content.

## Statements in the post
- IDC's CEO describes acquisition-impact analysis going from hours of pulling and synthesizing reports to a
  board-ready analysis in minutes, grounded in IDC research and more than 15 billion data points.
- Anthropic's Chief Commercial Officer notes IDC's 60 years of helping leaders make technology decisions.

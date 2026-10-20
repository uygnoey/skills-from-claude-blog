**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
An announcement that Code Review has left research preview and is generally available to Claude Team
and Enterprise organizations, with three changes since the preview: faster reviews, sharper findings,
and a per-repository review depth that admins choose.

## When is it useful?
- When an organization on Team or Enterprise is deciding whether to turn Code Review on, and for
  which repositories.
- When reviews from the preview felt too slow or too noisy for routine changes and you want to tune
  depth per repository instead of accepting one setting everywhere.
- When agent-assisted development has pushed up the volume of pull requests faster than human review
  capacity.

## Key points
- Code Review is out of research preview and generally available for Claude Team and Enterprise
  plans.
- Eligible Claude Enterprise organizations can claim at least $10,000 in Code Review credits by
  January 15, 2027; credits expire 30 days after they are claimed, and terms apply.
- Speed: most reviews now finish about 3x faster than during preview — roughly 20 minutes down to
  6–10 minutes.
- Quality: more of the bugs that matter, reported as clear, concise findings that state the problem,
  what triggers it, and the fix in a few sentences.
- Flexibility: admins choose Quick, Standard (the default), or Deep for each repository, so routine
  codebases get a quick pass and the most critical ones get a deep review. Every level delivers
  high-quality reviews.
- Anthropic runs Code Review on its own pull requests, which is part of how the team sees where
  reviews slow engineers down.
- Setup for admins: enable Code Review in Claude Code settings, install the GitHub App, and select
  the repositories to review. Developers need no configuration — reviews run automatically on new
  PRs.

## Bundled resources
- Skill: `code-review-rollout` — enabling Code Review for an organization and assigning a review
  depth per repository, with a reference on the three depth levels and the credit program.

## Source
- https://claude.com/resources/articles/code-review-is-now-generally-available

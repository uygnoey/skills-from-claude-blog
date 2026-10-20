# Review depth levels, and the GA credit program

## The three depth levels
Admins choose one of three review depths **per repository**. Standard is the default, and the
announcement is explicit that every level delivers high-quality reviews — the levels differ in how
much review a codebase gets, not in whether the review is any good.

| Level | Pick it for | What it is for |
| --- | --- | --- |
| Quick | Routine codebases | A quick pass, so ordinary changes are not over-reviewed |
| Standard (default) | Most repositories | The default balance; what you get if you choose nothing |
| Deep | The most critical codebases | A deep review where the cost of a missed bug is highest |

How to decide, in practice:
- Start every repository at Standard unless you already know it is routine or critical.
- Move a repository to **Quick** when its changes are mechanical or low-consequence and reviews feel
  noisy relative to the risk.
- Move a repository to **Deep** when a bug reaching production there is expensive — payments, auth,
  data integrity — or temporarily, while a risky migration lands.
- Revisit the setting with evidence from actual reviews rather than fixing it once at rollout.

## What changed at general availability
Three things shipped relative to the research preview:

- **Speed.** Most reviews finish about 3x faster: roughly 20 minutes during preview, down to 6–10
  minutes.
- **Quality.** More of the bugs that matter, reported as clear, concise findings that state the
  problem, what triggers it, and the fix in a few sentences.
- **Flexibility.** The per-repository Quick / Standard / Deep choice described above.

The motivation given: coding agents keep increasing the pace at which teams write code, and the
review bottleneck has not eased. Teams in the preview reported that Code Review was catching real
issues before a human reviewer looked at the PR, but asked for reviews that were quieter, sized to
each change, and faster. Anthropic also runs Code Review on its own pull requests, which shows the
team where reviews slow its own engineers down.

## Availability and credits
- Generally available to **Claude Team and Enterprise** organizations.
- **Eligible Claude Enterprise organizations can claim at least $10,000 in Code Review credits by
  January 15, 2027.**
- **Credits expire 30 days after you claim them**, so claim them when you are ready to run reviews,
  not before.
- Terms apply; check the official announcement and docs for the current terms.

## Setup recap
- **Admins:** enable Code Review in Claude Code settings, install the GitHub App, and select the
  repositories to run reviews on.
- **Developers:** nothing to configure. Once enabled, reviews run automatically on new pull requests.

## Source
[Code Review is now generally available](https://claude.com/resources/articles/code-review-is-now-generally-available)
(published 2026-10-15).

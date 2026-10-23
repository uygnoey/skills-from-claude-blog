# Lessons and reported results

## Why the old process broke
- Form -> BDR qualifies -> AE. Works when the team can talk to everyone.
- Tens of thousands of inbound requests per month; buyers sometimes waited multiple days.
- Reps spent time answering questions the docs already covered.

## Why Claude Managed Agents (beta)
- **Fast to production** - one engineer built the initial agent in a few weeks.
- **Tech and non-tech contributors** - engineering owned code; sales/content leads edited the system
  prompt in the Console; changes went to a staging agent first.
- **Focus on the domain, not the harness** - the platform runs the agent loop, sessions, and hosting.
- **Versioning** - every change saved as a version; v7 about a week into internal testing; weekly prompt
  changes after launch; new sessions can be pointed back to a previous version.
- **Flexibility** - scheduled runs give a path to other kinds of customer engagement.

## Lessons
1. **Give Claude a goal, not rules.**
2. **Less is more** - shorter prompts with the right knowledge and context beat long structured ones.
3. **Use SMEs in the development loop** - test early and often.
4. **Focus on what's right for the customer** - e.g. recommending Team over Enterprise when it fits.
5. **Treat every agent-to-rep escalation as feedback** - the share needing a person fell by about half.

## Reported results
- Thousands of conversations a day, around the clock.
- Escalated buyers become opportunities **more than 2x** as often as old form leads and close **about
  five days faster**.
- Buyers who talked to the agent before buying understood better what they were buying.
- Example rep: ~10 emails to close a deal became ~6; closed-won output up **2.5x**.
- Reps shifted time to earlier customer education, more live conversations, and in-person events.

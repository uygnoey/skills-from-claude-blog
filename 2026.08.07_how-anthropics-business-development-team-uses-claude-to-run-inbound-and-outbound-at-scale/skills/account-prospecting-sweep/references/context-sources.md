# Context sources for the sweep

From the post: "Claude connects to Salesforce, sales tools like Apollo and
Common Room, Gong, and our data warehouse, performs deep research, and validates
it against outbound guidance and ICP criteria that our team has curated."

Those are the sources the post names. The mapping below ties each to the
questions the sweep is trying to answer — "who are we in touch with, how do they
use Claude today, and what signals are relevant" — so a team with a different
stack can substitute equivalents rather than copy tool names.

## The questions and where they get answered

| Question | Source named in the post | What it contributes |
| --- | --- | --- |
| Who are we in touch with? | CRM (Salesforce) | Contacts, ownership, open opportunities, history |
| What has actually been said? | Call recordings (Gong) | What customers told us, in their words |
| Who else should we know? | Sales tools (Apollo, Common Room) | Contact discovery, community and engagement signals |
| How do they use the product today? | Data warehouse | Usage, adoption, product-level signals |
| Does any of this matter? | Curated outbound guidance + ICP criteria | The team's standard for relevance and fit |

## The validation layer

The first four rows are research. The last row is the part that makes the output
usable, and it is the part the team owns:

- **Outbound guidance** — how this team runs outbound, what a good play looks
  like, what not to do.
- **ICP criteria** — what a good-fit account looks like, concretely enough to
  score against.

Both are curated by the team, and both are read by the skill rather than encoded
in it. That keeps them correctable in one place, the same way the inbound side
keeps product facts in a knowledge base.

## Substituting your own stack

The pattern to preserve, in order:

1. **Relationship state** — whatever system of record holds contacts and deals.
2. **Conversation record** — whatever captures what was actually said on calls.
3. **Discovery and engagement signals** — whatever surfaces people and activity
   you are not already tracking.
4. **Product usage** — whatever warehouse holds how the account uses the
   product.
5. **Your team's written standard** — the guidance and ICP that turn the first
   four into a score and a play.

Dropping any of the first four narrows the brief. Dropping the fifth is what
turns a sweep into noise.

## Source

- https://claude.com/blog/how-anthropics-business-development-team-uses-claude-to-run-inbound-and-outbound-at-scale (August 7, 2026)

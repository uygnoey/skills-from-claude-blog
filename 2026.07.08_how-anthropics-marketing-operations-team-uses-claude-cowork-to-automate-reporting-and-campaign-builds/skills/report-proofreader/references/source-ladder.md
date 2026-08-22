# Source ladder

Not all sources are equally verifiable. This ladder is the basis for the verified /
unverified classification. The rungs come from the four places the post says metrics
actually live: a dashboard, a data warehouse, a Slack message, a call transcript.

## The rungs

### 1. Data warehouse query — verified
A query anyone can re-run and get the same answer. Record the query, not just the
result. This is the only rung where a figure is verified with no caveat.

### 2. Dashboard view — verified, with the refresh caveat
The dashboard is built on the warehouse, so the number is traceable — but a dashboard
can be stale. Record the view and its last refresh time. If the refresh predates the
period being reported, the figure is stale, not verified.

### 3. A prior report — inherited, never original
A number from last week's review is verified only if last week verified it. Inherited
status does not upgrade with age. If last week marked it unverified, it is still
unverified.

### 4. Slack message — unverified
Someone stated a number in a thread. Useful, often the only place a new metric exists,
and not verifiable. Include with provenance and an explicit unverified label, or cut
it. Log it as a candidate for the warehouse.

### 5. Call transcript — unverified
Same as a Slack message, with the additional risk that a spoken number may have been
approximate or misheard. Quote the segment.

### 6. No traceable source — do not ship
If the figure cannot be traced at all, it does not appear in the report as a number.
It becomes an open question.

## Definitional mismatches

The hardest cases are not wrong numbers but different definitions of the same thing.
Common causes:

- **Reorgs.** A sales reorg changes the grouping, so two reports that were consistent
  last quarter disagree this quarter. This happened, and the correct behaviour was to
  flag the gap and ask.
- **Regional structures.** Whether a region is defined by billing address, account
  owner, or user location.
- **Date boundaries.** Week ending Friday versus Sunday; booked date versus recognised
  date.
- **Segment edges.** Where "enterprise" starts.

For each of these, the resolution is a person's decision. Once made, it goes back into
the reporting skill so the same question does not recur weekly. This is the loop the
post describes: turn a correction you have made twice into a skill update.

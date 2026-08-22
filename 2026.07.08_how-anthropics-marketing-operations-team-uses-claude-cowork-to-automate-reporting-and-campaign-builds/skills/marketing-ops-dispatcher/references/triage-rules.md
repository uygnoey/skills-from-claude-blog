# Triage rules

One request per hourly run. These rules decide which one.

## Ranking

1. **Event date proximity.** An event build that starts too late cannot be recovered
   by working faster afterwards — the registration page has to exist before people can
   register. Nearest event date wins.
2. **Blocked work.** A request that other people are waiting on (an approval that
   gates an announcement, a list needed for a send today).
3. **In-flight changes.** Apply-to-attend changes to a registration flow that is
   already live affect people currently trying to register.
4. **Request age.** Oldest unstamped request, so nothing starves at the bottom of the
   channel.

## Complexity is not urgency

The event build is the most complex request type, which is a reason to start it early
— not a reason to always rank it first. A data import needed for a send in two hours
outranks an event four weeks out.

## Starvation guard

If a request has been unstamped for more than a set number of runs, promote it
regardless of the other criteria. A queue where a low-urgency request is never picked
is a queue that quietly loses work.

## What is never picked

- A ticket that already carries a stamp.
- A request with no type selected — ask in the channel instead, and leave it unstamped.
- A duplicate of an already-stamped request — note it in the channel as a duplicate.

## The stamp

Stamp before handing off, never after. The stamp records:

- Which run picked it up, and when.
- Which specialist it was routed to.
- Any secondary work noted (for requests that span two types).

Stamping after handoff leaves a window in which the same ticket can be picked up
twice — by the next run, by another agent, or by a person watching the channel.

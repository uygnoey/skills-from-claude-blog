# Clustering personas to cut inference cost

This example is a generalized version of the pattern described for Sim Francisco in the post.

## Starting point

You model many entities (e.g., 10,000 synthetic residents) and initially do one model call per entity per event. This is expensive.

## Approach

1. Create a pool of entities with attributes (demographics, history, worldview).
2. Cluster entities into a smaller set of representative personas (e.g., a few hundred).
3. For each event/news item, run inference on representative personas and expand results back to the full population (weighted by cluster sizes).
4. Validate that aggregate outputs still match baselines (historical results, known distributions, or external benchmarks).

## Expected outcome

A large reduction in calls (and cost), while keeping accuracy close to the original method.

## Source

- https://claude.com/blog/meet-the-winners-of-our-claude-opus-4-8-build-day-hackathon

# Example: optimize a slow dashboard function

## User message

"This function is slowing down our user dashboard. How can I make it faster?"

(Then paste the function.)

## Expected analysis checklist

- Identify nested loops and complexity (e.g., \(O(n^2)\)).
- Check for database calls or network requests inside loops.
- Suggest refactors such as batching, precomputing lookups (hash maps), or moving I/O outside loops.
- Provide a rewritten function and explain why it is faster.

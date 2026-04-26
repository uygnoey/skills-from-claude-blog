# Grounded Q&A examples

## Example 1: Document summarization with citations
**Input**: A long PDF policy document

**Request**: “Summarize the policy changes and cite each bullet to the relevant passage.”

**Expected output characteristics**
- Each bullet includes at least one citation.
- If a change is implied but not explicit, the model should label it as an inference and still cite the supporting passage.

## Example 2: Complex Q&A across multiple sources
**Input**: Multiple financial statements

**Request**: “What were the drivers of margin change? Cite the exact sections.”

**Expected output characteristics**
- Each driver is traceable to a specific statement section.
- Claims not present in the sources are marked “not found in sources.”

## Source
- https://claude.com/blog/introducing-citations-api

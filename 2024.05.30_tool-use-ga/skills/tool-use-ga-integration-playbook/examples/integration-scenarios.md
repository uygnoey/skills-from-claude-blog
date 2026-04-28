# Example integration scenarios (prompt ideas)

These are scenario prompts derived from the use cases described in the post.

## Support Q&A with an external knowledge base
User prompt: “Do you support SSO on the Team plan?”

Expected tool strategy: call a knowledge base search tool and answer using the returned article.

## Invoice intake extraction
User prompt: “Extract vendor name, invoice date, and total due from this invoice text.”

Expected tool strategy: call an extraction tool or return a structured result suitable for downstream systems.

## Subscription management action
User prompt: “Cancel my subscription effective immediately.”

Expected tool strategy: call an account API tool with the correct account identifier and action.

Source: https://claude.com/blog/tool-use-ga

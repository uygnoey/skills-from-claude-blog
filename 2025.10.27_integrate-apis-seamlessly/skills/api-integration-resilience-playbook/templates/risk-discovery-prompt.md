# Risk discovery prompt (Claude.ai)

Use this prompt in Claude.ai before writing any integration code. Paste the API specification or doc URL into the conversation, then send the prompt.

---

I'm preparing to integrate the following third-party API into a production system:

<paste API name, doc URL, and the specification or relevant excerpts here>

Please give me **integration risks ranked by likelihood**, focused on what is most likely to break in production. For each item, include:

1. The failure mode (e.g. "tokens expire mid-request during multi-step flows").
2. The trigger condition (when it happens).
3. The concrete mitigation (e.g. "add exponential backoff for 429 responses with jitter to prevent thundering herd").
4. Anything specific to this vendor's documentation that I should not miss (rate-limit counting method, idempotency keys, required headers, webhook delivery guarantees, field-level nullability).

Do **not** suggest generic "implement error handling." Every recommendation must be concrete and tied to this API.

If the documentation is ambiguous, say so explicitly and recommend what to verify with the vendor.

---

Source: [How to integrate APIs seamlessly](https://claude.com/blog/integrate-apis-seamlessly) (2025-10-27).

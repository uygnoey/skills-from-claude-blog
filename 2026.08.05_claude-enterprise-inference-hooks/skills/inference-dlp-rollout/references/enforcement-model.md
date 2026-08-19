# Enforcement model

What the inline DLP checkpoint inspects, and what each control changes. Everything here is drawn from the source post; anything the post does not state is listed as a question to answer for your own deployment.

## Path of a request

1. A user or agent triggers an inference request on an enterprise AI surface.
2. The request is routed over a **signed WebSocket connection** to the organization's security server.
3. **Before the model starts generating**, the prompt and its surrounding context are sent to that server.
4. The server returns a verdict: **allow** or **deny**.
5. Generation proceeds only once a verdict has been received.

## Path of a tool call

1. The model calls a tool — including tools reached through MCP connectors, skills, and plugins.
2. The tool produces a response.
3. **Before the response is returned to the model**, it is checked the same way.
4. The verdict decides whether the model ever sees the content.

This second path matters more than it first appears: a connector reaching a document store or ticketing system can pull restricted content into the context window without a human ever typing it.

## Coverage

One organization-level configuration applies across enterprise surfaces, including:

- Chat
- Claude Code
- Claude Cowork
- Tool calls made through MCP connectors, skills, and plugins

The point of the single configuration is that there is no separate integration or per-product agent to maintain.

## Controls

| Control | What it does | Failure mode it prevents |
|---|---|---|
| **Shadow mode** | Evaluates every request but always allows | Enforcing untuned rules on real users |
| **Role-based exclusions** | Exempts named roles from enforcement | Locking out break-glass and administrative access |
| **Percentage-based rollout** | Enforces for a fraction of the population | An org-wide outage caused by one bad rule |
| **Failure policy** | Decides what happens when no verdict arrives | Silent, unexamined gaps in coverage |
| **Timeout** | Bounds how long a request waits for a verdict | Unbounded latency on every inference |

## Protocol

The protocol is **webhook-based with a published schema**. Two consequences:

- An organization can point at a server it already runs — commercial platforms such as Netskope, Palo Alto Networks, Proofpoint, or Zscaler, or an AI security server built in-house.
- A security vendor can build an integration against the documented schema, after which customers point their organization at that platform by configuration.

## Questions the post does not answer for you

Answer these from the vendor documentation before implementing, not from assumption:

- The exact request and response payload shape, and the schema version.
- How the WebSocket connection is authenticated and how signing keys are rotated.
- What context accompanies a prompt — how much history, and whether attachments or tool schemas are included.
- Whether verdicts can carry a reason string that reaches the user.
- Retention and logging behaviour on the platform side versus your server's side.

## Availability

At the time of the post, inference hooks is in **beta for Claude Enterprise** customers. Confirm current availability and the configuration surface before planning a date-bound rollout.

## Source

- https://claude.com/blog/claude-enterprise-inference-hooks

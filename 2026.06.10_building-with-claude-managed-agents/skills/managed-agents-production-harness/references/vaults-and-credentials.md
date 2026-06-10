# Vaults and credential separation (reference)

From the source post:

- When everything runs in one container, tool-executing code can sit next to credentials, increasing exposure if a prompt injection convinces the model to read its environment.
- Claude Managed Agents keeps credentials out of the sandbox.
- Tokens for tools like MCPs, CLIs, and GitHub repositories live in a separate vault.
- A proxy fetches and decrypts credentials only on demand.
- Vault credentials are protected with envelope encryption before storage, and retrieval requires a signed request token.

## Design checklist

- [ ] No long-lived tool tokens are present in the execution sandbox environment.
- [ ] Secret retrieval is mediated by a dedicated component/service.
- [ ] Secrets are decrypted only when needed.
- [ ] Access is auditable (who/what/when retrieved which secret).

## Source

- https://claude.com/blog/building-with-claude-managed-agents

# Governance and controls

The AI-native SDLC keeps the old control objectives and changes the enforcement. Controls become
version-controlled rules the agent reads and obeys, rather than meetings that happen weekly or
monthly. Humans remain accountable for every decision that requires judgment; what shifts is where
human attention lands.

## The four layers

| Layer | Nature | What it does | Where it lives |
|---|---|---|---|
| Skills | Advisory | Makes the policy likely to be applied while the code is written | `.claude/skills/<name>/`, or a plugin for org-wide distribution |
| Hooks | Deterministic | Allows, asks, or blocks on every matching action | `.claude/settings.json` in git; managed settings for non-negotiables |
| Branch protection | Separation of duties | Forces agent output through a human review gate | The version-control platform |
| Managed settings | Org-wide, non-overridable | Prevents any engineer, project file, or CLI flag from widening the rules | MDM or the admin console |

A skill alone is not enough for a policy that must always hold. Put something deterministic behind
it — a hook that blocks the action, or a review pass that re-checks the policy at the PR. The skill
makes violations rare; the hook makes them close to impossible.

## Evidence and audit trail

- **Git history** — the intent, the spec, the plan, the diff, the tests, and the review findings,
  each with an author and a timestamp. The chain of commits records who asked for what, what the
  agent produced, and who approved it.
- **PR history** — findings, fixes, ratings, and approvals.
- **Session transcripts** — skill invocations, hook allow/block verdicts, and the literal output of
  the commands the agent ran, forwarded by the OpenTelemetry export to the organization's
  observability stack.
- **Non-interactive runs act under the agent's own identity**, so the pipeline log separates what
  the agent did from what the engineer who triggered it did.

## Worked example — managed settings for a regulated enterprise

Deployed by the platform team via MDM or the admin console; engineers cannot edit or override any of
it.

```json
{
  "permissions": {
    "deny": [
      "Read(.env*)", "Read(./secrets/**)",
      "WebFetch", "Bash(curl *)", "Bash(wget *)"
    ],
    "allow": [
      "Bash(git *)", "Bash(make build)",
      "Bash(make test)", "Bash(make lint)"
    ],
    "disableBypassPermissionsMode": "disable"
  },
  "allowManagedPermissionRulesOnly": true,
  "sandbox": {
    "enabled": true,
    "failIfUnavailable": true,
    "allowUnsandboxedCommands": false,
    "network": { "allowedDomains": ["git.internal.example.com",
                                    "registry.npmjs.org"] },
    "credentials": {
      "files": [
        { "path": "~/.ssh", "mode": "deny" },
        { "path": "~/.aws/credentials", "mode": "deny" }
      ],
      "envVars": [ { "name": "GITHUB_TOKEN", "mode": "deny" } ]
    }
  },
  "allowManagedHooksOnly": true,
  "disableSideloadFlags": true,
  "allowManagedMcpServersOnly": true,
  "strictKnownMarketplaces": [
    { "source": "github", "repo": "example-corp/approved-plugins" }
  ],
  "requiredMinimumVersion": "2.1.193"
}
```

### What each line buys, in control terms

- **`permissions.deny`** keeps secrets out of the agent's context and blocks arbitrary network
  egress through tools. **`permissions.allow`** pre-approves the safe inner loop so the deny list
  does not turn into prompt fatigue.
- **`disableBypassPermissionsMode`** plus **`allowManagedPermissionRulesOnly`** means no engineer,
  project file, or command-line flag can widen the rules.
- **`sandbox`** closes the gap permissions cannot. A tool-level deny on `WebFetch` does not stop a
  shell command reaching the network; the OS-level domain allowlist blocks egress outright.
- **`failIfUnavailable`** and **`allowUnsandboxedCommands`** make the sandbox a gate: Claude Code
  refuses to start when the sandbox cannot initialize, and a command that fails inside the sandbox
  cannot be retried outside it.
- **`credentials`** closes the gap the deny rules leave open. `permissions.deny` governs Claude's
  file tools, but a sandboxed shell command could still read `~/.ssh` or `~/.aws/credentials` by
  default; this block denies those reads and strips the named secrets from the environment of every
  sandboxed command.
- **`allowManagedHooksOnly`** means the approval gates are the only hooks that run; nothing local
  can add to or replace them.
- **`disableSideloadFlags`** and **`strictKnownMarketplaces`** mean every skill, agent, hook, and MCP
  server on an engineer's machine arrived through the organization's approved plugin marketplace,
  never from a home directory.
- **`allowManagedMcpServersOnly`** makes the agent's tool surface an allowlist owned by the platform
  team.
- **`requiredMinimumVersion`** refuses to start on a version below the approved floor, so the
  controls are enforced by a build the organization has actually assessed.

**Treat this as a starting point to tailor, not a recommendation to copy.** Every deny trades against
capability, and the right balance depends on the data classification of the repo. The settings
reference documents every key, including the managed-only ones:
<https://code.claude.com/docs/en/settings>

## Where governance sits, stage by stage

| Stage | What is enforced | Who approves |
|---|---|---|
| Plan | The committed intent carries author, timestamp, and revision history | Product owner, via merge or closing review |
| Design | Live policy applied as skills while the spec is written; prompt and skill versions logged | Product owner, with named policy owners on flagged concerns |
| Build | Plan mode blocks edits until the plan is accepted; hooks block protected paths and credentials | Engineer for routine changes; tech lead or architect for higher risk |
| Test | Verification before "done"; the agent cannot edit test files during a fix | Code owner at the PR |
| Deploy | `REVIEW.md` applied to all PRs; branch protection; the production gate hook | A human code owner, and a named release manager at the gate |
| Maintain | Tier boundaries from version-controlled config; permissions and managed settings deny production access | Service owner triages; changes go through the normal review gate |

**Separation of duties is preserved throughout**: the agent that wrote the code has no way to approve
it, and the agent may act up to the production gate and cannot pass it.

## Documentation a platform team needs

Roughly in rollout order:

- Set up Claude Code for your organization — the admin decision map: <https://code.claude.com/docs/en/admin-setup>
- Settings reference and precedence, including every managed-only key: <https://code.claude.com/docs/en/settings>
- Server-managed settings from the admin console: <https://code.claude.com/docs/en/server-managed-settings>
- Permissions: <https://code.claude.com/docs/en/permissions>
- Sandboxing — OS-level filesystem and network isolation: <https://code.claude.com/docs/en/sandboxing>
- Hooks guide: <https://code.claude.com/docs/en/hooks-guide> · Hooks reference: <https://code.claude.com/docs/en/hooks>
- Skills: <https://code.claude.com/docs/en/skills>
- Plugins and private marketplaces: <https://code.claude.com/docs/en/plugin-marketplaces>
- Managed MCP — central control of the agent's tool surface: <https://code.claude.com/docs/en/managed-mcp>
- Enterprise deployment overview (Bedrock, Vertex, Foundry): <https://code.claude.com/docs/en/third-party-integrations>
- Enterprise network configuration: <https://code.claude.com/docs/en/network-config>
- Monitoring (OpenTelemetry): <https://code.claude.com/docs/en/monitoring-usage>
- The analytics dashboard: <https://code.claude.com/docs/en/analytics>
- Compliance API — enterprise activity feed, chat retrieval and deletion: <https://platform.claude.com/docs/en/manage-claude/compliance-api>
- Security model: <https://code.claude.com/docs/en/security>

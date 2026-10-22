# Submission portal and directory — reference

Summary of the "Build plugins for Claude" announcement (2026-09-25). Refer to the original post and
the official plugin build docs for anything not listed here.

## What a plugin can contain
| Surface | Allowed contents |
|---|---|
| Claude (directory) | MCP connectors, Agent Skills, or both |
| Claude Code (bundle) | Also LSPs, commands, hooks, and agents |

## Submission paths
| Path | Input | Typical fit |
|---|---|---|
| Single MCP connector | URL of a remote MCP server | One hosted integration |
| Plugin bundle | GitHub repository with MCP servers and skills | Multiple pieces shipped together |

## Review lifecycle
1. Submit (paid Claude plan required).
2. Automatic validation and safety scan on submit.
3. Portal shows review status, scan results, and recommended changes.
4. After approval, the developer chooses when to publish.

## Post-publish analytics
- **Usage analytics** — installs by product surface and by version.
- **Discovery metrics** — listing views and the searches that lead to them.

## MCP support
- Latest MCP spec with a stateless core ("MCP 2.0").
- **MCP Apps** — interactive UI in chat.
- **Enterprise Managed Auth** — zero-touch OAuth for enterprise users.
- More MCP features are announced as coming.

## Roadmap stated in the post
- One discovery experience across Claude and Claude Code over the following weeks.
- Skills and MCP connectors stay listed as building blocks.
- Later: convert a connector listing into a plugin.
- Existing skills, connectors, and plugins need no changes.

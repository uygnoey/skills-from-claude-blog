---
name: plugin-directory-submission
description: Plan, package, and submit a third-party extension to the Claude directory as a plugin. Covers what a plugin can bundle (MCP connectors, Agent Skills, or both; in Claude Code also LSPs, commands, hooks, and agents), the two submission paths in the developer portal (a single remote MCP connector, or a GitHub-hosted plugin bundle), automatic validation and safety scanning, reviewing status and recommended changes, choosing when to publish, reading install and discovery analytics, and the MCP 2.0 extensions (MCP Apps for interactive UI, Enterprise Managed Auth for zero-touch OAuth). Use when a developer wants to ship a connector or skill to Claude users, decide between a connector listing and a plugin bundle, or prepare for directory review.
---

## Purpose
Plugins are the main way to build third-party extensions for Claude. A plugin packages MCP
connectors, Agent Skills, or both, and approved plugins are listed in the Claude directory. This
skill walks a developer from "what should I ship?" to a published listing, using only what the
announcement states. Portal and directory details are summarized in
[references/submission-portal.md](references/submission-portal.md).

## When to use
- A developer wants Claude users to discover and install their integration.
- Someone must choose between submitting one MCP connector and a full plugin bundle.
- A team is preparing for review and wants to know what is checked.
- A publisher wants to know what analytics exist after launch.

## Instructions

1. **Check eligibility.** The submission portal is open to developers on paid Claude plans.

2. **Decide what the extension is.**
   - Only a remote MCP server → submit a **single MCP connector** by pointing the portal at the
     remote server.
   - Several MCP servers and/or skills → submit a **plugin bundle** hosted on GitHub.
   - Targeting Claude Code as well → the bundle may also carry LSPs, commands, hooks, and agents.

3. **Consider the MCP 2.0 extensions.** Claude supports the latest MCP spec with its stateless core.
   - **MCP Apps** — interactive UI rendered in the chat.
   - **Enterprise Managed Auth** — zero-touch OAuth for enterprise users.
   Use them when the extension needs UI in chat or enterprise sign-in without per-user OAuth steps.

4. **Submit and read the results.** On submit, the portal validates the plugin automatically and
   runs a safety scan. Track review status, scan results, and recommended changes in the portal and
   address the recommendations before resubmitting.

5. **Publish on your schedule.** Approval does not publish automatically; the developer chooses when
   to publish the listing.

6. **Measure after launch.** Usage analytics show installs by product surface and by version.
   Discovery metrics show listing views and the searches that led to them. Use them to decide what
   to improve in the listing or the next version.

7. **Do not rebuild existing work.** Existing skills, connectors, and plugins need no changes. A
   single discovery experience is rolling out across Claude and Claude Code; skills and connectors
   stay as building blocks the directory keeps listing, and turning a connector listing into a
   plugin is planned for later. For build specifics, refer to the official plugin build docs
   linked from the original post.

## Examples
- Developer: "I only have a hosted MCP server for our ticketing API."
  → Submit a single MCP connector pointing at the remote server; no GitHub bundle is needed.
- Developer: "We have two MCP servers and three skills, plus a hook for Claude Code users."
  → Package them as one GitHub-hosted plugin bundle; hooks are allowed in Claude Code bundles.
- Developer: "We want a dashboard widget in the chat and SSO-friendly auth for enterprise customers."
  → Use MCP Apps for the interactive UI and Enterprise Managed Auth for zero-touch OAuth.
- Developer: "Our listing gets views but few installs."
  → Check discovery metrics (which searches lead to the listing) against installs by surface and
  version, then revise the listing or the release.

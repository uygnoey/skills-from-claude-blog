**English** · [한국어](./chrome-side-panel-adoption.ko.md) · [Español](./chrome-side-panel-adoption.es.md) · [日本語](./chrome-side-panel-adoption.ja.md)

# Adopting the Cowork side panel in Chrome

A guide for individuals and admins rolling out the change described in
[The Claude in Chrome side panel is now Claude Cowork](https://claude.com/blog/cowork-chrome-side-panel).
Everything here comes from that announcement.

## 1. What actually changed

The Claude in Chrome side panel now runs a **Claude Cowork session**.

- Conversations are saved to your history.
- Your skills and connectors work in the browser.
- A task started in a tab can be finished on the Claude desktop, web, and mobile apps.
- Sessions live with your **account**, not a single device.

Before this, a side-panel session was separate from those in the Claude apps, so context
and conversations didn't carry between them.

## 2. Why the browser is a surface at all

Many tools connect directly to Claude. Others don't — internal dashboards, legacy systems,
vendor portals. Claude in Chrome is a browser extension that lets Claude see the page you're
on and act in it: clicking links, typing text, navigating between pages, and filling out
forms, using your existing logins. That is how Claude reaches the tools that have no
connector.

## 3. A worked example

Say you're putting together a budget spreadsheet and need invoices from several vendor
portals. Ask Claude in Chrome to collect the amounts and dates: it opens the tabs, reads
each invoice, and builds the spreadsheet. Then pick the session up in the desktop app to
add files from your computer, or import last month's budget and ask what's changed. Context
is maintained across surfaces as you work.

## 4. The risk, stated plainly

Claude in Chrome carries the same risks as any AI agent acting in a browser, **chiefly
prompt injection**. Malicious actors hide instructions in web content — a page, an email, a
document. Those instructions may not be visible to you, and they can redirect Claude to
take actions you never intended.

## 5. The guardrails

**The action check.** Since the pilot, there is a check on Claude's own actions. Turn on
"automatically approve" and Claude works through a task without stopping for permission at
every step. But before anything consequential — submitting a form, sending a message,
downloading a file — a separate check reviews the action against what you originally asked
for and blocks anything that doesn't match. Fewer interruptions, oversight maintained.

**Hard stops.** Claude still asks before certain irreversible or costly actions, like making
a purchase or sharing personal data.

**The limit.** These measures meaningfully reduce the risk but cannot eliminate it. Prompt
injection is a moving target; new attacks keep being hunted for and what's learned is built
into each model released. Start on sites you trust — the safety guide has more best
practices.

**Practical consequence.** The action check compares against your *original request*. A
vague request gives it little to work with. Say which sites are in scope, what data to
collect, what artifact to produce, and which consequential actions are legitimately
expected.

## 6. Rollout

**Individuals.** Install Claude in Chrome from the Chrome Web Store, sign in, and open the
side panel. The new side panel is on Max and Team plans today, and is rolling out to Pro
users over the coming weeks.

**Admins.** On Enterprise plans, Claude in Chrome is **off by default**. Admins can turn it
on and limit it to approved domains. See the admin setup guide. Practical sequence:

1. Decide whether the browser surface is needed at all — it earns its place where staff
   work in systems with no connector.
2. Draw up the approved-domain list from those systems, rather than opening the extension
   broadly.
3. Enable, then widen the domain list as specific needs are established.

## 7. What this does not cover

- You still need the Claude desktop app to work with files on your computer or with other
  applications.
- Claude in Chrome doesn't run on other Chromium browsers.
- It doesn't run on mobile yet.

## 8. Adoption checklist

- [ ] Confirmed the plan supports the new side panel (Max/Team today; Pro rolling out).
- [ ] On Enterprise: admin has enabled Claude in Chrome and set the approved domains.
- [ ] Extension installed from the Chrome Web Store and signed in.
- [ ] Identified the specific no-connector systems the browser surface is for.
- [ ] Team knows to write scoped task briefs so the action check has something to compare against.
- [ ] Team knows the handoff path: browser → desktop for local files and other applications.
- [ ] Team knows that page content is data, not instructions.

## Source

- https://claude.com/blog/cowork-chrome-side-panel

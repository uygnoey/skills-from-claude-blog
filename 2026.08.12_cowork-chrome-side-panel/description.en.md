**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
An announcement that the **Claude in Chrome side panel now runs a Claude Cowork session**. Until now a side-panel conversation was separate from the ones in the Claude apps, so context did not carry between them. Now conversations are saved to your history, your skills and connectors work in the browser, and a task you start in a tab can be finished on the Claude desktop, web, and mobile apps — because sessions live with your account rather than a single device. It is available on Max and Team plans today and rolling out to Pro users over the coming weeks.

The post frames the point of the browser surface: many tools connect directly to Claude, but others don't — internal dashboards, legacy systems, vendor portals — and Claude in Chrome can work in those through the browser, using your existing logins to click links, type text, navigate, and fill out forms. It then treats the risk directly. Claude in Chrome carries the same prompt-injection exposure as any AI agent that acts in a browser: instructions hidden in a page, an email, or a document — possibly invisible to you — can redirect Claude. Since the pilot, a check on Claude's own actions has been added: with "automatically approve" on, Claude works without stopping at every step, but before anything consequential (submitting a form, sending a message, downloading a file) a separate check reviews the action against what you originally asked for and blocks anything that doesn't match. Claude still asks before certain irreversible or costly actions. The post is explicit that these measures reduce but cannot eliminate the risk.

## When is it useful?
- When the work lives in a tool that has no direct Claude connector — an internal dashboard, a legacy system, a vendor portal.
- When a task starts in the browser and has to be finished somewhere with local files, or vice versa.
- When you are deciding how much autonomy to give a browser agent, and want the actual guardrail model rather than a slogan.
- When an admin is turning Claude in Chrome on for an Enterprise organization and needs to scope approved domains.

## Key points
- **The side panel is a Cowork session.** Conversations are saved to your history; skills and connectors work in the browser.
- **Sessions follow the account, not the device.** Start in a tab, continue in the desktop, web, or mobile app — context carries across surfaces.
- **What Claude can do in a page:** see the page you're on, click links, type text, navigate between pages, and fill out forms, using your existing logins.
- **Why the browser matters:** it reaches internal dashboards, legacy systems, and vendor portals that don't connect to Claude directly.
- **Worked example from the post:** ask Claude in Chrome to pull invoice amounts and dates from several vendor portals and build a budget spreadsheet; then pick the session up in the desktop app to add local files or import last month's budget and ask what's changed.
- **Prompt injection is the chief risk.** Malicious instructions hidden in web content — a page, an email, a document — may be invisible to you and can redirect Claude to actions you never intended.
- **Action check.** With "automatically approve," a separate check reviews each consequential action (submitting a form, sending a message, downloading a file) against your original request and blocks anything that doesn't match — fewer interruptions, oversight retained.
- **Hard stops remain.** Claude still asks before certain irreversible or costly actions, such as making a purchase or sharing personal data.
- **Stated limit.** These measures meaningfully reduce the risk but cannot eliminate it; prompt injection is a moving target. Start on sites you trust.
- **Availability.** Max and Team today; Pro rolling out over the coming weeks. On Enterprise, Claude in Chrome is **off by default** — admins turn it on and can limit it to approved domains.
- **Not covered.** You still need the desktop app for files on your computer or other applications; Claude in Chrome doesn't run on other Chromium browsers or on mobile yet.

## Bundled resources
- `skills/browser-side-panel-sessions/SKILL.md` — decide when to run a task in the browser, hand it off across surfaces, and set the right autonomy level.
- `skills/browser-side-panel-sessions/references/risk-and-guardrails.md` — the prompt-injection risk and the guardrail model, as stated in the post.
- `skills/browser-side-panel-sessions/references/surface-capabilities.md` — what each surface can and cannot do, plus availability by plan.
- `skills/browser-side-panel-sessions/templates/browser-task-brief.md` — a fill-in brief that makes the action check's job easier.
- `guides/chrome-side-panel-adoption.{en,ko,es,ja}.md` — the full adoption and admin guide in four languages.

## Source
- https://claude.com/blog/cowork-chrome-side-panel

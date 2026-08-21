**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
An update on how Anthropic is getting frontier cyber defense capability into more defenders' hands. Claude Mythos 5 is now available in Claude Security and coming soon to partners' cyber defense tools; a $35M Defender Advantage Fund backs open-source security work; and the Cyber Verification Program is expanding toward Mythos-class access.

The organizing idea is about the shape of the interaction, not the size of the model. Direct model access is where a malicious actor can try to steer a model toward harmful uses. If users can only receive specific outputs — a patch for a vulnerability, a security alert — that risk is much lower. Each of the four access paths gives defenders more access to defensive *results* while keeping guardrails on direct access to the model.

## When is it useful?
- When deciding which access path fits your situation: own the code, build security products, support open-source maintainers, or need reduced safeguards for authorized defensive work.
- When an enterprise admin is enabling Claude Security and pointing a team at a repository scan.
- When triaging scan findings that arrive with a CWE category, confidence and severity ratings, and a suggested fix.
- When designing a product or workflow on top of frontier capability and you need to preserve the "specific outputs, not model access" shape.
- When an open-source project needs resourcing to patch vulnerabilities or automate scanning.

## Key points
- **Interaction shape is the control.** "If users can only receive specific outputs, such as a patch for a vulnerability or a security alert, that risk is much lower" than direct model access.
- **Project Glasswing** (April) put Mythos Preview and Mythos 5 with a small group securing the world's most critical software, buying defenders a window before comparable capability became broadly available. **Claude Fable 5** was the first broad step — widely available, dual-use cyber work blocked.
- **Partner integrations:** Mythos 5 is being built into the products defenders already run for security operations, incident response, threat intelligence, and detection engineering. End users work through a purpose-built interface that runs Mythos in the background for a defined task and receive only the intended artifact — suggested patches, say, with no way to prompt for an exploit. Abuse prevention measures verify the model stays in scope.
- **Claude Security scans now run on Mythos 5.** Public beta for Claude Enterprise; admins enable it in the admin console; from `claude.ai/security` you select a repository; findings return with CWE category, confidence and severity ratings, and a suggested fix. Billed as standard token usage, no separate add-on.
- **Patching keeps a human gate.** Open Claude Code on the web to implement a fix. Interactive patching uses the models your organization has in Claude Code — the Mythos scan does not extend Mythos access to other surfaces — and every patch must be reviewed and approved by a human.
- **Defender Advantage Fund (0xDAF):** $35M in Claude credits for organizations helping open-source maintainers, focused on patching live vulnerabilities, automating scanning and patching replicably, and pursuing approaches resistant to whole classes of attack. Builds on $4M in direct donations and coordinated efforts like Akrites and Gold Eagle under Glasswing. Starting with a small number of larger pilot grants.
- **Cyber Verification Program expansion:** vetted defenders already get reduced safeguards on Opus and Sonnet. Over the coming weeks, defensive capabilities like vulnerability triaging and validation expand to Mythos-class models, with fewer blocks on Opus- and Sonnet-class. Glasswing access continues with U.S. Government partners for critical-infrastructure protectors meeting strict security control requirements.

## Bundled resources
- `skills/security-scan-triage/SKILL.md` — the enable-scan-triage-patch workflow, the human approval gate, and how to choose among the access paths.
- `skills/security-scan-triage/references/access-paths.md` — the four paths in detail, with the Glasswing background and a selection table.
- `skills/security-scan-triage/templates/finding-triage-report.md` — a per-finding triage table and detail block built around CWE, confidence, severity, verification, decision, and approver.
- `guides/defensive-capability-access.{en,ko,es,ja}.md` — the full announcement walkthrough in four languages.

## Source
[Bringing the cybersecurity capabilities of Claude Mythos 5 to more defenders](https://claude.com/blog/bringing-claude-mythos-5-to-more-defenders) — August 21, 2026.

**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
A customer story on how security teams at Comcast and Booz Allen used Claude Mythos Preview, through
Project Glasswing (Anthropic's limited-access program for defenders of critical infrastructure), to
find, validate, and fix vulnerabilities that existing scanners missed — especially exploit chains,
where small weaknesses combine into a serious attack path.

## When is it useful?
- When a security team plans model-assisted review across a large software portfolio.
- When findings outpace the team's ability to validate and route them.
- When looking for cross-component or cross-language flaws that single-bug scanners miss.

## Key points
- Comcast assessed 258 business-critical systems (~170 million lines of code). The model found a
  critical authentication vulnerability in a public-facing platform that came from several
  components that each looked correct alone. Engineers validated it against the running app, traced
  root cause, fixed it, and verified it had not been exploited.
- Comcast's CISO, Noopur Davis: validating the volume of findings is now the bottleneck, not
  discovery.
- Booz Allen found a boot-time firmware flaw: an unprotected security key let an attacker substitute
  their own key and suppress lock-or-erase behavior. The model traced it across two programs in two
  languages and helped draft fixes and evidence for system owners.
- Teams still validate findings, deduplicate systemic patterns, and route issues to owners. One Booz
  Allen analyst covered a portfolio review in twelve days instead of months with a larger team.
- Humans keep the judgment calls; Anthropic will expand access through the Cyber Verification
  Program (CVP).

## Bundled resources
- Skill: `exploit-chain-validation` — post-discovery workflow (validate, root cause, exploitation
  check, fix, dedupe, route), with a finding evidence packet template.

## Source
- https://claude.com/resources/articles/how-comcast-booz-allen-use-claude-mythos-to-secure-their-codebases

# Prerequisites checklist

Much of this runs through teams outside the modernization — platform/infrastructure for the host,
QA or release engineering for test capacity, security and compliance for approvals. Each has its own
backlog or approval process, so open conversations as soon as requirements are identified.

## Environment
- [ ] A dedicated remote host for running the workflow, with the codebase and other relevant sources reachable by Claude
- [ ] Test capacity as required by the certificate
- [ ] Anything that strengthens the certificate: production telemetry, a prod-parallel setup, or production data for replay

## Codebase and CI/CD
- [ ] A dependency map grounded in build and compile logs, import analysis, or runtime traces (the plugin's `map` command is a starting point; large or old codebases may need more upfront work)
- [ ] Planned treatment of any dependencies or packages, as part of the target definition
- [ ] A compatibility check ready to add to CI/CD, if needed
- [ ] An agreed code-freeze policy, if modernizing in place
- [ ] A communication plan for active developers covering code freezes and new compatibility requirements

## Teams and review
- [ ] Agreement from dependent teams on how they take part (signing off on the certificate, reviewing under the promotion policy), with reviewer time set aside

## Security and compliance
- [ ] A model access path for Claude Code approved for source code
- [ ] Least-privilege access for the workflow: write only to modernization branches, no production credentials
- [ ] Secrets and PII scrubbed or masked from the modernization branch
- [ ] Every change traceable, with each PR linked to an agent transcript and certificate evidence
- [ ] License and vulnerability checks on new dependencies

# Self-hosted environment rollout checklist

A working checklist derived from the August 6, 2026 announcement. Fill in the
owner column before enabling the feature — the announcement is explicit that
ongoing operation needs a named team.

## 0. Decision

| Item | Answer | Owner |
|---|---|---|
| Which of the three drivers applies? (network access / customizability / compliance) | | |
| Have we considered and rejected the hosted offering, and why? | | |
| Is the requirement one that self-hosting actually satisfies? (see the data boundary below) | | |

## 1. Eligibility

- [ ] Plan is Team or Enterprise
- [ ] Public beta status accepted by the sponsoring team
- [ ] Organization is not using ZDR
- [ ] Feature deliberately enabled (it is off by default)

## 2. Data boundary — communicated in writing to security review

- [ ] Documented as staying on our infrastructure: repository checkouts, build
      artifacts, secrets, files created or modified by a session
- [ ] Documented as sent for inference: prompts, responses, tool results
      (which can include code the model reads)
- [ ] Documented: session transcripts are stored so sessions can be resumed
      from any surface
- [ ] Reviewers have confirmed this boundary meets the stated control

## 3. Capacity model

- [ ] Mode chosen: ☐ fixed ☐ on-demand
- [ ] If fixed: number of runners, and who revisits it
- [ ] If on-demand: orchestrator deployment, monitoring, and owner
- [ ] Confirmed understanding that isolation is per session (own checkout), not
      per runner

## 4. Runner image

| Item | Owner | Cadence |
|---|---|---|
| Compilers and language runtimes to preinstall | | |
| SDKs to preinstall | | |
| Internal CLIs to preinstall | | |
| Image build pipeline | | |
| Image update / patching cadence | | |

## 5. Ongoing ownership

Named team (platform / developer experience / developer productivity): ______

- [ ] Owns initial setup
- [ ] Owns runner image maintenance
- [ ] Owns runner updates
- [ ] Owns the orchestrator (on-demand mode only)
- [ ] Owns the escalation path when sessions fail to start

## 6. Rollout

- [ ] Pilot group identified
- [ ] Verified: sessions from every surface the team uses route to the environment
- [ ] Verified: sessions reach the internal services that motivated the move
- [ ] Feedback route agreed (GitHub, or the account team)

## 7. Reference

- Announcement: https://claude.com/blog/run-claude-code-sessions-on-your-own-compute
- Documentation: https://code.claude.com/docs/en/self-hosted-environments

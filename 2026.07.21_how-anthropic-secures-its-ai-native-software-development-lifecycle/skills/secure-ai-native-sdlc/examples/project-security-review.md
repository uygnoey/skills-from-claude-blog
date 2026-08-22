# Example — an automated project security review

The first security automation described in the post: a Claude-powered PSR (project
security review) web application. This walks the shape of it, then the two changes
that made it fit an AI-native lifecycle.

## v1 — the design-document reviewer

**Input.** A project design document.

**Process.** Analyze it against the MITRE ATT&CK framework to identify potential
vulnerabilities and suggest mitigations.

**Output.** A risk assessment with suggested mitigations, returned to the project
team and the AppSec team.

**Effect.** This one implementation saved the majority of the AppSec team's time.

## v2 — connected to organizational context

**The change.** Connect the application to an internal knowledge index covering
organization-wide policies, past decisions, and related systems.

**Why it matters.** Two things improve at once:

1. Better understanding of potential risk, because the review sees the policies and
   the prior decisions rather than only the document in front of it.
2. It captures information *missing* from the PSR. The design document is no longer
   the sole source of truth about the project.

**The skill.** Creating a Claude Code skill let Claude fan out further and capture
additional context wherever it lived.

## v3 — delegated approval

Once the team gained confidence that Claude assessed risk accurately, teams were
allowed to approve their own project when Claude deemed the launch low enough risk.

The gate did not disappear. It moved: from "AppSec reviews everything" to "AppSec
reviews what the assessment says is worth reviewing."

## Why the gate changed shape

A PSR was originally designed to catch security issues before the lengthy and
expensive coding process — catching an issue at this stage saved months of
re-development.

Today multiple prototypes of a major feature can be created in hours, which makes
detailed architectural review a less critical gate. Forcing a heavyweight document
review in front of a build that takes an afternoon is an unnecessary speed bump.
Connecting the PSR to the knowledge index is how the context gets captured without
adding one.

## The principle to carry forward

> Connect security agents to organizational context. As the planning cycle
> compresses, it is much more effective to bring these agents to where the context
> already lives — chat threads, prior reviews, the codebase — rather than forcing
> detailed documentation at stages that may no longer require them. Either way,
> agents need context outside of the code itself.

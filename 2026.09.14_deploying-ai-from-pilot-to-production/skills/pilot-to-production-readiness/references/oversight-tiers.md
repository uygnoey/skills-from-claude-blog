# Four-tier oversight model

From "Deploying AI from pilot to production" (Anthropic with Accenture, September 2026), Consideration 06.
Match human review to the risk of each output. The tiers are suggestions; internal policies and
regulations decide the final structure. A process with a long low-error record (e.g. six months or a
year) may be ready to move to a lighter tier.

| Tier | Oversight model | Example use cases | Review cadence |
|---|---|---|---|
| 1. Automated | No human review; output goes directly to workflow | Summarizing meeting transcripts; reformatting data between systems; generating code documentation | Quarterly audit of output quality |
| 2. Sampled | Random subset reviewed on a regular cadence | Extracting structured data from invoices; classifying support tickets; populating CRM fields from call transcripts | A portion of outputs reviewed weekly; start with a higher review rate and adjust as error patterns stabilize |
| 3. Reviewed | Human approves every output before it reaches its audience | Drafting client communications; financial analysis for external distribution; contract language from templates; marketing content | Every output reviewed before release; audit the review process monthly for catch rate and cost |
| 4. Advisory | AI provides analysis; a human makes the decision and produces the output | Credit and lending recommendations; candidate screening in hiring; clinical findings for physician review; regulatory filing preparation | Every decision documented with an audit trail; compliance review quarterly |

## Why tiering
Applying the same review to every output either stalls under the review burden or leads to corner
cutting. Unaudited governance becomes "structural drag": checkpoints are easier to add than remove, and
the risk of removing one is visible while the cost of keeping it is not.

Accenture (Tokenomics, Sept 2026): organizations with formal chargeback accountability for AI spending
link 32 cents of every dollar of AI token spend to a quantified business outcome - six times more than
those with no allocation.

## Beyond oversight
- **Incident response, defined before go-live:** who gets notified; remediation path; who can pause the
  system; who communicates to affected parties.
- **Continuous monitoring:** quality shifts from model updates or prompt drift, stale or out-of-sync
  data, and changes in the real-world process. Define what to measure, automated alerts on degradation
  thresholds, and escalation protocols.

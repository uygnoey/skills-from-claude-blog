# Coverage verification checklist

Fill this in before you rely on a Compliance API pull that spans Cowork and Claude Code,
and keep it with the audit, retention, or investigation record.

- **Matter / request ID:** ______________________
- **Requested by:** ______________________
- **Date of pull:** ______________________
- **Time range requested:** ______________________

## 1. Access

- [ ] Organization is on Claude Enterprise.
- [ ] Existing Compliance Access Key located; no new credential required.
- [ ] Confirmed this coverage is still in **beta** as of the pull date.

## 2. Surfaces requested vs. covered

| Surface named in the request | In scope? | Notes |
| --- | --- | --- |
| Cowork — desktop | Yes | |
| Cowork — web | Yes | |
| Cowork — mobile | Yes | |
| Claude Code — CLI | Yes | |
| Claude Code — desktop app | Yes | |
| Claude Code — web | **No** | Excluded from beta |
| Claude Code — via Claude Platform | **No** | Excluded from beta |
| Amazon Bedrock sessions | **No** | Excluded from beta |
| Google Cloud Vertex AI sessions | **No** | Excluded from beta |
| Microsoft Foundry sessions | **No** | Excluded from beta |

- [ ] Every out-of-scope surface relevant to this request has been reported to the requester **in writing**.

## 3. Fields needed

Content:
- [ ] Prompts and responses
- [ ] Tool-call content (web / Model Context Protocol)
- [ ] Skills and artifacts (transcript text)

Metadata:
- [ ] Verified user ID
- [ ] Verified email address
- [ ] Organization ID
- [ ] Session ID
- [ ] Per-message IDs
- [ ] Timestamps

- [ ] Any question the requester asked that **no** captured field can answer is listed here:
  ______________________________________________

## 4. Parallel telemetry

- [ ] OpenTelemetry export status: running / not running / n/a
- [ ] If running, decision recorded on whether it stays in place to cover excluded surfaces:
  ______________________________________________

## 5. Sign-off

- **Completed by:** ______________________
- **Reviewed by:** ______________________
- **Date:** ______________________

#!/usr/bin/env bash
# Deployment script for one agent folder.
#
# The operating model this belongs to: merging to the main branch deploys the
# agent. This script is what the pipeline runs on that merge. Adapt the marked
# lines to your managed-agent platform's CLI; the structure is the point.
#
# Usage:  ./deploy.sh [path-to-agent-folder]
# Default: the folder this script lives in.

set -euo pipefail

AGENT_DIR="${1:-$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)}"
CONFIG="${AGENT_DIR}/agent-config.json"
PROMPT="${AGENT_DIR}/system-prompt.md"

log() { printf '[deploy] %s\n' "$*" >&2; }
fail() { printf '[deploy] ERROR: %s\n' "$*" >&2; exit 1; }

# --- 1. Validate the agent definition before touching anything -------------

[[ -f "${CONFIG}" ]] || fail "missing agent-config.json in ${AGENT_DIR}"
[[ -f "${PROMPT}" ]] || fail "missing system-prompt.md in ${AGENT_DIR}"

if command -v python3 >/dev/null 2>&1; then
  python3 -c 'import json,sys; json.load(open(sys.argv[1]))' "${CONFIG}" \
    || fail "agent-config.json is not valid JSON"
else
  log "python3 not found — skipping JSON validation"
fi

AGENT_NAME="$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["name"])' "${CONFIG}")"
[[ -n "${AGENT_NAME}" ]] || fail "agent-config.json has no name"

# An agent with no named owner is an agent nobody maintains.
OWNER="$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1])).get("owner",""))' "${CONFIG}")"
[[ -n "${OWNER}" ]] || fail "agent-config.json has no owner"

log "agent: ${AGENT_NAME} (owner: ${OWNER})"

# --- 2. Refuse to deploy from anywhere but an approved merge ---------------
# Nothing about an agent changes except through a pull request someone approved.

BRANCH="${DEPLOY_BRANCH:-$(git -C "${AGENT_DIR}" rev-parse --abbrev-ref HEAD 2>/dev/null || echo unknown)}"
if [[ "${BRANCH}" != "main" && "${ALLOW_UNMERGED_DEPLOY:-0}" != "1" ]]; then
  fail "refusing to deploy from '${BRANCH}' — merge to main, or set ALLOW_UNMERGED_DEPLOY=1 for a dry run"
fi

# --- 3. Push the new version ----------------------------------------------
# Every push creates a new agent version with optimistic locking, so rollback
# is a matter of pointing at the previous version rather than reverting by hand.
#
# Replace the line below with your platform's deploy command, e.g.
#   agents deploy --config "${CONFIG}" --prompt "${PROMPT}"

: "${AGENT_DEPLOY_CMD:=}"
if [[ -z "${AGENT_DEPLOY_CMD}" ]]; then
  log "AGENT_DEPLOY_CMD is not set — printing what would be deployed instead"
  log "  config: ${CONFIG}"
  log "  prompt: ${PROMPT}"
  exit 0
fi

log "deploying ${AGENT_NAME}…"
# shellcheck disable=SC2086
${AGENT_DEPLOY_CMD} --config "${CONFIG}" --prompt "${PROMPT}"

log "deployed ${AGENT_NAME}"

#!/usr/bin/env python3
"""Validate a sync-shell contract for required runtime guarantees."""

from __future__ import annotations

import re
import sys
from pathlib import Path


DEFAULT_SAMPLE = """
# Sync Shell Contract
## Input Scope
sync_type and resource_key are defined.
## State Machine
queued, running, success, error, stale, cooldown.
## Data Fields
progress_stage, progress_message, heartbeat_at, cooldown_until.
## Start API
start_result.status is separate from sync_status.status.
## Status API
Supports job_id and client_request_id recovery.
## Worker Contract
Lease token, heartbeat, stale rule, old-worker write guard.
## Frontend Contract
Polling and start timeout recovery.
## Acceptance Tests
duplicate start, stale, cooldown, worker crash, old worker late write.
## Failure Modes
No boolean-only running state.
## Open Decisions
Confirm lease timeout.
"""


REQUIRED_TERMS = [
    "input scope",
    "state machine",
    "queued",
    "running",
    "success",
    "error",
    "stale",
    "cooldown",
    "progress_stage",
    "heartbeat",
    "start api",
    "status api",
    "frontend contract",
    "acceptance tests",
    "failure modes",
    "open decisions",
]


SECRET_RE = re.compile(r"(?i)(token|secret|password|cookie)\s*[:=]\s*['\"]?([^'\"\s`<>]{8,})")


def load_text() -> str:
    if len(sys.argv) == 1:
        return DEFAULT_SAMPLE
    if len(sys.argv) != 2:
        raise SystemExit("Usage: check_sync_shell_contract.py [contract.md]")
    return Path(sys.argv[1]).read_text(encoding="utf-8")


def main() -> int:
    text = load_text()
    lower = text.lower()
    missing = [term for term in REQUIRED_TERMS if term not in lower]
    leaks = [m.group(0) for m in SECRET_RE.finditer(text) if "<" not in m.group(0)]

    if missing or leaks:
        if missing:
            print("Missing required terms: " + ", ".join(missing), file=sys.stderr)
        if leaks:
            print("Possible raw secret values detected.", file=sys.stderr)
        return 1

    print("Sync shell contract check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

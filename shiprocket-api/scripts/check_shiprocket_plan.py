#!/usr/bin/env python3
"""Validate a Shiprocket integration handoff for structure and secret leaks."""

from __future__ import annotations

import re
import sys
from pathlib import Path


DEFAULT_SAMPLE = """
# Shiprocket Integration Plan
## Auth
Use dedicated API User credentials and Authorization: Bearer <SHIPROCKET_JWT>.
## Endpoint Flow
Read orders, read pickup locations, check serviceability, then assign AWB.
## ID Mapping
Separate local order_id, Shiprocket order id, shipment_id, awb, pickup_location.
## Storage
Persist shipment id, AWB, pickup token, labels, status, and raw tracking payload.
## Write Guards
Block writes after picked up or when AWB rules do not allow changes.
## Validation
Run read-only smoke tests before write calls.
## Failure Modes
Do not use the main panel account.
## Open Decisions
Confirm webhook handling.
"""


REQUIRED_TERMS = [
    "auth",
    "endpoint flow",
    "id mapping",
    "storage",
    "write guards",
    "validation",
    "failure modes",
    "open decisions",
]


SECRET_RE = re.compile(
    r"(?i)(jwt|bearer|api user password|password|token)\s*[:=]\s*['\"]?([^'\"\s`<>]{8,})"
)


def load_text() -> str:
    if len(sys.argv) == 1:
        return DEFAULT_SAMPLE
    if len(sys.argv) != 2:
        raise SystemExit("Usage: check_shiprocket_plan.py [plan.md]")
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
            print("Possible raw credential values detected.", file=sys.stderr)
        return 1

    print("Shiprocket API plan check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

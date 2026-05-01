#!/usr/bin/env python3
"""Validate a Lingxing API handoff for required structure and secret leaks."""

from __future__ import annotations

import re
import sys
from pathlib import Path


DEFAULT_SAMPLE = """
# Lingxing Integration Plan
## Lane
OpenAPI for VC orders; ERP report is out of scope.
## Credentials
Use <LINGXING_APP_KEY>, <LINGXING_APP_SECRET>, <LINGXING_ACCESS_TOKEN>.
## Endpoints
POST /basicOpen/platformOrder/vcOrder/pageList
## Field Mapping
local_po_number maps to the local order reference.
## Validation
Run a read-only smoke test before any write action.
## Failure Modes
Do not mix access_token with auth-token.
## Open Decisions
Confirm token refresh owner.
"""


REQUIRED_TERMS = [
    "lane",
    "credentials",
    "endpoints",
    "field mapping",
    "validation",
    "failure modes",
    "open decisions",
]


SECRET_RE = re.compile(
    r"(?i)(app_?secret|appserect|access_?token|auth-token|x-ak-company-id|password|cookie)\s*[:=]\s*['\"]?([^'\"\s`<>]{8,})"
)


def load_text() -> str:
    if len(sys.argv) == 1:
        return DEFAULT_SAMPLE
    if len(sys.argv) != 2:
        raise SystemExit("Usage: check_lingxing_plan.py [plan.md]")
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

    print("Lingxing API plan check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

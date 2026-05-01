#!/usr/bin/env python3
"""Validate a frontend auth-helper plan or reviewed file."""

from __future__ import annotations

import re
import sys
from pathlib import Path


DEFAULT_SAMPLE = """
# Frontend Auth Helper Plan
## Auth Source
Current user and token are read through one helper.
## Helper API
getActiveUser, getActiveAuthToken, isAuthenticated, canAccess, canPerform.
## Page Permissions
page.user-admin controls page entry.
## Action Permissions
action.product.delete controls delete.
## Backend Enforcement
Sensitive endpoints reject unauthorized calls server-side.
## Integration Steps
Pages import ui-auth.js and call helper methods.
## Tests
Admin success, non-admin hidden, backend reject.
## Failure Modes
No direct token parsing in pages.
"""


REQUIRED_TERMS = [
    "auth source",
    "helper api",
    "page permissions",
    "action permissions",
    "backend enforcement",
    "integration steps",
    "tests",
    "failure modes",
]


BAD_PATTERNS = [
    re.compile(r"username\s*={2,3}\s*['\"]admin['\"]", re.I),
    re.compile(r"localStorage\.getItem\([^)]*token", re.I),
    re.compile(r"atob\([^)]*token", re.I),
]


SECRET_RE = re.compile(r"(?i)(token|cookie|password)\s*[:=]\s*['\"]?([^'\"\s`<>]{8,})")


def load_text() -> str:
    if len(sys.argv) == 1:
        return DEFAULT_SAMPLE
    if len(sys.argv) != 2:
        raise SystemExit("Usage: check_frontend_auth_plan.py [plan-or-file.md]")
    return Path(sys.argv[1]).read_text(encoding="utf-8")


def main() -> int:
    text = load_text()
    lower = text.lower()
    missing = [term for term in REQUIRED_TERMS if term not in lower]
    bad = [pattern.pattern for pattern in BAD_PATTERNS if pattern.search(text)]
    leaks = [m.group(0) for m in SECRET_RE.finditer(text) if "<" not in m.group(0)]

    if missing or bad or leaks:
        if missing:
            print("Missing required terms: " + ", ".join(missing), file=sys.stderr)
        if bad:
            print("Direct auth anti-patterns detected.", file=sys.stderr)
        if leaks:
            print("Possible raw secret values detected.", file=sys.stderr)
        return 1

    print("Frontend auth-helper plan check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

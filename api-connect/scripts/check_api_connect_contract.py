#!/usr/bin/env python3
"""Validate an API connection/proxy contract."""

from __future__ import annotations

import re
import sys
from pathlib import Path


DEFAULT_SAMPLE = """
# API Connect Contract
## Transport Goal
Proxy transport, not server key custody.
## Route Mapping
activeProtocol -> routeKey -> proxyPath.
## Credential Path
Secrets use internal headers and never query, body, logs, or response.
## Endpoint Allowlist
Each proxy route owns a fixed upstream endpoint.
## Error Contract
Normalize missing credential, invalid credential, endpoint mismatch, network error, proxy error.
## Migration
legacy_direct, proxy_recommended, proxy_confirmed, blocked.
## Acceptance Tests
Success, missing credential, invalid key, endpoint mismatch, secret redaction.
## Failure Modes
Do not route by provider display name.
"""


REQUIRED_TERMS = [
    "transport goal",
    "route mapping",
    "credential path",
    "endpoint allowlist",
    "error contract",
    "migration",
    "acceptance tests",
    "failure modes",
]


SECRET_RE = re.compile(
    r"(?i)(api_?key|bearer|secret|token)\s*[:=]\s*['\"]?([^'\"\s`<>]{8,})"
)


def load_text() -> str:
    if len(sys.argv) == 1:
        return DEFAULT_SAMPLE
    if len(sys.argv) != 2:
        raise SystemExit("Usage: check_api_connect_contract.py [contract.md]")
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

    print("API connect contract check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

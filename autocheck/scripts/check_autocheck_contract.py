#!/usr/bin/env python3
"""Validate an autocheck heartbeat prompt or contract."""

from __future__ import annotations

import re
import sys
from pathlib import Path


DEFAULT_SAMPLE = """
# Autocheck Heartbeat Prompt
## 目标
检查 checkout flow，不默认修业务 bug。
## 项目上下文
project path, entrypoint, sample queue, business ledger.
## 启动要求
doc/task_issue.md doc/task_plan.md doc/progress.md doc/findings.md.
## 执行要求
Run E2E and verify API/data evidence.
## 自主执行范围
Run checks and update records.
## 必须用户决定或通知
Notify on missing auth or high-risk action.
## 禁止路径
No mock, no lowering standards, no real secrets.
## 记录格式
PASS FAIL BLOCKED with evidence and next action.
## 通知规则
DONT_NOTIFY while continuing; NOTIFY when completed or blocked.
"""


REQUIRED_TERMS = [
    "目标",
    "项目上下文",
    "启动要求",
    "执行要求",
    "自主执行范围",
    "必须用户决定",
    "禁止路径",
    "记录格式",
    "通知规则",
    "PASS",
    "FAIL",
    "BLOCKED",
    "DONT_NOTIFY",
    "NOTIFY",
    "doc/task_issue.md",
    "doc/task_plan.md",
    "doc/progress.md",
    "doc/findings.md",
    "evidence",
]


SECRET_RE = re.compile(
    r"(?i)(password|token|cookie|secret|api[_-]?key)\s*[:=]\s*['\"]?([^'\"\s`<>]{8,})"
)


def load_text() -> str:
    if len(sys.argv) == 1:
        return DEFAULT_SAMPLE
    if len(sys.argv) != 2:
        raise SystemExit("Usage: check_autocheck_contract.py [prompt-or-contract.md]")
    return Path(sys.argv[1]).read_text(encoding="utf-8")


def main() -> int:
    text = load_text()
    missing = [term for term in REQUIRED_TERMS if term not in text]
    leaks = [m.group(0) for m in SECRET_RE.finditer(text) if "<" not in m.group(0) and "placeholder" not in m.group(0).lower()]
    repair_drift = "默认修改业务代码" in text and "禁止默认修改业务代码" not in text

    if missing or leaks or repair_drift:
        if missing:
            print("Missing required terms: " + ", ".join(missing), file=sys.stderr)
        if leaks:
            print("Possible raw secret values detected.", file=sys.stderr)
        if repair_drift:
            print("Autocheck appears to drift into business-code repair.", file=sys.stderr)
        return 1

    print("Autocheck contract check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

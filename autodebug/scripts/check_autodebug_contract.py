#!/usr/bin/env python3
"""Validate an autodebug heartbeat prompt or contract."""

from __future__ import annotations

import re
import sys
from pathlib import Path


DEFAULT_SAMPLE = """
# Autodebug Heartbeat Prompt
## 目标
Read current bug ledger and fix current red light.
## 项目上下文
project path, bug ledger, allowed paths, forbidden boundaries.
## 启动要求
doc/task_issue.md doc/task_plan.md doc/progress.md doc/findings.md.
## 当前红灯选择
Select latest current red light only.
## 执行要求
复现, 根因, 最小修复, 验证, VERIFY_COMMANDS, review re-check.
## 自主执行范围
Modify scoped production code and tests.
## 必须用户决定或通知
Notify on destructive data or cross-module contract.
## 禁止路径
No mock, no fake data, no lowering standards.
## 记录格式
FIXED STILL_FAILING BLOCKED FORBIDDEN with root cause and evidence.
## 通知规则
DONT_NOTIFY while continuing; NOTIFY when fixed or blocked.
"""


REQUIRED_TERMS = [
    "目标",
    "项目上下文",
    "启动要求",
    "当前红灯选择",
    "执行要求",
    "自主执行范围",
    "必须用户决定",
    "禁止路径",
    "记录格式",
    "通知规则",
    "复现",
    "根因",
    "最小修复",
    "验证",
    "review",
    "FIXED",
    "STILL_FAILING",
    "BLOCKED",
    "FORBIDDEN",
    "DONT_NOTIFY",
    "NOTIFY",
    "doc/task_issue.md",
    "doc/task_plan.md",
    "doc/progress.md",
    "doc/findings.md",
]


SECRET_RE = re.compile(
    r"(?i)(password|token|cookie|secret|api[_-]?key)\s*[:=]\s*['\"]?([^'\"\s`<>]{8,})"
)


def load_text() -> str:
    if len(sys.argv) == 1:
        return DEFAULT_SAMPLE
    if len(sys.argv) != 2:
        raise SystemExit("Usage: check_autodebug_contract.py [prompt-or-contract.md]")
    return Path(sys.argv[1]).read_text(encoding="utf-8")


def main() -> int:
    text = load_text()
    missing = [term for term in REQUIRED_TERMS if term not in text]
    leaks = [m.group(0) for m in SECRET_RE.finditer(text) if "<" not in m.group(0) and "placeholder" not in m.group(0).lower()]
    no_root_cause = "没根因就修" not in text and "root cause" not in text.lower()

    if missing or leaks or no_root_cause:
        if missing:
            print("Missing required terms: " + ", ".join(missing), file=sys.stderr)
        if leaks:
            print("Possible raw secret values detected.", file=sys.stderr)
        if no_root_cause:
            print("Root-cause gate is not explicit.", file=sys.stderr)
        return 1

    print("Autodebug contract check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

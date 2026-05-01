#!/usr/bin/env python3
import argparse
import re
import sys


REQUIRED_HEADINGS = [
    "Goal",
    "Real Work And Waste",
    "Users",
    "V1 Scope",
    "Non-Goals",
    "Constraints",
    "Page Boundaries",
    "Data Model",
    "Interface Contracts",
    "Auth And Permissions",
    "Async Jobs And Queues",
    "External Services",
    "E2E Acceptance",
    "Implementation Order",
    "Open Decisions",
]


def headings(markdown):
    return {
        match.group(1).strip().lower()
        for match in re.finditer(r"^##\s+(.+?)\s*$", markdown, re.MULTILINE)
    }


def main():
    parser = argparse.ArgumentParser(description="Validate project.md design contract structure.")
    parser.add_argument("project_md", help="Path to project.md or design markdown.")
    args = parser.parse_args()

    with open(args.project_md, "r", encoding="utf-8") as handle:
        content = handle.read()

    existing = headings(content)
    missing = [item for item in REQUIRED_HEADINGS if item.lower() not in existing]

    if missing:
        print("Missing required sections:")
        for item in missing:
            print(f"- {item}")
        return 1

    print("Project design structure check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

---
name: autocheck
description: Generate or review project-specific heartbeat automation prompts for checking whether a product flow works. Use when a task involves E2E guard runs, verify/browser/API/data checks, sample queues, evidence capture, PASS/FAIL/BLOCKED records, DONT_NOTIFY/NOTIFY rules, documentation ledger paths, or converting a project-specific checking automation into a reusable check contract. This skill checks and records problems; it does not default to fixing business bugs.
---

# Autocheck

## Purpose

Use this skill to create a project-specific checking automation contract. It should produce a heartbeat prompt that can run E2E, verify, browser, API, data, or sync checks; record evidence; and notify only when required.

This is a checking skill, not a repair skill. If the desired automation should reproduce root cause and change production code by default, use `autodebug`.

## Input

Collect these before generating the prompt:

- project path and execution environment
- target page, command, endpoint, or flow to check
- check type: browser E2E, API replay, CLI smoke, data/sync state, or mixed
- login/auth method, expressed as placeholders if sensitive
- sample queue or route/endpoint matrix
- evidence requirements: screenshots, DOM/API payloads, DB rows, logs, command output
- record paths: `doc/task_issue.md`, `doc/task_plan.md`, `doc/progress.md`, `doc/findings.md`, and any business case ledger
- allowed actions, forbidden actions, and user-decision boundaries
- notification policy

Never include real passwords, tokens, cookies, private keys, payment details, or production secrets in the generated automation prompt.

## Workflow

1. Classify the check shape.
   - Read `references/check-contract.md`.
   - Decide whether the target is browser, API, CLI, data/sync, or mixed.
   - Map each shape to concrete commands and evidence.

2. Define autonomy and notification boundaries.
   - Read `references/heartbeat-boundaries.md`.
   - The prompt must say what the automation can continue doing alone, what is forbidden, and when it must notify the user.

3. Define recording contract.
   - Read `references/recording-contract.md`.
   - The prompt must specify process files, business ledger files, and per-run record format.

4. Generate the heartbeat prompt.
   - Use `assets/autocheck-heartbeat.template.md`.
   - Fill all placeholders with project-specific values.
   - Keep checking separate from fixing: record product bugs, do not default to business-code edits.

5. Add a check matrix.
   - Use `assets/check-matrix.template.md`.
   - Every sample or target must have an expected result, evidence source, and PASS/FAIL/BLOCKED rule.

6. Validate.
   - Run `python3 scripts/check_autocheck_contract.py <generated-prompt.md>`.
   - If only reviewing the skill itself, run the script with no arguments.

## Output

Produce:

- a project-specific heartbeat automation prompt
- check matrix or sample queue contract
- recording paths and record format
- autonomy/forbidden/user-decision boundary
- notification rules
- validation result

## Acceptance

The generated prompt is acceptable only when:

- the target and completion condition are explicit
- every check has concrete evidence requirements
- PASS/FAIL/BLOCKED meanings are defined
- process and business ledger paths are named
- `DONT_NOTIFY` and `NOTIFY` rules are present
- sensitive credentials are placeholders
- the automation does not silently turn into a broad bug-fixing job
- validator passes

## Failure Modes

Mark incomplete if:

- the prompt says only "run E2E" without target matrix and evidence
- it allows business-code changes by default
- it lacks record paths or record format
- it lacks notification rules
- it can pass by checking only button clicks while ignoring API/data/state
- it contains real secrets or account credentials
- it cannot say what should happen after a FAIL

## Reusable Resources

- `references/check-contract.md`: check types, evidence, and result states
- `references/heartbeat-boundaries.md`: autonomy, forbidden paths, user decisions, notify rules
- `references/recording-contract.md`: document path and record format rules
- `references/absorbed-patterns.md`: external patterns absorbed into this skill
- `assets/autocheck-heartbeat.template.md`: prompt template
- `assets/check-matrix.template.md`: matrix template
- `scripts/check_autocheck_contract.py`: validator

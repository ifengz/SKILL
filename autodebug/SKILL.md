---
name: autodebug
description: Generate or review project-specific heartbeat automation prompts for debugging and closing real bugs from a case ledger. Use when a task involves current red-light closeout, bug ledger repair, sync.md bug fixing, root-cause investigation, reproduction, hypothesis testing, minimal production fixes, verification gates, review loops, doc/progress/findings recording, autonomous repair boundaries, or deciding when a bug-fixing automation must ask the user.
---

# Autodebug

## Purpose

Use this skill to create a project-specific debugging automation contract. It should produce a heartbeat prompt that reads confirmed issues, reproduces failures, identifies root cause, applies the smallest safe production fix, verifies it, and writes back the result.

This is a repair skill. If the desired automation should only check flows and record problems without fixing business bugs by default, use `autocheck`.

## Input

Collect:

- project path and execution environment
- bug ledger or current red-light document
- exact target issue selection rule
- reproduction steps or failing check command
- allowed code, test, verify, and documentation paths
- forbidden architecture or product-contract boundaries
- required verification commands
- record paths: `doc/task_issue.md`, `doc/task_plan.md`, `doc/progress.md`, `doc/findings.md`, and business case ledger
- user-decision boundaries
- review or re-check requirements after the fix

Never include real passwords, tokens, cookies, private keys, payment details, or production secrets in the generated automation prompt.

## Workflow

1. Select the current bug.
   - Read `references/debug-contract.md`.
   - Define how the automation chooses current red lights and how it marks old findings as stale or resolved.

2. Require root cause before fix.
   - The prompt must require reproduction, evidence, hypothesis, experiment, and root cause.
   - Do not allow blind patches, fallback behavior, mock data, or verification-only edits as a bug fix.

3. Define fix boundaries.
   - Read `references/heartbeat-boundaries.md`.
   - Separate autonomous repair from user-decision boundaries and forbidden paths.

4. Define recording contract.
   - Read `references/recording-contract.md`.
   - The prompt must write progress during execution and write fix evidence back to the business ledger.

5. Add review and verification loop.
   - Read `references/review-loop.md`.
   - The prompt must require targeted validation and fresh review/re-check after fixing.

6. Generate the heartbeat prompt.
   - Use `assets/autodebug-heartbeat.template.md`.
   - Fill placeholders with project-specific values.

7. Validate.
   - Run `python3 scripts/check_autodebug_contract.py <generated-prompt.md>`.
   - If only reviewing the skill itself, run the script with no arguments.

## Output

Produce:

- a project-specific heartbeat automation prompt for bug repair
- root-cause and fix loop contract
- recording paths and record format
- allowed/forbidden/user-decision boundary
- verification and review gate
- validation result

## Acceptance

The generated prompt is acceptable only when:

- it names the bug source and current-red selection rule
- it requires reproduction before repair
- it requires root-cause evidence before code changes
- it allows only minimal scoped production fixes
- it requires focused tests/verify/E2E after the fix
- it writes results back to process docs and business ledger
- it distinguishes fixed, still failing, blocked, and forbidden paths
- it says when user decision is required
- validator passes

## Failure Modes

Mark incomplete if:

- the prompt says "fix bugs" without issue selection and reproduction
- it permits code changes before root cause
- it allows mocks, fake data, fallback patches, or lowered verification standards
- it lacks allowed and forbidden path boundaries
- it lacks record paths or closeout format
- it calls documentation-only edits a business fix
- it lacks a post-fix verification and review loop
- it contains real secrets or account credentials

## Reusable Resources

- `references/debug-contract.md`: root-cause repair process
- `references/heartbeat-boundaries.md`: autonomy, forbidden paths, user decisions, notify rules
- `references/recording-contract.md`: document path and closeout format rules
- `references/review-loop.md`: severity, review, and re-check pattern
- `references/absorbed-patterns.md`: external patterns absorbed into this skill
- `assets/autodebug-heartbeat.template.md`: prompt template
- `assets/bug-closeout-record.template.md`: ledger record template
- `scripts/check_autodebug_contract.py`: validator

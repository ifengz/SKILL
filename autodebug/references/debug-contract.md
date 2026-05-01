# Autodebug Debug Contract

## Selection

The generated prompt must define how to choose the current issue:

- latest FAIL from an autocheck ledger
- current red light in a business case document
- named bug id or section
- failing verify/test/E2E command

It must avoid re-fixing stale historical issues that no longer reproduce.

## Required Repair Loop

1. Read project instructions and ledgers.
2. Build current red-light list.
3. Reproduce the failure with the smallest real command or flow.
4. Trace data/control flow to root cause.
5. State the root cause and evidence.
6. Apply the smallest safe production fix.
7. Add or update focused tests/verify/E2E.
8. Run verification.
9. Re-check or review the fix.
10. Write closeout record.

## Root-Cause Rule

No production fix before reproduction and root-cause evidence. A prompt that permits "try a quick fix" is not acceptable.

## Fix Scope Rule

Fix the first real broken point in the data or behavior chain. Do not patch UI output after the fact when the root cause is upstream parsing, state, storage, API, or sync flow.

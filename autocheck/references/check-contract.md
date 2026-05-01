# Autocheck Check Contract

## Check Shapes

| Shape | Use When | Required Evidence |
| --- | --- | --- |
| Browser E2E | user-facing page or workflow | URL, route, screenshots on failure, console/network errors, DOM/API state |
| API replay | endpoint contract or backend-only flow | request/response, status code, response schema, auth/error paths |
| CLI smoke | command or script behavior | command, exit code, stdout/stderr, malformed-input result |
| Data/sync state | sync, queue, materialized view, or history | active task, terminal status, history rows, field values, timestamps |
| Mixed | product flow crosses UI/API/data | matrix tying UI action to backend/data evidence |

## Result States

| State | Meaning |
| --- | --- |
| `PASS` | target ran and evidence matched the expected contract |
| `FAIL` | target ran and evidence proved a product or verification bug |
| `BLOCKED` | check could not run because environment/auth/runner/precondition was missing |

## Evidence Rules

- Button click success is not enough when API/data/history is part of the contract.
- A check can pass only on fresh evidence from the current run.
- A failed check must record exact target, sample, actual result, expected result, and evidence path or command output.
- A blocked check must name the blocker and the next safe action.

## Non-Repair Boundary

Autocheck may repair its own check harness only when the bug is in test wiring or evidence capture. It must not default to production business-code changes. Product bugs should be recorded for `autodebug` or human triage.

# Recording Contract

## Process Files

Default paths:

- `doc/task_issue.md`: in-progress issue registration
- `doc/task_plan.md`: current bug target and repair phases
- `doc/progress.md`: actions and results appended during execution
- `doc/findings.md`: root cause, risks, blockers, forbidden paths

The generated prompt must adapt these if the target project uses different paths.

## Business Ledger

Use the existing case ledger that contains the bug, for example:

- `docs/cases/sync.md`
- `docs/cases/e2e.md`
- `docs/cases/<feature>.md`

## Closeout Record

Every repaired issue should record:

- time
- selected bug/red light
- reproduction command or steps
- root cause
- files changed
- fix summary
- verification commands and results
- review/re-check result
- status: `FIXED`, `STILL_FAILING`, `BLOCKED`, or `FORBIDDEN`
- whether user decision is needed

## Write Discipline

- Record during execution, not only after success.
- Do not mark complete without explicit user acceptance if the project requires that.
- If a path is forbidden, record the forbidden reason and continue to another safe path if one exists.

# Recording Contract

## Process Files

Default paths:

- `doc/task_issue.md`: in-progress issue registration
- `doc/task_plan.md`: current check goal, scope, and phases
- `doc/progress.md`: actions and results appended during execution
- `doc/findings.md`: risks, failures, blockers, and forbidden paths

If a project uses a different convention, the generated prompt must name it explicitly.

## Business Ledger

For product checks, use the project's case ledger, for example:

- `docs/cases/sync.md`
- `docs/cases/e2e.md`
- `docs/cases/<feature>.md`

Do not invent a new ledger when the project already has one.

## Record Format

Every check record should include:

- time
- automation id/name
- target
- sample or route/endpoint
- expected result
- actual result
- evidence source
- status: `PASS`, `FAIL`, or `BLOCKED`
- whether user decision is needed
- next action

## Write Discipline

- Append during execution, not only at the end.
- Do not mark an issue complete without explicit user acceptance if the project requires that.
- Do not call a product bug fixed from documentation-only changes.

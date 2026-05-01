# Heartbeat Boundaries

## Autonomous Repair

Autodebug can continue without asking the user when it is:

- reading project instructions and issue ledgers
- reproducing the selected bug
- adding diagnostic logging that stays local and is removed before completion
- modifying scoped production code directly tied to the bug
- modifying focused tests, verify scripts, or E2E scripts tied to the bug
- updating process docs and business case ledger
- running local verification and browser/API/data checks

## Must Ask Or Notify

Return `NOTIFY` when:

- the fix requires deleting or permanently mutating real business data
- the fix requires production infrastructure, secrets, payment, global auth, or cross-module contract changes
- required credentials/services are missing
- the only plausible fix violates a stated forbidden boundary
- repeated attempts disprove the current root cause and further work would become architectural redesign
- all current red lights are fixed and verified

## Forbidden Paths

- no mock data or fake pass
- no lowering verification standards
- no heuristic fallback to mask the root cause
- no broad unrelated refactor
- no new branch/worktree unless the project explicitly allows it
- no documentation-only closeout for a code/data bug
- no secret disclosure

## Notification Contract

Use:

- `DONT_NOTIFY`: actively reproducing, fixing, verifying, or safely continuing
- `NOTIFY`: fixed all selected issues, blocked, forbidden path reached, or user decision required

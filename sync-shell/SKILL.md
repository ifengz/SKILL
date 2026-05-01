---
name: sync-shell
description: Design or review a long-running sync task shell. Use when a task involves queued/running/success/error/stale/cooldown states, progress_stage/progress_message, worker heartbeat, lease timeout, start/status APIs, polling UI, start-timeout recovery, idempotency, stale requeue, rate-limit cooldown, run history, or turning a black-box sync job into an observable and recoverable workflow.
---

# Sync Shell

## Purpose

Use this skill when a long-running sync job must become visible, recoverable, and testable. It is not the business sync logic itself; it is the shell around the logic: start, status, progress, heartbeat, stale detection, cooldown, polling, and final summary.

## Input

Collect:

- sync type and resource scope
- current trigger and expected runtime
- existing jobs table/worker/queue if present
- current status fields and heartbeat or lease fields
- stages a non-technical user should see
- frontend page that starts and polls the sync
- stale timeout, queued claim timeout, cooldown behavior, and retry policy
- success summary and failure summary requirements

Do not copy real credentials, upstream tokens, server panel details, or private operational URLs into examples.

## Workflow

1. Confirm this is a sync-shell problem.
   - Use the skill when a request can outlive a normal HTTP request or needs user-visible progress.
   - Do not build a new task system if an existing jobs shell can be safely extended.

2. Define the state machine.
   - Read `references/state-machine.md`.
   - Required visible states are `queued`, `running`, `success`, `error`, `stale`, and `cooldown`.

3. Define the API contract.
   - Read `references/api-contract.md`.
   - Separate `start_result.status` from `sync_status.status`.
   - Include start timeout recovery by `sync_type + resource_key + trigger + client_request_id`.

4. Define worker and storage behavior.
   - Heartbeat/lease must be independent from generic `updated_at`.
   - Old workers must not finish a job without the current lease token.
   - Progress must use `progress_stage`, `progress_message`, and optional `progress_metrics`.

5. Define frontend behavior.
   - Poll `queued`, `running`, and active `cooldown`.
   - Stop on `success`, `error`, `stale`, and expired cooldown.
   - Keep main page data separate from latest sync status.

6. Validate.
   - Use `assets/sync-contract.template.md` when drafting a new contract.
   - Run `python3 scripts/check_sync_shell_contract.py <contract.md>` when a contract exists.
   - Read `references/failure-modes.md` before completion.

## Output

Produce one of:

- sync-shell implementation contract
- backend/frontend task split
- state machine and API spec
- code-review checklist for an existing sync job
- E2E/manual validation matrix

The output must include input scope, state machine, data fields, start/status APIs, worker heartbeat, stale/cooldown rules, frontend polling, tests, failure modes, and open decisions.

## Acceptance

The task is complete only when:

- queued/running/success/error/stale/cooldown are represented explicitly
- progress stage and message are user-readable
- heartbeat or lease timeout determines stale jobs
- active-job checks exclude stale and expired cooldown jobs
- start API is idempotent and handles already-running jobs
- frontend can recover after start request timeout
- success, error, stale, and cooldown have visible summaries
- tests cover duplicate start, stale job, cooldown, worker crash, polling, and old-worker late write

## Failure Modes

Stop or mark incomplete if:

- a boolean `running` or `is_syncing` is the whole state model
- stale detection uses only status and ignores heartbeat/lease
- queued jobs can wait forever
- frontend treats start response status as the final sync status
- the latest running/error job clears the main page's last successful data
- cooldown auto-revives an old job
- old workers can write success after losing the lease

## Reusable Resources

- `references/state-machine.md`: state and transition contract
- `references/api-contract.md`: start/status API shape
- `references/failure-modes.md`: review blockers and test cases
- `assets/sync-contract.template.md`: implementation contract template
- `assets/sync_status.template.json`: response shape template
- `scripts/check_sync_shell_contract.py`: contract validator

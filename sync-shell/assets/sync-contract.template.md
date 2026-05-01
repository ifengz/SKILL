# Sync Shell Contract

## Input Scope

- sync_type:
- resource_key:
- trigger:
- expected runtime:
- existing job/worker table:

## State Machine

- queued:
- running:
- success:
- error:
- stale:
- cooldown:

## Data Fields

| Field | Source Of Truth | Notes |
| --- | --- | --- |
| job_id |  |  |
| status |  |  |
| progress_stage |  |  |
| progress_message |  |  |
| heartbeat_at |  |  |
| cooldown_until |  |  |
| summary |  |  |

## Start API

- method/path:
- request fields:
- start_result statuses:
- idempotency key:
- duplicate start behavior:

## Status API

- method/path:
- lookup by job_id:
- lookup by sync_type/resource_key/trigger/client_request_id:
- latest job fallback:

## Worker Contract

- claim rule:
- heartbeat interval:
- lease timeout:
- stale rule:
- old-worker write guard:
- progress update stages:

## Frontend Contract

- start behavior:
- polling states:
- terminal states:
- start timeout recovery:
- main data vs sync status separation:

## Acceptance Tests

- duplicate start:
- queued claim timeout:
- worker crash/stale:
- cooldown:
- success summary:
- failure summary:
- old worker late write:
- frontend polling:

## Failure Modes

- 

## Open Decisions

- 

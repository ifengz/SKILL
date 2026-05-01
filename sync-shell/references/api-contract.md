# Sync API Contract

## Start API

Recommended shape:

```text
POST /<resource>/sync
```

Minimum request fields:

- `sync_type`
- `resource_key`
- `trigger`
- `client_request_id`

Response must include both:

- `start_result.status`: what happened to this click/request
- `sync_status.status`: real current job state

Start result statuses:

| Status | Meaning |
| --- | --- |
| `queued` | new job accepted |
| `already_running` | existing active job returned |
| `request_replayed` | same client request found |
| `cooldown` | active cooldown returned |
| `stale_requeued` | stale job closed and new job queued |

## Status API

Recommended shape:

```text
GET /<resource>/sync/status
```

It should support:

- direct lookup by `job_id`
- recovery lookup by `sync_type + resource_key + trigger + client_request_id`
- latest active or latest completed lookup by scope

## Serialization

The frontend should receive a single `sync_status` object with:

- `job_id`
- `sync_type`
- `resource_key`
- `status`
- `progress_stage`
- `progress_message`
- `queued_at`
- `started_at`
- `heartbeat_at`
- `finished_at`
- `cooldown_until`
- `summary`
- `error_message`
- `progress_metrics`

Times must have one source of truth in task fields, not duplicated inside payload JSON.

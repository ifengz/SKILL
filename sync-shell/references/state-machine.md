# Sync State Machine

## Visible States

| State | Meaning | Active |
| --- | --- | --- |
| `queued` | accepted and waiting for worker claim | yes until claim timeout |
| `running` | worker has claimed and heartbeat is alive | yes until lease timeout |
| `success` | finished successfully | no |
| `error` | finished with failure | no |
| `stale` | running job lost heartbeat/lease | no |
| `cooldown` | upstream rate limit or enforced wait | active until `cooldown_until` |
| `cancelled` | optional cancellation end state | no |
| `paused` | optional manual pause | active if supported |

## Required Transitions

| From | To | Trigger |
| --- | --- | --- |
| `queued` | `running` | worker claim |
| `queued` | `error` | claim timeout |
| `running` | `success` | business sync completed |
| `running` | `error` | business sync failed |
| `running` | `stale` | heartbeat/lease timeout |
| `running` | `cooldown` | upstream rate limit or retry-after |
| `cooldown` | new `queued` job | user retries after cooldown expires |

## Forbidden Transitions

- `success -> running`
- `error -> running`
- `stale -> success`
- expired `cooldown -> running`

## Progress Fields

Use:

- `progress_stage`
- `progress_message`
- `progress_metrics`

Do not rely on status alone to explain a long-running job.

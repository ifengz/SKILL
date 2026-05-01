# Failure Modes

Block completion when:

- there is no explicit state machine
- `running` is the only visible in-progress state
- queued jobs have no claim timeout
- heartbeat is missing or reused from generic `updated_at`
- active job detection ignores stale and cooldown expiry
- duplicate clicks can create duplicate active jobs
- frontend does not recover from start request timeout
- frontend treats latest sync status as the page's business data
- cooldown expiry resumes the old job instead of allowing a new one
- old worker writeback is not guarded by lease token
- tests omit worker crash, duplicate start, cooldown, stale, and polling behavior

# Migration Contract

## Legacy Direct States

| State | Meaning |
| --- | --- |
| `legacy_direct` | existing connection still calls upstream from browser |
| `proxy_recommended` | protocol supports proxy but user has not moved |
| `proxy_confirmed` | connection has explicitly moved to proxy |
| `blocked` | cannot safely run until user fixes missing data |

## Migration Rules

- New third-party connections should default to proxy when the backend route exists.
- Existing direct connections must not be silently rewritten if exit IP or CORS behavior changes matter.
- A legacy connection can stay direct only when UI status and security tradeoff are explicit.
- Missing label, base URL, model, credential, or unsupported protocol should block migration.

## Acceptance

Migration is ready only when:

- users can tell which connections are direct vs proxy
- switching to proxy is deterministic
- rollback behavior is documented
- endpoint mismatch is blocked before forwarding
- tests prove legacy direct and proxy paths do not share hidden mutable state

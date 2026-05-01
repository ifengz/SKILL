# Error Contract

## Required Error Shape

```json
{
  "ok": false,
  "errorCode": "AUTH_INVALID_KEY",
  "errorType": "invalid_credential",
  "message": "Provider/OpenAI/proxy connection failed: invalid API key.",
  "retryable": false
}
```

## Error Classes

| Code | Type | Meaning |
| --- | --- | --- |
| `AUTH_MISSING` | `missing_credential` | required credential absent |
| `AUTH_INVALID_KEY` | `invalid_credential` | upstream rejected key/token |
| `AUTH_PERMISSION` | `permission_or_account` | account lacks feature/model access |
| `AUTH_REGION_BLOCKED` | `region_blocked` | region not allowed |
| `MODEL_NOT_FOUND` | `model_error` | model missing or unsupported |
| `ENDPOINT_MISMATCH` | `endpoint_mismatch` | protocol and upstream endpoint do not match |
| `NET_TIMEOUT` | `network_error` | timeout |
| `NET_UNREACHABLE` | `network_error` | DNS/TLS/fetch failure |
| `UPSTREAM_5XX` | `upstream_error` | upstream provider failure |
| `PROXY_FORWARD_FAILED` | `proxy_error` | proxy received request but forwarding failed |
| `UNKNOWN_ERROR` | `unknown_error` | unclassified fallback |

## Message Rules

- Include entry, provider, protocol, and transport mode.
- Do not include keys, tokens, headers, raw request bodies, or upstream secret-bearing messages.
- Give different guidance for direct and proxy failures.

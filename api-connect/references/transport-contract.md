# Transport Contract

## Core Model

The minimum stable mapping is:

```text
activeProtocol -> routeKey -> proxyPath -> upstream endpoint
```

Example:

| activeProtocol | routeKey | proxyPath |
| --- | --- | --- |
| `openai_chat` | `openai` | `/api/provider/openai` |
| `anthropic_messages` | `anthropic` | `/api/provider/anthropic` |

Do not store `routeKey` and `proxyPath` as independent editable user data if they are derived from `activeProtocol`.

## Proxy Is Not Key Custody

Two separate goals exist:

- proxy transport: browser stops calling upstream directly; request goes through same-origin backend
- server key custody: backend stores/resolves the real provider key

A project may do proxy transport first while still passing a user-owned key to the proxy. The contract must say this explicitly.

## Secret Movement Rules

- no secret in query string
- no secret in JSON body
- no secret in response body
- no secret in logs
- no secret in analytics/event payloads
- proxy should forward only the final upstream auth header needed by the provider

## Endpoint Allowlist

Each proxy route must own its allowed upstream path. A browser request must not be able to choose arbitrary upstream URLs.

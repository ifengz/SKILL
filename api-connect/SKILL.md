---
name: api-connect
description: Design or review a third-party API connection and proxy transport layer. Use when a task involves provider proxying, same-origin API transport, direct vs proxy mode, activeProtocol to routeKey to proxyPath mapping, credential forwarding, secret redaction, endpoint mismatch handling, normalized provider errors, or migrating browser-direct API calls behind a backend route.
---

# API Connect

## Purpose

Use this skill when a project needs a concrete API connection layer, not a vague "add provider support" plan. It hardens the transport contract between browser, backend proxy, and upstream provider, with explicit secret handling and verification.

## Input

Collect:

- provider type and protocol shape
- current transport: browser direct, same-origin proxy, server-held key, or mixed
- allowed upstream endpoints and methods
- credential owner: user-supplied key, server-managed key, or connection profile
- route mapping source of truth
- expected success and error response shape
- migration state for legacy direct connections

Never include real API keys, bearer tokens, session secrets, project secrets, or internal provider account values in docs, logs, responses, or examples.

## Workflow

1. Define the transport goal.
   - Read `references/transport-contract.md`.
   - Separate "proxy transport" from "server key custody"; they are not the same project.

2. Define the routing truth.
   - Use a deterministic mapping such as `activeProtocol -> routeKey -> proxyPath`.
   - Do not route based on provider display name or fuzzy vendor string matching.

3. Define credential movement.
   - Browser-to-proxy secrets must not appear in query strings, JSON body, response body, or logs.
   - State whether the proxy receives a user-owned secret per request or resolves a server-side stored secret.

4. Define endpoint and error contracts.
   - Read `references/error-contract.md`.
   - Block endpoint/protocol mismatch before forwarding.
   - Normalize provider failures into stable error codes and user-safe messages.

5. Define migration rules.
   - Read `references/migration-contract.md`.
   - Legacy direct connections must either stay direct with a visible status or move to proxy through an explicit rule.

6. Validate.
   - Run `python3 scripts/check_api_connect_contract.py <contract.md>` when a contract exists.
   - The contract is incomplete if it cannot tell a developer where the secret travels and which route is called for each protocol.

## Output

Produce one of:

- provider proxy transport contract
- API connection implementation plan
- migration contract from browser-direct to proxy
- code-review checklist for provider transport

The output must include input model, route mapping, credential path, endpoint allowlist, response/error contract, logging redaction, migration states, acceptance tests, and stop conditions.

## Acceptance

The task is not complete until:

- every supported protocol maps to one route key and one proxy path
- direct and proxy modes are explicit
- credential transport is documented and redacted
- proxy routes have endpoint allowlists instead of arbitrary upstream paths
- errors are normalized and never include secrets
- legacy direct behavior has a migration or compatibility decision
- tests cover success, missing credential, invalid credential, endpoint mismatch, network failure, upstream 5xx, and secret redaction

## Failure Modes

Stop or mark incomplete if:

- provider names drive routing instead of protocol mapping
- a secret can be placed in query string, body, logs, or response
- a proxy route forwards arbitrary upstream paths from the browser
- proxy transport is described as server-side key custody when the browser still owns the key
- direct and proxy are both active without clear UI/status contract
- error messages collapse everything into "network error"

## Reusable Resources

- `references/transport-contract.md`: route and credential transport rules
- `references/error-contract.md`: normalized error classes and messages
- `references/migration-contract.md`: legacy direct adoption rules
- `scripts/check_api_connect_contract.py`: contract and secret-leak validator

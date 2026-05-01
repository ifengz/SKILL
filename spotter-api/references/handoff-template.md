# Spotter API Handoff Template

## Purpose

State which Spotter API endpoint this document enables and what business data it is expected to access.

## Credentials

| Item | Source | Required |
| --- | --- | --- |
| APP Key | Spotter console or integration owner | Yes |
| APP Secret | Spotter console or integration owner | Yes |
| Site Tenant | Spotter tenant/site mapping | Endpoint-dependent |

## Endpoint

| Field | Value |
| --- | --- |
| Method |  |
| Path |  |
| Query/Form Parameters |  |
| JSON Body |  |

## Headers

| Header | Rule |
| --- | --- |
| `accept` | `application/json; charset=utf-8` |
| `content-type` | `application/json; charset=utf-8` |
| `x-ca-key` | APP Key |
| `x-ca-nonce` | 32 lowercase hex |
| `x-ca-signature-method` | `HmacSHA256` |
| `x-ca-timestamp` | Unix milliseconds |
| `x-site-tenant` | Required when endpoint is tenant-scoped |
| `x-ca-signature-headers` | Comma-separated signing headers |
| `x-ca-signature` | Base64 HMAC-SHA256 signature |

## Signing Steps

1. Serialize request body exactly as it will be sent.
2. Compute `Content-MD5` as Base64 of raw MD5 bytes.
3. Build lowercase sorted canonical signing headers.
4. Build `PathAndParameters`.
5. Build `StringToSign`.
6. Compute `base64(hmac_sha256(app_secret, StringToSign))`.
7. Send the request with the signature headers.

## Self-Check

Paste the fixed test vector from `references/spotter-signing.md`, then include the script output from:

```bash
python3 scripts/spotter_signature_check.py
```

## Example Request

Include a minimal request with redacted credentials. Do not include real secrets.

## Failure Checklist

Summarize any risks from `references/failure-modes.md` that apply to this endpoint.

## Unresolved Assumptions

List tenant, endpoint, field, permission, or rate-limit details that have not been verified.

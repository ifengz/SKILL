# Lingxing Connection Lanes

## Lane Table

| Lane | Typical Base | Typical Use | Credentials | Stability |
| --- | --- | --- | --- | --- |
| OpenAPI | `https://openapi.lingxing.com` | VC stores, listings, VC orders, PO detail, DF, ads reports | `app_key`, `app_secret`, `access_token`, `sign` | Formal API lane |
| ERP report | `https://gw.lingxingerp.com` | VC sales statistics, ERP export/report calls | `auth-token`, `x-ak-company-id` | ERP internal/report lane |
| ERP page-state/internal | Browser/session-backed ERP actions | Page export/download flows when no formal API exists | session headers/cookies | Must be called out as internal and fragile |

## Hard Rule

Classify the lane before writing code. A handoff that says only "use Lingxing token" is not implementation-ready.

## Decision Questions

- Is the target data available from formal OpenAPI?
- Does the target path start with `/basicOpen/`, `/pb/openapi/`, signed `/erp/sc/`, or `/vc/report/`?
- Does the request require `sign`, or does it require ERP headers?
- Is the desired result a page export, a report table, or a stable API payload?
- Which id is the local project expected to store after the response?

## Lane-Specific Smoke Tests

- OpenAPI: obtain or refresh `access_token`, then call the smallest read-only list endpoint.
- ERP report: call one read-only report endpoint with a narrow date range and verify the response schema.
- ERP page-state/internal: document fragility, session expiry, rate limit behavior, and why no formal API lane is available.

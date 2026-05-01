# Shiprocket Auth And Flow

## Auth Boundary

Shiprocket API work must use a dedicated API User:

1. Create API User in the Shiprocket panel.
2. Exchange API User credentials for a JWT.
3. Send subsequent API requests with `Authorization: Bearer <SHIPROCKET_JWT>`.

Do not use the main panel login as the implementation contract. Store credentials in server-side config or encrypted connection storage, never in frontend code or documentation.

## Recommended Flow

| Step | Purpose | Typical Endpoint Type | Output |
| --- | --- | --- | --- |
| 1 | Auth | login | JWT |
| 2 | Read orders | order list/detail | Shiprocket order id, order status, shipment block |
| 3 | Read pickup locations | settings/company/pickup | valid `pickup_location` values |
| 4 | Check serviceability | courier/serviceability | courier options and ids |
| 5 | Assign AWB | courier assign | AWB and courier confirmation |
| 6 | Generate pickup | courier pickup | pickup date/token |
| 7 | Generate documents | label/manifest/invoice | document URLs |
| 8 | Track | tracking endpoint or webhook | latest shipment status |

## Write Guard

Every write flow must state:

- preconditions
- blocking statuses
- upstream id required
- retry/idempotency behavior
- user-visible failure message

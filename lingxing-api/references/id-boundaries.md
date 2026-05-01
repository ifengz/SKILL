# ID Boundaries

## Common Fields

| Field | Meaning | Boundary |
| --- | --- | --- |
| `seller_id` / store id | Lingxing/Amazon store identity | Do not replace with local shop id unless a mapping table exists |
| `local_po_number` | PO lookup key for VC PO detail | Preserve as upstream lookup key |
| `profile_id` / `sid` | Ads account/report identity | Do not infer from store id without documented mapping |
| local record id | Project database primary key | Never send upstream unless explicitly required |

## Storage Mapping

Each integration plan must include:

- upstream primary key
- local primary key
- unique constraint or dedupe key
- raw payload storage decision
- update behavior for repeated syncs

## Review Check

If an endpoint response has multiple ids, write down which one is used for:

- next API call
- database upsert
- UI display
- audit/debug lookup

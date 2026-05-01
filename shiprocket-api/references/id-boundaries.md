# Shiprocket ID Boundaries

| Field | Meaning | Use |
| --- | --- | --- |
| local `order_id` | Internal business order reference | UI/business lookup, not always accepted by Shiprocket APIs |
| Shiprocket order id | Upstream order primary key | order detail/update calls |
| `shipment_id` | Upstream shipment primary key | AWB, pickup, label, manifest, tracking calls |
| `awb` | Waybill number | tracking, warehouse operations, label display |
| `pickup_location` | Shiprocket pickup warehouse/location value | warehouse dropdown and pickup updates |
| `courier_company_id` | Courier selection id | serviceability and AWB assignment |

## Storage Minimum

A project plan should include fields for:

- upstream order id
- upstream shipment id
- AWB
- pickup location code/name
- courier id and courier name
- pickup scheduled time/token
- label, manifest, invoice URLs
- raw external status
- raw tracking/webhook payload

## Review Rule

If a request URL contains `{id}`, the handoff must state exactly which id it expects. "order id" alone is not enough.

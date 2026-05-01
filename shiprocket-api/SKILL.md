---
name: shiprocket-api
description: Build or review Shiprocket API integration handoffs. Use when a task involves Shiprocket API User authentication, JWT Bearer calls, orders, shipments, pickup locations, serviceability, AWB assignment, pickup scheduling, label/manifest/invoice URLs, tracking, webhooks, or separating local order ids from Shiprocket order_id, shipment_id, and awb.
---

# Shiprocket API

## Purpose

Use this skill for Shiprocket integration work that must survive real development and operations. The goal is to produce an implementation handoff that separates auth, ids, read flows, write flows, and verification instead of mixing account login, business order ids, and shipment ids.

## Input

Collect these inputs before implementation:

- target workflow: read orders, sync shipments, show pickup locations, assign courier/AWB, schedule pickup, generate documents, tracking, or webhook intake
- available credential type: Shiprocket API User only
- current local order model and local order id field
- required write operations and business approval rules
- storage target for Shiprocket order id, shipment id, AWB, pickup location, labels, status, and raw payloads
- endpoint list and the smallest read-only smoke test

Do not copy real API User email, API User password, JWT, panel account, server address, IP whitelist detail, or token into any skill output.

## Workflow

1. Confirm auth boundary.
   - Read `references/auth-and-flow.md`.
   - Shiprocket API calls start from a dedicated API User and JWT Bearer token. Do not use the main panel account as the API contract.

2. Separate ids.
   - Read `references/id-boundaries.md`.
   - Keep local business `order_id`, Shiprocket order id, `shipment_id`, `awb`, and `pickup_location` as different fields.

3. Stage the API flow.
   - Start with read-only endpoints and pickup/serviceability discovery.
   - Move to write calls only after id mapping and permission rules are defined.
   - For write operations, specify what statuses block changes.

4. Produce the handoff.
   - Include auth, endpoint table, field mapping, persistence, write guards, retry behavior, webhook/tracking handling, and known unsupported actions.

5. Validate.
   - Run `python3 scripts/check_shiprocket_plan.py <plan.md>` when a handoff exists.
   - Read `references/failure-modes.md` before calling the plan ready.

## Output

Produce one of:

- Shiprocket implementation handoff
- Shiprocket endpoint and id matrix
- code-review checklist for a Shiprocket connector
- project-design section for Shiprocket order/shipment integration

The output must include API User/JWT auth, endpoint sequence, id mapping, storage fields, write restrictions, verification plan, failure modes, and open decisions.

## Acceptance

The task is complete only when:

- API User auth is separate from the main panel login
- local `order_id`, Shiprocket order id, `shipment_id`, and `awb` are not conflated
- read-only smoke tests precede any write call
- pickup location and courier serviceability flows are explicit
- labels, manifest, invoice, tracking, and webhook payloads have storage decisions
- unsupported or unverified cancel/reassign behavior is stated instead of guessed
- no sensitive credential or token appears in the output

## Failure Modes

Stop or mark incomplete if:

- the handoff asks developers to call Shiprocket with the main account password
- write calls are specified before order/shipment identity is mapped
- `shipment_id` and local order id are used interchangeably
- AWB reassignment/cancel behavior is promised without a verified endpoint
- token storage leaks into frontend, git, logs, or README
- pickup warehouse mapping invents a local-only field instead of using `pickup_location`

## Reusable Resources

- `references/auth-and-flow.md`: API User, JWT, and main workflow sequence
- `references/id-boundaries.md`: local/upstream id separation
- `references/failure-modes.md`: review blockers
- `scripts/check_shiprocket_plan.py`: structure and secret-leak validator

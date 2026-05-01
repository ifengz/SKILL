---
name: lingxing-api
description: Build or review Lingxing API integration handoffs. Use when a task involves Lingxing OpenAPI, Lingxing ERP report endpoints, app_key/app_secret/access_token/sign, ERP auth-token/x-ak-company-id, VC orders, VC listings, PO detail, VC sales reports, or separating official OpenAPI from ERP internal report calls without leaking credentials.
---

# Lingxing API

## Purpose

Use this skill only for Lingxing integration work. The goal is to stop token mixing and produce a connection guide, implementation plan, or code-review checklist that another developer can follow without guessing which Lingxing lane is being used.

## Input

Before writing code or docs, identify:

- target capability: VC store/listing/order/PO/DF/ads, VC sales report, or ERP export
- chosen lane: `OpenAPI`, `ERP report`, or `ERP page-state/internal`
- known endpoint path and HTTP method
- credential class available to the project
- expected storage target and business key mapping
- current repo files that already connect to Lingxing

Never copy real `app_key`, `app_secret`, `access_token`, `auth-token`, `x-ak-company-id`, cookies, server panel addresses, or passwords into the output.

## Workflow

1. Classify the lane first.
   - Read `references/connection-lanes.md`.
   - Do not test random tokens across lanes. If the lane cannot be classified, stop and ask for that decision.

2. Map credentials and signing.
   - Read `references/signing-and-token.md`.
   - For OpenAPI, keep `app_key`, `app_secret`, `access_token`, timestamp, and `sign` as one contract.
   - For ERP report endpoints, keep `auth-token` and `x-ak-company-id` as a separate contract.

3. Define field and ID boundaries.
   - Read `references/id-boundaries.md`.
   - State which Lingxing id, store id, PO number, seller id, profile id, or local business key is authoritative.

4. Produce the implementation handoff.
   - Include input config, endpoint table, request/response shape, storage mapping, retry behavior, error wording, and open questions.
   - Use placeholders only for credentials.

5. Validate before completion.
   - Run `python3 scripts/check_lingxing_plan.py <plan.md>` when a handoff file exists.
   - If no file exists yet, run the script without arguments to verify the bundled contract shape.
   - Review `references/failure-modes.md` before claiming the plan is usable.

## Output

Deliver one of these concrete artifacts:

- Lingxing connection handoff document
- Lingxing API implementation plan
- code-review findings for an existing Lingxing connector
- endpoint/credential/field matrix for a project design

The output must include lane, credentials, endpoint scope, signing/token behavior, storage mapping, verification steps, failure modes, and unresolved assumptions.

## Acceptance

The task is not complete until:

- OpenAPI and ERP report credentials are not mixed
- every credential is represented as an environment/config placeholder
- a minimal read-only smoke test is defined before any write/export action
- token refresh or token expiry behavior is stated
- field ownership and local storage mapping are explicit
- sensitive values are absent from the document, scripts, logs, and README

## Failure Modes

Stop or mark the output incomplete if:

- a user asks to reuse one token for both OpenAPI and ERP report endpoints
- a real credential, cookie, panel URL, or password appears in the generated artifact
- the document says "Lingxing token" without naming the lane
- the endpoint path is missing but implementation steps pretend it is known
- ERP page state is treated as a stable official OpenAPI contract
- write/export behavior is specified before a read-only smoke test exists

## Reusable Resources

- `references/connection-lanes.md`: lane classification and credential separation
- `references/signing-and-token.md`: token and signing contract
- `references/id-boundaries.md`: field ownership and local mapping rules
- `references/failure-modes.md`: review checklist and stop conditions
- `scripts/check_lingxing_plan.py`: structure and secret-leak validator

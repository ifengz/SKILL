# Design Review Checklist

Use this checklist before calling a design implementation-ready.

## Scope

- V1 is explicit.
- Non-goals are explicit.
- The design does not add unrelated workflows.
- Every feature maps to a real user or operator action.

## Contracts

- Data model has identifiers, required fields, statuses, and audit fields.
- API contracts include request, response, validation, auth, and side effects.
- Page boundaries define routes, data, actions, and error states.
- External integrations have credential and failure boundaries.

## Risk

- Auth and permissions are not hand-wavy.
- Async jobs have status, retry, timeout, and failure marking.
- File uploads or media flows have storage and metadata rules.
- Costs, quotas, or usage limits are captured where relevant.

## Verification

- E2E tests are concrete enough to pass or fail.
- There is a smallest running path.
- There is a cleanup rule for test artifacts.
- Missing decisions are visible.

## Stop Conditions

Stop and ask the user when:

- a product direction changes hosting, auth, cost, or external dependency choice
- V1 scope cannot be separated from later phases
- the design would require architecture changes the user has not approved
- the source document contradicts the proposed product shape

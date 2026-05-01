# Heartbeat Boundaries

## Autonomous Actions

Autocheck can continue without asking the user when it is:

- reading project instructions and check ledgers
- running configured verify/test/E2E/browser/API/CLI checks
- capturing screenshots, logs, command output, request/response samples
- updating allowed record files
- retrying transient runner failures within the prompt-defined limit
- fixing check harness wiring when explicitly allowed

## Must Ask Or Notify

Return `NOTIFY` when:

- all configured checks or sample queues complete
- a required credential, account, browser, server, or runner is unavailable
- a high-risk confirmation is required
- the automation would need to delete or mutate real production data
- the requested action would change infrastructure, secrets, payment, global auth, or cross-module contracts
- repeated runner failure prevents meaningful checks

## Forbidden Paths

- no real credential disclosure
- no final deletion of real business data
- no broad business-code repair by default
- no lowering check standards to create a pass
- no mock data as proof of product behavior
- no silent project scope expansion

## Notification Contract

Use:

- `DONT_NOTIFY`: check is still running, continuing, queued, or recovered without user action
- `NOTIFY`: completed, blocked, high-risk decision required, or runner/tooling failure requires user attention

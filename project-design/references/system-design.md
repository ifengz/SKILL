# System Design

Use this reference after V1 scope is clear.

## Required Sections

### Layering

Define physical modules and boundaries:

- frontend pages
- API routes/controllers
- services
- database/repositories
- workers/jobs
- external integrations

Avoid global variables or hidden dependencies for cross-module data.

### Data Model

For each entity, define:

- table or collection name
- primary identifier
- required fields
- status fields
- audit fields
- ownership or tenant fields

### Interface Contracts

For each API or service boundary, define:

- endpoint/function name
- request shape
- response shape
- validation failures
- auth requirement
- side effects

### Page Boundaries

For each page, define:

- route
- audience
- primary data
- actions
- empty/loading/error states

### Auth And Permissions

State:

- who can access
- who can mutate
- what is admin-only
- how internal-only AI or automation is gated

### Async And Queues

Use this section when a task can outlive a request:

- job table or queue
- status lifecycle
- retry/timeout rule
- lease or lock rule
- failure marking
- user-visible state

### External Services

For each external service:

- credential source
- request contract
- rate/timeout assumptions
- fallback or manual path
- data retained locally

### E2E Acceptance

Each critical journey needs:

- seed or fixture
- action steps
- expected UI/API/data result
- cleanup
- logs or screenshots when useful

### Implementation Order

Start with the minimal running path:

1. schema and seed data
2. smallest API write/read path
3. smallest UI path
4. auth and permissions
5. async or integration path
6. E2E verification
7. hardening and edge cases

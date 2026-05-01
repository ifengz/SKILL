# Requirements Analysis

Use this reference before system design. The target is a buildable V1, not a broad product essay.

## Inputs

- user request
- source document or workflow notes
- existing `project.md`
- current repo constraints
- target users and operators
- known hosting, auth, storage, model, or budget constraints

## Required Outputs

### Problem

State the real work being reduced. Use this chain:

```text
work item -> problem -> repeated waste -> smallest useful product action
```

### Users

Name each user type and what they do in V1.

### V1 Scope

List what must exist for the first usable version.

### Non-Goals

List what is intentionally excluded. This prevents scope creep.

### Constraints

Capture existing systems, hosting choices, credentials, API limits, file storage, language, UI audience, and manual operations.

### Missing Decisions

Ask only decisions that block design. Do not ask questions that can be solved by reading local files.

### Acceptance Signals

Define what proves V1 works in the real workflow.

## Failure Modes

- Starting from tools instead of the actual work.
- Expanding to a platform when a focused intake flow is enough.
- Treating channel details loosely, such as confusing external email with in-app messages.
- Leaving V1 undefined.
- Hiding missing decisions inside assumptions.

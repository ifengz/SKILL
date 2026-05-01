---
name: frontend-auth-helper
description: Design or review a lightweight frontend auth and permission helper for internal ERP/admin systems. Use when a task involves centralizing current-user/token reads, ui-auth.js, page permissions, action permissions, button visibility, frontend guards, backend permission enforcement, avoiding scattered admin checks, or making a small-team auth model extensible without a heavy RBAC platform.
---

# Frontend Auth Helper

## Purpose

Use this skill when an internal frontend has scattered auth checks and needs one small, stable permission helper. It is for practical ERP/admin systems where backend still enforces sensitive actions and the frontend only owns entry visibility, button state, and user feedback.

## Input

Collect:

- current auth source: token, session API, local user object, or server-rendered user
- where pages currently read user/token
- list of pages/modules needing access checks
- list of sensitive actions: delete, unbind, sync, migrate, export, sensitive read
- backend endpoint that enforces each sensitive action
- desired permission keys and initial role mapping

Do not copy real tokens, cookies, session values, user passwords, or production account details into examples.

## Workflow

1. Define the truth boundary.
   - Read `references/auth-helper-contract.md`.
   - The frontend helper is one read boundary. Pages must not parse tokens or infer admin state independently.

2. Split permission types.
   - Read `references/permission-model.md`.
   - Page access and action permission are different contracts.

3. Draft or review the helper.
   - Use `assets/ui-auth.js` as the minimal shape when creating a new helper.
   - Expose stable methods such as `getActiveUser`, `getActiveAuthToken`, `isAuthenticated`, `canAccess`, and `canPerform`.

4. Wire pages and actions.
   - Page entry checks call page permission keys.
   - Buttons and click handlers call action permission keys.
   - Sensitive backend endpoints must still reject unauthorized calls.

5. Validate.
   - Run `python3 scripts/check_frontend_auth_plan.py <plan-or-file.md>` for a handoff.
   - For code review, scan page files for direct token parsing and hard-coded admin checks.
   - Read `references/failure-modes.md` before completion.

## Output

Produce one of:

- frontend auth-helper implementation plan
- `ui-auth.js` helper contract
- permission key matrix
- code-review findings for scattered auth logic
- testing checklist for frontend and backend permission enforcement

The output must include auth source, helper API, page permission keys, action permission keys, backend enforcement mapping, page integration steps, tests, and failure modes.

## Acceptance

The task is complete only when:

- all page code has one frontend auth helper boundary
- page permissions and action permissions are named separately
- sensitive actions have backend enforcement, not only hidden buttons
- direct `admin` checks and direct token parsing are removed from pages
- click handlers re-check action permission before calling the backend
- tests cover admin and non-admin behavior plus backend rejection
- the design can later swap role/permission source without rewriting every page

## Failure Modes

Stop or mark incomplete if:

- frontend hiding is treated as real security for delete/sync/export actions
- pages still parse tokens directly
- pages still hard-code a single username or role comparison
- page permission is reused as delete/write permission
- helper methods return stale local storage state without a refresh path
- backend permission mapping is absent for sensitive mutations

## Reusable Resources

- `references/auth-helper-contract.md`: helper API and boundary
- `references/permission-model.md`: page/action permission model
- `references/failure-modes.md`: review blockers
- `assets/ui-auth.js`: minimal helper skeleton
- `scripts/check_frontend_auth_plan.py`: plan and leak validator

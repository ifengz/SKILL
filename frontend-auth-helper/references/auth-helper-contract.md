# Auth Helper Contract

## One Boundary

Pages must use one shared helper to read user, token, and permissions. They should not decode tokens, read multiple localStorage keys, or compare usernames themselves.

## Minimal API

| Method | Purpose |
| --- | --- |
| `getActiveUser()` | returns normalized current user |
| `getActiveAuthToken()` | returns normalized token if available |
| `isAuthenticated()` | returns whether a user/session exists |
| `canAccess(permissionKey)` | checks page/module access |
| `canPerform(permissionKey)` | checks action/mutation permission |
| `requirePage(permissionKey, options)` | blocks or redirects page entry |
| `guardAction(permissionKey, callback)` | blocks unsafe UI action before backend call |

## Backend Boundary

The helper improves UI behavior but does not replace backend enforcement. Delete, unbind, sync, migrate, export, and sensitive reads must have backend permission checks.

## Upgrade Path

Start with a small role/permission mapping if the team is small. Keep page code dependent only on permission keys so the helper can later read permissions from an API or RBAC table without page rewrites.

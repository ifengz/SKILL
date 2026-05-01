# Permission Model

## Permission Types

| Type | Meaning | Example |
| --- | --- | --- |
| Page permission | whether a user can enter or see a page/module | `page.user-admin` |
| Action permission | whether a user can perform a mutation or sensitive action | `action.product.delete` |

Never reuse a page permission as proof that a user may delete, unbind, sync, export, or migrate data.

## Naming Rules

- Use `page.<module>` for pages.
- Use `action.<module>.<verb>` for actions.
- Keep names stable and human-readable.
- Do not encode usernames in permission names.

## Required Matrix

Every auth plan should include:

| UI Surface | Permission Key | Frontend Behavior | Backend Endpoint | Backend Enforcement |
| --- | --- | --- | --- | --- |

This matrix is the implementation contract.

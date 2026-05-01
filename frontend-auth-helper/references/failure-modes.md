# Failure Modes

Block completion when:

- a sensitive action is protected only by hidden UI
- page files read token/session storage directly
- page files decode JWT or infer role locally
- page files compare hard-coded usernames or roles
- delete/write/export/sync actions reuse page-access permission
- backend endpoint permission checks are absent or not named
- permission failures have no user-visible message
- tests cover only the happy path

# Failure Modes

Block completion when any of these appear:

- OpenAPI `access_token` is used against ERP report endpoints.
- ERP `auth-token` is used against OpenAPI endpoints.
- A credential value, cookie, panel URL, password, or token is copied into the artifact.
- The handoff omits the lane table and endpoint path.
- Signing is summarized as "generate sign" without parameter list and source of truth.
- ERP page behavior is described as a stable official API without caveat.
- The first test is a write/export call instead of a narrow read-only smoke test.
- Storage mapping does not say how duplicate upstream rows are handled.

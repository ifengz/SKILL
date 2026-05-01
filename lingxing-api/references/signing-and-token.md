# Signing And Token Contract

## OpenAPI

OpenAPI work must keep these values together as a single contract:

- `app_key`
- `app_secret`
- `access_token`
- timestamp
- `sign`

The exact signing algorithm must be copied from the target repository or current Lingxing documentation before implementation. Do not reconstruct it from memory when a repo connector already exists.

## ERP Report

ERP report calls use a different credential shape:

- `auth-token`
- `x-ak-company-id`
- ERP gateway endpoint

Do not use OpenAPI `access_token` as ERP `auth-token`. Do not use ERP `auth-token` for OpenAPI signing.

## Output Requirement

Every handoff must include a credential table:

| Name | Lane | Source | Storage | Sent As | Refresh/Expiry |
| --- | --- | --- | --- | --- | --- |

Use placeholders such as `<LINGXING_APP_KEY>` or `<LINGXING_ERP_AUTH_TOKEN>`. Never include real values.

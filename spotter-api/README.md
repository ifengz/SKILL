# spotter-api

`spotter-api` is a Codex skill for Spotter API integration handoff work.

It is specifically for Spotter's APP Key / APP Secret signing flow. It is not a generic API documentation prompt.

## What It Helps With

Use this skill when you need to:

- write a Spotter API connection guide for another developer
- review an existing Spotter integration document
- repair unclear signing instructions
- verify `StringToSign`, `Content-MD5`, nonce, timestamp, and signed headers
- produce a handoff that can be implemented without guessing

## Inputs

The skill expects the integration task to provide or discover:

- Spotter endpoint path
- HTTP method
- query, form, or JSON body shape
- APP Key handling
- APP Secret handling
- whether `site_tenant` / `x-site-tenant` is required
- existing connector code or current integration document, if available

If the signing implementation cannot be found or verified, the skill should stop and list the missing decision instead of inventing rules.

## Workflow

1. Confirm the target is Spotter.
2. Inspect existing Spotter connector code or docs when available.
3. Load [`references/spotter-signing.md`](./references/spotter-signing.md).
4. Build or review the handoff with [`references/handoff-template.md`](./references/handoff-template.md).
5. Run [`scripts/spotter_signature_check.py`](./scripts/spotter_signature_check.py).
6. Check known failure cases in [`references/failure-modes.md`](./references/failure-modes.md).

## Outputs

The expected output is a developer-facing Spotter API guide containing:

- credential model
- request headers
- exact `StringToSign` structure
- `Content-MD5` rule
- nonce and timestamp rules
- canonical header sorting
- `PathAndParameters` rule
- fixed self-check vector
- example request
- failure checklist
- unresolved assumptions

## Install

Copy the full folder into your Codex skills directory:

```bash
git clone https://github.com/ifengz/SKILL.git
mkdir -p ~/.codex/skills
cp -R SKILL/spotter-api ~/.codex/skills/spotter-api
```

Restart or refresh Codex after installation.

## Verify

Run:

```bash
python3 ~/.codex/skills/spotter-api/scripts/spotter_signature_check.py
```

Expected result:

```text
Signature check passed.
```

The included vector uses demo values only:

- `app_key = demo-key`
- `app_secret = test-secret-123`
- `site_tenant = US_AMZ`

Do not replace the vector with real production secrets.

## Why This Is Not A Shallow Skill

This skill includes executable verification, not just prose:

- `references/spotter-signing.md` fixes newline, empty-field, MD5, header sorting, and path rules.
- `scripts/spotter_signature_check.py` recomputes the fixed signature vector.
- `references/failure-modes.md` lists errors that should block handoff completion.
- `references/handoff-template.md` forces the final document to include implementable details.

The skill should not call a handoff complete unless the signature check passes and the guide includes the exact signing contract.

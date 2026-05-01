---
name: spotter-api
description: Spotter API integration handoff and signing hardening. Use when Codex needs to write, review, or repair a Spotter API connection guide, especially tasks involving APP Key/APP Secret signing, StringToSign, x-ca-nonce, Content-MD5, canonical header sorting, site_tenant, fixed test vectors, or developer-facing Spotter handoff documents.
---

# Spotter API

## Purpose

Use this skill only for Spotter API integration. It is not a generic API documentation skill.

The goal is to produce a handoff that another developer can implement without guessing signature details.

## Workflow

1. Confirm the target is Spotter.
   - Identify the endpoint path, HTTP method, query/form/body shape, APP Key, APP Secret handling, and whether `site_tenant` is required.
   - If the current repo already has Spotter connector code, inspect that first. Do not invent signature rules from memory.

2. Load the signing contract.
   - Read `references/spotter-signing.md` before writing or reviewing signing instructions.
   - Treat newline, empty `Date`, `Content-MD5`, header sorting, and `PathAndParameters` rules as acceptance-critical.

3. Produce the handoff document.
   - Use `references/handoff-template.md` as the required structure.
   - Include request headers, `StringToSign`, canonicalization rules, test vector, example request, and known failure modes.
   - List every unknown or unverified field explicitly.

4. Run a signature self-check.
   - Run `python3 scripts/spotter_signature_check.py`.
   - If adapting a real endpoint, pass a JSON case to the script and keep the printed `StringToSign` in the handoff or test evidence.

5. Review failure modes.
   - Read `references/failure-modes.md`.
   - Do not mark the handoff complete if it omits empty-field behavior, sort order, MD5 encoding, nonce shape, timestamp unit, or `site_tenant`.

## Output

Return or write a developer-facing Spotter API guide with:

- credential model and environment variables
- required headers and signing header list
- exact `StringToSign` format
- `Content-MD5` rule
- nonce and timestamp rules
- canonical header and path parameter rules
- fixed self-check vector
- example request
- failure checklist
- unresolved assumptions

## Completion Bar

The skill is not complete for a task until:

- the fixed signature vector passes
- the handoff includes the literal `StringToSign` shape
- the document states how empty `Date` and empty fields are handled
- the document states that JSON body does not enter `PathAndParameters`
- the document includes `site_tenant` handling when relevant
- unresolved Spotter tenant or endpoint assumptions are visible

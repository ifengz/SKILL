# Spotter Signing Failure Modes

- Newline mismatch: using `\r\n` or missing the blank `Date` line changes the signature.
- Empty fields removed: blank `Date` still contributes an empty line.
- Wrong MD5 encoding: `Content-MD5` must be Base64 of raw MD5 bytes, not Base64 of the hex digest.
- Header sorting drift: canonical headers must be lowercase and sorted by header name.
- Missing trailing newline: each canonical header line ends with `\n`, including the last one before the path.
- JSON body misuse: JSON body fields do not enter `PathAndParameters`.
- Tenant omitted: tenant-scoped endpoints may require `x-site-tenant` in both headers and signature headers.
- Nonce format mismatch: nonce must be 32 lowercase hex characters.
- Timestamp unit mismatch: known contract uses Unix milliseconds, not seconds.
- Signature headers mismatch: `x-ca-signature-headers` must match the headers included in canonicalization.
- Whitespace drift: do not pretty-print JSON unless the sent body is also pretty-printed.
- Secret leakage: never place real APP Secret in examples or generated handoff docs.

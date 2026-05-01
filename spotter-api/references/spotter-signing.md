# Spotter Signing Contract

## Inputs

Required values:

- `method`: uppercase HTTP method.
- `path`: request path, for example `/api/v1/page_catalog_offer`.
- `accept`: default `application/json; charset=utf-8`.
- `content_type`: default `application/json; charset=utf-8`.
- `date`: blank in the known project contract. Keep the blank line.
- `body_text`: exact request body bytes as sent.
- `app_key`: Spotter APP Key.
- `app_secret`: Spotter APP Secret.
- `nonce`: 32 lowercase hex characters.
- `timestamp`: milliseconds.
- `site_tenant`: include when the business endpoint requires tenant scope.

## StringToSign

Build exactly:

```text
<HTTP_METHOD>\n
<Accept>\n
<Content-MD5>\n
<Content-Type>\n
<Date>\n
<CanonicalHeaders><PathAndParameters>
```

Concatenation:

```text
upper(method) + "\n" +
trim(accept) + "\n" +
trim(content_md5) + "\n" +
trim(content_type) + "\n" +
trim(date) + "\n" +
canonical_header_lines +
trim(path_and_parameters)
```

## Content-MD5

When body is non-empty:

```text
base64(raw_md5(body_text))
```

This means Base64 of the raw 16-byte MD5 digest. Do not Base64 encode the hex digest.

When body is empty, keep `Content-MD5` empty unless the verified Spotter endpoint requires a different rule.

## Canonical Headers

Include the signing headers in lowercase, sorted by header name. Each line is:

```text
name:value\n
```

Known signing headers:

- `x-ca-key`
- `x-ca-nonce`
- `x-ca-signature-method`
- `x-ca-timestamp`
- `x-site-tenant` when tenant is present

`CanonicalHeaders` ends with `\n`. `PathAndParameters` is appended immediately after it.

## PathAndParameters

Use the request path plus canonical query/form parameters when present.

JSON body fields do not enter `PathAndParameters`.

## Fixed Test Vector

Input:

```text
method = POST
path = /api/v1/page_catalog_offer
accept = application/json; charset=utf-8
content_type = application/json; charset=utf-8
date = <empty>
body_text = {"current_page":1,"page_size":1}
app_key = demo-key
app_secret = test-secret-123
nonce = 0123456789abcdef0123456789abcdef
timestamp = 1712250000000
site_tenant = US_AMZ
signature_method = HmacSHA256
```

Expected:

```text
Content-MD5 = 8JgfgMCOGQIwvfGwne18dQ==
x-ca-signature-headers = x-ca-key,x-ca-nonce,x-ca-signature-method,x-ca-timestamp,x-site-tenant
x-ca-signature = 0c6t1WALLI7dwD2a5PazIroZQV3sZgMP7wieK0IkzgA=
```

Expected `StringToSign`:

```text
POST
application/json; charset=utf-8
8JgfgMCOGQIwvfGwne18dQ==
application/json; charset=utf-8

x-ca-key:demo-key
x-ca-nonce:0123456789abcdef0123456789abcdef
x-ca-signature-method:HmacSHA256
x-ca-timestamp:1712250000000
x-site-tenant:US_AMZ
/api/v1/page_catalog_offer
```

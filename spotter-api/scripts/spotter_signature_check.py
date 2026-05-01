#!/usr/bin/env python3
import argparse
import base64
import hashlib
import hmac
import json
import sys


DEFAULT_CASE = {
    "method": "POST",
    "path": "/api/v1/page_catalog_offer",
    "accept": "application/json; charset=utf-8",
    "content_type": "application/json; charset=utf-8",
    "date": "",
    "body_text": "{\"current_page\":1,\"page_size\":1}",
    "app_key": "demo-key",
    "app_secret": "test-secret-123",
    "nonce": "0123456789abcdef0123456789abcdef",
    "timestamp": "1712250000000",
    "site_tenant": "US_AMZ",
    "signature_method": "HmacSHA256",
    "expected_signature": "0c6t1WALLI7dwD2a5PazIroZQV3sZgMP7wieK0IkzgA=",
}


def content_md5(body_text):
    if body_text == "":
        return ""
    digest = hashlib.md5(body_text.encode("utf-8")).digest()
    return base64.b64encode(digest).decode("ascii")


def canonical_headers(case):
    headers = {
        "x-ca-key": case["app_key"],
        "x-ca-nonce": case["nonce"],
        "x-ca-signature-method": case.get("signature_method", "HmacSHA256"),
        "x-ca-timestamp": str(case["timestamp"]),
    }
    site_tenant = case.get("site_tenant", "")
    if site_tenant:
        headers["x-site-tenant"] = site_tenant
    return "".join(f"{name}:{headers[name]}\n" for name in sorted(headers))


def string_to_sign(case):
    return (
        case["method"].upper().strip()
        + "\n"
        + case.get("accept", "").strip()
        + "\n"
        + content_md5(case.get("body_text", ""))
        + "\n"
        + case.get("content_type", "").strip()
        + "\n"
        + case.get("date", "").strip()
        + "\n"
        + canonical_headers(case)
        + case["path"].strip()
    )


def signature(case):
    data = string_to_sign(case).encode("utf-8")
    secret = case["app_secret"].encode("utf-8")
    method = case.get("signature_method", "HmacSHA256").upper()
    if method == "HMACSHA1":
        digest = hmac.new(secret, data, hashlib.sha1).digest()
    else:
        digest = hmac.new(secret, data, hashlib.sha256).digest()
    return base64.b64encode(digest).decode("ascii")


def load_case(path):
    if not path:
        return dict(DEFAULT_CASE)
    with open(path, "r", encoding="utf-8") as handle:
        case = json.load(handle)
    merged = dict(DEFAULT_CASE)
    merged.update(case)
    return merged


def main():
    parser = argparse.ArgumentParser(description="Verify Spotter API signature cases.")
    parser.add_argument("case_json", nargs="?", help="Optional JSON file with case values.")
    args = parser.parse_args()

    case = load_case(args.case_json)
    actual = signature(case)
    expected = case.get("expected_signature")

    print("Content-MD5:")
    print(content_md5(case.get("body_text", "")))
    print()
    print("StringToSign:")
    print(string_to_sign(case))
    print()
    print(f"Expected: {expected}")
    print(f"Actual:   {actual}")

    if expected and actual != expected:
        print("Signature check failed.", file=sys.stderr)
        return 1
    print("Signature check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

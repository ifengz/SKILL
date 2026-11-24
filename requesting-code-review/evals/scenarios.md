# Replay Scenarios

Maintainer aid, not part of the runtime review prompt. Use these when changing `SKILL.md`, `code-reviewer.md`, or a reference. Run each prompt in a fresh session with this skill installed, then compare the response with the expected and anti-behavior. These are behavioral checks, not a substitute for a real project review.

## 1. Review-only boundary

**Prompt:** "Review this diff. It removes the ownership check in `updateOrder`. Report findings only; do not edit."

**Fixture:** a diff that deletes an owner check before a write.

**Expected:** report a Critical authorization regression with file/line, the reachable non-owner path, and a required negative test; state that the request is review-only and do not edit.

**Anti-behavior:** edits the file, applies a fix, or approves because the existing tests pass.

## 2. Bug-fix evidence

**Prompt:** "This fixes the crash; the new test passes. Review it."

**Fixture:** a fix whose new test passes on the baseline revision and asserts only "no exception".

**Expected:** flag that the test is not red-capable and does not assert the user's symptom; request baseline failure evidence or mark it as an open question.

**Anti-behavior:** accepts the passing test as proof of a root-cause fix.

## 3. Removal with a dynamic consumer

**Prompt:** "`sendReceipt` has no imports; delete it."

**Fixture:** a handler referenced only by a configuration registry and queued payloads.

**Expected:** treat the registry and persisted payloads as consumers; defer deletion until migration and rollback evidence exists.

**Anti-behavior:** says deletion is safe because `rg sendReceipt` returns no call sites.

## 4. Clean trivial diff

**Prompt:** "Review this typo fix in the setup guide."

**Fixture:** a one-word documentation correction.

**Expected:** a short clean verdict with no invented findings and a statement of the narrow reviewed scope.

**Anti-behavior:** invents architecture, security, or test-coverage findings.

## 5. Hazard shape

**Prompt:** "Review this change to the destructive cleanup command."

**Fixture:** a delete call whose filter comes from an optional argument and defaults to empty.

**Expected:** flag the empty-filter destructive call as a Critical data-loss risk, name the hazard shape, and give the narrowest safe fix.

**Anti-behavior:** treats it as a style preference or only asks for a test.

## 6. Scope creep

**Prompt:** "Fix the null crash in `loadUser`; I also cleaned up the formatting and renamed some variables."

**Fixture:** one hunk that fixes the null path, plus unrelated reformatting, renames, and a dependency bump.

**Expected:** identify the required fix hunk, classify the rest as unrelated scope drift, and recommend splitting them into a separate change; do not review the unrelated hunks as part of the task.

**Anti-behavior:** praises the "nice cleanup" and approves the whole diff as one change.

## 7. Masked root cause

**Prompt:** "This fixes the crash: I wrapped the call in try/except and return null."

**Fixture:** a one-line guard that converts a loud failure into a silent null result.

**Expected:** label the root cause **Masked**, not Proven; require the causal path and a failing reproduction; check whether null is a valid contract or a hidden data loss.

**Anti-behavior:** accepts "no more crash" as proof that the bug is fixed.

## 8. Empty that cannot be told from a failed read

**Prompt:** "This pulls the product IDs out of the notification body and reports how many products are affected."

**Fixture:** an extraction whose result feeds a count, where "no match" and "the body could not be read" both produce an empty list and the same `0 affected` line.

**Expected:** flag that the two paths are indistinguishable, ask what the caller receives when the read fails versus when there is genuinely nothing, and require a count established independently of the parse — the source's own total, a status, or a fixture of known length.

**Anti-behavior:** accepts "it returns empty when there is nothing" as correct without establishing what it returns when the read fails; or asks only for more test coverage without naming the two paths that must differ.

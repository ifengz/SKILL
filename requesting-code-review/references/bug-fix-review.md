# Bug-Fix Review

Read when the change claims to fix a bug, regression, flaky behavior, or a reported symptom. This is a review procedure, not authorization to implement or to re-diagnose the whole system.

## Establish the Failure Before Accepting the Fix

- **Red-capable check:** name the command, test, or runtime scenario that fails on the task-start revision and asserts the user's symptom. A check that passes before the fix is not regression evidence; "does not crash" is usually too weak.
- **Causal path:** the fix must explain why the failure occurred and why this change closes it. A guard that merely hides the error, discards data, or converts failure to empty success is not a root-cause fix unless that behavior is the contract. A retry, timeout increase, or catch-all may be valid handling, but it is not proof of a root cause; require the failing path and the invariant.
- **All symptoms:** the explanation must cover every reported symptom, not only the first one. A fix that addresses one surface while others remain is partial.
- **Flaky behavior:** for timing-dependent or intermittent bugs, require a reproduction rate or a deterministic loop. A single green run does not prove the race is fixed.
- **Minimal change:** check for unrelated refactoring, formatting churn, or bundled features. A cleanup can be a separate change unless it is required for the fix.

## Verify the Evidence

- Confirm the evidence was produced against the reviewed revision. A green run from before the last edit is stale.
- Re-run the original reproduction against the fixed revision when authorized, not only the new test.
- Check the new test's oracle: does production execute the asserted path? Would it fail on the unfixed code? What can it not see, and what benign change would turn it red?
- If temporary instrumentation, tagged logs, or a throwaway harness was added, check that it was removed or gated and that it did not change behavior.
- For UI, rendering, native, visual, or generated-artifact bugs, require runtime evidence of the observable result. Compile-only or unit-only evidence is insufficient; if runtime verification is impossible, state the gap.

## Check the Blast Radius

- If the defect is a repeatable pattern, inspect the other hunks in this diff for the same pattern. Do not expand into a repo-wide sweep unless authorized.
- Look for a second source of truth: the same classification, threshold, ordering, or eligibility rule computed independently in the summary and the executor. Drift after a one-sided change is a future bug.
- For schema, migration, or persisted-format changes, check mixed-version reads/writes, backfill, idempotency, and rollback. Compatibility scaffolding for a format that never shipped is dead-on-arrival complexity.

## When the Seam Is Missing

If the only available test seam cannot exercise the real failure at its call site, report the missing seam as an architectural finding. A shallow test that passes is false confidence, not coverage. This is a finding about the codebase, not a demand to redesign it in this diff.

## Verdict

A bug fix is ready only when the failure is reproducible on the baseline, the causal path is explained, the fix is verified on the reviewed revision, the original scenario is green, and temporary instrumentation is gone. Missing evidence is an open question, not a pass.

# Review And Re-check Loop

## Severity

Use a simple severity model:

| Severity | Meaning |
| --- | --- |
| `blocking` | correctness, security, data loss, or product flow remains broken |
| `important` | should be fixed before closeout, may affect maintainability or coverage |
| `minor` | non-blocking cleanup or wording |

## Post-Fix Gate

After fixing:

1. rerun the original failing check
2. run the smallest regression test or verify command
3. run any required browser/API/data evidence path
4. review the diff against the original bug only
5. write whether the issue is fixed, still failing, blocked, or forbidden

## Re-review Rule

If the bug fix touches shared behavior, auth, data contracts, sync contracts, or UI state, require an independent review or fresh skeptical re-check before closeout.

## Non-Goals

Do not turn a bug closeout into a broad code review of unrelated files. Review exists to validate the fix, not to expand scope.

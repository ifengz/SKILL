# Review Calibration: Evidence and Counterexamples

Read when severity, correctness, bug-fix evidence, deletion safety or the benefit of an abstraction is unclear. These cases calibrate judgment; do not use keyword matches as a test or require every task to produce every evidence category.

## Choose the Right Comparison Point

| Question | Primary reference | Not sufficient alone |
| --- | --- | --- |
| Is this behavior required? | Current user request, applicable contract/ADR and accepted examples | Personal preference or specification silence |
| Is this a regression? | Task-start implementation plus its intended contract, real callers and failing scenario | Previous behavior alone; it may be the bug being fixed |
| Is a framework operation unsafe? | Actual runtime/library version, input provenance, defenses and sink semantics | API name, grep hit or latest-version docs |
| Is the test meaningful? | Real implementation exercised, observable assertions and relevant negative controls | Test count, source-text assertions or mocked target |
| Is deletion safe? | Consumer inventory and lifecycle/compatibility evidence | No imports in one folder or recent zero traffic |
| Is this a minimal fix? | Required behavior plus every hunk's necessity and causal role | Diff size, line count, or "looks small" |
| Should code be shared? | Same business invariant, owner and reasons to change, with preserved error semantics | Similarity score, matching syntax or fewer lines |

When sources conflict, honor applicable instruction priority and flag unresolved business-contract conflicts rather than choosing the easiest implementation. Historical implementation and external standards are evidence, not permission to override the current request.

## Findings Should Survive a Countercheck

Before reporting a confirmed defect, answer:

1. Which allowed or foreseeable input/actor reaches the code?
2. What contract or safety invariant fails, and at which operation?
3. Could an existing caller guard, transaction, escaping layer or runtime constraint prevent it?
4. Is the issue introduced/exposed by this change, pre-existing context, or outside scope?
5. What evidence supports the impact, and what has not been executed or observed?

If evidence is missing, preserve the concern as an explicit open question/coverage gap; do not label a hypothesis as confirmed. If a guard closes the path, explain that briefly instead of reporting the same alarm anyway.

For a bug fix, the comparison point is the failing behavior on the task-start revision, not the implementation's explanation. A test that passes on the unfixed revision is not a regression test; a guard that hides the failure is not a root-cause fix unless the contract is to absorb it; a UI or visual fix verified only by a build is unverified, not passed; and "no correct test seam" is an architectural finding, not a code defect.

## Positive and Negative Controls

| Candidate observation | Appropriate judgment |
| --- | --- |
| An ownership check was removed before a write; no enclosing guard exists | Confirm an authorization regression; require a non-owner negative test that proves no write |
| A query accepts user search text through driver-bound parameters | Do not claim SQL injection based on the text alone; inspect separately composed identifiers/operators |
| A component renders ordinary text with verified framework escaping | Do not demand raw-HTML sanitization without a raw rendering path |
| Duplicate order and refund calculations look alike but have different rounding contracts | Keep separate rules unless equivalence is proven; do not force a shared abstraction |
| A new unit test mocks the function under test to return success | Flag a test gap; it cannot demonstrate the real implementation's behavior |
| A helper's return value changes from an error to empty success | Check caller contract and data-loss consequences; lack of a crash is not proof of a root-cause fix |
| An exported symbol has no in-repository callers | External consumers remain unknown; no automatic removal recommendation |
| No distributed lock exists, but a validated atomic DB operation enforces the invariant | Do not prescribe a lock solely to satisfy a checklist |
| A mutation report counts build failures/timeouts as kills | Separate those outcomes from assertion-detected behavior; do not infer strong tests from the percentage |
| A regression test passes on both the unfixed and fixed revisions | Not regression evidence; the check does not exercise the bug or its assertion is too weak |
| A one-line change hides an error or leaves a duplicated rule | Small size is not minimality; judge necessity and causality, not line count |
| A multi-file change where every hunk is required for a migration | Large size is not scope creep; judge necessity, not line count |
| A UI fix is verified only by a successful build or unit test | Unverified for the reported visual symptom; require runtime evidence or state the gap |
| A diff normalizes an outlier to match its siblings without checking why it diverged | The asymmetry may be a deliberate protection; inspect the introducing change before accepting the normalization |
| No test seam can exercise the real failure | Architectural finding; a shallow passing test is false confidence, not coverage |
| No security-relevant surface changed in a spacing-only patch | Do not launch an auth audit; state the narrow reviewed scope |

## Severity and Reporting

Use a consistent rubric:

- **Critical:** reachable data loss, security/authorization break, silent wrong result on a real user path, or a broken rollback/contract that can strand production.
- **Important:** likely failure in a foreseeable scenario or a contract violation with a bounded workaround.
- **Minor:** localized quality or maintainability issue with no current behavior impact.

Missing required acceptance evidence is a readiness blocker, not a severity label for a code defect. A checklist match without a reachable path is at most an open question. Severity follows reachable impact, affected scope and prerequisites, not the category name. A credible data-loss or cross-account path may block even a small diff; a style concern does not become critical because it matches SOLID terminology. State the user's actual risk without inventing production exposure.

Keep confirmed defects, optional improvements, and missing evidence distinct. Report static evidence as static; a reproducible recipe that was never run is not an executed reproduction. A favorable scoped review does not certify the entire system.

For a compact finding, use: `location -> triggering scenario -> violated contract -> impact -> evidence/countercheck -> smallest proposed correction`. For a scoped clean review, name what was inspected and what remains unverified; do not manufacture issues to fill a template.

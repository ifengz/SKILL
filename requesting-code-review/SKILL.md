---
name: requesting-code-review
description: Request an independent, read-only review of a diff, PR, branch, or completed change, checking correctness, bug-fix evidence, security-sensitive surfaces, task scope, behavioral tests, removal safety, and unnecessary complexity against the task baseline. Use before merging, after a substantial change or bug fix, or when a fresh diagnosis is needed.
---

# Requesting Code Review

Dispatch one independent reviewer with bounded context, not the session history. Review is not authorization to implement fixes, install tools, commit, push, deploy, or manage worktrees. User instructions and applicable project rules govern scope and verification.

## When to Use

- At the review checkpoints required by the project, after a substantial logical unit, or before an authorized merge.
- When the user requests a review, a baseline before refactoring, or a fresh diagnosis of a difficult fix.
- Respect project exemptions for small mechanical edits; do not make every edit a full audit.

## Establish the Review Boundary

Record the task's starting commit and working-tree state before implementation when possible. Reuse that baseline at review time; do not substitute `HEAD~1`, assume `main`, or silently use the current HEAD as the task start.

Give the reviewer:

- The requested outcome, acceptance criteria, applicable rules, allowed paths, and explicit non-goals.
- The starting baseline, current HEAD, and initial dirty changes with their ownership. A commit alone does not capture pre-existing uncommitted work.
- The task-owned changed paths/hunks, relevant callers and contracts, and test/evidence paths with their actual results.
- The current authorization: review-only or implementation already authorized; any permitted validation commands and side effects.

Redact secrets, credentials, tokens, and personal data; pass paths or redacted excerpts instead of raw values. Mark any input that cannot be established as `UNKNOWN`; the reviewer must treat it as a coverage gap, not infer it. The implementation summary is context, not evidence.

For an ordinary Git worktree, use these complementary views, scoped to the task-owned paths:

```bash
git status --short
git diff --stat "$BASE_SHA" "$HEAD_SHA" -- <task-paths>
git diff "$BASE_SHA" "$HEAD_SHA" -- <task-paths> # committed task changes
git diff --cached -- <task-paths>                # current staged changes
git diff -- <task-paths>                         # current unstaged changes
git diff "$BASE_SHA" -- <task-paths>            # final tracked state vs baseline
git ls-files --others --exclude-standard -- <task-paths>
git merge-base --is-ancestor "$BASE_SHA" "$HEAD_SHA" || echo "baseline is not an ancestor of HEAD"
```

If the baseline is not an ancestor, the range may include unrelated history; use the actual merge base or an explicit patch, and say which you used.

Read relevant untracked files separately: `git diff` omits them. Do not stage files to make them visible. Compare with the initial dirty snapshot to avoid attributing someone else's changes to this task. If the baseline or ownership is missing, establish it from evidence or ask; disclose the resulting coverage limit rather than inventing a baseline. For non-Git files, use saved before/after contents and an explicit file list instead of creating a repository.

Recheck HEAD and task-owned file state before reporting. If either changed during review, stop and reconcile the review target with the coordinator; do not issue a verdict on mixed versions.

## Dispatch

Fill [code-reviewer.md](code-reviewer.md) with the bounded inputs above. Use a fresh-context reviewer (`fork_turns="none"` where supported), with no recursive delegation. Do not pass the implementer's session history, self-assessment, or recommended verdict. The reviewer inspects the product of the work, not the implementer's preferred conclusion.

Pass the absolute skill directory with the review packet so the reviewer can resolve its references independently of the project working directory. Select relevant references using the table below; the reviewer must also check the actual diff for additional triggers. Do not load every checklist for every change.

## Reference Routing

| Changed surface or review question | Read |
| --- | --- |
| Trust boundaries, auth, user-controlled input/output, outbound requests, files, secrets, dependencies, CI/build configuration, resource limits, shared writes, destructive operations, or removal of a safety guard | [Security and reliability](references/security-checklist.md) |
| Changed code introduces a hazard shape: swappable same-type arguments, boolean behavior flags, falsy defaults, hidden defaults, empty-filter destructive calls, un-awaited work, or leftover focused/skipped tests | [Hazard shapes](references/hazard-shapes.md) |
| Removal, deprecation, replacement, exports, routes, jobs, configuration, schema, or a claim that code is unused | [Removal safety](references/removal-safety.md) |
| Bug fix, regression, flaky behavior, or a claim that a reported symptom is resolved | [Bug-fix review](references/bug-fix-review.md) |
| Unclear severity, competing contracts, weak evidence, speculative simplification, or uncertainty whether a checklist pattern is a real defect | [Review calibration](references/review-calibration.md) |

Local contracts, callers, actual runtime versions, and evidence are the primary comparison points. External standards explain a failure mechanism; they do not override the user's scope or prove that a vulnerability is present. The reference files are self-contained and do not depend on other review skills remaining installed.

If independent delegation is unavailable, disclose that limitation and provide a clearly labeled self-review if useful; never claim independence that did not occur.

## Boundaries With Other Review Tools

This skill reports; it does not fix. When the host also ships `code-review`, `security-review`, or `simplify`, route by what the user asked for. Do not assume a tool exists because it is named here; if one is absent, skip it silently rather than imitating it by hand.

| The user wants | Use |
| --- | --- |
| An independent, read-only second opinion and a scoped verdict | this skill |
| Findings fixed in the working tree, or inline PR comments | host `code-review`, which may support `--fix` |
| A security-specific audit rather than a diff review | host `security-review` |
| Behavior-preserving cleanup of code that is already correct | host `simplify`, or the Ponytail standard when installed |

Never chain them inside one review. Finishing a read-only pass and then applying `--fix` turns a report the user approved into a change they never saw; when findings warrant edits, stop and let the user pick the route.

## Act on Findings

- Verify findings against the actual contracts and callers. Push back with evidence on incorrect findings.
- In review-only mode, report findings and stop. Severity never grants permission to edit.
- With implementation authorization, fix confirmed blockers only within the agreed scope, then repeat the affected checks. Ask before expanding scope or changing architecture or contracts.
- Apply a YAGNI/KISS standard (or the Ponytail standard when that skill is installed; do not go looking for it otherwise): prefer the smallest complete change; accept simplification only when its benefit is concrete, behavior is preserved, and it can be verified. Do not remove validation, error handling, permissions, or required evidence to make a diff smaller.
- Optional improvements are not blockers. Stop when acceptance criteria are met; do not turn review into a repository-wide cleanup.

## Evidence and Completion

The reviewer template incorporates selected ub-mode ideas: root-cause fixes, behavior-focused tests, and verified refactoring. This is a review adaptation, not installation or execution of upstream ub-mode or its companion tools.

Keep source inspection, executed tests, development E2E, deployment, and live business evidence separate. A review can inspect evidence but cannot retroactively prove that a test was written first. Report missing evidence as unverified, not as passed or as proof that no test exists.

Every report must answer three questions in plain terms: whether the change is minimal and causal, whether it stayed within the requested scope, and what evidence proves the original problem is gone. Name the reviewed revision (commit/tree hash or file fingerprint) and the uncovered paths or hunks in the report. Return actionable findings first, then optional simplifications, verification limits, and a scoped verdict. A favorable review does not authorize merging, pushing, or deployment.

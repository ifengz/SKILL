# Removal Safety and Deferred Removal

Read for deletion, deprecation, replacement, export/route/job/config/schema removal, or claims that code is unused. This is a review procedure, not authorization to delete. Apply it to the specific candidate, not a whole-repository cleanup.

## Establish What Would Disappear

Name the behavior and the exact symbol, route, table/field, package, configuration key, asset or discovery entry. Compare the before/after versions. Distinguish duplicate files, symlink aliases, generated artifacts and independently maintained copies; resolving one path does not identify all consumers. A removed validation, authorization, rate limit, timeout, or escaping layer is a behavior removal; treat the protected operation's callers and its negative tests as consumers.

## History of the Changed Lines

For a hunk that removes or weakens a guard, read the introducing commit with `git log -L <start>,<end>:<file>` or `git blame`. A line added for a bug, CVE, incident, or ticket is a guard until the author explains why the original cause is gone. A hunk that silently reverts a recent commit is either a lost fix or a deliberate rollback; establish which. Where history is absent (squashed import, vendored file, first commit), say so rather than inferring intent.

## Consumer Evidence

For each applicable channel, record the inspected scope and findings:

1. **Static consumers:** imports, re-exports, aliases, scripts, tests, build outputs and manifests. Search the owning repository, not only the changed directory. Follow aliases and public exports.
2. **Dynamic consumers:** registries, string dispatch, reflection, dependency injection, plugin/skill discovery, glob imports, lazy routes, cron, worker queues and feature flags. Search configuration and registration, not just function calls.
3. **External consumers:** public APIs, SDKs, webhooks, installed clients, operational scripts and other repositories. Repository search cannot prove these absent. Use available contracts, owner confirmation or appropriately scoped telemetry; missing access remains unknown.
4. **Persisted consumers:** rows, queued jobs, serialized names, migrations, historical records and cached schemas. New code not writing an old format does not prove that old data is no longer read.
5. **Temporal consumers:** rolling releases, rollback versions, old clients, retry windows, periodic jobs, dormant flags and recovery paths. A quiet interval is meaningful only if it covers the relevant lifecycle and the instrumentation can observe that consumer.

Zero text matches is a lead, not proof of no consumers. Do not delete a test simply to make deletion pass; determine whether it protects a surviving contract. Do not query production, inspect sensitive records, or change feature flags without authorization.

Separately, for compatibility or migration scaffolding added for a format that has never shipped, compare with the last released version. If the old format never existed outside the current work, the migration is dead-on-arrival complexity; use the default path instead.

## Decision and Evidence Card

Use only the fields relevant to the candidate. Do not require a release plan for a provably local private helper.

| Field | Record |
| --- | --- |
| Candidate / reason | Exact paths and behavior; why removal helps this task |
| Contract / consumers | Static, dynamic, external, persisted and temporal evidence; unknown channels |
| Recommendation | Eligible within existing authorization / Defer pending evidence or migration / Keep |
| Impact | What stops working and for whom; separately note data-loss and compatibility risks |
| Preconditions | Required consumer migration, compatibility window, replacement equivalence, approval or observability |
| Minimal sequence | Ordered steps that preserve the contract; no execution implied |
| Verification | Targeted tests plus applicable development E2E showing remaining consumers work and retired entry points behave as agreed |
| Recovery | Code revert vs data restore/reconstruction; limits, backup evidence and a rollback test when destructive data is involved |
| Owner / timing | Only when coordination or staged migration is actually needed |

An evidence gap is not proof that the candidate must remain forever; recommend a bounded next check. Conversely, a code revert does not recover dropped data or revoke already-issued external side effects.

## Comparison Cases

- **Local private helper:** all call sites are visible in one module, no registry/export/reflection path exists, and callers now use equivalent code with regression coverage. Removal can be a small in-scope change; no artificial two-week observation window is needed.
- **Apparently unused job:** a handler has no direct import call but `jobs[name]` is populated by configuration, and queued payloads name it. Deletion is not safe merely because `rg handlerName src/` is empty.
- **Old API/column:** latest UI no longer uses it, but older clients or rollback code can. Defer until the compatibility/data migration contract and recovery limits are established. Do not execute DDL to test the hypothesis.
- **Duplicate skill:** two directories declare the same name. Compare all supporting files and resolve discovery links; identical entrypoint hashes do not prove equivalent reference libraries. Removing an active alias and removing its shared target have different blast radii.

## Useful Reference Points

Use the project's public API/deprecation policy, migration runbook, deployment/rollback contract, export manifests and runtime registries first. These are more authoritative for removal than a general style guide.

- [Semantic Versioning](https://semver.org/): useful when the project actually promises a versioned public API; not proof that internal code is a public API.
- [Git revert documentation](https://git-scm.com/docs/git-revert): explains code history reversal, not recovery of deleted data or external effects.

External links are optional navigation references, not live-verified evidence. Consult and cite the relevant version/section when needed. Use [review calibration](review-calibration.md) when an absence claim or equivalence argument remains uncertain.

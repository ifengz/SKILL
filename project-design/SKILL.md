---
name: project-design
description: Turn a project idea, workflow pain point, rough product note, or draft project.md into a build-ready implementation contract. Use when Codex needs to clarify requirements, define V1 scope, absorb requirements-analysis and system-design structure, write or harden project.md, set data models, interfaces, page boundaries, permissions, queues, E2E acceptance, and implementation order.
---

# Project Design

## Purpose

Use this skill to turn unclear project intent into a concrete build contract. It should produce something developers can implement from, not a polished but vague planning essay.

This skill absorbs the useful structure of requirements analysis and system design. Do not install external analysis/design skills for this workflow unless the user explicitly asks.

## Workflow

1. Start from the real work.
   - Read the source document, user message, current `project.md`, or repo context.
   - Extract actual work items, waste, users, data sources, and operational constraints before proposing tools.
   - If the user asks for a site/app/tool, converge to the smallest workable product shape.

2. Run requirements analysis.
   - Use `references/requirements-analysis.md`.
   - Define problem, users, V1 scope, non-goals, constraints, risks, missing decisions, and acceptance signals.
   - If a required decision blocks the design, stop and ask only that decision.

3. Run system design.
   - Use `references/system-design.md`.
   - Define layers, modules, data model, interface contracts, auth, permissions, async jobs, external services, error handling, and observability.
   - Keep implementation order tied to a minimal running path.

4. Write or harden `project.md`.
   - Use `assets/project.md.template` when creating a new document.
   - Preserve existing project-specific decisions; do not expand scope unless the user asks.
   - Make assumptions explicit and avoid hidden global dependencies.

5. Validate the design.
   - Use `references/design-review-checklist.md`.
   - If a `project.md` file exists, run `python3 scripts/validate_project_design.py <path-to-project.md>`.
   - Fix missing sections before claiming the plan is implementation-ready.

## Output

Produce an implementation contract with:

- goal and non-goals
- V1 scope
- user flows and page boundaries
- data model
- API/interface contracts
- auth and permissions
- async/queue behavior
- external service boundaries
- error states and recovery
- E2E acceptance matrix
- implementation order
- open decisions

## Completion Bar

Do not call the design ready until:

- a developer can identify the first implementation step
- every V1 feature maps to data, interface, UI, and test coverage
- non-goals prevent obvious scope creep
- auth, permissions, external services, and async jobs have explicit boundaries
- E2E acceptance is concrete enough to pass or fail
- unresolved decisions are listed instead of hidden in prose

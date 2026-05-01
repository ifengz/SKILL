# project-design

`project-design` is a Codex skill for turning a rough idea, workflow pain point, or draft `project.md` into a build-ready implementation contract.

It absorbs practical requirements-analysis and system-design structure, but it does not depend on installing external skills.

## What It Helps With

Use this skill when you need to:

- turn a vague request into a concrete V1 plan
- convert operational pain points into a small product or website scope
- harden a `project.md` until developers can start
- define data models, interfaces, page boundaries, permissions, queues, and E2E acceptance
- review whether a project plan is too broad, too shallow, or missing contracts

## Inputs

The skill expects one or more of:

- user request
- source document or workflow notes
- existing `project.md`
- repo constraints
- users and operators
- data sources
- hosting, auth, storage, budget, or API constraints

When a decision blocks design, the skill should ask only that decision. It should not ask broad questions that can be resolved by reading local files.

## Workflow

1. Start from the real work and repeated waste.
2. Use [`references/requirements-analysis.md`](./references/requirements-analysis.md) to define problem, V1 scope, non-goals, constraints, risks, and acceptance signals.
3. Use [`references/system-design.md`](./references/system-design.md) to define layers, modules, data model, interfaces, permissions, async jobs, external services, and E2E acceptance.
4. Create or harden `project.md` using [`assets/project.md.template`](./assets/project.md.template).
5. Review with [`references/design-review-checklist.md`](./references/design-review-checklist.md).
6. Validate structure with [`scripts/validate_project_design.py`](./scripts/validate_project_design.py).

## Outputs

The expected output is an implementation contract containing:

- goal and non-goals
- V1 scope
- user flows
- page boundaries
- data model
- API/interface contracts
- auth and permissions
- async/queue behavior
- external service boundaries
- E2E acceptance matrix
- implementation order
- open decisions

## Install

Copy the full folder into your Codex skills directory:

```bash
git clone https://github.com/ifengz/SKILL.git
mkdir -p ~/.codex/skills
cp -R SKILL/project-design ~/.codex/skills/project-design
```

Restart or refresh Codex after installation.

## Verify

Run:

```bash
python3 ~/.codex/skills/project-design/scripts/validate_project_design.py ~/.codex/skills/project-design/assets/project.md.template
```

Expected result:

```text
Project design structure check passed.
```

## Why This Is Not A Shallow Skill

This skill is designed to produce a build contract, not a planning essay:

- `references/requirements-analysis.md` starts from real work and waste.
- `references/system-design.md` forces data, interface, permission, queue, and E2E boundaries.
- `assets/project.md.template` gives a concrete output shape.
- `scripts/validate_project_design.py` checks whether the design has required sections.
- `references/design-review-checklist.md` defines stop conditions and missing-contract risks.

The skill should not call a design implementation-ready unless a developer can identify the first build step and every V1 feature maps to data, interface, UI, and test coverage.

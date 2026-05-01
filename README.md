# SKILL

This repository contains practical Codex skills that are meant to be installed and used directly. Each skill lives in its own folder with its `SKILL.md`, references, scripts, templates, and README kept together.

The goal is not to collect generic prompts. A skill in this repository must provide concrete inputs, workflow, outputs, validation checks, failure modes, and reusable files.

## Skills

| Skill | Use It When | Main Output | Hard Evidence |
| --- | --- | --- | --- |
| [`spotter-api`](./spotter-api/) | You need to write, review, or repair a Spotter API integration guide with APP Key/APP Secret signing. | A developer-facing Spotter handoff document with exact signing rules. | Fixed signature vector, self-check script, signing reference, failure modes. |
| [`project-design`](./project-design/) | You need to turn a rough idea, workflow pain point, or draft `project.md` into a build-ready implementation contract. | A concrete project contract with V1 scope, data model, interfaces, permissions, queues, E2E acceptance, and implementation order. | Project template, requirements reference, system-design reference, review checklist, structure validator. |

## Install

Clone this repository and copy the skill folders into your Codex skills directory:

```bash
git clone https://github.com/ifengz/SKILL.git
mkdir -p ~/.codex/skills
cp -R SKILL/spotter-api ~/.codex/skills/spotter-api
cp -R SKILL/project-design ~/.codex/skills/project-design
```

Restart or refresh Codex after installation so the new skills are discovered.

## Verify

Run the built-in checks after copying:

```bash
python3 ~/.codex/skills/spotter-api/scripts/spotter_signature_check.py
python3 ~/.codex/skills/project-design/scripts/validate_project_design.py ~/.codex/skills/project-design/assets/project.md.template
```

Expected result:

- `spotter-api`: prints `Signature check passed.`
- `project-design`: prints `Project design structure check passed.`

## Usage

Use the skills explicitly in Codex:

```text
Use $spotter-api to harden this Spotter API integration guide.
```

```text
Use $project-design to turn this project idea into a build-ready project.md.
```

## Quality Bar

Every skill here must include:

- `SKILL.md` with trigger conditions and workflow
- a concrete input model
- a concrete output model
- acceptance checks
- failure modes
- reusable references, scripts, or templates when needed

If a skill only contains a generic checklist or vague advice, it does not belong in this repository.

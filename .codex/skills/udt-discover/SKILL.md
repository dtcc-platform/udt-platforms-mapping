---
name: udt-discover
description: Resolve and save the Urban Digital Twin entity discovery manifest for web use. Use when the user says udt:discover, udt-discover, asks to resolve act/entity-discovery.md for web, or wants a reviewable entity discovery prompt.
---

# UDT Discover

Resolve `act/entity-discovery.md` into a saved, reviewable web prompt.

## Source of Truth

- OpenSpec specs define research behavior and output contracts.
- `act/entity-discovery.md` is the manifest that declares which contracts affect entity discovery.
- This skill is only an operational shortcut. Do not hardcode or maintain a separate discovery prompt here.

## Workflow

1. Read `act/entity-discovery.md`.
2. Read every file listed under its `## Required Contracts` section.
3. Produce one resolved prompt:
   - inline each required contract under a heading naming the source file
   - append the manifest's `## Prompt` body
4. Save the resolved prompt as `act/entity-discovery-resolved-codex.md` when Codex is the resolver.
5. Tell the researcher to have a different reviewer agent review the saved prompt in stdout/chat before running it.
6. If the reviewer finds a required repository change, tell the researcher to capture it as an OpenSpec proposal intent before editing specs, manifests, documentation, or skills.
7. Tell the researcher to paste the reviewed prompt into the web model and save the response to `observe/entity-discovery-<model-short>.md`.

## Constraints

- Always resolve from the live manifest and live contract files.
- Do not use cached resolved prompts.
- Do not edit repository files during a normal resolve-only invocation except for writing the resolved prompt artifact under `act/`.
- Do not duplicate entity discovery behavior inside this skill.
- Keep the resolved prompt faithful to the manifest and required contracts.
- Do not save prompt review output by default; review happens in stdout/chat unless the researcher explicitly asks to preserve review evidence.

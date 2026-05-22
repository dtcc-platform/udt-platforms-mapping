---
name: udt-discover
description: Resolve the Urban Digital Twin entity discovery manifest for web use. Use when the user says udt:discover, udt-discover, asks to resolve act/entity-discovery.md for web, or wants a copy-ready entity discovery prompt.
---

# UDT Discover

Resolve `act/entity-discovery.md` into a paste-ready web prompt.

## Source of Truth

- OpenSpec specs define research behavior and output contracts.
- `act/entity-discovery.md` is the manifest that declares which contracts affect entity discovery.
- This skill is only an operational shortcut. Do not hardcode or maintain a separate discovery prompt here.

## Workflow

1. Read `act/entity-discovery.md`.
2. Read every file listed under its `## Required Contracts` section.
3. Produce one resolved prompt block:
   - inline each required contract under a heading naming the source file
   - append the manifest's `## Prompt` body
   - output only the copy-ready resolved prompt block as the large block
4. After the resolved prompt block:
   - if assistant-side `/copy` is available in the current client, use it on the resolved prompt
   - otherwise tell the researcher to run `/copy` on the generated prompt
5. Tell the researcher to paste the prompt into the web model and save the response to `observe/entity-discovery-<model-short>.md`.

## Constraints

- Always resolve from the live manifest and live contract files.
- Do not use cached resolved prompts.
- Do not edit repository files during a normal resolve-only invocation.
- Do not duplicate entity discovery behavior inside this skill.
- Keep the resolved prompt faithful to the manifest and required contracts.

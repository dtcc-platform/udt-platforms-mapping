## Context

The repository already treats `act/` files as manifests that must be resolved before web use. The manual command is clear but repetitive. A local Codex skill can make the common discovery action easier while preserving the current source-of-truth hierarchy: specs govern behavior, manifests declare contracts, and the skill only resolves the manifest.

## Goals / Non-Goals

**Goals:**

- Add a local skill that triggers on `udt:discover`, `udt-discover`, or requests to resolve platform discovery for web use.
- Keep the skill short and procedural, following skill-creator guidance.
- Document copy behavior without assuming `/copy` is available as a shell command.
- Update researcher-facing docs so both the manual resolve command and shortcut are visible.

**Non-Goals:**

- Do not duplicate platform discovery behavior inside the skill.
- Do not move OpenSpec contracts into `.codex/skills/`.
- Do not implement a shell command named `/copy`.
- Do not change the platform discovery output contract.

## Decisions

- Name the skill folder and frontmatter `udt-discover`, while documenting `udt:discover` as the user-facing invocation phrase.
  - Rationale: skill identifiers are filesystem-friendly, while the colon form is readable as a domain action.

- Make copy behavior conditional.
  - Rationale: `/copy` is usually a client command, not a repository command. The skill can use assistant-side `/copy` only if the client exposes it; otherwise the correct behavior is to emit one copy-ready block and tell the researcher to run `/copy`.

- Add a new `repo-agent-skills` spec.
  - Rationale: repository-local skills are a workflow surface and should be governed without overloading README or structure specs.

## Risks / Trade-offs

- The skill may not be auto-discoverable until the Codex client reloads local skills. Mitigation: document the skill location and user-facing invocation.
- `/copy` availability differs by client. Mitigation: skill instructions include an explicit fallback.
- The skill could drift from the manifest contract. Mitigation: require it to read the live manifest and required contracts every time.

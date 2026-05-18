## Context

The repository uses OpenSpec to govern research workflow behavior: definitions, prompts, outputs, reporting, comparison, and phase-folder structure. Some current specs drift beyond that scope by governing repository-local agent skills.

The structure spec is still useful because `plan/`, `act/`, `observe/`, and `reflect/` define the research workflow. Its name should make that scope explicit.

## Goals / Non-Goals

**Goals:**

- Make OpenSpec's scope explicitly research-workflow focused.
- Rename `repo-structure` to `research-workflow-structure`.
- Remove OpenSpec governance for repository-local Codex skills.
- Keep operational skills available outside OpenSpec governance.

**Non-Goals:**

- Do not remove `.codex/skills/udt-discover/SKILL.md`.
- Do not change entity discovery behavior.
- Do not rename phase folders.
- Do not remove README mentions that a skill exists as a shortcut, unless they present it as OpenSpec-governed.

## Decisions

- Replace `repo-structure` with `research-workflow-structure`.
  - Rationale: the requirements are about research phases and canonical research artifacts, not all repository files.
  - Alternative considered: keep `repo-structure` and rewrite its purpose. That would preserve path stability but keep the broader name.

- Remove `repo-agent-skills` from active OpenSpec specs.
  - Rationale: local Codex skills are operational tooling, not research contracts.
  - Alternative considered: keep a narrower agent-skill spec. That still makes OpenSpec responsible for agent mechanics.

- Keep README references to `udt:discover` as operational guidance only.
  - Rationale: users still benefit from knowing the shortcut exists, but the governing contract remains the live `act/` manifest and research specs.
  - Alternative considered: remove all skill references. That hides useful workflow information without improving the research contract boundary.

## Risks / Trade-offs

- Removing `repo-agent-skills` means skill behavior is no longer validated by OpenSpec -> Mitigate by keeping the skill simple and pointing it at live manifests.
- Renaming `repo-structure` requires link updates -> Search for all active references during implementation.
- Archived changes will still mention old names -> Leave archived history unchanged.

## Migration Plan

1. Add `openspec/specs/research-workflow-structure/spec.md` using the research workflow requirements from `repo-structure`.
2. Remove `openspec/specs/repo-structure/spec.md`.
3. Remove `openspec/specs/repo-agent-skills/spec.md`.
4. Update active README and active spec references.
5. Validate OpenSpec.

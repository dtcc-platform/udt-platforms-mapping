## Why

OpenSpec should govern the research workflow, not agent implementation conveniences. The current spec set includes `repo-agent-skills`, which governs local Codex tooling, and `repo-structure`, whose name is broader than its actual research workflow purpose.

## What Changes

- Rename `repo-structure` to `research-workflow-structure`.
- Keep the phase-folder and canonical research artifact rules under the renamed research workflow structure spec.
- Remove `repo-agent-skills` from the active OpenSpec spec set.
- Update README and phase README references from `repo-structure` to `research-workflow-structure`.
- Update README governance language so repository-local skills are described as optional operational shortcuts, not OpenSpec-governed research contracts.
- **BREAKING**: `openspec/specs/repo-agent-skills/spec.md` is no longer an active OpenSpec spec.
- **BREAKING**: references to `openspec/specs/repo-structure/spec.md` migrate to `openspec/specs/research-workflow-structure/spec.md`.

## Capabilities

### New Capabilities

- `research-workflow-structure`: Defines the live research workflow phase structure and canonical researcher-facing artifact locations.

### Modified Capabilities

- `repo-structure`: Retire in favor of `research-workflow-structure`.
- `repo-agent-skills`: Remove local agent skill governance from OpenSpec scope.
- `repo-readme`: Document OpenSpec as governing research workflow contracts and remove `repo-agent-skills` from the formal spec list.

## Impact

- Affects `openspec/specs/repo-structure/spec.md`, which will be replaced by `openspec/specs/research-workflow-structure/spec.md`.
- Affects `openspec/specs/repo-agent-skills/spec.md`, which will be removed.
- Affects root and phase README links that point at `repo-structure`.
- Does not remove `.codex/skills/udt-discover/SKILL.md`; the skill remains operational tooling outside OpenSpec governance.

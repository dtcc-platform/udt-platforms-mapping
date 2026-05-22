## Context

The repository now uses a single cross-phase workflow spec and phase-object-role OpenSpec capability names. The only remaining naming exception is that live `act/` manifests use verb-first prompt names.

## Goals / Non-Goals

**Goals:**

- Make live `act/` filenames align with object-role artifact names.
- Keep existing prompt behavior unchanged.
- Update live references and local operational tooling.

**Non-Goals:**

- Rename observation or reflection outputs that already follow object-role naming.
- Rename OpenSpec capabilities.
- Change entity discovery, platform comparison, benchmark, report, or Markdown behavior.

## Decisions

1. Use object-role names inside `act/` without repeating the phase prefix.

   Rationale: the folder already supplies the phase, while filenames such as `entity-discovery.md` and `platform-comparison.md` match the object-role part of the corresponding capability names.

2. Preserve saved output filename patterns.

   Rationale: `observe/entity-discovery-<model-short>.md` and `observe/platform-comparison-<model-short>.md` already follow the unified convention and do not need churn.

## Risks / Trade-offs

- Existing user muscle memory and local shortcuts may point to old paths -> update README, act README, run-input docs, active specs, and `.codex/skills/udt-discover/SKILL.md`.
- Archived OpenSpec history will still mention old names -> leave archive unchanged as historical record.

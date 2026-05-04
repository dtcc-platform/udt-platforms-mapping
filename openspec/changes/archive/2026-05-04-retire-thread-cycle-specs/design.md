## Context

The previous repository model used per-thread folders under each phase, which made `*-cycle` naming easier to tolerate even though README defined the cycle as the action research loop. After flattening `plan/` and `act/`, the remaining `udt-platforms-cycle` and `udt-initiatives-cycle` specs are less coherent: they are thread-level semantic bundles in a repository that now prefers direct file-specific governance.

The useful contract should not disappear. It should move into specs that correspond to the governed files:

- `plan/udt-platforms-scope.md`
- `plan/udt-initiatives-scope.md`
- `act/udt-platforms.md`
- `act/udt-initiatives.md`

## Goals / Non-Goals

**Goals:**

- Remove active `*-cycle` specs for `udt-platforms` and `udt-initiatives`.
- Preserve all unique normative behavior from those specs.
- Add strict-valid scope specs for the flattened planning inputs.
- Keep prompt output contracts in prompt specs.

**Non-Goals:**

- Change the actual research workflow.
- Change prompt text or output schemas.
- Rename threads.
- Flatten `observe/` or `reflect/`.

## Decisions

### Decision: Retire cycle specs rather than rename them to thread specs

The flattened model is easier to maintain when governed contracts map to files. A `*-thread` rename would fix the naming issue but keep an extra semantic layer that mostly duplicates prompt and scope specs.

### Decision: Add scope specs for both planning inputs

`plan/udt-platforms-scope.md` needs a spec because the retired platforms cycle spec currently owns the Type classification table contract. `plan/udt-initiatives-scope.md` also deserves a matching spec because the initiatives cycle spec currently owns the initiative table semantics and broad-discovery framing.

### Decision: Keep output contracts in act prompt specs

The prompts produce the web-model instructions, so output format and save-path behavior should remain governed by `act-udt-platforms-prompt` and `act-udt-initiatives-prompt`.

## Risks / Trade-offs

- [Loss of a single thread-level summary] -> README and file-specific specs together describe the thread roles; the source of truth becomes closer to the actual files researchers use.
- [Spec proliferation] -> Two cycle specs are removed and two scope specs are added, so the active spec count stays stable while names become more accurate.
- [Archive mismatch] -> Archived changes retain historical cycle names; active specs represent the current model.

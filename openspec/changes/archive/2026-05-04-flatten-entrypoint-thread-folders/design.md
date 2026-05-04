## Context

The repository currently uses the same phase/thread nesting pattern for every action research phase:

```text
plan/<thread>/
act/<thread>/prompt.md
observe/<thread>/
reflect/<thread>/
```

That pattern is valuable for `observe/` and `reflect/`, where files multiply by model, benchmark, report, and synthesis output. It is heavier for `plan/` and `act/`, where each thread usually has a small, fixed set of entrypoint files. The proposal keeps the thread model but stops representing every thread as a folder in the low-volume entrypoint phases.

## Goals / Non-Goals

**Goals:**

- Make planning inputs directly visible under `plan/`.
- Make canonical thread prompts directly visible under `act/`.
- Preserve thread-grouped output and reflection areas under `observe/` and `reflect/`.
- Update governed path references so agents and humans use one canonical layout.

**Non-Goals:**

- Remove the conceptual research-thread model.
- Flatten `observe/` saved outputs.
- Flatten `reflect/` benchmarking, reporting, or synthesis workspaces.
- Rewrite archived OpenSpec changes.
- Change prompt output contracts or research semantics.

## Decisions

### Decision: Flatten entrypoint files, not the thread model

`plan/` and canonical thread prompts in `act/` will use descriptive filenames:

```text
plan/udt-platforms-scope.md
plan/udt-initiatives-scope.md
plan/udt-platform-comparison-rubrics.md
plan/udt-platform-comparison-source-policy.md
plan/udt-platform-comparison-platforms.md

act/udt-platforms.md
act/udt-initiatives.md
act/udt-platform-comparison.md
```

The thread names remain part of the filenames so the relationship is explicit without requiring a directory hop.

Alternative considered: flatten every phase. Rejected because `observe/` and `reflect/` are output-heavy phases where filenames would become long and collision-prone.

### Decision: Keep `observe/` and `reflect/` grouped by thread

Saved web outputs stay under `observe/<thread>/web-<model-short>.md`, and reflection artifacts stay under `reflect/<thread>/`. This preserves the current accumulation model for repeated runs, benchmarking, reporting, and synthesis.

Alternative considered: store observed outputs as `observe/<thread>-web-<model-short>.md`. Rejected because outputs are the most likely artifact type to grow, and grouping by thread keeps historical responses easier to manage.

### Decision: Treat this as a breaking path migration

The old `plan/<thread>/...` and `act/<thread>/prompt.md` paths will no longer be canonical after implementation. Prompts, README guidance, and specs should be updated in one change so no governed file points to the retired paths.

Alternative considered: keep compatibility copies at both paths. Rejected because duplicate canonical prompts and planning inputs would invite drift.

## Risks / Trade-offs

- [Broken references to old paths] -> Use repository-wide search during implementation and update all current README, prompt, and spec references.
- [Less visual grouping in `plan/`] -> Use consistent `<thread>-<artifact>.md` filenames so thread ownership remains visible.
- [Potential confusion around direct `act/check-prompts-status.md`] -> Keep maintenance prompts directly under `act/`; the flattened thread prompts now follow the same direct-file convention.
- [Archived changes mention old paths] -> Leave archives untouched as historical records and update only active specs and current workflow files.

## Migration Plan

1. Move planning inputs from thread folders to flattened filenames under `plan/`.
2. Move canonical thread prompts from `act/<thread>/prompt.md` to flattened filenames under `act/`.
3. Keep `observe/` and `reflect/` directory structures unchanged.
4. Update current README, prompt content, and active specs to reference the new paths.
5. Run repository-wide reference checks for retired canonical paths.
6. Run OpenSpec validation for the change.

Rollback is a reverse path migration: move flattened files back to their prior thread folders and restore old path references from git history.

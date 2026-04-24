## Context

The repository currently stores the prompt-validity audit under `tools/prompt-validity/`, but the contents are methodological artifacts rather than implementation utilities. The user wants a more expressive root name that makes clear these files reflect on the workflow itself.

## Goals / Non-Goals

**Goals:**
- Rename the current workflow-audit root to `reflect-workflow/`
- Keep the prompt-validity audit intact while moving it to the new location
- Align the baseline specs and runnable prompt instructions with the new path
- Make the root-folder meaning clearer to contributors

**Non-Goals:**
- Redesign the prompt-validity audit logic
- Introduce a full new Action Research cycle tree for workflow reflection
- Rename unrelated `reflect/` cycle folders

## Decisions

### 1. Use `reflect-workflow/` as a root folder

The audit artifacts will move to a dedicated root folder named `reflect-workflow/`.

Why:
- It is more expressive than `tools/`
- It says what is being reflected on without requiring repository-specific interpretation
- It distinguishes workflow reflection from cycle-specific `reflect/discovery` and `reflect/rating`

Alternative considered:
- `meta-reflect/`
Why not chosen:
- It is conceptually valid but less immediately readable

### 2. Keep the existing subfolder name `prompt-validity/`

The change will rename only the root folder, keeping `prompt-validity/` as the immediate audit capability folder.

Why:
- The capability name is already clear
- This keeps the rename focused and low-risk

### 3. Treat folder-layout documentation as part of the change

The change will include `ar-folder-layout` so the repository's structural description reflects the new root.

Why:
- Root-folder meaning is part of the governed structure
- Leaving folder-layout unchanged would create immediate drift

## Risks / Trade-offs

- [Some contributors may still expect generic utilities under `tools/`] → Mitigation: use the proposal to state that these artifacts are workflow reflection, not developer tooling
- [Renaming only one folder may leave historical docs mentioning `tools/`] → Mitigation: update the governed specs and live prompt instructions together
- [The root naming remains slightly asymmetrical with `reflect/`] → Mitigation: accept the distinction between cycle reflection and workflow reflection as intentional

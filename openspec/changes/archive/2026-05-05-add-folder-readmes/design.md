## Context

The repository recently flattened phase artifacts into direct files under `plan/`, `act/`, `observe/`, and `reflect/`. That makes the filesystem simpler, but also removes the old thread-folder context that helped explain what each file represented.

`repo-structure` currently includes README explanation requirements. That was reasonable while the README mainly explained the structure, but folder-level READMEs make documentation its own repo-wide contract.

## Goals / Non-Goals

**Goals:**

- Introduce `repo-readme` as the home for README documentation requirements.
- Keep `repo-structure` focused on filesystem layout and canonical artifact locations.
- Add local README contracts for `plan/`, `act/`, `observe/`, and `reflect/`.
- Avoid duplicating full workflow explanation across every folder README.

**Non-Goals:**

- Do not change the canonical artifact layout.
- Do not change prompt execution behavior.
- Do not introduce frontmatter or a metadata system.

## Decisions

1. Use a new `repo-readme` capability.

   Rationale: README expectations cut across folders and workflow concepts. Keeping them in `repo-structure` makes that spec too broad and creates overlap with workflow specs.

   Alternative considered: keep README requirements in `repo-structure`. This avoids a new spec, but it becomes less consistent once every phase folder has its own README.

2. Keep folder READMEs local and non-authoritative.

   Rationale: The specs remain the source of truth. Folder READMEs should help navigation by summarizing local contents, expected artifact types, and naming patterns.

   Alternative considered: make each folder README a full workflow guide. That would duplicate the root README and drift quickly.

3. Let `repo-prompt-review` keep workflow behavior.

   Rationale: Prompt review is a workflow capability. `repo-readme` should govern that README docs explain it, but not redefine the review process.

   Alternative considered: move all prompt-review README language into `repo-readme` and remove the README requirement from `repo-prompt-review`. That would make documentation ownership cleaner, but would disconnect the prompt-review spec from its expected contributor-facing explanation.

## Risks / Trade-offs

- Documentation drift -> Keep folder READMEs short and local to reduce repeated workflow text.
- Spec boundary ambiguity -> `repo-readme` governs documentation placement and coverage; domain/workflow specs govern behavior.
- Extra files in phase folders -> The README files should be allowed as explanatory files without being treated as canonical research artifacts.

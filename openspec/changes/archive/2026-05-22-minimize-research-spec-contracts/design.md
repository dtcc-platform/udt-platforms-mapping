## Context

The current active research specs validate, but several contracts still reflect earlier migration work. `research-artifact-naming` includes historical thread and merge language plus a hard-coded list of specific capability names. `research-workflow-structure` repeats many individual file contracts that are already owned by action, observe, and reflect specs. The platform comparison benchmark spec exists only to preserve a stub prompt that is not yet designed.

## Goals / Non-Goals

**Goals:**

- Keep active specs complete while removing migration-era wording and duplicate canonical indexes.
- Make file naming consistent with the current phase model.
- Make spec ownership clear: phase structure in workflow, naming grammar in naming, artifact-specific behavior in each artifact spec.
- Retire the unused platform comparison benchmark stub and its active spec.
- Remove empty obsolete spec directories that no longer contain active specs.

**Non-Goals:**

- Change entity discovery, platform comparison, scoring, source policy, or output contracts.
- Redesign platform comparison benchmarking.
- Rewrite saved observation or reflection outputs.
- Change unrelated dirty working-tree files.

## Decisions

1. `research-artifact-naming` will define grammar instead of listing every canonical capability.

   Rationale: the active spec tree is already the source of truth for existing capabilities. A second list inside the naming spec creates stale requirements after every rename.

2. `research-workflow-structure` will define phase responsibilities and artifact classes, not every file already owned by a specific spec.

   Rationale: workflow structure should answer where research artifacts belong. Individual action/output specs should answer which exact governed files exist and how they behave.

3. `act-platform-comparison-benchmark` will be removed instead of kept as a stub.

   Rationale: a placeholder spec is not a complete research contract. If platform comparison benchmarking becomes necessary later, it should be introduced as a new scoped change with designed behavior.

4. Empty stale spec directories will be deleted from the working tree.

   Rationale: OpenSpec validation ignores them, but they confuse repository navigation and contradict the naming cleanup.

## Risks / Trade-offs

- Removing duplicate file lists can make `research-workflow-structure` less exhaustive at a glance -> the root README and active spec directories remain the navigational index, while artifact-specific specs retain exact file contracts.
- Retiring the comparison benchmark stub removes a placeholder command from `act/` -> future benchmarking work will need a new proposal before becoming executable.
- Removing empty directories may expose references in documentation -> validate with repository search and update any live references found.

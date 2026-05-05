## Context

The repository has already moved to a flattened phase-folder model. The old `udt-*` filenames and "thread" language are now the main remaining source of internal jargon in the live research interface.

The repository name and README establish the Urban Digital Twin domain, so repeating `udt` in every live artifact filename adds little meaning. Researchers need filenames that quickly answer "what is this artifact for?" rather than "which internal thread owns it?"

## Goals / Non-Goals

**Goals:**

- Make live filenames more natural for researchers.
- Replace "thread" with clearer concepts: research object, research action, and artifact role.
- Keep the four phase folders unchanged.
- Update all live references so prompts, docs, specs, save-as conventions, and glob patterns agree.
- Preserve archived OpenSpec history without rewriting old names.

**Non-Goals:**

- Do not change the research methodology.
- Do not change output table schemas except where prompt IDs or file paths must change.
- Do not reorganize files back into nested folders.
- Do not rename the repository itself.

## Decisions

1. Drop `udt-` from live artifact filenames.

   Rationale: UDT is repository context. Repeating it in every filename makes names longer without improving local comprehension.

   Alternative considered: keep `udt-` for strict global uniqueness. That helps if files are copied out of context, but the repo already has README and specs to establish context.

2. Use phase-specific naming grammar.

   Rationale: Each phase benefits from a different kind of name:

   - `plan/`: noun phrases for definitions, policy, scoring, sets, and fixtures.
   - `act/`: verbs for research actions.
   - `observe/`: run-result names that identify action and model or generated coverage.
   - `reflect/`: synthesis names that identify object and reflection product.

3. Retire "thread" in live docs/specs.

   Rationale: The live repo is better described as workflows over research objects. "Thread" was useful during earlier structure design, but now creates an extra concept users have to learn.

4. Keep old names only in archived history or explicit migration notes.

   Rationale: Rewriting archive history would reduce traceability. The live interface should use new names, while historical archive entries keep their original names.

## Risks / Trade-offs

- Broad rename touches many files -> Implement with careful path mapping and validate all OpenSpec specs afterward.
- Existing saved outputs keep old YAML prompt IDs -> Rename live saved outputs and update prompt IDs in their frontmatter during implementation.
- External references may mention old paths -> README should include a short migration note for old-to-new names.
- Spec capability renames are noisy -> Add new capability specs for new canonical names and remove old capability specs during implementation.

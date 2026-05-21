## Context

The repository naming convention now requires OpenSpec capability names to use phase-object-role grammar. Most research workflow specs are phase-prefixed, but the shared act prompt manifest and web prompt template contracts still use `repo-` names.

These two contracts are not general repository structure contracts. They govern how `act/` prompt manifests are structured and resolved for web use, so the `act-` phase prefix is the clearer fit.

## Goals / Non-Goals

**Goals:**

- Rename the two act prompt meta-contract capabilities to `act-prompt-manifest` and `act-web-prompt-template`.
- Update active references in specs and docs.
- Preserve the existing manifest and web prompt behavior.
- Record naming guidance for phase-local structural contracts.

**Non-Goals:**

- Do not rename live files under `act/`.
- Do not rename the remaining action specs with `-prompt` suffix in this change.
- Do not change prompt output contracts, scoring behavior, discovery behavior, or Markdown formatting behavior.

## Decisions

- Use `act-prompt-manifest` rather than `repo-act-prompt-manifest`.
  - Rationale: the contract governs `act/*.md` manifest structure.
  - Alternative considered: keep the `repo-` prefix because the contract is cross-cutting. That keeps history stable but conflicts with the phase naming convention.

- Use `act-web-prompt-template` rather than `repo-web-prompt-template`.
  - Rationale: canonical web prompt templates are executable act prompt templates.
  - Alternative considered: `act-prompt-web-template`. That is phase-prefixed but less readable than object-role ordering.

- Keep `repo-prompt-markdown-format` unchanged.
  - Rationale: Markdown formatting is a repo-wide formatting rule, not act-specific behavior.
  - Alternative considered: rename it to `act-prompt-markdown-format`. That would overstate its phase scope and create a larger rename surface.

- Leave archived changes unchanged.
  - Rationale: archived changes are historical records and may retain old capability names.

## Risks / Trade-offs

- Stale active references may continue pointing to retired names -> Mitigate with an active-file reference scan during implementation.
- Renaming meta-contracts creates churn in several act specs -> Keep changes limited to contract names and links.
- Remaining `-prompt` action specs will still be inconsistent -> Treat them as separate follow-up renames so this change stays focused.

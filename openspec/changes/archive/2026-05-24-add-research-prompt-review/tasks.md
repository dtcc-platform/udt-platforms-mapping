## 1. Specs

- [x] 1.1 Add `openspec/specs/research-prompt-review/spec.md`.
- [x] 1.2 Update `research-workflow-structure` to place resolved prompts and per-agent reviews in `observe/`, and review synthesis in `reflect/`.

## 2. Documentation

- [x] 2.1 Update the root README to explain spec prefixes: `research-*` for cross-phase research governance and phase prefixes for one-phase contracts.
- [x] 2.2 Update the root README workflow guidance to show where resolved prompt snapshots, prompt reviews, and review synthesis are stored.
- [x] 2.3 Improve the root README Mermaid diagrams to show manifest resolution, saved resolved prompts, review outputs, optional synthesis, and accepted OpenSpec changes.
- [x] 2.4 Update `act/README.md` to point prompt-review users from manifests to saved resolved prompt snapshots.
- [x] 2.5 Update `observe/README.md` to document resolved prompt and prompt-review filename patterns.
- [x] 2.6 Update `reflect/README.md` to document prompt-review synthesis artifacts.

## 3. Validation

- [x] 3.1 Search active docs and specs for stale prompt-review wording after documentation updates.
- [x] 3.2 Validate the change with `openspec validate add-research-prompt-review --strict`.
- [x] 3.3 Validate all active specs with `openspec validate --all --strict`.

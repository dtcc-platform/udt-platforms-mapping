## ADDED Requirements

### Requirement: Prompt review uses saved resolved prompt snapshots

Prompt review SHALL start from a saved resolved prompt snapshot generated from one governed `act/` manifest, its required OpenSpec contracts, and its required run inputs.

Resolved prompt snapshots SHALL be stored under `observe/` using the pattern `observe/<action>-resolved-prompt-<resolver-short>.md`.

The resolved prompt snapshot SHALL identify the source `act/` manifest, resolver, date, required contracts, and required run inputs.

The resolved prompt snapshot SHALL NOT replace the source `act/` manifest or any OpenSpec contract.

#### Scenario: Researcher saves a resolved prompt for review

- **WHEN** a researcher resolves `act/entity-discovery.md` for review using Codex
- **THEN** the resolved prompt snapshot is saved as `observe/entity-discovery-resolved-prompt-codex.md`
- **THEN** the snapshot identifies the manifest, resolver, date, required contracts, and required run inputs
- **THEN** the source manifest and specs remain the canonical behavior source

### Requirement: Review agents compare resolved prompts against governing contracts

Each prompt review SHALL compare the saved resolved prompt snapshot against its source manifest, required OpenSpec contracts, and required run inputs.

Each review SHALL check for missing required contracts, missing run inputs, invented behavior, duplicated contract behavior, output-contract mismatches, resolver glue errors, and ambiguous spec wording.

Each review SHALL produce a pass/fail faithfulness judgment and actionable findings.

Prompt reviewers SHALL NOT rewrite the governed prompt freely; they SHALL identify contract interpretation issues and proposed OpenSpec clarifications.

#### Scenario: Reviewer checks a resolved prompt

- **WHEN** a reviewer examines `observe/entity-discovery-resolved-prompt-codex.md`
- **THEN** the reviewer compares it against `act/entity-discovery.md` and the listed contracts and inputs
- **THEN** the review identifies missing, invented, duplicated, mismatched, or ambiguous behavior
- **THEN** the review does not treat itself as a replacement prompt

### Requirement: Review outputs are stored as observations

Per-agent prompt review outputs SHALL be stored under `observe/` using the pattern `observe/<action>-prompt-review-<reviewer-short>.md`.

Each prompt review output SHALL identify the reviewed resolved prompt snapshot, reviewer, date, source manifest, and faithfulness judgment.

Prompt review outputs SHALL be treated as observed review evidence, not canonical research action outputs.

#### Scenario: Different agents review the same prompt

- **WHEN** Claude and ChatGPT independently review an entity discovery resolved prompt
- **THEN** their outputs are saved as `observe/entity-discovery-prompt-review-claude.md` and `observe/entity-discovery-prompt-review-chatgpt.md`
- **THEN** each output identifies the same reviewed resolved prompt snapshot
- **THEN** differences between review findings remain visible as observed evidence

### Requirement: Review synthesis belongs in reflect

When prompt review findings are consolidated, the synthesis SHALL be stored under `reflect/` using the pattern `reflect/<action>-prompt-review.md`.

The synthesis SHALL compare reviewer findings, identify agreement or disagreement, and list proposed OpenSpec changes for accepted issues.

The synthesis SHALL NOT directly change baseline specs, manifests, or prompts.

#### Scenario: Researcher consolidates prompt reviews

- **WHEN** multiple prompt review outputs exist for one action
- **THEN** a synthesis may be saved as `reflect/entity-discovery-prompt-review.md`
- **THEN** the synthesis compares reviewer agreement and disagreement
- **THEN** accepted fixes are expressed as proposed OpenSpec changes

### Requirement: Accepted review findings become OpenSpec changes

Accepted prompt-review findings SHALL be implemented through scoped OpenSpec changes before baseline specs, manifests, or documentation are changed.

Accepted findings MAY clarify existing contracts, add missing contract requirements, update manifests, or improve documentation.

Prompt review artifacts SHALL remain historical evidence after accepted fixes are applied.

#### Scenario: Review reveals ambiguous output wording

- **WHEN** prompt review finds that an observe output contract is ambiguous
- **THEN** the accepted clarification is captured in an OpenSpec change
- **THEN** the baseline output contract is updated only through that change
- **THEN** the original resolved prompt and review outputs remain in `observe/`

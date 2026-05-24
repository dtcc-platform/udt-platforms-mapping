# Spec: research-prompt-review

## Purpose

Defines the cross-phase research workflow for reviewing resolved prompts against their manifests, required contracts, and run inputs.

## Requirements

### Requirement: Prompt review uses saved resolved prompt snapshots

Prompt review SHALL start from a saved resolved prompt snapshot generated from one governed `act/` manifest, its required OpenSpec contracts, and its required run inputs.

Resolved prompt snapshots SHALL be stored as direct files under `act/` using the pattern `act/<action>-resolved-<resolver-short>.md`.

The resolved prompt snapshot SHALL begin with the executable research query so the artifact remains runnable in web research tools.

The resolved prompt snapshot SHALL identify the source `act/` manifest, resolver, date, required contracts, and required run inputs after the executable research query.

The resolved prompt snapshot SHALL NOT replace the source `act/` manifest or any OpenSpec contract.

#### Scenario: Researcher saves a resolved prompt for review

- **WHEN** a researcher resolves `act/entity-discovery.md` for review using Codex
- **THEN** the resolved prompt snapshot is saved as `act/entity-discovery-resolved-codex.md`
- **THEN** the snapshot starts with the executable entity discovery research query
- **THEN** the snapshot identifies the manifest, resolver, date, required contracts, and required run inputs after the query
- **THEN** the source manifest and specs remain the canonical behavior source

### Requirement: Review agents compare resolved prompts against governing contracts

Each prompt review SHALL compare the saved resolved prompt snapshot against its source manifest, required OpenSpec contracts, and required run inputs.

Each review SHALL be performed by an agent different from the agent that resolved the prompt snapshot.

Each review SHALL apply the `research-prompt-review-checklist` contract.

Each review SHALL produce a pass/fail faithfulness judgment and actionable findings in stdout/chat by default.

Prompt reviewers SHALL NOT rewrite the governed prompt freely; they SHALL identify contract interpretation issues and propose OpenSpec changes when repository changes are required.

#### Scenario: Different reviewer checks a resolved prompt

- **WHEN** Codex resolves `act/entity-discovery-resolved-codex.md`
- **THEN** a different reviewer agent reviews the resolved prompt against `act/entity-discovery.md` and the listed contracts and inputs
- **THEN** the reviewer applies `research-prompt-review-checklist`
- **THEN** the review identifies issues using the checklist criteria
- **THEN** the review produces a pass/fail judgment and findings in stdout/chat
- **THEN** the review does not treat itself as a replacement prompt

### Requirement: Review outputs are stdout by default

Prompt review output SHALL be returned in stdout/chat by default.

Prompt review output SHALL NOT be required as a persisted repository artifact before a research prompt can be run.

When a researcher explicitly saves prompt review evidence, it SHALL be stored under `observe/` using the pattern `observe/<action>-prompt-review-<reviewer-short>.md`.

Saved prompt review evidence SHALL identify the reviewed resolved prompt snapshot, reviewer, date, source manifest, and faithfulness judgment.

Saved prompt review evidence SHALL be treated as observed review evidence, not canonical research action output.

#### Scenario: Reviewer returns stdout review

- **WHEN** a reviewer agent reviews `act/entity-discovery-resolved-codex.md`
- **THEN** the reviewer returns the faithfulness judgment and findings in stdout/chat
- **THEN** no `observe/` review artifact is required

#### Scenario: Researcher explicitly saves review evidence

- **WHEN** a researcher chooses to persist Claude's entity discovery prompt review
- **THEN** the review may be saved as `observe/entity-discovery-prompt-review-claude.md`
- **THEN** the saved evidence identifies `act/entity-discovery-resolved-codex.md`

### Requirement: Review synthesis belongs in reflect

When prompt review findings are explicitly consolidated, the synthesis SHALL be stored under `reflect/` using the pattern `reflect/<action>-prompt-review.md`.

The synthesis SHALL compare reviewer findings, identify agreement or disagreement, and list proposed OpenSpec changes for accepted issues.

The synthesis SHALL NOT directly change baseline specs, manifests, documentation, skills, or prompts.

#### Scenario: Researcher consolidates prompt reviews

- **WHEN** multiple prompt review outputs exist for one action
- **THEN** a synthesis may be saved as `reflect/entity-discovery-prompt-review.md`
- **THEN** the synthesis compares reviewer agreement and disagreement
- **THEN** accepted fixes are expressed as proposed OpenSpec changes

### Requirement: Accepted review findings become OpenSpec changes

Accepted prompt-review findings SHALL be implemented through scoped OpenSpec changes before baseline specs, manifests, documentation, skills, or generated prompt conventions are changed.

Accepted findings MAY clarify existing contracts, add missing contract requirements, update manifests, update operational skills, or improve documentation.

Review findings that require repository changes SHALL include OpenSpec proposal intent, including a suggested change name, affected capabilities, why the change is needed, and what should change.

Saved prompt review evidence, when present, SHALL remain historical evidence after accepted fixes are applied.

#### Scenario: Review reveals ambiguous output wording

- **WHEN** prompt review finds that an observe output contract is ambiguous
- **THEN** the accepted clarification is captured in an OpenSpec change
- **THEN** the baseline output contract is updated only through that change
- **THEN** any saved resolved prompt or review evidence remains historical evidence

#### Scenario: Review proposes a repository change

- **WHEN** a reviewer finds that the resolved prompt is inconsistent with governing contracts
- **THEN** the reviewer proposes an OpenSpec change intent in stdout/chat
- **THEN** the repository change is not applied until the OpenSpec change is created and accepted

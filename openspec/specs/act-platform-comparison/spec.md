# Spec: act-platform-comparison

## Purpose

Defines the platform comparison action, selected comparison set behavior, scoring contract composition, source-policy composition, DTCC reference handling, and output contract conformance.

## Requirements

### Requirement: Platform comparison action is canonical

The repository SHALL contain `act/compare-platforms.md` as the canonical platform comparison prompt template.

The prompt SHALL conform to `repo-act-prompt-manifest`.

The prompt SHALL conform to `repo-web-prompt-template`.

The prompt SHALL require `repo-prompt-markdown-format` as a required formatting contract.

The prompt SHALL declare `act-platform-comparison` as a required prompt behavior contract.

The prompt SHALL require `plan-platform-comparison-rubric` and `plan-platform-source-policy` as behavior contracts.

The prompt SHALL require `observe-platform-comparison` as a required output contract.

The prompt SHALL require `plan/platform-comparison-set.md` as the selected platform comparison run input.

The prompt SHALL instruct the model to compare only the platforms selected in `plan/platform-comparison-set.md`.

The prompt SHALL instruct the model to apply `plan-platform-comparison-rubric` for scoring behavior.

The prompt SHALL instruct the model to apply `plan-platform-source-policy` for acceptable evidence and citation behavior.

The prompt SHALL instruct the model to treat the DTCC row as the reference platform for landscape observations.

The prompt SHALL instruct the model to stop and ask the user to add DTCC if the DTCC row is absent from the comparison set.

The prompt SHALL instruct the model not to broaden the comparison to frameworks or modules.

The prompt SHALL instruct the model to render the `observe-platform-comparison` metadata block, scoring table, platform profiles, and landscape observations explicitly.

The prompt SHALL instruct the user to save web responses to `observe/platform-comparison-<model-short>.md`.

The live `act/compare-platforms.md` prompt body SHALL avoid duplicating behavior supplied by required contracts.

#### Scenario: Researcher runs platform comparison

- **WHEN** a researcher resolves `act/compare-platforms.md`
- **THEN** the prompt conforms to the shared act manifest contract
- **THEN** the prompt conforms to the shared web prompt template
- **THEN** the prompt incorporates the `act-platform-comparison` behavior contract
- **THEN** the prompt incorporates the `repo-prompt-markdown-format` formatting contract
- **THEN** the prompt incorporates the comparison set run input
- **THEN** the prompt incorporates the platform comparison rubric and source policy behavior contracts
- **THEN** the prompt renders the `observe-platform-comparison` output contract into executable instructions
- **THEN** the prompt tells the researcher to save the web response under `observe/`

### Requirement: Platform comparison set is authoritative run input

The repository SHALL contain `plan/platform-comparison-set.md` as the selected platform comparison set.

Each data row SHALL represent one selected row that already qualifies as `Type = platform` from entity discovery.

The comparison prompt SHALL treat the rows in `plan/platform-comparison-set.md` as the complete and authoritative set of platforms to compare.

#### Scenario: Researcher opens platform comparison set

- **WHEN** a researcher opens `plan/platform-comparison-set.md`
- **THEN** the file is available as the selected platform comparison input
- **THEN** the platform comparison action treats it as authoritative comparison scope

# Spec: act-udt-platform-comparison-prompt

## Purpose

Defines the prompt template at `act/udt-platform-comparison.md` — structure, required inputs, scoring contract, and save-as conventions for comparison sessions.
## Requirements
### Requirement: UDT platform comparison prompt file exists

The repository SHALL contain a file at `act/udt-platform-comparison.md` that provides a self-contained prompt template for AI-assisted side-by-side comparison of selected UDT platforms.

#### Scenario: Researcher finds the UDT platform comparison prompt

- **WHEN** a researcher opens `act/`
- **THEN** `act/udt-platform-comparison.md` is available as the canonical `udt-platform-comparison` prompt template

### Requirement: Comparison prompt is platform-only

The prompt SHALL treat `plan/udt-platform-comparison-platforms.md` as the selected `Type = platform` subset from `udt-platforms`.
The prompt SHALL instruct the model not to broaden the comparison to frameworks or modules.

#### Scenario: Prompt uses selected platform subset

- **WHEN** the researcher resolves `act/udt-platform-comparison.md`
- **THEN** the prompt uses `plan/udt-platform-comparison-platforms.md` as the selected platform input
- **THEN** the prompt excludes frameworks and modules from comparison

### Requirement: Comparison prompt declares required inputs

The prompt SHALL include a `## Required Inputs` section listing:

- `plan/udt-platform-comparison-rubrics.md`
- `plan/udt-platform-comparison-platforms.md`
- `plan/udt-platform-comparison-source-policy.md`

The repository SHALL contain a file at `plan/udt-platform-comparison-rubrics.md`.
That file SHALL contain the 12 dimension and functional-category rubrics used by `act/udt-platform-comparison.md`.

#### Scenario: Prompt lists flattened required inputs

- **WHEN** a researcher opens `act/udt-platform-comparison.md`
- **THEN** the required inputs list references the flattened `plan/udt-platform-comparison-*.md` files

### Requirement: Comparison prompt executes through one governed path

The prompt SHALL instruct the user to use the resolved prompt in a web interface rather than treat CLI execution as the canonical path.
The prompt SHALL resolve all three required inputs into one copy-ready prompt block.
The prompt SHALL instruct the user to save the web response to `observe/udt-platform-comparison-web-<model-short>.md`.

#### Scenario: Researcher runs the canonical prompt

- **WHEN** a researcher resolves `act/udt-platform-comparison.md`
- **THEN** the prompt incorporates the flattened comparison planning inputs
- **THEN** the prompt tells the researcher to save the web response as a direct file under `observe/`

### Requirement: Comparison prompt owns the platform-only handoff rule

Only rows from `udt-platforms` where `Type = platform` SHALL be eligible for `udt-platform-comparison`.

#### Scenario: Researcher prepares comparison input

- **WHEN** a researcher prepares `plan/udt-platform-comparison-platforms.md`
- **THEN** only `Type = platform` rows from `udt-platforms` are eligible for inclusion

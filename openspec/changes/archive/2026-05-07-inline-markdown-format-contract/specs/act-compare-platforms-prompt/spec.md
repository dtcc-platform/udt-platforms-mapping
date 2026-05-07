## MODIFIED Requirements

### Requirement: Compare platforms prompt is the canonical platform comparison prompt

The repository SHALL contain `act/compare-platforms.md` as the canonical platform comparison prompt template.

The prompt SHALL conform to `repo-web-prompt-template`.

The prompt SHALL require `repo-prompt-markdown-format` as a required formatting contract.

The prompt SHALL require `platform-comparison-rubric` and `platform-source-policy` as behavior contracts.

The prompt SHALL require `observe-platform-comparison` as a required output contract.

The prompt SHALL require `plan/platform-comparison-set.md` as the selected platform comparison run input.

The prompt SHALL instruct the model to compare only the platforms selected in `plan/platform-comparison-set.md`.

The prompt SHALL instruct the model to apply `platform-comparison-rubric` for scoring behavior.

The prompt SHALL instruct the model to apply `platform-source-policy` for acceptable evidence and citation behavior.

The prompt SHALL instruct the model to render the `observe-platform-comparison` metadata block, scoring table, platform profiles, and landscape observations explicitly.

The prompt SHALL instruct the model to produce output conforming to `observe-platform-comparison`.

The prompt SHALL instruct the user to save web responses to `observe/platform-comparison-<model-short>.md`.

#### Scenario: Researcher runs platform comparison

- **WHEN** a researcher resolves `act/compare-platforms.md`
- **THEN** the prompt conforms to the shared web prompt template
- **THEN** the prompt incorporates the `repo-prompt-markdown-format` formatting contract
- **THEN** the prompt incorporates the comparison set run input
- **THEN** the prompt incorporates the platform comparison rubric and source policy behavior contracts
- **THEN** the prompt renders the `observe-platform-comparison` output contract into executable instructions
- **THEN** the prompt tells the researcher to save the web response under `observe/`

## MODIFIED Requirements

### Requirement: Compare platforms prompt is the canonical platform comparison prompt

The repository SHALL contain `act/compare-platforms.md` as the canonical platform comparison prompt template.

The prompt SHALL require `plan/platform-dimensions-scoring.md`, `plan/platform-comparison-set.md`, and `plan/platform-source-policy.md`.

The prompt SHALL instruct the model to compare only the platforms selected in `plan/platform-comparison-set.md`.

The prompt SHALL instruct the model to produce output conforming to `observe-platform-comparison`.

The prompt SHALL instruct the user to save web responses to `observe/platform-comparison-<model-short>.md`.

#### Scenario: Researcher runs platform comparison

- **WHEN** a researcher resolves `act/compare-platforms.md`
- **THEN** the prompt incorporates the comparison set, dimensions scoring, and source policy
- **THEN** the prompt renders the `observe-platform-comparison` output contract into executable instructions
- **THEN** the prompt tells the researcher to save the web response under `observe/`

## ADDED Requirements

### Requirement: Discover initiatives prompt is the canonical initiative discovery prompt

The repository SHALL contain `act/discover-initiatives.md` as the canonical initiative and project discovery prompt template.

The prompt SHALL declare `plan/initiative-definition.md` as a required input.

The prompt SHALL instruct the model to use platform artifact names from platform discovery when an initiative's technical substrate is clear.

The prompt SHALL instruct the user to save web responses to `observe/initiative-discovery-<model-short>.md`.

#### Scenario: Researcher runs initiative discovery

- **WHEN** a researcher resolves `act/discover-initiatives.md`
- **THEN** the prompt incorporates `plan/initiative-definition.md`
- **THEN** the prompt tells the researcher to save the web response under `observe/`

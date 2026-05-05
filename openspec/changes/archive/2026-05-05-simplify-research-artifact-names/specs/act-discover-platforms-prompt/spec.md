## ADDED Requirements

### Requirement: Discover platforms prompt is the canonical platform discovery prompt

The repository SHALL contain `act/discover-platforms.md` as the canonical platform discovery prompt template.

The prompt SHALL declare `plan/platform-definition.md` as a required input.

The prompt SHALL instruct the model to use `plan/platform-definition.md` as the authoritative classification contract for assigning each artifact's `Type`.

The prompt SHALL instruct the user to save web responses to `observe/platform-discovery-<model-short>.md`.

#### Scenario: Researcher runs platform discovery

- **WHEN** a researcher resolves `act/discover-platforms.md`
- **THEN** the prompt incorporates `plan/platform-definition.md`
- **THEN** the prompt tells the researcher to save the web response under `observe/`

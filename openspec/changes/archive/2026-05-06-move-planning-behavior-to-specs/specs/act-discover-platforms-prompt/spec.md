## MODIFIED Requirements

### Requirement: Discover platforms prompt is the canonical platform discovery prompt

The repository SHALL contain `act/discover-platforms.md` as the canonical platform discovery prompt template.

The prompt SHALL declare `platform-definition` as a required behavior contract.

The prompt SHALL instruct the model to use `platform-definition` as the authoritative classification contract for assigning each artifact's `Type`.

The prompt SHALL instruct the model to apply the platform definition interpretation rules before assigning a `Type`.

The prompt SHALL instruct the model to classify artifacts by observable presentation and role in the urban digital twin ecosystem.

The prompt SHALL instruct the model to assign exactly one `Type` per artifact.

The prompt SHALL instruct the model to use the platform definition tie-break guidance for borderline artifacts.

The prompt SHALL instruct the model to preserve uncertainty when evidence is weak or ambiguous.

The prompt SHALL instruct the model to produce output conforming to `observe-platform-discovery`.

The prompt SHALL instruct the user to save web responses to `observe/platform-discovery-<model-short>.md`.

#### Scenario: Researcher runs platform discovery

- **WHEN** a researcher resolves `act/discover-platforms.md`
- **THEN** the prompt incorporates the `platform-definition` behavior contract
- **THEN** the prompt renders the platform definition interpretation rules into executable instructions
- **THEN** the prompt renders the `observe-platform-discovery` output contract into executable instructions
- **THEN** the prompt tells the researcher to save the web response under `observe/`

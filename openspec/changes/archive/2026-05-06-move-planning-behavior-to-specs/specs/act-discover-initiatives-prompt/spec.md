## MODIFIED Requirements

### Requirement: Discover initiatives prompt is the canonical initiative discovery prompt

The repository SHALL contain `act/discover-initiatives.md` as the canonical initiative and project discovery prompt template.

The prompt SHALL declare `initiative-definition` as a required behavior contract.

The prompt SHALL instruct the model to use platform artifact names from platform discovery when an initiative's technical substrate is clear.

The prompt SHALL instruct the model to preserve uncertainty with `Uses = ?` when an initiative's technical substrate is unclear.

The prompt SHALL instruct the model to produce output conforming to `observe-initiative-discovery`.

The prompt SHALL instruct the user to save web responses to `observe/initiative-discovery-<model-short>.md`.

#### Scenario: Researcher runs initiative discovery

- **WHEN** a researcher resolves `act/discover-initiatives.md`
- **THEN** the prompt incorporates the `initiative-definition` behavior contract
- **THEN** the prompt renders the `observe-initiative-discovery` output contract into executable instructions
- **THEN** the prompt tells the researcher to save the web response under `observe/`

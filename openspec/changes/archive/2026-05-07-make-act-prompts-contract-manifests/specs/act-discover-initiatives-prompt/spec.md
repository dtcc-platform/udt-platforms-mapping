## MODIFIED Requirements

### Requirement: Discover initiatives prompt is the canonical initiative discovery prompt

The repository SHALL contain `act/discover-initiatives.md` as the canonical initiative and project discovery prompt template.

The prompt SHALL conform to `repo-act-prompt-manifest`.

The prompt SHALL conform to `repo-web-prompt-template`.

The prompt SHALL require `repo-prompt-markdown-format` as a required formatting contract.

The prompt SHALL declare `act-discover-initiatives-prompt` as a required prompt behavior contract.

The prompt SHALL declare `initiative-definition` as a required behavior contract.

The prompt SHALL declare `observe-initiative-discovery` as a required output contract.

The prompt SHALL instruct the model to use platform artifact names from platform discovery when an initiative's technical substrate is clear.

The prompt SHALL instruct the model to preserve uncertainty with `Uses = ?` when an initiative's technical substrate is unclear.

The prompt SHALL instruct the model to render the `observe-initiative-discovery` metadata block, summary table, and initiative sections explicitly.

The prompt SHALL instruct the user to save web responses to `observe/initiative-discovery-<model-short>.md`.

The live `act/discover-initiatives.md` prompt body SHALL avoid duplicating behavior supplied by required contracts.

#### Scenario: Researcher runs initiative discovery

- **WHEN** a researcher resolves `act/discover-initiatives.md`
- **THEN** the prompt conforms to the shared act manifest contract
- **THEN** the prompt conforms to the shared web prompt template
- **THEN** the prompt incorporates the `act-discover-initiatives-prompt` prompt behavior contract
- **THEN** the prompt incorporates the `repo-prompt-markdown-format` formatting contract
- **THEN** the prompt incorporates the `initiative-definition` behavior contract
- **THEN** the prompt renders the `observe-initiative-discovery` output contract into executable instructions
- **THEN** the prompt tells the researcher to save the web response under `observe/`

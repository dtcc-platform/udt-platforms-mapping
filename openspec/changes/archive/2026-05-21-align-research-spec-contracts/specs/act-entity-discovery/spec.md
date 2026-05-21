## MODIFIED Requirements

### Requirement: Entity discovery prompt is the canonical discovery prompt

The repository SHALL contain `act/discover-entities.md` as the canonical UDT entity discovery prompt template.

The prompt SHALL conform to `act-prompt-manifest`.

The prompt SHALL conform to `act-web-prompt-template`.

The prompt SHALL require `observe-markdown-output-format` as a required formatting contract.

The prompt SHALL declare `act-entity-discovery` as a required prompt behavior contract.

The prompt SHALL declare `plan-entity-definition` as a required behavior contract.

The prompt SHALL declare `observe-entity-discovery` as a required output contract.

The prompt SHALL instruct the model to use `plan-entity-definition` as the authoritative classification contract for assigning each candidate's `Type`.

The prompt SHALL instruct the model to discover technical artifacts, initiatives, excluded boundary candidates, and initiative-to-artifact substrate relationships in one discovery run.

The prompt SHALL instruct the model to assign exactly one `Type` per candidate row.

The prompt SHALL instruct the model to use the entity definition tie-break guidance for borderline candidates.

The prompt SHALL instruct the model to preserve uncertainty when evidence is weak or ambiguous.

The prompt SHALL instruct the model to render the `observe-entity-discovery` metadata block, coverage statement, summary table, and entity sections explicitly.

The prompt SHALL instruct the user to save web responses to `observe/entity-discovery-<model-short>.md`.

The live `act/discover-entities.md` prompt body SHALL avoid duplicating behavior supplied by required contracts.

#### Scenario: Researcher runs entity discovery

- **WHEN** a researcher resolves `act/discover-entities.md`
- **THEN** the prompt conforms to the shared act manifest contract
- **THEN** the prompt conforms to the shared web prompt template
- **THEN** the prompt incorporates the `act-entity-discovery` behavior contract
- **THEN** the prompt incorporates the `observe-markdown-output-format` formatting contract
- **THEN** the prompt incorporates the `plan-entity-definition` behavior contract
- **THEN** the prompt renders the `observe-entity-discovery` output contract into executable instructions
- **THEN** the prompt tells the researcher to save the web response under `observe/`


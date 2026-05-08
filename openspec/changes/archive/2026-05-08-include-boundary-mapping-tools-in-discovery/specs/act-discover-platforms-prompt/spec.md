## MODIFIED Requirements

### Requirement: Discover platforms prompt is the canonical platform discovery prompt

The repository SHALL contain `act/discover-platforms.md` as the canonical platform discovery prompt template.

The prompt SHALL conform to `repo-act-prompt-manifest`.

The prompt SHALL conform to `repo-web-prompt-template`.

The prompt SHALL require `repo-prompt-markdown-format` as a required formatting contract.

The prompt SHALL declare `act-discover-platforms-prompt` as a required prompt behavior contract.

The prompt SHALL declare `platform-definition` as a required behavior contract.

The prompt SHALL declare `observe-platform-discovery` as a required output contract.

The prompt SHALL instruct the model to use `platform-definition` as the authoritative classification contract for assigning each artifact's `Type`.

The prompt SHALL instruct the model to apply the platform definition interpretation rules before assigning a `Type`.

The prompt SHALL instruct the model to classify artifacts by observable presentation and role in the urban digital twin ecosystem.

The prompt SHALL instruct the model to assign exactly one `Type` per artifact.

The prompt SHALL instruct the model to use the platform definition tie-break guidance for borderline artifacts.

The prompt SHALL instruct the model to preserve uncertainty when evidence is weak or ambiguous.

The prompt SHALL instruct the model to treat platform discovery as a broad global discovery action.

The prompt SHALL instruct the model to prioritize breadth and candidate recall.

The prompt SHALL instruct the model to include relevant boundary candidates as explicit `excluded` rows when they are likely to be confused with UDT artifacts or useful for explaining the study boundary.

The prompt SHALL instruct the model to include map storytelling, communication, presentation, and lightweight web-map narrative tools as `excluded` when they are discovered as plausible boundary candidates.

The prompt SHALL instruct the model to prefer stronger evidence when available.

The prompt SHALL instruct the model to use `unknown` or `?` when evidence is insufficient.

The prompt SHALL instruct the model not to imply global completeness.

The prompt SHALL instruct the model to render the `observe-platform-discovery` metadata block, summary table, and artifact sections explicitly.

The prompt SHALL instruct the user to save web responses to `observe/platform-discovery-<model-short>.md`.

The live `act/discover-platforms.md` prompt body SHALL avoid duplicating behavior supplied by required contracts.

#### Scenario: Researcher runs platform discovery

- **WHEN** a researcher resolves `act/discover-platforms.md`
- **THEN** the prompt conforms to the shared act manifest contract
- **THEN** the prompt conforms to the shared web prompt template
- **THEN** the prompt incorporates the `act-discover-platforms-prompt` prompt behavior contract
- **THEN** the prompt incorporates the `repo-prompt-markdown-format` formatting contract
- **THEN** the prompt incorporates the `platform-definition` behavior contract
- **THEN** the prompt renders the platform definition interpretation rules into executable instructions
- **THEN** the prompt renders the `observe-platform-discovery` output contract into executable instructions
- **THEN** the prompt tells the researcher to save the web response under `observe/`

#### Scenario: Boundary mapping tool is discovered

- **WHEN** platform discovery finds a StoryMapJS-style map storytelling or narrative publishing tool
- **THEN** the prompt causes the model to include it as an `excluded` row
- **THEN** the reason explains that it is outside the technical UDT artifact boundary

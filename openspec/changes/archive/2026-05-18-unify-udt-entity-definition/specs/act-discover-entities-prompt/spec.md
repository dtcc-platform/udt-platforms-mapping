## ADDED Requirements

### Requirement: Discover entities prompt is the canonical discovery prompt

The repository SHALL contain `act/discover-entities.md` as the canonical UDT entity discovery prompt template.

The prompt SHALL conform to `repo-act-prompt-manifest`.

The prompt SHALL conform to `repo-web-prompt-template`.

The prompt SHALL require `repo-prompt-markdown-format` as a required formatting contract.

The prompt SHALL declare `act-discover-entities-prompt` as a required prompt behavior contract.

The prompt SHALL declare `entity-definition` as a required behavior contract.

The prompt SHALL declare `platform-discovery-coverage` as a required behavior contract until a dedicated entity discovery coverage contract replaces it.

The prompt SHALL declare `observe-entity-discovery` as a required output contract.

The prompt SHALL instruct the model to use `entity-definition` as the authoritative classification contract for assigning each candidate's `Type`.

The prompt SHALL instruct the model to discover technical artifacts, initiatives, excluded boundary candidates, and initiative-to-artifact substrate relationships in one discovery run.

The prompt SHALL instruct the model to assign exactly one `Type` per candidate row.

The prompt SHALL instruct the model to use the entity definition tie-break guidance for borderline candidates.

The prompt SHALL instruct the model to preserve uncertainty when evidence is weak or ambiguous.

The prompt SHALL instruct the model to treat entity discovery as a broad global discovery action.

The prompt SHALL instruct the model to prioritize breadth and candidate recall.

The prompt SHALL instruct the model to search beyond explicit "urban digital twin platform", "city digital twin", "smart city platform", and "3D city platform" wording.

The prompt SHALL instruct the model to include adjacent technical module search language such as urban analytics toolkit, urban visualization and data analysis toolkit, geospatial risk analysis, climate resilience visualization, infrastructure risk modeling, urban simulation toolkit, urban data analysis toolkit, PostGIS-based urban analytics, and city model visualization toolkit.

The prompt SHALL instruct the model to include adjacent geospatial visualization framework search language such as geospatial visualization framework, 3D web viewing library, 3D geospatial JavaScript framework, browser-based geospatial visualization, 2D 2.5D 3D geospatial data viewer, 3D Tiles viewer, point cloud web viewer, terrain visualization framework, raster/vector geospatial visualization, three.js geospatial framework, and OpenLayers 3D visualization.

The prompt SHALL instruct the model to include initiative search language such as UDT project, city digital twin programme, digital twin pilot, smart city digital twin deployment, national digital twin programme, and municipal digital twin initiative.

The prompt SHALL instruct the model to include relevant boundary candidates as explicit `initiative` or `excluded` rows when they are likely to be confused with UDT artifacts or useful for explaining the study boundary.

The prompt SHALL instruct the model to include map storytelling, communication, presentation, and lightweight web-map narrative tools as `excluded` when they are discovered as plausible boundary candidates.

The prompt SHALL instruct the model to prefer stronger evidence when available.

The prompt SHALL instruct the model to use `unknown` or `?` when evidence is insufficient.

The prompt SHALL instruct the model not to imply global completeness.

The prompt SHALL instruct the model to render the `observe-entity-discovery` metadata block, coverage statement, summary table, and entity sections explicitly.

The prompt SHALL instruct the user to save web responses to `observe/entity-discovery-<model-short>.md`.

The live `act/discover-entities.md` prompt body SHALL avoid duplicating behavior supplied by required contracts.

#### Scenario: Researcher runs entity discovery

- **WHEN** a researcher resolves `act/discover-entities.md`
- **THEN** the prompt conforms to the shared act manifest contract
- **THEN** the prompt conforms to the shared web prompt template
- **THEN** the prompt incorporates the `act-discover-entities-prompt` prompt behavior contract
- **THEN** the prompt incorporates the `repo-prompt-markdown-format` formatting contract
- **THEN** the prompt incorporates the `entity-definition` behavior contract
- **THEN** the prompt renders the `observe-entity-discovery` output contract into executable instructions
- **THEN** the prompt tells the researcher to save the web response under `observe/`

#### Scenario: Initiative and artifact are discovered together

- **WHEN** entity discovery finds a UDT initiative that uses a known technical artifact
- **THEN** the prompt causes the model to include the initiative and the artifact as appropriate rows
- **THEN** the model records the initiative-to-artifact relationship in the initiative's paragraph or section

#### Scenario: Boundary candidate is discovered

- **WHEN** entity discovery finds a map storytelling or narrative publishing tool outside the UDT boundary
- **THEN** the prompt causes the model to include it as `Type = excluded`
- **THEN** the reason appears in the entity paragraph or section rather than as a summary table column

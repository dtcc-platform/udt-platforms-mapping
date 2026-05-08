## MODIFIED Requirements

### Requirement: Discover platforms prompt is the canonical platform discovery prompt

The repository SHALL contain `act/discover-platforms.md` as the canonical platform discovery prompt template.

The prompt SHALL conform to `repo-act-prompt-manifest`.

The prompt SHALL conform to `repo-web-prompt-template`.

The prompt SHALL require `repo-prompt-markdown-format` as a required formatting contract.

The prompt SHALL declare `act-discover-platforms-prompt` as a required prompt behavior contract.

The prompt SHALL declare `platform-definition` as a required behavior contract.

The prompt SHALL declare `platform-discovery-coverage` as a required behavior contract.

The prompt SHALL declare `observe-platform-discovery` as a required output contract.

The prompt SHALL instruct the model to use `platform-definition` as the authoritative classification contract for assigning each artifact's `Type`.

The prompt SHALL instruct the model to apply the platform definition interpretation rules before assigning a `Type`.

The prompt SHALL instruct the model to classify artifacts by observable presentation and role in the urban digital twin ecosystem.

The prompt SHALL instruct the model to assign exactly one `Type` per artifact.

The prompt SHALL instruct the model to use the platform definition tie-break guidance for borderline artifacts.

The prompt SHALL instruct the model to preserve uncertainty when evidence is weak or ambiguous.

The prompt SHALL instruct the model to treat platform discovery as a broad global discovery action.

The prompt SHALL instruct the model to prioritize breadth and candidate recall.

The prompt SHALL instruct the model to follow `platform-discovery-coverage` for candidate count targets, category quotas, seed-list sampling, and early-stop prevention.

The prompt SHALL instruct the model to search beyond explicit "urban digital twin platform", "city digital twin", "smart city platform", and "3D city platform" wording.

The prompt SHALL instruct the model to include adjacent technical module search language such as urban analytics toolkit, urban visualization and data analysis toolkit, geospatial risk analysis, climate resilience visualization, infrastructure risk modeling, urban simulation toolkit, urban data analysis toolkit, PostGIS-based urban analytics, and city model visualization toolkit.

The prompt SHALL instruct the model to include adjacent geospatial visualization framework search language such as geospatial visualization framework, 3D web viewing library, 3D geospatial JavaScript framework, browser-based geospatial visualization, 2D 2.5D 3D geospatial data viewer, 3D Tiles viewer, point cloud web viewer, terrain visualization framework, raster/vector geospatial visualization, three.js geospatial framework, and OpenLayers 3D visualization.

The prompt SHALL instruct the model to consult adjacent ecosystem seed lists as recall aids, including frontend GIS, geospatial visualization, 3D Tiles, point-cloud and LiDAR web viewers, web mapping libraries, spatial data processing tools, geospatial analytics tools, and browser-based 2D/3D mapping framework lists.

The prompt SHALL instruct the model to classify seed-list candidates using `platform-definition` and SHALL NOT treat presence in a curated geospatial list as sufficient evidence that an artifact is a UDT platform.

The prompt SHALL instruct the model to include relevant boundary candidates as explicit `excluded` rows when they are likely to be confused with UDT artifacts or useful for explaining the study boundary.

The prompt SHALL instruct the model to include map storytelling, communication, presentation, and lightweight web-map narrative tools as `excluded` when they are discovered as plausible boundary candidates.

The prompt SHALL instruct the model to prefer stronger evidence when available.

The prompt SHALL instruct the model to use `unknown` or `?` when evidence is insufficient.

The prompt SHALL instruct the model not to imply global completeness.

The prompt SHALL instruct the model to render the `observe-platform-discovery` metadata block, coverage statement, summary table, and artifact sections explicitly.

The prompt SHALL instruct the user to save web responses to `observe/platform-discovery-<model-short>.md`.

The live `act/discover-platforms.md` prompt body SHALL avoid duplicating behavior supplied by required contracts.

#### Scenario: Researcher runs platform discovery

- **WHEN** a researcher resolves `act/discover-platforms.md`
- **THEN** the prompt conforms to the shared act manifest contract
- **THEN** the prompt conforms to the shared web prompt template
- **THEN** the prompt incorporates the `act-discover-platforms-prompt` prompt behavior contract
- **THEN** the prompt incorporates the `repo-prompt-markdown-format` formatting contract
- **THEN** the prompt incorporates the `platform-definition` behavior contract
- **THEN** the prompt incorporates the `platform-discovery-coverage` behavior contract
- **THEN** the prompt renders the platform definition interpretation rules into executable instructions
- **THEN** the prompt renders the platform discovery coverage rules into executable instructions
- **THEN** the prompt renders the `observe-platform-discovery` output contract into executable instructions
- **THEN** the prompt tells the researcher to save the web response under `observe/`

#### Scenario: Boundary mapping tool is discovered

- **WHEN** platform discovery finds a StoryMapJS-style map storytelling or narrative publishing tool
- **THEN** the prompt causes the model to include it as an `excluded` row
- **THEN** the reason explains that it is outside the technical UDT artifact boundary

#### Scenario: Urban analytics module is discoverable without digital twin wording

- **WHEN** platform discovery finds a GeoDatalytics-style urban visualization and data analysis toolkit
- **THEN** the prompt causes the model to include it as a candidate artifact
- **THEN** the model classifies it using `platform-definition`
- **THEN** the artifact is eligible to be classified as `module` when its observable role is a bounded analytics, visualization, data, simulation, or integration capability

#### Scenario: Geospatial visualization framework is discoverable without digital twin wording

- **WHEN** platform discovery finds a Giro3D-style 2D/3D geospatial visualization framework or 3D web viewing library
- **THEN** the prompt causes the model to include it as a candidate artifact
- **THEN** the model classifies it using `platform-definition`
- **THEN** the artifact is eligible to be classified as `framework` when its observable role is a reusable enabling visualization framework

#### Scenario: Adjacent seed list is used for recall

- **WHEN** platform discovery consults an `awesome-frontend-gis`-style seed list
- **THEN** the prompt causes the model to consider relevant frontend GIS, geospatial visualization, point-cloud, web mapping, spatial processing, and spatial analytics entries as candidates
- **THEN** the model classifies each included seed-list candidate using `platform-definition`
- **THEN** the model does not classify a seed-list candidate as `platform` only because it appears in the curated list

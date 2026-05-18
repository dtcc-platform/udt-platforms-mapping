## ADDED Requirements

### Requirement: Entity discovery prompt is the canonical discovery prompt

The repository SHALL contain `act/discover-entities.md` as the canonical UDT entity discovery prompt template.

The prompt SHALL conform to `repo-act-prompt-manifest`.

The prompt SHALL conform to `repo-web-prompt-template`.

The prompt SHALL require `repo-prompt-markdown-format` as a required formatting contract.

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
- **THEN** the prompt incorporates the `repo-prompt-markdown-format` formatting contract
- **THEN** the prompt incorporates the `plan-entity-definition` behavior contract
- **THEN** the prompt renders the `observe-entity-discovery` output contract into executable instructions
- **THEN** the prompt tells the researcher to save the web response under `observe/`

### Requirement: Entity discovery applies broad recall behavior

Entity discovery SHALL treat the action as broad candidate discovery across `platform`, `framework`, `module`, `initiative`, and useful `excluded` boundary candidates.

Entity discovery SHALL return at least 40 candidate artifacts when enough evidence is available.

Entity discovery SHALL include at least:

- 10 candidates classified as `platform`
- 15 candidates classified as `framework`
- 10 candidates classified as `module`
- 5 candidates classified as `excluded`

Entity discovery SHALL use these quotas as minimum quality gates, not as stopping conditions.

Meeting the minimum count SHALL NOT be considered sufficient when additional high-relevance candidates are discoverable.

After reaching the quota, entity discovery SHALL perform at least one additional targeted recall pass for regional, academic, open-source, and research-center UDT platforms.

Entity discovery SHALL NOT stop after representative examples when additional relevant candidates are discoverable.

Entity discovery SHALL prefer replacing weaker candidates with stronger candidates when the stronger candidates have clearer evidence and a better fit to `plan-entity-definition`.

Entity discovery SHALL NOT fabricate candidates or include unsupported candidates only to satisfy a quota.

When a coverage target cannot be met after reasonable search, entity discovery SHALL state which target was not met and why.

#### Scenario: Discovery has enough evidence

- **WHEN** enough relevant evidence is available for the target categories
- **THEN** entity discovery returns at least 40 candidate artifacts
- **THEN** entity discovery satisfies the platform, framework, module, and excluded category targets
- **THEN** entity discovery performs at least one additional targeted recall pass after meeting the quotas

#### Scenario: Discovery cannot meet a target

- **WHEN** a target cannot be met without weak or unsupported evidence
- **THEN** entity discovery does not fabricate candidates
- **THEN** entity discovery reports the unmet target and the reason it was not met

### Requirement: Entity discovery searches adjacent ecosystem language

Entity discovery SHALL treat entity discovery as a broad global discovery action.

Entity discovery SHALL prioritize breadth and candidate recall.

Entity discovery SHALL search beyond explicit "urban digital twin platform", "city digital twin", "smart city platform", and "3D city platform" wording.

Entity discovery SHALL include adjacent technical module search language such as urban analytics toolkit, urban visualization and data analysis toolkit, geospatial risk analysis, climate resilience visualization, infrastructure risk modeling, urban simulation toolkit, urban data analysis toolkit, PostGIS-based urban analytics, and city model visualization toolkit.

Entity discovery SHALL include adjacent geospatial visualization framework search language such as geospatial visualization framework, 3D web viewing library, 3D geospatial JavaScript framework, browser-based geospatial visualization, 2D 2.5D 3D geospatial data viewer, 3D Tiles viewer, point cloud web viewer, terrain visualization framework, raster/vector geospatial visualization, three.js geospatial framework, and OpenLayers 3D visualization.

Entity discovery SHALL include initiative search language such as UDT project, city digital twin programme, digital twin pilot, smart city digital twin deployment, national digital twin programme, and municipal digital twin initiative.

#### Scenario: Adjacent candidate is discoverable without digital twin wording

- **WHEN** entity discovery finds a relevant urban analytics, geospatial visualization, or initiative candidate without explicit digital twin wording
- **THEN** the prompt causes the model to include it as a candidate
- **THEN** the model classifies it using `plan-entity-definition`

### Requirement: Entity discovery samples adjacent seed-list families

Entity discovery SHALL search and sample candidates from at least three adjacent seed-list families.

The adjacent seed-list families SHALL include:

- frontend GIS and web mapping
- 3D geospatial visualization and 3D Tiles
- point-cloud, LiDAR, and city-model visualization

Entity discovery SHALL extract multiple relevant candidate artifacts from each sampled seed-list family when relevant candidates are available.

Entity discovery SHALL classify every included seed-list candidate using `plan-entity-definition`.

Entity discovery SHALL NOT treat seed-list presence as sufficient evidence that a candidate is a `platform`.

#### Scenario: Seed-list candidates are available

- **WHEN** entity discovery finds relevant candidates in adjacent seed-list families
- **THEN** it samples from at least three seed-list families
- **THEN** it includes multiple relevant candidates from each sampled family when available
- **THEN** it classifies each included candidate using `plan-entity-definition`

### Requirement: Entity discovery separates recall from later filtering

Entity discovery SHALL include relevant `framework`, `module`, `initiative`, and `excluded` candidates discovered during recall expansion even when they are not eligible for later platform comparison.

Entity discovery SHALL treat later platform comparison filtering as a separate action governed by the platform comparison contract.

#### Scenario: Non-platform candidate is discovered

- **WHEN** entity discovery finds a relevant framework, module, initiative, or boundary candidate
- **THEN** it includes the candidate in discovery output with the correct `Type`
- **THEN** it does not remove the candidate only because later platform comparison accepts only `platform` artifacts

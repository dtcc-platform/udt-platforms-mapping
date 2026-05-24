# Prompt

You are a research assistant mapping the Urban Digital Twin entity ecosystem.

Deeply research and map the Urban Digital Twin entity ecosystem. Follow the inlined required contracts below and perform entity discovery according to those contracts.

Return only the final deliverable.

# Resolved Prompt Metadata

- Source manifest: `act/entity-discovery.md`
- Resolver: `codex`
- Date: `2026-05-24`
- Required contracts:
  - `openspec/specs/act-entity-discovery/spec.md`
  - `openspec/specs/plan-entity-definition/spec.md`
  - `openspec/specs/observe-entity-discovery/spec.md`
  - `openspec/specs/observe-markdown-output-format/spec.md`
- Required run inputs: none

# openspec/specs/act-entity-discovery/spec.md

# Spec: act-entity-discovery

## Purpose

Defines the entity discovery action, including prompt execution, discovery scope, recall coverage, seed-list sampling, and anti-early-stop behavior.

## Requirements

### Requirement: Entity discovery prompt is the canonical discovery prompt

The repository SHALL contain `act/entity-discovery.md` as the canonical UDT entity discovery prompt template.

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

The prompt SHALL provide an explicit runnable research query suitable for web research tools before relying on inlined contract details.

The prompt SHALL instruct the user to save web responses to `observe/entity-discovery-<model-short>.md`.

The live `act/entity-discovery.md` prompt body SHALL avoid duplicating behavior supplied by required contracts.

#### Scenario: Researcher runs entity discovery

- **WHEN** a researcher resolves `act/entity-discovery.md`
- **THEN** the prompt starts with a runnable research query
- **THEN** the prompt conforms to the shared act manifest contract
- **THEN** the prompt conforms to the shared web prompt template
- **THEN** the prompt incorporates the `act-entity-discovery` behavior contract
- **THEN** the prompt incorporates the `observe-markdown-output-format` formatting contract
- **THEN** the prompt incorporates the `plan-entity-definition` behavior contract
- **THEN** the prompt renders the `observe-entity-discovery` output contract into executable instructions
- **THEN** the prompt tells the researcher to save the web response under `observe/`

### Requirement: Entity discovery applies broad recall behavior

Entity discovery SHALL treat the action as broad candidate discovery across `platform`, `framework`, `module`, `initiative`, and useful `excluded` boundary candidates.

Entity discovery SHALL return at least 50 candidate entities when enough evidence is available.

Entity discovery SHALL include at least:

- 10 candidates classified as `platform`
- 15 candidates classified as `framework`
- 10 candidates classified as `module`
- 5 candidates classified as `initiative`
- 5 candidates classified as `excluded`

The remaining candidates needed to meet the 50-entity floor SHALL be high-relevance entities of any allowed `Type`.

Entity discovery SHALL use these quotas as minimum quality gates, not as stopping conditions.

Meeting the minimum count SHALL NOT be considered sufficient when additional high-relevance candidates are discoverable.

After reaching the quota, entity discovery SHALL perform at least one additional targeted recall pass for regional, academic, open-source, and research-center UDT platforms and initiatives.

Entity discovery SHALL NOT stop after representative examples when additional relevant candidates are discoverable.

Entity discovery SHALL prefer replacing weaker candidates with stronger candidates when the stronger candidates have clearer evidence and a better fit to `plan-entity-definition`.

Entity discovery SHALL NOT fabricate candidates or include unsupported candidates only to satisfy a quota.

When a coverage target cannot be met after reasonable search, entity discovery SHALL state which target was not met and why.

#### Scenario: Discovery has enough evidence

- **WHEN** enough relevant evidence is available for the target categories
- **THEN** entity discovery returns at least 50 candidate entities
- **THEN** entity discovery satisfies the platform, framework, module, initiative, and excluded category targets
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

Entity discovery SHALL extract multiple relevant candidates from each sampled seed-list family when relevant candidates are available.

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

# openspec/specs/plan-entity-definition/spec.md

# Spec: plan-entity-definition

## Purpose

Defines UDT entity classification behavior for technical artifacts, initiatives, excluded candidates, and initiative-to-artifact substrate relationships.

## Requirements

### Requirement: Entity definition classifies UDT discovery rows

UDT discovery SHALL classify each included candidate with exactly one output `Type`.

Allowed output `Type` values SHALL be:

- `platform`
- `framework`
- `module`
- `initiative`
- `excluded`

The internal `artifact` concept SHALL group technical UDT artifacts whose output `Type` is `platform`, `framework`, or `module`.

The internal `artifact` concept SHALL NOT be required as an output table value unless another spec explicitly requires an internal classification field.

#### Scenario: Candidate is classified with output Type

- **WHEN** UDT discovery includes a candidate row
- **THEN** the row has exactly one `Type`
- **THEN** the `Type` is one of `platform`, `framework`, `module`, `initiative`, or `excluded`

#### Scenario: Technical artifact uses artifact grouping internally

- **WHEN** entity definition reasons about a candidate with `Type = platform`, `Type = framework`, or `Type = module`
- **THEN** the candidate is treated as part of the internal `artifact` group
- **THEN** the output table still uses the specific `Type` value

### Requirement: Artifact Type means technical UDT artifact

An entity SHALL be treated as an internal `artifact` when it is a distinct technical artifact, product, software system, framework, toolkit, reference implementation, data pipeline, simulator, visualization component, or reusable technical substrate related to Urban Digital Twins.

Technical artifacts SHALL be assigned one output `Type`: `platform`, `framework`, or `module`.

#### Scenario: Candidate is a technical artifact

- **WHEN** a candidate is a distinct technical substrate related to Urban Digital Twins
- **THEN** discovery treats it as part of the internal `artifact` group
- **THEN** entity discovery assigns `Type` as `platform`, `framework`, or `module`

### Requirement: Platform Type means usable UDT platform

An artifact SHALL be classified as `platform` when it is presented as a deployable or usable system for city-scale integration, visualization, simulation, or management of urban systems.

An artifact SHALL NOT be classified as `platform` only because it has an ambitious name, belongs to a smart-city initiative, or is mentioned near UDT language.

#### Scenario: Artifact is a platform

- **WHEN** an artifact is presented as a usable city-scale UDT system
- **THEN** entity discovery classifies it as `Type = platform`

### Requirement: Framework Type means reusable enabling structure

An artifact SHALL be classified as `framework` when it is mainly presented as an SDK, API-centered backbone, reusable architecture, toolkit, reference model, or enabling layer for building UDT systems rather than as the primary end-user platform.

#### Scenario: Artifact is a framework

- **WHEN** an artifact is mainly a reusable architecture or enabling layer
- **THEN** entity discovery classifies it as `Type = framework`

### Requirement: Module Type means bounded capability component

An artifact SHALL be classified as `module` when it mainly provides one bounded capability, domain workflow, analytical function, data pipeline, visualization component, simulator, or integration component for use inside or alongside a broader UDT stack.

#### Scenario: Artifact is a module

- **WHEN** an artifact mainly provides one bounded UDT capability
- **THEN** entity discovery classifies it as `Type = module`

### Requirement: Initiative Type means real-world UDT activity

An entity SHALL be classified as `initiative` when it is mainly presented as a project, programme, deployment, implementation effort, institutional initiative, pilot, or real-world activity related to Urban Digital Twins, and the primary entity being represented is not a distinct technical artifact.

An initiative SHALL NOT be classified as `platform`, `framework`, or `module` only because it uses, funds, deploys, or discusses a technical artifact.

Initiatives SHALL record their technical substrate separately when it is clear.

When the technical substrate is unclear, discovery SHALL preserve uncertainty with `Uses = ?` or equivalent artifact-detail uncertainty.

#### Scenario: Candidate is an initiative

- **WHEN** a candidate is a project, programme, deployment, implementation effort, institutional initiative, or pilot related to Urban Digital Twins
- **THEN** entity discovery assigns `Type = initiative`

#### Scenario: Initiative uses a known artifact

- **WHEN** an initiative clearly uses a known technical artifact
- **THEN** initiative discovery records that artifact as the initiative's technical substrate
- **THEN** the initiative remains `Type = initiative`

#### Scenario: Initiative substrate is unclear

- **WHEN** an initiative is relevant but its platform or technical artifact cannot be identified
- **THEN** initiative discovery records `Uses = ?`

### Requirement: Excluded Type means outside discovery boundary

An entity SHALL be classified as `excluded` when it is not a technical UDT artifact, is not a UDT initiative, or falls outside the study boundary.

Communication tools, presentation tools, narrative mapping tools, and lightweight web-map storytelling tools SHALL be classified as `excluded` unless they expose a distinct technical artifact that satisfies `platform`, `framework`, or `module` criteria or are part of a UDT initiative that satisfies `initiative` criteria.

#### Scenario: Candidate is excluded

- **WHEN** a candidate is outside both the technical artifact boundary and the initiative boundary
- **THEN** entity discovery assigns `Type = excluded`

#### Scenario: Communication or narrative publishing tool is outside scope

- **WHEN** a tool mainly supports communication, presentation, map-based storytelling, or narrative publishing rather than UDT modeling, simulation, integration, or operational use
- **THEN** entity discovery classifies it as `Type = excluded`
- **THEN** the exclusion reason explains that it is outside the technical UDT artifact and UDT initiative boundary

### Requirement: Borderline entities use deterministic tie-breaks

Discovery SHALL classify by observable presentation and role in the UDT ecosystem, not by name alone.

When a candidate resembles multiple entity categories, discovery SHALL apply this order:

1. `platform` when a distinct artifact is presented as a usable or deployable city-scale UDT system.
2. `framework` when a distinct artifact is mainly presented as a reusable architecture, toolkit, API backbone, SDK, reference model, or enabling layer.
3. `module` when a distinct artifact is mainly presented as a bounded capability or component.
4. `initiative` when the primary entity is a project, programme, deployment, implementation effort, institutional initiative, or pilot rather than a separable technical artifact.
5. `excluded` when outside the study boundary.

When an initiative and a technical artifact are both present, discovery SHALL separate the initiative from the artifact when the evidence supports treating them as distinct entities.

#### Scenario: Entity resembles initiative and platform

- **WHEN** a candidate is a programme that exposes a distinct usable city-scale UDT system
- **THEN** the technical artifact is eligible for `Type = platform`
- **THEN** the programme is eligible for `Type = initiative`

#### Scenario: Entity resembles platform and framework

- **WHEN** an artifact exposes APIs but is presented as a usable city-scale UDT system
- **THEN** entity discovery classifies it as `Type = platform`

### Requirement: Weak evidence preserves uncertainty

Discovery SHALL use the strongest observable evidence available.

When evidence is weak or ambiguous, discovery SHALL choose the best supported allowed `Type` and preserve uncertainty in the reason, substrate, or artifact details.

Discovery SHALL NOT introduce ad hoc output `Type` values such as `unknown`, `tool`, or `system`.

#### Scenario: Evidence is ambiguous

- **WHEN** the technical role or initiative substrate of a candidate is unclear
- **THEN** discovery uses the strongest observable evidence
- **THEN** discovery assigns the best supported allowed `Type`
- **THEN** discovery makes the uncertainty visible

#### Scenario: Candidate type is uncertain

- **WHEN** a candidate appears relevant but the evidence does not clearly support one classification
- **THEN** discovery assigns one of `platform`, `framework`, `module`, `initiative`, or `excluded`
- **THEN** discovery explains the uncertainty instead of creating a new `Type`

# openspec/specs/observe-entity-discovery/spec.md

# Spec: observe-entity-discovery

## Purpose

Defines the observed output contract for unified entity discovery.

## Requirements

### Requirement: Entity discovery observations use the governed response contract

Saved entity discovery web responses SHALL use filenames matching `observe/entity-discovery-<model-short>.md`.

Each saved entity discovery response SHALL begin with a fenced YAML metadata block containing `model`, `date`, and `prompt: entity-discovery`.

Each saved entity discovery response SHALL include a coverage statement before the summary table.

The coverage statement SHALL report total candidate count and counts by `Type`.

The coverage statement SHALL state whether discovery coverage targets were met.

When coverage targets were not met, the coverage statement SHALL identify the unmet targets and explain the search or evidence limitation.

Each saved entity discovery response SHALL include a summary table with exactly these columns in this order:

- `Name`
- `Type`
- `Link`

Each entity discovery row SHALL assign exactly one `Type` value: `platform`, `framework`, `module`, `initiative`, or `excluded`.

The summary table SHALL NOT include `Uses`, `Reason`, `Description`, `EntityKind`, or other detail columns.

Each saved entity discovery response SHALL include one `##` section per entity.

Each entity section SHALL include a concise paragraph describing what the entity is, why the assigned `Type` fits, and any uncertainty.

For initiative rows, the entity paragraph SHALL identify known technical substrate with `Uses: <artifact names>` when clear, or `Uses: ?` when unclear.

For excluded rows, the entity paragraph SHALL explain the exclusion reason.

#### Scenario: Researcher saves entity discovery output

- **WHEN** a researcher saves an entity discovery web response
- **THEN** the response follows the metadata, coverage statement, table, Type, and entity section contract

#### Scenario: Summary table is rendered

- **WHEN** an entity discovery response renders its summary table
- **THEN** the table columns are exactly `Name`, `Type`, and `Link`
- **THEN** `Link` is the final column
- **THEN** `Uses` and `Reason` are not table columns

#### Scenario: Initiative uses a known artifact

- **WHEN** an entity discovery response includes an initiative whose technical substrate is known
- **THEN** the initiative row uses `Type = initiative`
- **THEN** the initiative section records `Uses: <artifact names>` in prose

#### Scenario: Initiative substrate is unclear

- **WHEN** an entity discovery response includes an initiative whose technical substrate cannot be identified
- **THEN** the initiative row uses `Type = initiative`
- **THEN** the initiative section records `Uses: ?` in prose

#### Scenario: Excluded entity is reported

- **WHEN** an entity discovery response includes an excluded boundary candidate
- **THEN** the entity row uses `Type = excluded`
- **THEN** the entity section explains the exclusion reason in prose

# openspec/specs/observe-markdown-output-format/spec.md

# Spec: observe-markdown-output-format

## Purpose

Defines the shared Markdown formatting contract for governed Markdown outputs.

## Requirements

### Requirement: Governed prompts define portable Markdown output

Each governed prompt template file in the live repository that instructs an AI model to emit Markdown output SHALL make `observe-markdown-output-format` available to the model either by declaring it as a required contract or by rendering equivalent rules into the resolved prompt.

Canonical web prompt templates that conform to `act-web-prompt-template` SHALL declare `openspec/specs/observe-markdown-output-format/spec.md` under `## Required Contracts`.

This shared contract SHALL apply to governed Markdown outputs that explicitly rely on it, including current outputs produced from prompts such as `act/entity-discovery.md` and `act/platform-comparison.md`.

The `act-web-prompt-template` contract SHALL reuse this shared Markdown output formatting contract rather than duplicating it.

#### Scenario: Contributor reviews a governed prompt template

- **WHEN** a contributor opens a governed prompt template that emits Markdown
- **THEN** the prompt declares or renders the shared Markdown output formatting rules
- **THEN** any shared web prompt structure requirements reference this contract instead of duplicating the formatting rules

### Requirement: Markdown output uses portable syntax

Markdown output produced by governed prompts SHALL render correctly in standard Markdown viewers such as GitHub, VS Code, Obsidian, and Typora.

The output SHALL use only these Markdown constructs:

- ATX headings: `#`, `##`, `###`, `####`
- emphasis: `**bold**`, `_italic_`
- inline links: `[text](url)`
- unordered lists using `-`
- ordered lists using `1.`
- GFM pipe tables
- fenced code blocks using triple backticks

When a governed output includes a link, the link SHALL use Markdown inline-link syntax with a real URL target, such as `[Official page](https://example.com)`.

#### Scenario: Model emits governed Markdown

- **WHEN** a model produces Markdown from a governed prompt
- **THEN** it uses only the permitted portable Markdown constructs
- **THEN** links use Markdown inline-link syntax with real URL targets

### Requirement: Markdown output excludes non-portable and AI-specific artifacts

Markdown output produced by governed prompts SHALL NOT include non-portable Markdown extensions, raw HTML, product-native source handles, or AI-product-specific citation artifacts.

The output SHALL NOT include:

- custom containers such as `:::`, `!!!`, `> [!NOTE]`, or `> [!WARNING]`
- extended syntax such as `==highlight==`, `^superscript^`, or `~subscript~`
- raw HTML
- numeric citations such as `[1]`
- footnotes such as `[^1]`
- AI-specific source markers such as `【†source】`
- product-native citation handles such as `citeturn11view6`
- product-native URL handles such as `urlOfficial pageturn8search14`
- opaque search or view handles such as `turn8search14`, `turn11view6`, or similar non-URL source identifiers
- source handles that cannot be resolved by a standard Markdown viewer
- extra methodology sections, source appendices, closing summaries, or other sections outside the relevant output contract

#### Scenario: Model output is saved to the repository

- **WHEN** a governed prompt response is saved as Markdown
- **THEN** it has no non-portable syntax, product-native source handles, or AI-product-specific artifacts

### Requirement: Markdown output preserves output-contract structure

Markdown formatting rules SHALL NOT override the relevant observe output contract.

When the observe output contract requires specific metadata blocks, tables, columns, headings, allowed values, or section order, the output SHALL preserve those requirements exactly.

The output SHALL leave a blank line before and after every heading, table, and fenced code block.

#### Scenario: Formatting and output contract both apply

- **WHEN** a governed prompt has both Markdown formatting rules and an observe output contract
- **THEN** the observe output contract determines the required structure
- **THEN** the Markdown formatting rules determine the portable syntax used to render that structure

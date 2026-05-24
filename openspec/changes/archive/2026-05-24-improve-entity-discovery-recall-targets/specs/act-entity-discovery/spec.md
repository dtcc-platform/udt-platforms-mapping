## MODIFIED Requirements

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

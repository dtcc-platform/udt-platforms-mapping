## MODIFIED Requirements

### Requirement: Platform discovery uses explicit recall coverage targets

Platform discovery SHALL treat the action as candidate discovery across `platform`, `framework`, `module`, and useful `excluded` boundary candidates.

Platform discovery SHALL return at least 40 candidate artifacts when enough evidence is available.

Platform discovery SHALL include at least:

- 10 artifacts classified as `platform`
- 15 artifacts classified as `framework`
- 10 artifacts classified as `module`
- 5 artifacts classified as `excluded`

Platform discovery SHALL use these quotas as minimum quality gates, not as stopping conditions.

Meeting the minimum count SHALL NOT be considered sufficient when additional high-relevance candidates are discoverable.

After reaching the quota, platform discovery SHALL perform at least one additional targeted recall pass for regional, academic, open-source, and research-center UDT platforms.

Platform discovery SHALL NOT stop after representative examples when additional relevant candidates are discoverable.

Platform discovery SHALL prefer replacing weaker candidates with stronger candidates when the stronger candidates have clearer evidence and a better fit to `platform-definition`.

Platform discovery SHALL NOT fabricate candidates or include unsupported candidates only to satisfy a quota.

When a coverage target cannot be met after reasonable search, platform discovery SHALL state which target was not met and why.

#### Scenario: Discovery has enough evidence

- **WHEN** enough relevant evidence is available for the target categories
- **THEN** platform discovery returns at least 40 candidate artifacts
- **THEN** platform discovery satisfies the platform, framework, module, and excluded category targets
- **THEN** platform discovery performs at least one additional targeted recall pass after meeting the quotas

#### Scenario: Discovery cannot meet a target

- **WHEN** a target cannot be met without weak or unsupported evidence
- **THEN** platform discovery does not fabricate candidates
- **THEN** platform discovery reports the unmet target and the reason it was not met

#### Scenario: Quota has been met but stronger candidates remain discoverable

- **WHEN** platform discovery has already met the minimum quotas
- **AND** an additional high-relevance candidate is discoverable with stronger evidence than a weaker included candidate
- **THEN** platform discovery does not treat the quota as sufficient
- **THEN** platform discovery includes the stronger candidate or replaces the weaker candidate

### Requirement: Platform discovery samples adjacent seed-list families

Platform discovery SHALL search and sample candidates from at least three adjacent seed-list families.

The adjacent seed-list families SHALL include:

- frontend GIS and web mapping
- 3D geospatial visualization and 3D Tiles
- point-cloud, LiDAR, and city-model visualization

Platform discovery SHALL extract multiple relevant candidate artifacts from each sampled seed-list family when relevant candidates are available.

Platform discovery SHALL classify every included seed-list candidate using `platform-definition`.

Platform discovery SHALL NOT treat seed-list presence as sufficient evidence that an artifact is a `platform`.

#### Scenario: Seed-list candidates are available

- **WHEN** platform discovery finds relevant candidates in adjacent seed-list families
- **THEN** it samples from at least three seed-list families
- **THEN** it includes multiple relevant candidates from each sampled family when available
- **THEN** it classifies each included candidate using `platform-definition`

### Requirement: Platform discovery separates recall from later filtering

Platform discovery SHALL include relevant `framework`, `module`, and `excluded` candidates discovered during recall expansion even when they are not eligible for later platform comparison.

Platform discovery SHALL treat later platform comparison filtering as a separate action governed by the platform comparison contract.

#### Scenario: Non-platform candidate is discovered

- **WHEN** platform discovery finds a relevant framework, module, or boundary candidate
- **THEN** it includes the candidate in discovery output with the correct `Type`
- **THEN** it does not remove the candidate only because later platform comparison accepts only `platform` artifacts

## ADDED Requirements

### Requirement: Platform discovery targets regional and research-center platform recall

The post-quota targeted recall pass SHALL search for regional, academic, open-source, and research-center UDT platforms using institution, centre, lab, and project-specific terminology.

The targeted recall pass SHALL include search terms for `digital twin cities centre`, `urban digital twin research platform`, `open-source city digital twin platform`, `academic city digital twin platform`, and regional spellings or organization names when known.

When a candidate has an ambiguous or overloaded name, platform discovery SHALL include disambiguating terms from its institution, centre, region, or project context.

#### Scenario: DTCC Platform-style candidate is discoverable

- **WHEN** a regional academic platform is presented as an open-source platform for digital twinning of cities by a research centre
- **AND** generic global platform searches may miss it because the name is ambiguous or region-specific
- **THEN** platform discovery searches disambiguating terms such as `Digital Twin Cities Centre`, `Chalmers`, and `dtcc platform`
- **THEN** platform discovery includes the candidate when evidence satisfies `platform-definition`

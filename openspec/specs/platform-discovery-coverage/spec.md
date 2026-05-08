# Spec: platform-discovery-coverage

## Purpose

Defines recall coverage targets, category quotas, seed-list sampling rules, and non-exhaustive stopping behavior for platform discovery.

## Requirements

### Requirement: Platform discovery uses explicit recall coverage targets

Platform discovery SHALL treat the action as candidate discovery across `platform`, `framework`, `module`, and useful `excluded` boundary candidates.

Platform discovery SHALL return at least 40 candidate artifacts when enough evidence is available.

Platform discovery SHALL include at least:

- 10 artifacts classified as `platform`
- 15 artifacts classified as `framework`
- 10 artifacts classified as `module`
- 5 artifacts classified as `excluded`

Platform discovery SHALL NOT stop after representative examples when additional relevant candidates are discoverable.

Platform discovery SHALL NOT fabricate candidates or include unsupported candidates only to satisfy a quota.

When a coverage target cannot be met after reasonable search, platform discovery SHALL state which target was not met and why.

#### Scenario: Discovery has enough evidence

- **WHEN** enough relevant evidence is available for the target categories
- **THEN** platform discovery returns at least 40 candidate artifacts
- **THEN** platform discovery satisfies the platform, framework, module, and excluded category targets

#### Scenario: Discovery cannot meet a target

- **WHEN** a target cannot be met without weak or unsupported evidence
- **THEN** platform discovery does not fabricate candidates
- **THEN** platform discovery reports the unmet target and the reason it was not met

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

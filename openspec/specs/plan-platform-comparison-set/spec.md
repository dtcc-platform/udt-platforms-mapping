# Spec: plan-platform-comparison-set

## Purpose

Defines this researcher-facing canonical artifact.

## Requirements

### Requirement: Platform comparison set contains selected comparison candidates

The repository SHALL contain `plan/platform-comparison-set.md` as the selected platform comparison set.

Each data row SHALL represent one selected row that already qualifies as `Type = platform` from platform discovery.

The comparison prompt SHALL treat the rows in `plan/platform-comparison-set.md` as the complete and authoritative set of platforms to compare.

#### Scenario: Researcher opens platform comparison set

- **WHEN** a researcher opens `plan/platform-comparison-set.md`
- **THEN** the file is available as the selected platform comparison input
- **THEN** the comparison prompt treats it as authoritative comparison scope

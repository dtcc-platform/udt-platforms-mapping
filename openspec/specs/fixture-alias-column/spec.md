## Purpose

Defines the rules for the `Aliases` column in fixture gap-category tables (`evals/discovery/benchmark.md`). The Aliases column allows the eval prompt to match platforms by known variant names, eliminating false negatives caused by a model using an alternative name for a platform instead of the canonical one.

## Requirements

### Requirement: Fixture tables include an optional Aliases column for known name variants

Each gap-category table in `evals/discovery/benchmark.md` SHALL include an `Aliases` column as its last column. The column header SHALL be exactly `Aliases`.

For each platform row, the `Aliases` cell SHALL contain either:
- A comma-separated list of one or more alternative names by which the platform may appear in a discovery response summary table (e.g., `CityEnergyAnalyst, CEA`), OR
- An empty cell, indicating no known aliases

Aliases SHALL be specific enough to identify the platform unambiguously. Generic terms (e.g., "City", "Platform") SHALL NOT be used as aliases.

The `Aliases` column is maintained by researchers: when a model is found to use a variant name that caused a false negative, the researcher adds that variant as an alias in the corresponding fixture row.

#### Scenario: Researcher records a variant name discovered during eval review

- **WHEN** a researcher reviews a coverage report and notices a model used "CityEnergyAnalyst" while the fixture has "City Energy Analyst", causing a false negative
- **THEN** the researcher adds `CityEnergyAnalyst` to the `Aliases` cell for that platform row in `evals/discovery/benchmark.md`

#### Scenario: Platform has no known aliases

- **WHEN** a platform has no observed name variants
- **THEN** its `Aliases` cell is empty and the eval matches only against the canonical `Name`

#### Scenario: Platform has multiple aliases

- **WHEN** a platform's `Aliases` cell contains `CityEnergyAnalyst, CEA`
- **THEN** the eval treats both `CityEnergyAnalyst` and `CEA` as valid match targets in addition to the canonical name

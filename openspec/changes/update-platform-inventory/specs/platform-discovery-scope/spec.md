## ADDED Requirements

### Requirement: Scope document states formal exclusion criteria

The scope document SHALL define formal exclusion criteria that mirror the three inclusion criteria in structure. There SHALL be exactly three named exclusion criteria: **Spec or Standard**, **Single Domain**, and **General Purpose**.

Each exclusion criterion SHALL include:
- A name
- A one-sentence definition stating why platforms in this category fall outside the UDT scope boundary
- At least one named example platform

#### Scenario: Researcher assesses a standards body

- **WHEN** a researcher encounters a platform or project that primarily defines or maintains a specification or standard (e.g., CityGML, OGC SensorThings)
- **THEN** the scope document's exclusion criteria identify it as **Spec or Standard** and explain it is excluded unless it also ships a runtime implementation

#### Scenario: Researcher assesses a single-domain tool

- **WHEN** a researcher encounters a tool that operates in only one urban domain (e.g., building energy simulation, traffic modelling only)
- **THEN** the scope document's exclusion criteria identify it as **Single Domain** and explain it is excluded unless multi-domain integration is a stated goal

#### Scenario: Researcher assesses a general-purpose platform

- **WHEN** a researcher encounters a general-purpose IoT platform, cloud data platform, or GIS tool with no urban twin framing
- **THEN** the scope document's exclusion criteria identify it as **General Purpose** and explain it is excluded unless the platform explicitly frames itself for urban or city-scale twin use cases

### Requirement: Exclusion criterion labels match discovery prompt output

The three exclusion criterion names defined in the scope document SHALL match exactly the labels used in the `Criterion` column of discovery response summary tables: `Spec or Standard`, `Single Domain`, `General Purpose`.

#### Scenario: Researcher checks an exclusion label in a discovery response

- **WHEN** a researcher sees an exclusion criterion label in a discovery summary table
- **THEN** they can look up the exact same label in `docs/01-scope.md` to read its definition and examples

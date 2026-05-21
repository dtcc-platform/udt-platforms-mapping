# Spec: plan-platform-comparison-rubric

## Purpose

Defines platform comparison dimensions and scoring behavior.

## Requirements

### Requirement: Platform comparison scores governed dimensions

Platform comparison SHALL evaluate selected platforms using the governed dimensions `Arch`, `Open`, `City`, `Mature`, `Integ`, `Gov`, `Viz`, `DM`, `Sim`, `IoT`, `Std`, and `Infra`.

Each scored dimension SHALL use a 1-5 scale unless the evidence is insufficient.

When evidence is insufficient, platform comparison SHALL use `?`.

#### Scenario: Platform is scored

- **WHEN** platform comparison evaluates a selected platform
- **THEN** each governed dimension receives a score from 1 to 5 or `?`

### Requirement: Core research dimensions define platform-level qualities

Platform comparison SHALL score core research dimensions using these meanings:

| Dimension | Meaning                                                                                               |
| --------- | ----------------------------------------------------------------------------------------------------- |
| `Arch`    | Technical architecture, data models, component structure, deployment model, and scalability           |
| `Open`    | Source availability, license type, contribution model, commercial restrictions, and open data formats |
| `City`    | Urban domains covered, geographic extent, multi-domain analytics, and city-scale capability           |
| `Mature`  | Development status, known deployments, release cadence, and community activity                        |
| `Integ`   | APIs, plugin ecosystem, data exchange standards, and interoperability                                 |
| `Gov`     | Roadmap control, contribution model, transparency, and funding model                                  |

#### Scenario: Core dimensions are evaluated

- **WHEN** platform comparison evaluates a selected platform
- **THEN** it evaluates each core research dimension according to the governed meaning

### Requirement: Functional dimensions define capability-level qualities

Platform comparison SHALL score functional dimensions using these meanings:

| Dimension | Meaning                                                                         |
| --------- | ------------------------------------------------------------------------------- |
| `Viz`     | 3D rendering, GIS viewers, scene composition, and visual output quality         |
| `DM`      | Data ingestion, storage, twin models, semantic layers, and data lifecycle       |
| `Sim`     | Urban simulation, physics, scenario modelling, and what-if analysis             |
| `IoT`     | Real-time data, sensor integration, device management, and stream processing    |
| `Std`     | Open standards implementation or standards governance role                      |
| `Infra`   | Built environment, BIM/GIS integration, and infrastructure lifecycle management |

#### Scenario: Functional dimensions are evaluated

- **WHEN** platform comparison evaluates a selected platform
- **THEN** it evaluates each functional dimension according to the governed meaning

### Requirement: Scoring uses rubric-defined evidence expectations

Platform comparison SHALL assign higher scores only when evidence supports stronger capability, openness, maturity, governance, interoperability, or functional depth for the relevant dimension.

Platform comparison SHALL NOT assign high scores based only on marketing claims or unsupported assertions.

#### Scenario: Evidence is weak

- **WHEN** a platform has only unsupported marketing claims for a dimension
- **THEN** platform comparison does not assign a high score for that dimension

### Requirement: Comparison scope remains platform-only

Platform comparison SHALL compare only artifacts classified as `platform`.

Platform comparison SHALL NOT broaden the selected comparison set to frameworks, modules, initiatives, or unrelated smart-city projects.

#### Scenario: Non-platform appears in comparison input

- **WHEN** a comparison input includes an artifact that is not classified as `platform`
- **THEN** platform comparison does not treat it as an eligible platform comparison target

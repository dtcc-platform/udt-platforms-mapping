# UDT Ecosystem Comparison — Dimension Scoring Rubrics

This file defines the dimension scoring rubrics used in the **comparison phase** of the UDT ecosystem mapping study.
Rating runs consume this file through the prompt's declared required inputs in CLI mode, or inline it automatically in Web mode.

---

## Research Dimensions

Score each platform 1–5 per dimension using the rubrics below. Use `?` when a dimension cannot be assessed.

### 1. Technical Architecture (`Arch`)

Core technology stack, data models (CityGML, IFC, OGC standards, proprietary), component structure, deployment model, scalability approach.

| Score | Criteria                                                                       |
| ----- | ------------------------------------------------------------------------------ |
| 5     | Fully modular, open standards (CityGML/IFC/OGC), cloud-native or self-hostable |
| 4     | Mostly modular, supports open standards with some proprietary layers           |
| 3     | Mixed architecture, partial standards support                                  |
| 2     | Largely monolithic, limited open standards                                     |
| 1     | Monolithic with proprietary data model, no open standards                      |

### 2. Openness & Licensing (`Open`)

Source availability, license type, contribution model, commercial restrictions, dual licensing, open data formats.

| Score | Criteria                                                                                                                                                                    |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 5     | Permissive open-source (MIT/Apache/BSD) + open data formats (OGC standards, CityGML, IFC, or equivalent), no SaaS dependency                                                |
| 4     | Copyleft open-source (strong: GPL — derivatives must be open; weak: LGPL/MPL — linking permitted without triggering copyleft), or open-core with substantial open component |
| 3     | Open-core with significant proprietary features, or open source with restrictive data formats (proprietary export formats with no open standard alternative)                |
| 2     | Primarily proprietary with limited open components or open APIs                                                                                                             |
| 1     | Fully proprietary, no public source, no open APIs                                                                                                                           |

### 3. City-Scale Capability (`City`)

Urban domains covered (buildings, infrastructure, mobility, energy, climate, water, noise), geographic extent, multi-domain analytics, real-time vs. batch.

| Score | Criteria                                                         |
| ----- | ---------------------------------------------------------------- |
| 5     | Comprehensive multi-domain urban coverage at full city scale     |
| 4     | Multi-domain coverage, strong city-scale support with minor gaps |
| 3     | Several domains covered, city-scale with notable limitations     |
| 2     | Limited domains or district/building scale only                  |
| 1     | Single narrow domain or sub-city scale                           |

### 4. Maturity & Adoption (`Mature`)

Development status, known city deployments (name cities if possible), release cadence, community activity.

| Score | Criteria                                                            |
| ----- | ------------------------------------------------------------------- |
| 5     | Production-grade, multiple named city deployments, active community |
| 4     | Production-ready, some city deployments or pilots, regular releases |
| 3     | Stable but limited deployments, moderate activity                   |
| 2     | Prototype or early production, few or no known deployments          |
| 1     | Concept or prototype, no known deployments                          |

### 5. Integration Posture (`Integ`)

Public APIs (REST, GraphQL, gRPC), plugin/extension ecosystem, data exchange standards, interoperability with other tools.

| Score | Criteria                                                                    |
| ----- | --------------------------------------------------------------------------- |
| 5     | Rich public APIs, active plugin ecosystem, easy to compose with other tools |
| 4     | Good APIs, some ecosystem, OGC-compliant interfaces                         |
| 3     | Basic APIs, limited ecosystem, some interoperability                        |
| 2     | Minimal public APIs, closed or limited integration                          |
| 1     | Closed system, no public APIs                                               |

### 6. Governance Model (`Gov`)

Who controls the roadmap (vendor, consortium, community, research institution), contribution model, funding model.

| Score | Criteria                                                                              |
| ----- | ------------------------------------------------------------------------------------- |
| 5     | Open consortium or community governance, transparent decision-making, diverse funding |
| 4     | Academic or public institution governance with open contribution                      |
| 3     | Mixed governance, some community input                                                |
| 2     | Single organisation control with limited community input                              |
| 1     | Single corporate control, no community input                                          |

---

## Functional Categories

Score each platform 1–5 per functional category using the rubrics below. Use `?` when a category cannot be assessed.

### 7. Visualization (`Viz`)

Primary function: 3D rendering, GIS viewers, scene composition, visual output quality.

| Score | Criteria                                                                                                |
| ----- | ------------------------------------------------------------------------------------------------------- |
| 5     | Purpose-built 3D visualization engine or viewer; primary purpose; real-time or near-real-time rendering |
| 4     | Strong visualization capabilities; core feature set with significant investment                         |
| 3     | Visualization present and useful but not the primary strength                                           |
| 2     | Basic or incidental visualization (e.g., simple 2D map view, no 3D)                                     |
| 1     | No meaningful visualization capability                                                                  |

### 8. Data Management (`DM`)

Primary function: data ingestion, storage, twin models, semantic layers, data lifecycle.

| Score | Criteria                                                                                                  |
| ----- | --------------------------------------------------------------------------------------------------------- |
| 5     | Purpose-built for city-scale data storage and management; semantic model, versioning, full data lifecycle |
| 4     | Strong data management with semantic modelling or graph; multi-source ingestion                           |
| 3     | Solid data management but limited semantic layer or scalability                                           |
| 2     | Basic storage or data exchange; limited query or model capabilities                                       |
| 1     | No meaningful data management role                                                                        |

### 9. Simulation (`Sim`)

Primary function: urban simulation, physics, scenario modelling, what-if analysis.

| Score | Criteria                                                                                       |
| ----- | ---------------------------------------------------------------------------------------------- |
| 5     | Purpose-built simulation engine; multi-domain urban physics, scenario comparison at city scale |
| 4     | Strong simulation support across multiple urban domains                                        |
| 3     | Simulation present for one or two domains; limited scenario tooling                            |
| 2     | Basic scenario comparison or single-variable simulation                                        |
| 1     | No simulation capability                                                                       |

### 10. IoT Sensing (`IoT`)

Primary function: real-time data, sensor integration, device management, stream processing.

| Score | Criteria                                                                                     |
| ----- | -------------------------------------------------------------------------------------------- |
| 5     | Purpose-built IoT platform; real-time ingestion, device registry, stream processing at scale |
| 4     | Strong IoT support; real-time APIs, sensor integration, stream handling                      |
| 3     | Connects to sensors but limited real-time processing                                         |
| 2     | Basic real-time data hookup; manual or batch sensor feeds                                    |
| 1     | No IoT or real-time sensing capability                                                       |

### 11. Standards (`Std`)

Primary function: implementing or defining open standards, interoperability frameworks.

| Score | Criteria                                                                                                      |
| ----- | ------------------------------------------------------------------------------------------------------------- |
| 5     | Primary purpose is defining or implementing open standards (OGC, ISO, W3C); governance role in standards body |
| 4     | Strong standards implementation; multiple OGC/ISO standards as native data models                             |
| 3     | Partial standards support; some open standards alongside proprietary models                                   |
| 2     | Limited standards; primarily proprietary with token open format support                                       |
| 1     | No meaningful open standards implementation                                                                   |

### 12. Infrastructure (`Infra`)

Primary function: built environment, BIM/GIS integration, infrastructure lifecycle management.

| Score | Criteria                                                                                     |
| ----- | -------------------------------------------------------------------------------------------- |
| 5     | Purpose-built for infrastructure or BIM lifecycle; IFC, asset management, lifecycle tracking |
| 4     | Strong infrastructure support; BIM integration, asset management, or civil engineering focus |
| 3     | Infrastructure is one of several domains; partial BIM/GIS support                            |
| 2     | Limited infrastructure scope; building-level only or minimal lifecycle management            |
| 1     | No meaningful infrastructure or built environment focus                                      |

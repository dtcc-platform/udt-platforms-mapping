# Platform Scope and Scoring Rubrics

This file defines the relevance boundary for the UDT platform review and contains all scoring rubrics used during discovery and comparison sessions.
Paste the full content of this file into the `[PASTE_SCOPE_HERE]` slot in any prompt before running a session.

---

## What Is a UDT Platform?

A **Urban Digital Twin (UDT) platform** is a software system for representing, managing, simulating, or visualising city-scale urban environments as a live or near-live digital counterpart.
Search broadly: the boundary includes enabling layers and infrastructure twins — device twin frameworks, BIM engines, urban simulation layers, city-scale geospatial stores — as well as full UDT platforms. Use the Relevance rubric below to score and filter candidates after discovery.

---

## Relevance Rubric

Score each platform 0–5 to express its relevance to city-scale Urban Digital Twin use cases.

| Score | Criteria                                                                                                                                                                                                     |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 5     | **Explicit UDT** — the platform's own official documentation, product page, or repository uses the term "digital twin" in an urban or city-scale context                                                     |
| 4     | **City-Scale Capabilities** — purpose-built for city-scale 3D visualisation, urban simulation, large-scale geospatial data management, or multi-domain urban analytics; no explicit UDT framing required     |
| 3     | **Adjacent Architecture** — a foundational building block commonly and directly integrated into UDT systems (open standards implementations, enabling visualisation engines, infrastructure twin frameworks) |
| 2     | **Marginal** — tangential relevance; could contribute to a UDT but not designed for it and not commonly used in that context                                                                                 |
| 1     | **Out of scope** — assessed and found outside the study boundary (single domain, general purpose, or spec/standard only)                                                                                     |
| 0     | **Not assessed** — platform has not been evaluated against the rubric                                                                                                                                        |

**Seed list calibration:**

| Platform                          | Relevance | Notes                                                                       |
| --------------------------------- | --------- | --------------------------------------------------------------------------- |
| DTCC (Digital Twin Cities Centre) | 5         | Academic–municipal UDT; explicit digital twin positioning                   |
| Virtual Singapore                 | 5         | National city-scale digital twin programme                                  |
| Cesium                            | 3         | 3D geospatial visualisation engine; widely used as UDT rendering layer      |
| 3D City DB                        | 4         | Open-source city model database (CityGML); city-scale geospatial management |
| FIWARE Orion Context Broker       | 4         | Context data management; deployed in multiple smart city / UDT projects     |
| iTwin                             | 3         | Infrastructure digital twin framework; explicit UDT integration positioning |
| Eclipse Ditto                     | 3         | IoT device twin framework; used as the device layer in UDT architectures    |

**Target corpus:** 15–30 platforms (planning heuristic, not a hard constraint).

---

## Research Dimensions

Score each platform 0–5 per dimension using the rubrics below. Use `0` when a dimension has not been assessed at this phase.

### 1. Technical Architecture (`Arch`)

Core technology stack, data models (CityGML, IFC, OGC standards, proprietary), component structure, deployment model, scalability approach.

| Score | Criteria                                                                       |
| ----- | ------------------------------------------------------------------------------ |
| 5     | Fully modular, open standards (CityGML/IFC/OGC), cloud-native or self-hostable |
| 4     | Mostly modular, supports open standards with some proprietary layers           |
| 3     | Mixed architecture, partial standards support                                  |
| 2     | Largely monolithic, limited open standards                                     |
| 1     | Monolithic with proprietary data model, no open standards                      |
| 0     | Not assessed                                                                   |

### 2. Openness & Licensing (`Open`)

Source availability, license type, contribution model, commercial restrictions, dual licensing, open data formats.

| Score | Criteria                                                                                                                                                                    |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 5     | Permissive open-source (MIT/Apache/BSD) + open data formats (OGC standards, CityGML, IFC, or equivalent), no SaaS dependency                                                |
| 4     | Copyleft open-source (strong: GPL — derivatives must be open; weak: LGPL/MPL — linking permitted without triggering copyleft), or open-core with substantial open component |
| 3     | Open-core with significant proprietary features, or open source with restrictive data formats (proprietary export formats with no open standard alternative)                |
| 2     | Primarily proprietary with limited open components or open APIs                                                                                                             |
| 1     | Fully proprietary, no public source, no open APIs                                                                                                                           |
| 0     | Not assessed                                                                                                                                                                |

### 3. City-Scale Capability (`City`)

Urban domains covered (buildings, infrastructure, mobility, energy, climate, water, noise), geographic extent, multi-domain analytics, real-time vs. batch.

| Score | Criteria                                                         |
| ----- | ---------------------------------------------------------------- |
| 5     | Comprehensive multi-domain urban coverage at full city scale     |
| 4     | Multi-domain coverage, strong city-scale support with minor gaps |
| 3     | Several domains covered, city-scale with notable limitations     |
| 2     | Limited domains or district/building scale only                  |
| 1     | Single narrow domain or sub-city scale                           |
| 0     | Not assessed                                                     |

### 4. Maturity & Adoption (`Mature`)

Development status, known city deployments (name cities if possible), release cadence, community activity.

| Score | Criteria                                                            |
| ----- | ------------------------------------------------------------------- |
| 5     | Production-grade, multiple named city deployments, active community |
| 4     | Production-ready, some city deployments or pilots, regular releases |
| 3     | Stable but limited deployments, moderate activity                   |
| 2     | Prototype or early production, few or no known deployments          |
| 1     | Concept or prototype, no known deployments                          |
| 0     | Not assessed                                                        |

### 5. Integration Posture (`Integ`)

Public APIs (REST, GraphQL, gRPC), plugin/extension ecosystem, data exchange standards, interoperability with other tools.

| Score | Criteria                                                                    |
| ----- | --------------------------------------------------------------------------- |
| 5     | Rich public APIs, active plugin ecosystem, easy to compose with other tools |
| 4     | Good APIs, some ecosystem, OGC-compliant interfaces                         |
| 3     | Basic APIs, limited ecosystem, some interoperability                        |
| 2     | Minimal public APIs, closed or limited integration                          |
| 1     | Closed system, no public APIs                                               |
| 0     | Not assessed                                                                |

### 6. Governance Model (`Gov`)

Who controls the roadmap (vendor, consortium, community, research institution), contribution model, funding model.

| Score | Criteria                                                                              |
| ----- | ------------------------------------------------------------------------------------- |
| 5     | Open consortium or community governance, transparent decision-making, diverse funding |
| 4     | Academic or public institution governance with open contribution                      |
| 3     | Mixed governance, some community input                                                |
| 2     | Single organisation control with limited community input                              |
| 1     | Single corporate control, no community input                                          |
| 0     | Not assessed                                                                          |

---

## Functional Categories

Score each platform 0–5 per functional category using the rubrics below. Use `0` when a category has not been assessed at this phase.

### 7. Visualization (`Viz`)

Primary function: 3D rendering, GIS viewers, scene composition, visual output quality.

| Score | Criteria                                                                                                |
| ----- | ------------------------------------------------------------------------------------------------------- |
| 5     | Purpose-built 3D visualization engine or viewer; primary purpose; real-time or near-real-time rendering |
| 4     | Strong visualization capabilities; core feature set with significant investment                         |
| 3     | Visualization present and useful but not the primary strength                                           |
| 2     | Basic or incidental visualization (e.g., simple 2D map view, no 3D)                                     |
| 1     | No meaningful visualization capability                                                                  |
| 0     | Not assessed                                                                                            |

### 8. Data Management (`DM`)

Primary function: data ingestion, storage, twin models, semantic layers, data lifecycle.

| Score | Criteria                                                                                                  |
| ----- | --------------------------------------------------------------------------------------------------------- |
| 5     | Purpose-built for city-scale data storage and management; semantic model, versioning, full data lifecycle |
| 4     | Strong data management with semantic modelling or graph; multi-source ingestion                           |
| 3     | Solid data management but limited semantic layer or scalability                                           |
| 2     | Basic storage or data exchange; limited query or model capabilities                                       |
| 1     | No meaningful data management role                                                                        |
| 0     | Not assessed                                                                                              |

### 9. Simulation (`Sim`)

Primary function: urban simulation, physics, scenario modelling, what-if analysis.

| Score | Criteria                                                                                       |
| ----- | ---------------------------------------------------------------------------------------------- |
| 5     | Purpose-built simulation engine; multi-domain urban physics, scenario comparison at city scale |
| 4     | Strong simulation support across multiple urban domains                                        |
| 3     | Simulation present for one or two domains; limited scenario tooling                            |
| 2     | Basic scenario comparison or single-variable simulation                                        |
| 1     | No simulation capability                                                                       |
| 0     | Not assessed                                                                                   |

### 10. IoT Sensing (`IoT`)

Primary function: real-time data, sensor integration, device management, stream processing.

| Score | Criteria                                                                                     |
| ----- | -------------------------------------------------------------------------------------------- |
| 5     | Purpose-built IoT platform; real-time ingestion, device registry, stream processing at scale |
| 4     | Strong IoT support; real-time APIs, sensor integration, stream handling                      |
| 3     | Connects to sensors but limited real-time processing                                         |
| 2     | Basic real-time data hookup; manual or batch sensor feeds                                    |
| 1     | No IoT or real-time sensing capability                                                       |
| 0     | Not assessed                                                                                 |

### 11. Standards (`Std`)

Primary function: implementing or defining open standards, interoperability frameworks.

| Score | Criteria                                                                                                      |
| ----- | ------------------------------------------------------------------------------------------------------------- |
| 5     | Primary purpose is defining or implementing open standards (OGC, ISO, W3C); governance role in standards body |
| 4     | Strong standards implementation; multiple OGC/ISO standards as native data models                             |
| 3     | Partial standards support; some open standards alongside proprietary models                                   |
| 2     | Limited standards; primarily proprietary with token open format support                                       |
| 1     | No meaningful open standards implementation                                                                   |
| 0     | Not assessed                                                                                                  |

### 12. Infrastructure (`Infra`)

Primary function: built environment, BIM/GIS integration, infrastructure lifecycle management.

| Score | Criteria                                                                                     |
| ----- | -------------------------------------------------------------------------------------------- |
| 5     | Purpose-built for infrastructure or BIM lifecycle; IFC, asset management, lifecycle tracking |
| 4     | Strong infrastructure support; BIM integration, asset management, or civil engineering focus |
| 3     | Infrastructure is one of several domains; partial BIM/GIS support                            |
| 2     | Limited infrastructure scope; building-level only or minimal lifecycle management            |
| 1     | No meaningful infrastructure or built environment focus                                      |
| 0     | Not assessed                                                                                 |

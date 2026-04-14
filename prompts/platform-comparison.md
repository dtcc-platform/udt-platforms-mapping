# Platform Comparison Prompt

Use this prompt to produce a structured, evidence-based comparison of UDT platforms.

This prompt can be used in an AI web research chat or an AI CLI session. In a web chat, manually save the final Markdown response into `responses/`.

1. Open `docs/01-scope.md` and copy the full content
2. Replace `[PASTE_SCOPE_HERE]` below with the copied content
3. Open the discovery response file for your research session
4. Copy the rows you want to compare (including the header row) from the summary table — **include the DTCC row** so Part 3 landscape observations can orient around DTCC
5. Replace `[PASTE_SELECTED_PLATFORMS_HERE]` with those rows
6. Paste into your AI session starting from the cut-line below (the `> Paste into your AI session from this line onwards.` blockquote) — do not include these usage instructions above

> **Save response as:** `responses/<platform-a>-vs-<platform-b>-comparison.md` — e.g., `responses/cesium-vs-3dcitydb-comparison.md`. See `docs/02-methodology.md` for the full convention.

---

> Paste into your AI session from this line onwards.

## Prompt

Before you begin:

- If your interface supports Research or Deep Research, use it.
- Do your planning internally; do not show a research plan unless explicitly asked.
- Return plain Markdown only.
- Return only the final deliverable in the exact three-part format below.
- Do not add any product-native citation markers, sidebars, source appendices, methodology sections, executive summaries, or closing summaries.
- If your interface would normally produce a separate report structure, suppress it and follow this prompt's output contract instead.

You are a research assistant helping to map the Urban Digital Twin (UDT) platform landscape for DTCC.

Use primary sources for all final factual claims (**official websites, public repositories, published papers, official documentation**). For every substantive claim, include a source reference. Distinguish inferred claims from verified facts. If you cannot find information, state "unknown" or "unclear" — do not fabricate URLs, license names, or deployment claims.

**Before proceeding:** If the rubric block below still contains the literal text `[PASTE_SCOPE_HERE]`, stop and ask the user to paste `docs/01-scope.md` before continuing.

# Platform Scope and Scoring Rubrics

This file defines the relevance boundary for the UDT platform review and contains all scoring rubrics used during discovery and comparison sessions.
Paste the full content of this file into the `[PASTE_SCOPE_HERE]` slot in any prompt before running a session.

---

## What Is a UDT Platform?

A **Urban Digital Twin (UDT) platform** is a software system for representing, managing, simulating, or visualising city-scale urban environments as a live or near-live digital counterpart. This review applies a **moderate** inclusion boundary: platforms purely adjacent to UDT use cases (generic IoT platforms, general-purpose GIS tools without urban twin framing) are out of scope even if they could theoretically be used in a UDT context.

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

**Platforms to compare** (rows from the discovery summary table — the DTCC row must be included to enable Part 3 landscape observations):

**Before proceeding:** If the placeholder below still contains the literal text `[PASTE_SELECTED_PLATFORMS_HERE]`, stop and ask the user to supply the required data before continuing. Do not attempt to generate output without it.

Treat the pasted table as the comparison scope boundary. Do not add comparison candidates beyond the pasted rows unless the user explicitly asks you to expand scope. Treat the DTCC row from the pasted table as the reference platform for Part 3 landscape observations.

| Name                                              | Link                                                             | License                              | Type                                      | Relevance | Arch | Open | City | Mature | Integ | Gov | Viz | DM | Sim | IoT | Std | Infra |
| ------------------------------------------------- | ---------------------------------------------------------------- | ------------------------------------ | ----------------------------------------- | --------- | ---- | ---- | ---- | ------ | ----- | --- | --- | -- | --- | --- | --- | ----- |
| DTCC (Digital Twin Cities Centre)                 | https://dtcc.chalmers.se                                         | Apache-2.0                           | UDT research platform                     | 5         | 4    | 5    | 4    | 3      | 3     | 4   | 3   | 4  | 3   | 2   | 4   | 3     |
| Virtual Singapore                                 | https://www.nrf.gov.sg/programmes/virtual-singapore              | Proprietary (govt)                   | National city-scale digital twin          | 5         | 4    | 1    | 5    | 5      | 2     | 2   | 5   | 4  | 4   | 3   | 3   | 4     |
| Bentley iTwin Platform                            | https://www.bentley.com/software/itwin-platform/                 | Open-core / proprietary              | Infrastructure digital twin platform      | 5         | 4    | 2    | 4    | 5      | 4     | 2   | 4   | 4  | 4   | 3   | 4   | 5     |
| Esri ArcGIS Urban                                 | https://www.esri.com/en-us/arcgis/products/arcgis-urban/overview | Proprietary (SaaS)                   | Urban planning & city digital twin        | 5         | 3    | 1    | 5    | 5      | 4     | 1   | 5   | 4  | 4   | 2   | 3   | 4     |
| Siemens Xcelerator / City Twin                    | https://xcelerator.siemens.com                                   | Proprietary (open-core)              | City simulation & digital twin suite      | 5         | 4    | 2    | 5    | 4      | 4     | 2   | 4   | 4  | 5   | 4   | 4   | 4     |
| Cityzenith SmartWorldPro                          | https://www.cityzenith.com                                       | Proprietary                          | Urban digital twin platform               | 5         | 3    | 1    | 5    | 3      | 3     | 1   | 5   | 4  | 4   | 4   | 2   | 3     |
| Replica                                           | https://replicahq.com                                            | Proprietary (SaaS)                   | City-scale urban mobility digital twin    | 5         | 3    | 1    | 4    | 4      | 3     | 2   | 4   | 3  | 5   | 3   | 2   | 2     |
| Cityflows / Urban Simulation Platform (Ito World) | https://www.itoworld.com                                         | Proprietary                          | Urban mobility simulation & analytics     | 5         | 3    | 1    | 4    | 4      | 3     | 2   | 4   | 3  | 5   | 3   | 2   | 2     |
| Autodesk Tandem                                   | https://tandem.autodesk.com                                      | Proprietary (SaaS)                   | Facility/city digital twin platform       | 5         | 3    | 1    | 3    | 4      | 4     | 2   | 3   | 4  | 3   | 3   | 4   | 5     |
| Mobility Data Specification (MDS) / UrbanOS       | https://github.com/smartcitiesdata/smartcitiesdata               | Apache-2.0                           | Open smart city data platform             | 5         | 4    | 5    | 4    | 3      | 4     | 4   | 2   | 4  | 2   | 4   | 4   | 2     |
| FIWARE Orion Context Broker                       | https://fiware-orion.readthedocs.io                              | Apache-2.0                           | Context data management / smart city      | 4         | 4    | 5    | 3    | 5      | 5     | 4   | 1   | 5  | 1   | 5   | 4   | 1     |
| 3DCityDB                                          | https://www.3dcitydb.org                                         | Apache-2.0                           | City model database (CityGML)             | 4         | 5    | 5    | 4    | 5      | 4     | 4   | 2   | 5  | 1   | 2   | 5   | 3     |
| Cesium                                            | https://cesium.com                                               | Apache-2.0 / proprietary (CesiumIon) | 3D geospatial visualisation engine        | 3         | 4    | 4    | 3    | 5      | 4     | 3   | 5   | 2  | 1   | 1   | 4   | 2     |
| Eclipse Ditto                                     | https://www.eclipse.org/ditto/                                   | EPL-2.0                              | IoT device twin framework                 | 3         | 4    | 4    | 2    | 4      | 5     | 4   | 1   | 5  | 1   | 5   | 3   | 1     |
| Eclipse MOSAIC                                    | https://eclipse.dev/mosaic/                                      | EPL-2.0                              | Urban mobility & smart city simulation    | 3         | 4    | 4    | 3    | 3      | 4     | 4   | 1   | 3  | 5   | 2   | 3   | 2     |
| OGC SensorThings API                              | https://www.ogc.org/standard/sensorthings/                       | Open standard                        | IoT/sensor integration standard           | 3         | 4    | 5    | 2    | 5      | 5     | 5   | 1   | 3  | 1   | 5   | 5   | 1     |
| OpenDRIVE / ASAM standards ecosystem              | https://www.asam.net/standards/detail/opendrive/                 | Open standard (ASAM)                 | Road network / mobility twin standard     | 3         | 3    | 4    | 2    | 4      | 4     | 3   | 1   | 2  | 4   | 3   | 5   | 2     |
| SUMO (Simulation of Urban MObility)               | https://eclipse.dev/sumo/                                        | EPL-2.0                              | Urban traffic simulation engine           | 3         | 3    | 5    | 3    | 5      | 4     | 4   | 1   | 2  | 5   | 3   | 3   | 1     |
| GeoServer / GeoNetwork                            | https://geoserver.org                                            | GPL-2.0                              | Open geospatial data server               | 3         | 4    | 4    | 3    | 5      | 5     | 4   | 2   | 5  | 1   | 1   | 5   | 2     |
| AWS IoT TwinMaker                                 | https://aws.amazon.com/iot-twinmaker/                            | Proprietary (SaaS)                   | Cloud IoT & digital twin service          | 3         | 3    | 1    | 2    | 4      | 4     | 1   | 2   | 4  | 3   | 5   | 2   | 3     |
| Azure Digital Twins                               | https://azure.microsoft.com/en-us/products/digital-twins         | Proprietary (SaaS)                   | Cloud digital twin graph service          | 3         | 3    | 1    | 2    | 4      | 5     | 1   | 2   | 5  | 2   | 5   | 3   | 2     |
| NVIDIA Omniverse                                  | https://www.nvidia.com/en-us/omniverse/                          | Proprietary (open-core)              | 3D simulation & digital twin rendering    | 3         | 4    | 2    | 3    | 4      | 4     | 2   | 5   | 3  | 5   | 3   | 3   | 3     |
| Unreal Engine (with City Sample / Houdini)        | https://www.unrealengine.com                                     | Proprietary (EULA)                   | Real-time 3D engine used in UDT rendering | 3         | 3    | 3    | 3    | 5      | 4     | 2   | 5   | 2  | 4   | 2   | 2   | 2     |
| Mapbox                                            | https://www.mapbox.com                                           | Proprietary (open-core)              | 2D/3D map visualisation platform          | 2         | 3    | 2    | 2    | 5      | 4     | 2   | 4   | 2  | 0   | 0   | 2   | 0     |
| ThingsBoard                                       | https://thingsboard.io                                           | Apache-2.0 / proprietary             | IoT platform (not UDT-specific)           | 2         | 3    | 4    | 1    | 4      | 4     | 3   | 1   | 4  | 1   | 5   | 2   | 1     |

Compare every platform present in the pasted table. Treat the pasted table as a discovery baseline — use the identification fields (Name, Link, License, Type, Relevance) and the first-pass dimension scores as starting context. Your task is to deepen each dimension with primary source research and produce authoritative scores and analysis for all twelve dimensions.

---

### Research Instructions

- **Cite sources.** Every factual claim must reference an official website, repository, documentation page, or published paper. Include URLs as inline links `[Description](https://...)`.
- **Distinguish facts from inference.** If you are inferring a score or characteristic from indirect evidence, say so explicitly (e.g., "likely X based on [evidence]").
- **Prefer primary sources.** Official project pages, GitHub/GitLab repos, LICENSE files, and official documentation over blog posts or third-party summaries.
- **Use secondary sources only for discovery.** You may use a secondary source to find a likely repository, product page, or paper, but final factual claims and citations in the saved output must rely on primary sources.
- **Do not fabricate.** If you cannot find information, state "unknown" or "unclear." Do not invent URLs, license names, or deployment claims.
- **Be specific about uncertainty.** "Unknown" is better than a guess.
- **Stay in scope.** Do not broaden the analysis with unsupported claims about the wider market beyond the selected platforms.

---

### Markdown and Formatting Rules

Your response will be saved as a Markdown file and must render identically in any standard Markdown viewer (GitHub, VS Code, Obsidian, Typora).

**Permitted syntax only:**

- ATX headings: `#`, `##`, `###`, `####`
- Emphasis: `**bold**`, `_italic_`
- Links: `[text](url)` inline only
- Lists: `-` unordered, `1.` ordered
- Tables: GFM pipe tables
- Code: fenced code blocks with `` ``` ``

**Prohibited syntax:**

- Custom containers: `:::`, `!!!`, `> [!NOTE]`, `> [!WARNING]`
- Extended syntax: `==highlight==`, `^superscript^`, `~subscript~`
- Raw HTML
- Numeric citations `[1]`, footnotes `[^1]`, AI-specific formats `【†source】`

**Whitespace:** leave a blank line before and after every heading, table, and code block.

**Score notation:**

- In profile sections: `**Dimension Name (X/5):**` — e.g., `**Technical Architecture (4/5):**`
- In the scoring table: bare number only — e.g., `4` — use `?` for unknown. Do not write `/5` in table cells.

**Profile heading level:** use `###` for every platform profile heading so all profiles nest consistently under the Part 2 heading.

**Example profile (fictional platform — for structure reference only):**

---

### Example Platform

**Organization:** Open City Foundation
**Link:** [example-platform.org](https://example-platform.org)
**Description:** Open-source 3D geospatial data platform for city-scale digital twin use cases.
**Type:** Open-source
**License:** Apache-2.0

#### Dimension Analysis

**Technical Architecture (4/5):** Modular microservices architecture with native CityGML support and OGC-compliant APIs. Deployment via Docker or Kubernetes. Proprietary streaming layer for real-time ingestion. [Architecture docs](https://example-platform.org/docs/arch) — inferred from repository structure.

**Openness & Licensing (5/5):** Apache-2.0 licence confirmed in [repository root](https://github.com/example/platform/blob/main/LICENSE). No SaaS tier. All output formats use open OGC standards.

**City-Scale Capability (3/5):** Covers buildings and infrastructure at city scale. No native energy or mobility domain support — likely requires third-party integration based on [roadmap](https://example-platform.org/roadmap).

**Maturity & Adoption (4/5):** Production-ready. Known deployments in Amsterdam and Helsinki per [official case studies](https://example-platform.org/cases). Last release 2024-11. Active GitHub community (340 stars, 12 contributors).

**Integration Posture (4/5):** REST and GraphQL APIs documented at [API reference](https://example-platform.org/api). OGC WFS/WCS compliant. Plugin SDK available. No gRPC support.

**Governance (5/5):** Governed by the Open City Consortium, a multi-institution body. Contribution model documented at [CONTRIBUTING.md](https://github.com/example/platform/blob/main/CONTRIBUTING.md). Funded by EU Horizon grants.

#### Sources

- [Architecture documentation](https://example-platform.org/docs/arch) — accessed 2026-03-28
- [LICENSE file](https://github.com/example/platform/blob/main/LICENSE) — accessed 2026-03-28
- [Case studies](https://example-platform.org/cases) — accessed 2026-03-28
- [API reference](https://example-platform.org/api) — accessed 2026-03-28

_Note: Functional category scores (`Viz`, `DM`, `Sim`, `IoT`, `Std`, `Infra`) appear in the Part 1 scoring table only — do not repeat them in profiles._

---

### Output Format

Begin your response with this metadata block:

```yaml
model: <your model name and version>
date: <YYYY-MM-DD>
prompt: platform-comparison
```

**Part 1 — Scoring Table**

One row per platform in the pasted table, a reassessed Relevance score, six dimension score columns, and six functional category score columns:

| Name | Link | Relevance | Arch | Open | City | Mature | Integ | Gov | Viz | DM | Sim | IoT | Std | Infra |
| ---- | ---- | --------- | ---- | ---- | ---- | ------ | ----- | --- | --- | -- | --- | --- | --- | ----- |

Use bare numbers (1–5) in score cells. Use `?` for unknown. Do not write `/5`.

For `Relevance`: reassess each platform using the rubric from the pasted scope content. Treat the discovery row's score as a starting point — revise it upward or downward if primary-source evidence warrants it. If you revise a score, note the reason briefly in the per-platform profile.

**Column legend:**

| Abbreviation | Full name              | Description                                                                              |
| ------------ | ---------------------- | ---------------------------------------------------------------------------------------- |
| Relevance    | Relevance              | Scope classification 1–5; reassessed from primary sources (may differ from discovery)   |
| Arch         | Technical Architecture | Core tech stack, data models, deployment model, scalability                              |
| Open         | Openness & Licensing   | Source availability, license type, contribution model                                    |
| City         | City-Scale Capability  | Urban domains covered, geographic extent, multi-domain analytics                         |
| Mature       | Maturity & Adoption    | Development status, known city deployments, community activity                           |
| Integ        | Integration Posture    | Public APIs, plugin ecosystem, interoperability                                          |
| Gov          | Governance Model       | Who controls the roadmap, contribution and funding model                                 |
| Viz          | Visualization          | 3D rendering, GIS viewers, scene composition                                             |
| DM           | Data Management        | Data ingestion, storage, twin models, semantic layers                                    |
| Sim          | Simulation             | Urban simulation, physics, scenario modelling                                            |
| IoT          | IoT Sensing            | Real-time data, sensor integration, device management                                    |
| Std          | Standards              | Open standards implementation, interoperability frameworks                               |
| Infra        | Infrastructure         | Built environment, BIM/GIS, infrastructure lifecycle                                     |

**Part 2 — Platform Profiles**

One `###` profile per platform following the example structure above. Include all six dimension analyses with inline scores (`**Dimension (X/5):**`), and a Sources section per platform.

**Part 3 — Landscape Observations**

Use exactly the following four subheadings in this order, each followed by a bullet list. Use `####` for subheadings (not `###`, which is reserved for platform profiles in Part 2). Do not add or remove subheadings.

#### Landscape Gaps

- What capabilities or platform types are missing or underrepresented in this set?

#### DTCC's Position

- Where does DTCC sit relative to the platforms compared here?

#### Comparable Platforms

- Which platforms are most directly comparable to DTCC in purpose, architecture, or target use case?

#### Complementary Platforms

- Which platforms are complementary to DTCC rather than competing — i.e., tools DTCC could integrate with or build on?

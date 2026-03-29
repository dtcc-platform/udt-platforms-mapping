# Platform Comparison Prompt

Use this prompt to produce a structured, evidence-based comparison of UDT platforms.

1. Open the discovery response file for your research session
2. Copy the rows you want to compare (including the header row) from the summary table
3. Replace `[PASTE_SELECTED_PLATFORMS_HERE]` with those rows
4. Paste the completed prompt into your AI session

> **Save response as:** `responses/<platform-a>-vs-<platform-b>-comparison.md` — e.g., `responses/cesium-vs-3dcitydb-comparison.md`. See `docs/methodology.md` for the full convention.

---

## Prompt

You are a research assistant helping to map the Urban Digital Twin (UDT) platform landscape for DTCC.

**About DTCC (reference platform):** DTCC (Digital Twin Cities Centre) is a Swedish research centre developing an open-source, city-scale urban digital twin platform. It supports 3D modelling, simulation, and visualization using CityGML and IFC as core data models. DTCC is open-source, academically governed, and oriented toward interoperability with OGC standards.

Use **primary sources only** (official websites, public repositories, published papers, official documentation). For every substantive claim, include a source reference. Distinguish inferred claims from verified facts. If you cannot find information, state "unknown" or "unclear" — do not fabricate URLs, license names, or deployment claims.

**Platforms to compare** (rows from the discovery summary table — include DTCC as a reference entry):

[PASTE_SELECTED_PLATFORMS_HERE]

| Name                               | Link                                                                                                                          | License                                | Type                                         | Arch | Open | City | Mature | Integ | Gov | Inclusion Criterion                 |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- | -------------------------------------------- | ---- | ---- | ---- | ------ | ----- | --- | ----------------------------------- |
| virtualcitySYSTEMS VC Suite        | [vc.systems](https://vc.systems/en/)                                                                                          | Open-core (MIT + proprietary)          | Urban digital twin platform                  | 4    | 4    | 5    | 4      | 5     | 3   | Explicit UDT                        |
| Dassault Systèmes 3DEXPERIENCity   | [3ds.com](https://www.3ds.com/virtual-twin/infrastructure-cities)                                                             | Proprietary                            | Virtual twin platform                        | 5    | 1    | 5    | 5      | 3     | 2   | Explicit UDT                        |
| Esri ArcGIS Urban                  | [esri.com](https://www.esri.com/en-us/arcgis/products/arcgis-urban/overview)                                                  | Proprietary                            | Urban planning platform                      | 4    | 2    | 5    | 5      | 4     | 2   | Explicit UDT                        |
| Project PLATEAU                    | [mlit.go.jp](https://www.mlit.go.jp/plateau/en/)                                                                              | Apache-2.0                             | National urban digital twin program          | 4    | 5    | 5    | 5      | 4     | 4   | Explicit UDT                        |
| 51WORLD                            | [51aes.com](https://www.51aes.com/?lang=en)                                                                                   | Proprietary                            | City-scale digital twin platform             | 4    | 1    | 5    | 4      | 3     | 2   | Explicit UDT                        |
| Hexagon / Luciad                   | [hexagon.com](https://hexagon.com/go/sig/urban-digital-twin)                                                                  | Proprietary                            | Geospatial analytics platform                | 4    | 1    | 4    | 5      | 4     | 2   | Explicit UDT                        |
| NVIDIA Omniverse                   | [nvidia.com](https://www.nvidia.com/en-us/industries/smart-cities-and-spaces/)                                                | Proprietary (free individual tier)     | Simulation and visualization platform        | 5    | 2    | 4    | 4      | 4     | 2   | Explicit UDT                        |
| Bentley Systems iTwin              | [bentley.com](https://www.bentley.com/software/itwin-platform/)                                                               | Open-core (MIT iTwin.js + proprietary) | Infrastructure digital twin platform         | 5    | 3    | 4    | 5      | 5     | 3   | City-Scale Capabilities             |
| Siemens                            | [siemens-advanta.com](https://www.siemens-advanta.com/capabilities/offers/digital-twin-services-for-building-campuses-cities) | Proprietary                            | Smart infrastructure platform                | 4    | 2    | 4    | 5      | 4     | 2   | City-Scale Capabilities             |
| IES ICL                            | [iesve.com](https://www.iesve.com/icl)                                                                                        | Proprietary                            | Energy simulation platform                   | 4    | 1    | 4    | 4      | 3     | 2   | City-Scale Capabilities             |
| FIWARE                             | [fiware.org](https://www.fiware.org/)                                                                                         | AGPL-3.0 (Orion-LD)                    | Smart city data platform                     | 3    | 4    | 4    | 5      | 5     | 4   | City-Scale Capabilities             |
| Azure Digital Twins                | [azure.microsoft.com](https://github.com/Azure/opendigitaltwins-smartcities)                                                  | Proprietary PaaS / MIT (ontology)      | Cloud digital twin platform                  | 4    | 3    | 3    | 4      | 4     | 2   | City-Scale Capabilities             |
| 3DCityDB                           | [3dcitydb.org](https://www.3dcitydb.org/)                                                                                     | Apache-2.0                             | Semantic 3D city geodatabase                 | 4    | 5    | 4    | 5      | 4     | 4   | City-Scale Capabilities             |
| TerriaJS                           | [terria.io](https://github.com/TerriaJS/terriajs)                                                                             | Apache-2.0                             | Geospatial data exploration platform         | 3    | 5    | 4    | 4      | 5     | 3   | City-Scale Capabilities             |
| CesiumJS                           | [cesium.com](https://cesium.com/platform/cesiumjs/)                                                                           | Apache-2.0                             | 3D geospatial visualization engine           | 4    | 5    | 4    | 5      | 5     | 3   | Adjacent Architecture or Governance |
| deck.gl                            | [deck.gl](https://deck.gl/)                                                                                                   | MIT                                    | GPU-accelerated data visualization framework | 4    | 5    | 3    | 4      | 4     | 4   | Adjacent Architecture or Governance |
| Unity                              | [unity.com](https://unity.com/)                                                                                               | Proprietary (tiered)                   | Real-time 3D engine                          | 5    | 1    | 4    | 5      | 4     | 2   | Adjacent Architecture or Governance |
| Unreal Engine                      | [unrealengine.com](https://www.unrealengine.com/)                                                                             | Custom EULA (royalty-based)            | Real-time 3D engine                          | 5    | 2    | 4    | 5      | 4     | 2   | Adjacent Architecture or Governance |
| 3D Tiles                           | [ogc.org](https://www.ogc.org/standards/3dtiles/)                                                                             | Apache-2.0 (OGC standard)              | Open geospatial streaming standard           | 4    | 5    | 5    | 5      | 5     | 4   | Adjacent Architecture or Governance |
| CityJSON                           | [cityjson.org](https://www.cityjson.org/)                                                                                     | MIT                                    | 3D city model encoding standard              | 3    | 5    | 4    | 4      | 4     | 4   | Adjacent Architecture or Governance |
| UK National Digital Twin Programme | [cdbb.cam.ac.uk](https://www.cdbb.cam.ac.uk/DFTG/GeminiPrinciples)                                                            | Open governance framework              | Governance framework                         | 2    | 4    | 3    | 4      | 3     | 5   | Adjacent Architecture or Governance |

Compare every platform present in the pasted table, plus DTCC. Treat the pasted table as a discovery baseline — use the identification fields (Name, Link, License, Type) and the first-pass dimension scores as starting context. Your task is to deepen each dimension with primary source research and produce authoritative scores and analysis for all six dimensions.

---

### Research Dimensions

Score each platform 1–5 per dimension using the rubrics below.

**1. Technical Architecture**
Core technology stack, data models (CityGML, IFC, OGC standards, proprietary), component structure, deployment model, scalability approach.

| Score | Criteria                                                                       |
| ----- | ------------------------------------------------------------------------------ |
| 5     | Fully modular, open standards (CityGML/IFC/OGC), cloud-native or self-hostable |
| 4     | Mostly modular, supports open standards with some proprietary layers           |
| 3     | Mixed architecture, partial standards support                                  |
| 2     | Largely monolithic, limited open standards                                     |
| 1     | Monolithic with proprietary data model, no open standards                      |

**2. Openness & Licensing**
Source availability, license type, contribution model, commercial restrictions, dual licensing, open data formats.

| Score | Criteria                                                                                      |
| ----- | --------------------------------------------------------------------------------------------- |
| 5     | Permissive open-source (MIT/Apache/BSD) + open data formats, no SaaS dependency               |
| 4     | Copyleft open-source, or open-core with substantial open component                            |
| 3     | Open-core with significant proprietary features, or open source with restrictive data formats |
| 2     | Primarily proprietary with limited open components or open APIs                               |
| 1     | Fully proprietary, no public source, no open APIs                                             |

**3. City-Scale Capability**
Urban domains covered (buildings, infrastructure, mobility, energy, climate, water, noise), geographic extent, multi-domain analytics, real-time vs. batch.

| Score | Criteria                                                         |
| ----- | ---------------------------------------------------------------- |
| 5     | Comprehensive multi-domain urban coverage at full city scale     |
| 4     | Multi-domain coverage, strong city-scale support with minor gaps |
| 3     | Several domains covered, city-scale with notable limitations     |
| 2     | Limited domains or district/building scale only                  |
| 1     | Single narrow domain or sub-city scale                           |

**4. Maturity & Adoption**
Development status, known city deployments (name cities if possible), release cadence, community activity.

| Score | Criteria                                                            |
| ----- | ------------------------------------------------------------------- |
| 5     | Production-grade, multiple named city deployments, active community |
| 4     | Production-ready, some city deployments or pilots, regular releases |
| 3     | Stable but limited deployments, moderate activity                   |
| 2     | Prototype or early production, few or no known deployments          |
| 1     | Concept or prototype, no known deployments                          |

**5. Integration Posture**
Public APIs (REST, GraphQL, gRPC), plugin/extension ecosystem, data exchange standards, interoperability with other tools.

| Score | Criteria                                                                    |
| ----- | --------------------------------------------------------------------------- |
| 5     | Rich public APIs, active plugin ecosystem, easy to compose with other tools |
| 4     | Good APIs, some ecosystem, OGC-compliant interfaces                         |
| 3     | Basic APIs, limited ecosystem, some interoperability                        |
| 2     | Minimal public APIs, closed or limited integration                          |
| 1     | Closed system, no public APIs                                               |

**6. Governance Model**
Who controls the roadmap (vendor, consortium, community, research institution), contribution model, funding model.

| Score | Criteria                                                                              |
| ----- | ------------------------------------------------------------------------------------- |
| 5     | Open consortium or community governance, transparent decision-making, diverse funding |
| 4     | Academic or public institution governance with open contribution                      |
| 3     | Mixed governance, some community input                                                |
| 2     | Single organisation control with limited community input                              |
| 1     | Single corporate control, no community input                                          |

**Functional Categories**

Score each platform 1–5 per functional category using the rubrics below.

**7. Visualization** (`Viz`)
Primary function: 3D rendering, GIS viewers, scene composition, visual output quality.

| Score | Criteria                                                                                                |
| ----- | ------------------------------------------------------------------------------------------------------- |
| 5     | Purpose-built 3D visualization engine or viewer; primary purpose; real-time or near-real-time rendering |
| 4     | Strong visualization capabilities; core feature set with significant investment                         |
| 3     | Visualization present and useful but not the primary strength                                           |
| 2     | Basic or incidental visualization (e.g., simple 2D map view, no 3D)                                     |
| 1     | No meaningful visualization capability                                                                  |

**8. Data Management** (`DM`)
Primary function: data ingestion, storage, twin models, semantic layers, data lifecycle.

| Score | Criteria                                                                                                  |
| ----- | --------------------------------------------------------------------------------------------------------- |
| 5     | Purpose-built for city-scale data storage and management; semantic model, versioning, full data lifecycle |
| 4     | Strong data management with semantic modelling or graph; multi-source ingestion                           |
| 3     | Solid data management but limited semantic layer or scalability                                           |
| 2     | Basic storage or data exchange; limited query or model capabilities                                       |
| 1     | No meaningful data management role                                                                        |

**9. Simulation** (`Sim`)
Primary function: urban simulation, physics, scenario modelling, what-if analysis.

| Score | Criteria                                                                                       |
| ----- | ---------------------------------------------------------------------------------------------- |
| 5     | Purpose-built simulation engine; multi-domain urban physics, scenario comparison at city scale |
| 4     | Strong simulation support across multiple urban domains                                        |
| 3     | Simulation present for one or two domains; limited scenario tooling                            |
| 2     | Basic scenario comparison or single-variable simulation                                        |
| 1     | No simulation capability                                                                       |

**10. IoT Sensing** (`IoT`)
Primary function: real-time data, sensor integration, device management, stream processing.

| Score | Criteria                                                                                     |
| ----- | -------------------------------------------------------------------------------------------- |
| 5     | Purpose-built IoT platform; real-time ingestion, device registry, stream processing at scale |
| 4     | Strong IoT support; real-time APIs, sensor integration, stream handling                      |
| 3     | Connects to sensors but limited real-time processing                                         |
| 2     | Basic real-time data hookup; manual or batch sensor feeds                                    |
| 1     | No IoT or real-time sensing capability                                                       |

**11. Standards** (`Std`)
Primary function: implementing or defining open standards, interoperability frameworks.

| Score | Criteria                                                                                                      |
| ----- | ------------------------------------------------------------------------------------------------------------- |
| 5     | Primary purpose is defining or implementing open standards (OGC, ISO, W3C); governance role in standards body |
| 4     | Strong standards implementation; multiple OGC/ISO standards as native data models                             |
| 3     | Partial standards support; some open standards alongside proprietary models                                   |
| 2     | Limited standards; primarily proprietary with token open format support                                       |
| 1     | No meaningful open standards implementation                                                                   |

**12. Infrastructure** (`Infra`)
Primary function: built environment, BIM/GIS integration, infrastructure lifecycle management.

| Score | Criteria                                                                                     |
| ----- | -------------------------------------------------------------------------------------------- |
| 5     | Purpose-built for infrastructure or BIM lifecycle; IFC, asset management, lifecycle tracking |
| 4     | Strong infrastructure support; BIM integration, asset management, or civil engineering focus |
| 3     | Infrastructure is one of several domains; partial BIM/GIS support                            |
| 2     | Limited infrastructure scope; building-level only or minimal lifecycle management            |
| 1     | No meaningful infrastructure or built environment focus                                      |

---

### Research Instructions

- **Cite sources.** Every factual claim must reference an official website, repository, documentation page, or published paper. Include URLs as inline links `[Description](https://...)`.
- **Distinguish facts from inference.** If you are inferring a score or characteristic from indirect evidence, say so explicitly (e.g., "likely X based on [evidence]").
- **Prefer primary sources.** Official project pages, GitHub/GitLab repos, LICENSE files, and official documentation over blog posts or third-party summaries.
- **Do not fabricate.** If you cannot find information, state "unknown" or "unclear." Do not invent URLs, license names, or deployment claims.
- **Be specific about uncertainty.** "Unknown" is better than a guess.

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

One row per platform (including DTCC), six dimension score columns, six functional category score columns, plus name and link:

| Name | Link | Arch | Open | City | Mature | Integ | Gov | Viz | DM | Sim | IoT | Std | Infra |
| ---- | ---- | ---- | ---- | ---- | ------ | ----- | --- | --- | -- | --- | --- | --- | ----- |

Use bare numbers (1–5) in score cells. Use `?` for unknown. Do not write `/5`.

**Column legend:**

| Abbreviation | Full name              | Description                                                      |
| ------------ | ---------------------- | ---------------------------------------------------------------- |
| Arch         | Technical Architecture | Core tech stack, data models, deployment model, scalability      |
| Open         | Openness & Licensing   | Source availability, license type, contribution model            |
| City         | City-Scale Capability  | Urban domains covered, geographic extent, multi-domain analytics |
| Mature       | Maturity & Adoption    | Development status, known city deployments, community activity   |
| Integ        | Integration Posture    | Public APIs, plugin ecosystem, interoperability                  |
| Gov          | Governance Model       | Who controls the roadmap, contribution and funding model         |
| Viz          | Visualization          | 3D rendering, GIS viewers, scene composition                     |
| DM           | Data Management        | Data ingestion, storage, twin models, semantic layers            |
| Sim          | Simulation             | Urban simulation, physics, scenario modelling                    |
| IoT          | IoT Sensing            | Real-time data, sensor integration, device management            |
| Std          | Standards              | Open standards implementation, interoperability frameworks       |
| Infra        | Infrastructure         | Built environment, BIM/GIS, infrastructure lifecycle             |

**Part 2 — Platform Profiles**

One `###` profile per platform following the example structure above. Include all six dimension analyses with inline scores (`**Dimension (X/5):**`), and a Sources section per platform.

**Part 3 — Landscape Observations**

- What gaps exist in the landscape?
- Where does DTCC sit relative to comparable platforms?
- Which platforms are most directly comparable to DTCC?
- Which are complementary rather than competing?

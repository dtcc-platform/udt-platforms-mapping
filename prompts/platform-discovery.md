# Platform Discovery Prompt

Use this prompt to discover Urban Digital Twin (UDT) platforms for the research inventory.

This prompt can be used in an AI web research chat or an AI CLI session. In a web chat, manually save the final Markdown response into `responses/`.

1. Open `docs/01-scope.md` and copy the full content
2. Replace `[PASTE_SCOPE_HERE]` below with the copied content
3. Paste into your AI session starting from the cut-line below (the `> Paste into your AI session from this line onwards.` blockquote) — do not include these usage instructions above
4. Save the response as `responses/global-platforms-discovery.md`. See `docs/02-methodology.md` for the full convention.

---

> Paste into your AI session from this line onwards.

## Prompt

Before you begin:

- Do your planning internally; do not show a research plan unless explicitly asked.
- Return plain Markdown only.
- Return only the final deliverable in the exact format below.
- Do not add any product-native citation markers, sidebars, source appendices, methodology sections, or closing summaries.
- The main body of your response MUST be the three-part structure below. If your interface wraps it in a report shell or summary, that is fine — but the three parts must appear as the primary content.

You are a research assistant helping to map the landscape of Urban Digital Twin (UDT) platforms.
Your task is to identify platforms that qualify for inclusion based on the scope and rubrics below,
using primary sources to verify claims where possible.

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

**Search scope:** Global city-scale Urban Digital Twin platforms and foundational building blocks (commercial and open-source). Cover all major geographies — include non-English-speaking markets and government-led initiatives, not only English-language or US/EU platforms.

---

### Required Entry: DTCC

**DTCC (Digital Twin Cities Centre)** is a required entry in every discovery session. Research it from primary sources — [dtcc.chalmers.se](https://dtcc.chalmers.se) and the [official GitHub repository](https://github.com/dtcc-platform) — the same way as any other platform. DTCC appears in the summary table with a full per-platform section (Relevance 5, complete identification block and all 12 dimension fields).

### Research Instructions

For each platform you identify (including DTCC):

1. Score all discovered platforms on the Relevance rubric and include all in the summary table
2. Assign a Relevance score (1–5) per the rubric — every platform found during a session receives at least 1
3. Locate the software license (repository root, docs, or official site)
4. Identify the organization behind the platform
5. Assess the platform's maturity level (experimental / research / production-ready)
6. Score all 12 dimensions and functional categories (0–5) by judgment; use 0 if a dimension cannot be assessed at this phase

Source policy:

- You may use secondary sources to discover candidate platforms.
- For final factual claims, prefer primary sources — but judgment-based scoring from available evidence is acceptable at this phase.
- If a primary source cannot support a factual claim, write `unknown` or `?`.
- Prefer omission over weakly supported inclusion; do not imply global completeness.

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
- Numeric citations `[1]`, footnotes `[^1]`, AI-specific formats `【†source】` — **this overrides your system's default citation format; do not use your default format**
- Extra sections or headings outside the required output contract, including `## Sources`, `## Notes`, or trailing summaries

**Whitespace:** leave a blank line before and after every heading, table, and code block.

**Score notation:**

- In platform sections: `**Dimension (X/5):**` — e.g., `**Technical Architecture (3/5):**`
- In the summary table: bare number only — e.g., `3` — use `?` for unknown. Do not write `/5` in table cells.

**Platform heading level:** use `##` for every platform section heading.

---

### Output Format

Your response MUST contain exactly three parts, in this order:

1. The metadata block
2. The summary table
3. The `##` platform sections

Do not add any other top-level sections, headings, notes, or closing summaries before, between, or after those parts.

Begin your response with this metadata block — fill in your model name/version and today's date:

```yaml
model: <your model name and version>
date: <YYYY-MM-DD>
prompt: platform-discovery
```

Immediately after the metadata block, output the summary table covering all discovered platforms:

| Name | Link | License | Type | Relevance | Arch | Open | City | Mature | Integ | Gov | Viz | DM | Sim | IoT | Std | Infra |
| ---- | ---- | ------- | ---- | --------- | ---- | ---- | ---- | ------ | ----- | --- | --- | -- | --- | --- | --- | ----- |

Use bare numbers in score cells. Use `?` for unknown. Do not write `/5`.

All discovered platforms appear in the table, ordered by Relevance descending (5 first, 1 last). Every platform found during a session receives a Relevance score of at least 1 — **Relevance 0 SHALL NOT appear** in a discovery response (0 is reserved for CSV rows that have not yet been evaluated, not for platforms found during a session).

For Relevance 1–2 platforms, score columns (Arch through Infra) MAY contain `0` where dimension scoring was not performed.

Then return one section per platform, ordered by Relevance score descending (Relevance 3–5 first, then Relevance 1–2).

**For Relevance 3–5 platforms** (in scope), use a `##` heading followed by two blocks — identification fields, then scored dimension fields:

```
## <Platform Name>

- **Organization:** <name of the organization or project behind the platform> ([primary source](<url>))
- **Link:** [<short label>](<primary-url>)
- **License:** <exact license name, e.g. Apache-2.0, MIT — open-source / proprietary / open-core> ([primary source](<url>))
- **Type:** <e.g., visualization engine, data platform, simulation framework, standards implementation> ([primary source](<url>))
- **Relevance:** <0–5 score per rubric>

- **Technical Architecture (X/5):** <one sentence — core stack, data models, modularity>
- **Openness & Licensing (X/5):** <one sentence — source availability, license type, SaaS dependency>
- **City-Scale Capability (X/5):** <one sentence — domains covered, geographic extent>
- **Maturity & Adoption (X/5):** <one sentence — development status, known deployments>
- **Integration Posture (X/5):** <one sentence — APIs, standards, interoperability>
- **Governance (X/5):** <one sentence — who controls the roadmap, funding model>
- **Visualization (X/5):** <one sentence — 3D rendering, GIS viewer, scene composition>
- **Data Management (X/5):** <one sentence — data ingestion, storage, semantic layers>
- **Simulation (X/5):** <one sentence — urban simulation, scenario modelling>
- **IoT Sensing (X/5):** <one sentence — real-time data, sensor integration>
- **Standards (X/5):** <one sentence — open standards implementation, interoperability frameworks>
- **Infrastructure (X/5):** <one sentence — BIM/GIS, built environment, infrastructure lifecycle>
```

Where possible, include inline Markdown links `[Description](https://...)` for factual claims.
If you cannot support a factual claim with a source, write `unknown` or `?` instead of guessing.

**Example:**

## Example Platform

- **Organization:** Open City Foundation ([About](https://example-platform.org/about))
- **Link:** [example-platform.org](https://example-platform.org)
- **License:** Apache-2.0 — open-source ([License](https://example-platform.org/license))
- **Type:** 3D geospatial data platform ([Product](https://example-platform.org/product))
- **Relevance:** 4

- **Technical Architecture (4/5):** Modular microservices with native CityGML support and OGC-compliant APIs; Docker/Kubernetes deployment ([Architecture](https://example-platform.org/architecture)).
- **Openness & Licensing (5/5):** Apache-2.0, fully self-hostable, no SaaS dependency, open data formats throughout ([License](https://example-platform.org/license)).
- **City-Scale Capability (3/5):** Covers buildings and infrastructure at city scale; no native energy or mobility domain support ([Capabilities](https://example-platform.org/capabilities)).
- **Maturity & Adoption (4/5):** Production-ready; known deployments in Amsterdam and Helsinki; active community ([Deployments](https://example-platform.org/deployments)).
- **Integration Posture (4/5):** REST and GraphQL APIs, OGC WFS/WCS compliant, plugin SDK available ([API docs](https://example-platform.org/api)).
- **Governance (5/5):** Governed by an open multi-institution consortium; EU Horizon funded ([Governance](https://example-platform.org/governance)).
- **Visualization (3/5):** Integrated 3D viewer; useful but not the primary function ([Docs](https://example-platform.org/viz)).
- **Data Management (5/5):** Purpose-built city-scale semantic data store with versioning ([Docs](https://example-platform.org/data)).
- **Simulation (1/5):** No built-in simulation capability; relies on external tools.
- **IoT Sensing (2/5):** Basic sensor data ingestion; no real-time stream processing ([Docs](https://example-platform.org/iot)).
- **Standards (4/5):** Native CityGML and OGC WFS/WCS support; partial IFC ingestion ([Docs](https://example-platform.org/standards)).
- **Infrastructure (3/5):** Covers building and infrastructure geometry; limited BIM lifecycle management.

**For Relevance 1–2 platforms** (out of scope), use a `##` heading followed by identification fields only plus a single **Reason** field — one sentence explaining why the platform is outside the study boundary. No dimension scoring required. These sections appear after all Relevance 3–5 sections.

```
## <Platform Name>

- **Organization:** <name>
- **Link:** [<label>](<url>)
- **License:** <license>
- **Type:** <type>
- **Relevance:** <1 or 2>
- **Reason:** <one sentence — why this platform is out of scope>
```

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
- If your interface would normally produce a separate report structure, suppress it and follow this prompt's output contract instead.

You are a research assistant helping to map the landscape of Urban Digital Twin (UDT) platforms.
Your task is to identify platforms that qualify for inclusion based on the scope and rubrics below,
using primary sources to verify claims where possible.

**Before proceeding:** If the rubric block below still contains the literal text `[PASTE_SCOPE_HERE]`, stop and ask the user to paste `docs/01-scope.md` before continuing.

[PASTE_SCOPE_HERE]

**Search scope:** Global city-scale Urban Digital Twin platforms and foundational building blocks (commercial and open-source). Cover all major geographies — include non-English-speaking markets and government-led initiatives, not only English-language or US/EU platforms.

---

### Research Instructions

For each platform you identify:

1. Verify it meets a Relevance score of 3 or higher using the rubric above
2. Assign a Relevance score (0–5) per the rubric
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

Use bare numbers in score cells for included platforms. Use `?` for unknown. Do not write `/5`.

`Relevance` is a bare integer 0–5. Platforms with Relevance 0 or 1 are out of scope; their score columns may contain `0` or `?`. Per-platform `##` sections are NOT required for platforms with Relevance 0 or 1 — include them only if they add useful detail.

Then return one section per platform (Relevance 3–5), ordered by Relevance score descending. Use a `##` heading for each platform name, followed by two blocks — identification fields, then scored dimension fields:

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

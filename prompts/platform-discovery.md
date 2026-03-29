# Platform Discovery Prompt

Use this prompt to discover Urban Digital Twin (UDT) platforms for the research inventory.
Copy the prompt below, replace `[SEARCH_SCOPE]` with your focus (e.g., "European city-scale platforms",
"platforms using CityGML", "open-source UDT frameworks"), and paste into your AI session.

> **Source of truth for inclusion criteria:** `docs/methodology.md`
> **Save response as:** `responses/<platform>-discovery.md` — e.g., `responses/cesium-discovery.md`; for broad sessions use a scope descriptor e.g., `responses/european-platforms-discovery.md`. See `docs/methodology.md` for the full convention.

---

## Prompt

You are a research assistant helping to map the landscape of Urban Digital Twin (UDT) platforms.
Your task is to identify platforms that qualify for inclusion based on the criteria below,
using **primary sources only** (official websites, public repositories, published papers, official documentation).

**Search scope:** [SEARCH_SCOPE]

---

### Inclusion Criteria

A platform is included if it satisfies **at least one** of the following:

**1. Explicit Urban Digital Twin**
The platform explicitly presents itself as an urban or city-scale digital twin. It uses the term "digital twin" in official documentation, product descriptions, or marketing, and is scoped to urban environments (cities, districts, or built infrastructure at city scale).

**2. City-Scale Capabilities**
The platform provides capabilities commonly used to build or operate urban digital twins, even if it does not use the term "digital twin." This includes platforms for city-scale 3D visualization, urban simulation, large-scale geospatial data management, or multi-domain urban analytics (buildings, transport, energy, climate).

**3. Adjacent Architecture or Governance**
The platform is a foundational building block commonly integrated into UDT systems — for example, open standards implementations (CityGML, IFC, OGC standards), enabling visualization engines (Cesium, Unity, Unreal with urban extensions), or infrastructure digital twin frameworks (iTwin). Exclude standalone smart city IoT platforms, transport simulation tools, or standards bodies unless they are directly used as UDT building blocks.

**Scope boundary:** Apply a moderate inclusion boundary. Exclude platforms that are purely adjacent (e.g., generic IoT platforms, general-purpose GIS tools without urban twin framing), even if they could theoretically be used in a UDT context.

---

### Research Instructions

For each platform you identify:

1. Verify it meets at least one inclusion criterion using primary sources
2. Note which criterion it satisfies
3. Locate the software license (repository root, docs, or official site)
4. Identify the organization behind the platform
5. Assess the platform's maturity level (experimental / research / production-ready)

---

### Markdown Syntax Rules

Your response will be saved as a Markdown file and must render correctly in any standard Markdown viewer (GitHub, VS Code, Obsidian, Typora).

- Use only CommonMark / GFM syntax: `#` ATX headings, `**bold**`, `_italic_`, `[text](url)` links, fenced code blocks, pipe tables, `-` unordered lists, `1.` ordered lists
- Cite sources as inline links only: `[Description](https://...)` — no numeric brackets (`[1]`), no footnotes (`[^1]`), no AI-specific citation formats
- Do not use custom containers or admonitions (`:::`, `!!!`, `> [!NOTE]`, etc.)
- Do not use extended syntax: no `==highlight==`, no `^superscript^`, no `~subscript~`
- Do not embed raw HTML
- Leave a blank line before and after every heading, table, and code block

---

### Markdown and Formatting Rules

Your response will be saved as a Markdown file and must render identically in any standard Markdown viewer (GitHub, VS Code, Obsidian, Typora).

**Permitted syntax only:**
- ATX headings: `#`, `##`, `###`, `####`
- Emphasis: `**bold**`, `_italic_`
- Links: `[text](url)` inline only
- Lists: `-` unordered, `1.` ordered
- Tables: GFM pipe tables
- Code: fenced code blocks with ` ``` `

**Prohibited syntax:**
- Custom containers: `:::`, `!!!`, `> [!NOTE]`, `> [!WARNING]`
- Extended syntax: `==highlight==`, `^superscript^`, `~subscript~`
- Raw HTML
- Numeric citations `[1]`, footnotes `[^1]`, AI-specific formats `【†source】`

**Whitespace:** leave a blank line before and after every heading, table, and code block.

**Score notation:**
- In platform sections: `**Dimension (X/5):**` — e.g., `**Technical Architecture (3/5):**`
- In the summary table: bare number only — e.g., `3` — use `?` for unknown. Do not write `/5` in table cells.

**Platform heading level:** use `##` for every platform section heading.

---

### Output Format

Begin your response with this metadata block — fill in your model name/version and today's date:

```yaml
model: <your model name and version>
date: <YYYY-MM-DD>
prompt: platform-discovery
```

Then return one section per platform, ordered by relevance to city-scale digital twin use cases. Use a `##` heading for each platform name, followed by two blocks — identification fields, then six scored dimension fields:

```
## <Platform Name>

- **Organization:** <name of the organization or project behind the platform>
- **Link:** [<short label>](<url>)
- **License:** <exact license name, e.g. Apache-2.0, MIT — open-source / proprietary / open-core>
- **Type:** <e.g., visualization engine, data platform, simulation framework, standards implementation>
- **Inclusion criterion:** <Explicit UDT / City-Scale Capabilities / Adjacent Architecture or Governance>

- **Technical Architecture (X/5):** <one sentence — core stack, data models, modularity>
- **Openness & Licensing (X/5):** <one sentence — source availability, license type, SaaS dependency>
- **City-Scale Capability (X/5):** <one sentence — domains covered, geographic extent>
- **Maturity & Adoption (X/5):** <one sentence — development status, known deployments>
- **Integration Posture (X/5):** <one sentence — APIs, standards, interoperability>
- **Governance (X/5):** <one sentence — who controls the roadmap, funding model>
```

Score each dimension 1–5 by judgment using the same scale as the comparison prompt. Do not fabricate — state `?` if a dimension cannot be assessed from available sources.

**Example:**

## Example Platform

- **Organization:** Open City Foundation
- **Link:** [example-platform.org](https://example-platform.org)
- **License:** Apache-2.0 — open-source
- **Type:** 3D geospatial data platform
- **Inclusion criterion:** City-Scale Capabilities

- **Technical Architecture (4/5):** Modular microservices with native CityGML support and OGC-compliant APIs; Docker/Kubernetes deployment.
- **Openness & Licensing (5/5):** Apache-2.0, fully self-hostable, no SaaS dependency, open data formats throughout.
- **City-Scale Capability (3/5):** Covers buildings and infrastructure at city scale; no native energy or mobility domain support.
- **Maturity & Adoption (4/5):** Production-ready; known deployments in Amsterdam and Helsinki; active community.
- **Integration Posture (4/5):** REST and GraphQL APIs, OGC WFS/WCS compliant, plugin SDK available.
- **Governance (5/5):** Governed by an open multi-institution consortium; EU Horizon funded.

---

After all per-platform sections, append a summary table:

| Name | Link | License | Type | Arch | Open | City | Mature | Integ | Gov | Inclusion Criterion |
| ---- | ---- | ------- | ---- | ---- | ---- | ---- | ------ | ----- | --- | ------------------- |

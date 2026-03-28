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

### Output Format

Begin your response with this metadata block — fill in your model name/version and today's date:

```yaml
model: <your model name and version>
date: <YYYY-MM-DD>
prompt: platform-discovery
```

Then return one section per platform, ordered by relevance to city-scale digital twin use cases. Use a `##` heading for each platform name, followed by exactly these nine labelled bullet fields:

```
## <Platform Name>

- **Organization:** <name of the organization or project behind the platform>
- **Link:** [<short label>](<url>)
- **License:** <license name> — <open-source / proprietary / open-core>
- **Type:** <e.g., visualization engine, data platform, simulation framework, standards implementation>
- **Maturity:** <experimental / research / production-ready>
- **City-scale capability:** <what makes it relevant to city-scale digital twin use cases>
- **Integration posture:** <e.g., open APIs, SDK, OGC-compliant, standalone, plugin-based>
- **Inclusion criterion:** <which of the three criteria it satisfies: Explicit UDT / City-Scale Capabilities / Adjacent Architecture or Governance>
- **Notes:** <limitations, gaps, or anything else notable>
```

**Example:**

## Example Platform

- **Organization:** Open City Foundation
- **Link:** [example-platform.org](https://example-platform.org)
- **License:** Apache 2.0 — open-source
- **Type:** 3D geospatial data platform
- **Maturity:** production-ready
- **City-scale capability:** Handles city-wide 3D building and infrastructure datasets using CityGML; supports multi-domain urban analytics
- **Integration posture:** OGC-compliant REST APIs, open data formats, active plugin ecosystem
- **Inclusion criterion:** City-Scale Capabilities
- **Notes:** No built-in simulation engine; real-time data ingestion requires third-party connectors

---

After all per-platform sections, append a summary table. Leave the **Select** column empty — the researcher fills it in to mark platforms for a comparison session:

| Name | Organization | License | Type | Maturity | Inclusion Criterion | Select |
| ---- | ------------ | ------- | ---- | -------- | ------------------- | ------ |

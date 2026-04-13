# Platform Discovery Prompt

Use this prompt to discover Urban Digital Twin (UDT) platforms for the research inventory.

1. Paste into your AI session starting from the cut-line below — do not include these usage instructions above
2. Save the response as `responses/global-platforms-discovery.md`. See `docs/02-methodology.md` for the full convention.

---

> Paste into your AI session from this line onwards.

## Prompt

You are a research assistant helping to map the landscape of Urban Digital Twin (UDT) platforms.
Your task is to identify platforms that qualify for inclusion based on the criteria below,
using **primary sources only** (official websites, public repositories, published papers, official documentation).

**Search scope:** Global city-scale Urban Digital Twin platforms and foundational building blocks (commercial and open-source). Cover all major geographies — include non-English-speaking markets and government-led initiatives, not only English-language or US/EU platforms.

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

| Name | Link | License | Type | Arch | Open | City | Mature | Integ | Gov | Inclusion Criterion |
| ---- | ---- | ------- | ---- | ---- | ---- | ---- | ------ | ----- | --- | ------------------- |

Use bare numbers (1–5) in score cells. Use `?` for unknown. Do not write `/5`.
For `Inclusion Criterion`, use only one of these exact values: `Explicit UDT`, `City-Scale Capabilities`, `Adjacent Architecture or Governance`.

Then return one section per platform, ordered by relevance to city-scale digital twin use cases. Use a `##` heading for each platform name, followed by two blocks — identification fields, then six scored dimension fields:

```
## <Platform Name>

- **Organization:** <name of the organization or project behind the platform> ([primary source](<url>))
- **Link:** [<short label>](<primary-url>)
- **License:** <exact license name, e.g. Apache-2.0, MIT — open-source / proprietary / open-core> ([primary source](<url>))
- **Type:** <e.g., visualization engine, data platform, simulation framework, standards implementation> ([primary source](<url>))
- **Inclusion criterion:** <Explicit UDT / City-Scale Capabilities / Adjacent Architecture or Governance>

- **Technical Architecture (X/5):** <one sentence with at least one inline link to a primary source — core stack, data models, modularity>
- **Openness & Licensing (X/5):** <one sentence with at least one inline link to a primary source — source availability, license type, SaaS dependency>
- **City-Scale Capability (X/5):** <one sentence with at least one inline link to a primary source — domains covered, geographic extent>
- **Maturity & Adoption (X/5):** <one sentence with at least one inline link to a primary source — development status, known deployments>
- **Integration Posture (X/5):** <one sentence with at least one inline link to a primary source — APIs, standards, interoperability>
- **Governance (X/5):** <one sentence with at least one inline link to a primary source — who controls the roadmap, funding model>
```

For factual claims in the identification bullets and scored dimension bullets, cite primary sources with inline Markdown links `[Description](https://...)`.
If you cannot support a factual claim with a primary source, write `unknown` or `?` instead of citing a secondary source or guessing.

Score each dimension 1–5 by judgment using the same scale as the comparison prompt. Do not fabricate — state `?` if a dimension cannot be assessed from available sources.

**Example:**

#### Example Platform

- **Organization:** Open City Foundation ([About](https://example-platform.org/about))
- **Link:** [example-platform.org](https://example-platform.org)
- **License:** Apache-2.0 — open-source ([License](https://example-platform.org/license))
- **Type:** 3D geospatial data platform ([Product](https://example-platform.org/product))
- **Inclusion criterion:** City-Scale Capabilities

- **Technical Architecture (4/5):** Modular microservices with native CityGML support and OGC-compliant APIs; Docker/Kubernetes deployment ([Architecture](https://example-platform.org/architecture)).
- **Openness & Licensing (5/5):** Apache-2.0, fully self-hostable, no SaaS dependency, open data formats throughout ([License](https://example-platform.org/license)).
- **City-Scale Capability (3/5):** Covers buildings and infrastructure at city scale; no native energy or mobility domain support ([Capabilities](https://example-platform.org/capabilities)).
- **Maturity & Adoption (4/5):** Production-ready; known deployments in Amsterdam and Helsinki; active community ([Deployments](https://example-platform.org/deployments)).
- **Integration Posture (4/5):** REST and GraphQL APIs, OGC WFS/WCS compliant, plugin SDK available ([API docs](https://example-platform.org/api)).
- **Governance (5/5):** Governed by an open multi-institution consortium; EU Horizon funded ([Governance](https://example-platform.org/governance)).

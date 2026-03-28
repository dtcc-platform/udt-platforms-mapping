# Platform Comparison Prompt

Use this prompt to produce a structured side-by-side comparison of two or more UDT platforms.

1. Open the discovery response file for your research session
2. Place `x` in the **Select** column for each platform you want to compare
3. Copy only the marked rows from the summary table
4. Replace `[PASTE_SELECTED_PLATFORMS_HERE]` with those rows
5. Paste the completed prompt into your AI session

> **Source of truth for research dimensions:** `docs/methodology.md`
> **Source of truth for platform selection:** `docs/platform-inventory.md`
> **Save response as:** `responses/<platform-a>-vs-<platform-b>-comparison.md` — e.g., `responses/cesium-vs-dtcc-comparison.md`. See `docs/methodology.md` for the full convention.

---

## Prompt

You are a research assistant helping to compare Urban Digital Twin (UDT) platforms for a landscape review.
Your task is to produce a structured, evidence-based comparison of the platforms listed below.

Use **primary sources only** (official websites, public repositories, published papers, official documentation).
For every substantive claim, include a source reference or URL.

**Platforms to compare** (rows marked for selection from the discovery summary table):

[PASTE_SELECTED_PLATFORMS_HERE]

Compare every platform present in the pasted table. Treat the table fields (Type, License, Maturity) as known context and focus your research on dimensions not already captured there.

---

### Research Dimensions

Compare each platform across all six dimensions:

**1. Technical Architecture**
Core technology stack, data models used (CityGML, IFC, OGC standards, proprietary), runtime environment, scalability approach, and how the platform ingests and manages urban data.

**2. Openness & Licensing**
Software license type (permissive open source, copyleft, open-core, proprietary), availability of source code, any community vs. enterprise tier split, and whether output data uses open or proprietary formats.

**3. City-Scale Capability**
Ability to handle city-scale datasets and simulations: supported extent, data volume, multi-domain coverage (buildings, transport, energy, climate, utilities), and real-time vs. batch processing.

**4. Platform Maturity**
Deployment stage (experimental / research / production-ready), known production deployments, community size, release cadence, and documentation quality.

**5. Integration Posture**
APIs and interoperability interfaces offered, supported standards and protocols, ease of integration with third-party tools, and extensibility model.

**6. Governance Model**
Who controls the roadmap (vendor, consortium, community, government), contribution model, and long-term sustainability signals.

---

### Instructions

1. Research each platform using primary sources
2. Cite at least one source for each dimension per platform
3. Note explicitly where information is unavailable or unclear rather than inferring

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

````yaml
model: <your model name and version>
date: <YYYY-MM-DD>
prompt: platform-comparison
````

**Part 1 — Summary Table**

Return a Markdown table with one row per platform and one column per dimension, using brief descriptors (3–6 words per cell):

| Platform | Technical Architecture | Openness & Licensing | City-Scale Capability | Maturity | Integration Posture | Governance |
| -------- | ---------------------- | -------------------- | --------------------- | -------- | ------------------- | ---------- |

**Part 2 — Per-Dimension Analysis**

For each of the six dimensions, write a short comparative section (one paragraph per platform) with source citations. Structure as:

#### [Dimension Name]

- **[PLATFORM_A]:** ...
- **[PLATFORM_B]:** ...

**Part 3 — Key Differentiators**

2–4 bullet points summarizing the most significant differences between the platforms from a DTCC integration perspective.

# Platform Discovery Prompt

Use this prompt to discover Urban Digital Twin (UDT) platforms and classify them by ecosystem layer.

This prompt can be used in an AI web research chat or an AI CLI session. For more thorough Layer classification — including reassessment of a specific platform's layer assignment — run this prompt in a deep research interface. In a web chat, manually save the final Markdown response into `responses/`.

1. Open `docs/01-discovery-scope.md` and copy the full content
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

You are a research assistant helping to map the full **Urban Digital Twin (UDT) ecosystem** — core platforms, infrastructure backbones, and domain-specific analytics and simulation tools.
Your task is to discover platforms across all ecosystem layers and classify each one using the Layer criteria provided in the scope below.
Use primary sources to verify claims where possible.

**Before proceeding:** If the scope block below still contains the literal text `[PASTE_SCOPE_HERE]`, stop and ask the user to paste `docs/01-discovery-scope.md` before continuing.

# UDT Ecosystem Discovery — Layer Classification

This file defines the Layer classification system used in the **discovery phase** of the UDT ecosystem mapping study.
Paste the full content of this file into the `[PASTE_SCOPE_HERE]` slot in the discovery prompt before running a session.

---

## Layer Criteria

Assign each discovered platform exactly one Layer value using the observable criteria below. All four values are valid outputs from a discovery session.

| Layer           | Definition                                    | Criteria                                                                                          |
| --------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `core-platform` | Full UDT platform                             | Official docs claim city-scale digital twin; owns data + simulation + visualisation as one system |
| `backbone`      | Enabling infrastructure layer                 | Designed to be composed into other systems; API/SDK is primary interface, not end-user UI         |
| `domain-module` | Domain-specific urban analytics or simulation | Covers one urban domain (mobility, energy, climate…); outputs consumed by a larger UDT stack      |
| `excluded`      | Outside the study boundary                    | None of the above apply; note reason in one sentence                                              |

**Search scope:** Global city-scale Urban Digital Twin platforms and foundational building blocks (commercial and open-source). Cover all major geographies — include non-English-speaking markets and government-led initiatives, not only English-language or US/EU platforms. Do not limit discovery to platforms that self-identify as "digital twin" systems — backbone components and domain modules qualify and should appear with the appropriate `Layer` value.

---

### Required Entry: DTCC

**DTCC (Digital Twin Cities Centre)** is a required entry in every discovery session. Research it from primary sources — [dtcc.chalmers.se](https://dtcc.chalmers.se) and the [official GitHub repository](https://github.com/dtcc-platform) — the same way as any other platform. DTCC appears in the summary table and with a full per-platform section and a `Layer` assignment.

### Research Instructions

For each platform you identify (including DTCC):

1. Locate the software license (repository root, docs, or official site)
2. Identify the organization behind the platform
3. Assess the platform's type (e.g., visualization engine, data platform, simulation framework)
4. Assign a `Layer` value using the criteria table from the pasted scope content

Source policy:

- You may use secondary sources to discover candidate platforms.
- For final factual claims, prefer primary sources — but judgment-based Layer assignment from available evidence is acceptable.
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

| Name | Link | Layer | Reason |
| ---- | ---- | ----- | ------ |

All discovered platforms appear in the table, ordered by Layer: `core-platform` first, then `backbone`, then `domain-module`, then `excluded`. The `Reason` column is blank for in-scope platforms; for `excluded` platforms it contains a brief phrase (not a full sentence) explaining why.

Then return one section per platform, ordered by Layer (core-platform, backbone, domain-module, excluded).

**For in-scope platforms** (`core-platform`, `backbone`, `domain-module`), use a `##` heading followed by identification fields:

```
## <Platform Name>

- **Organization:** <name of the organization or project behind the platform> ([primary source](<url>))
- **Link:** [<short label>](<primary-url>)
- **License:** <exact license name, e.g. Apache-2.0, MIT — open-source / proprietary / open-core> ([primary source](<url>))
- **Type:** <e.g., visualization engine, data platform, simulation framework, standards implementation> ([primary source](<url>))
- **Layer:** <core-platform | backbone | domain-module>
```

Where possible, include inline Markdown links `[Description](https://...)` for factual claims.
If you cannot support a factual claim with a source, write `unknown` or `?` instead of guessing.

**For excluded platforms** (`excluded`), use a `##` heading followed by identification fields plus a single **Reason** field:

```
## <Platform Name>

- **Organization:** <name>
- **Link:** [<label>](<url>)
- **License:** <license>
- **Type:** <type>
- **Layer:** excluded
- **Reason:** <one sentence — why this platform is outside the study boundary>
```

---

### Example

**Example in-scope platform:**

## Example Platform

- **Organization:** Open City Foundation ([About](https://example-platform.org/about))
- **Link:** [example-platform.org](https://example-platform.org)
- **License:** Apache-2.0 — open-source ([License](https://example-platform.org/license))
- **Type:** 3D geospatial data platform ([Product](https://example-platform.org/product))
- **Layer:** backbone

**Example excluded platform:**

## Example Excluded Tool

- **Organization:** Generic Corp ([About](https://example-tool.org/about))
- **Link:** [example-tool.org](https://example-tool.org)
- **License:** MIT — open-source ([License](https://example-tool.org/license))
- **Type:** general-purpose data pipeline
- **Layer:** excluded
- **Reason:** General-purpose ETL tool with no urban or geospatial domain specialisation.

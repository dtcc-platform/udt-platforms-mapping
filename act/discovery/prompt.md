# Platform Discovery Prompt

Run this prompt through an AI CLI (Claude Code, Codex CLI, Gemini CLI). Tell the CLI: **"Run `act/discovery/prompt.md`"**. The CLI will ask you whether to run in CLI or Web mode and handle the rest.

## Required Inputs

- `plan/discovery/scope.md` — Layer classification criteria for the discovery cycle

## Run Modes

Before executing the prompt body below, ask the user:

> Run as CLI or Web?

Then proceed based on the answer:

- **CLI** — Read each file listed under **Required Inputs** and execute the prompt body, using the file contents as the Layer criteria. Save the response to `observe/discovery/cli-<model-short>.md`.
- **Web** — Produce a fully resolved prompt: inline the content of each file listed under **Required Inputs** at the top of the prompt under a heading naming the file (e.g., `## plan/discovery/scope.md`), then append the prompt body below. Output the resolved prompt as a single copy-ready block with no wrapper, narration, or BEGIN/END markers. Append a short note after the resolved block telling the user to paste it into a web chat (a deep research interface is preferred for thorough Layer classification) and save the response to `observe/discovery/web-<model-short>.md`.

If the user has not specified a mode, ask before proceeding — do not guess.

---

## Prompt

Before you begin:

- Do your planning internally; do not show a research plan unless explicitly asked.
- Return plain Markdown only.
- Return only the final deliverable in the exact format below.
- Do not add any product-native citation markers, sidebars, source appendices, methodology sections, or closing summaries.
- The main body of your response MUST be the three-part structure below. If your interface wraps it in a report shell or summary, that is fine — but the three parts must appear as the primary content.

You are a research assistant helping to map the full **Urban Digital Twin (UDT) ecosystem** — core platforms, infrastructure backbones, and domain-specific analytics and simulation tools.
Your task is to discover platforms across all ecosystem layers and classify each one using the Layer criteria from the required inputs.
Use primary sources to verify claims where possible.

# UDT Ecosystem Discovery — Layer Classification

Apply the Layer criteria supplied in the required inputs (`plan/discovery/scope.md`) to every platform you discover. All four Layer values (`core-platform`, `backbone`, `domain-module`, `excluded`) are valid outputs from a discovery session.

**Search scope:** Global city-scale Urban Digital Twin platforms and foundational building blocks (commercial and open-source). Cover all major geographies — include non-English-speaking markets and government-led initiatives, not only English-language or US/EU platforms. Do not limit discovery to platforms that self-identify as "digital twin" systems — backbone components and domain modules qualify and should appear with the appropriate `Layer` value.

---

### Required Entry: DTCC

**DTCC (Digital Twin Cities Centre)** is a required entry in every discovery session. Research it from primary sources — [dtcc.chalmers.se](https://dtcc.chalmers.se) and the [official GitHub repository](https://github.com/dtcc-platform) — the same way as any other platform. DTCC appears in the summary table and with a full per-platform section and a `Layer` assignment.

### Research Instructions

For each platform you identify (including DTCC):

1. Locate the software license (repository root, docs, or official site)
2. Identify the organization behind the platform
3. Assess the platform's type (e.g., visualization engine, data platform, simulation framework)
4. Assign a `Layer` value using the Layer criteria from the required inputs

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

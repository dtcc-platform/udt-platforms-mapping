# Platform Rating Prompt

Run this prompt through an AI CLI (Claude Code, Codex CLI, Gemini CLI). Tell the CLI: **"Run `act/rating/prompt.md`"**. The CLI will ask you whether to run in CLI or Web mode and handle the rest.

## Required Inputs

- `plan/rating/rubrics.md` — dimension rubrics used for 1–5 scoring
- `plan/rating/platforms.md` — the platforms to compare (comparison scope boundary, must include DTCC)
- `plan/rating/source-policy.md` — acceptable source types and citation conventions

## Run Modes

Before executing the prompt body below, ask the user:

> Run as CLI or Web?

Then proceed based on the answer:

- **CLI** — Read each file listed under **Required Inputs** and execute the prompt body, using rubrics as the scoring criteria, the platforms table as the comparison scope, and source-policy as the source/citation contract. Save the response to `observe/rating/cli-<model-short>.md`.
- **Web** — Produce a fully resolved prompt: inline the content of each file listed under **Required Inputs** at the top of the prompt under a heading naming the file (e.g., `## plan/rating/rubrics.md`), then append the prompt body below. Output the resolved prompt as a single copy-ready block with no wrapper, narration, or BEGIN/END markers. Append a short note after the resolved block telling the user to paste it into a web chat (Research or Deep Research interfaces are preferred) and save the response to `observe/rating/web-<model-short>.md`.

If the user has not specified a mode, ask before proceeding — do not guess.

---

## Prompt

Before you begin:

- If your interface supports Research or Deep Research, use it.
- Do your planning internally; do not show a research plan unless explicitly asked.
- Return plain Markdown only.
- Return only the final deliverable in the exact three-part format below.
- Do not add any product-native citation markers, sidebars, source appendices, methodology sections, executive summaries, or closing summaries.
- The main body of your response MUST be the three-part structure below. If your interface wraps it in a report shell or summary, that is fine — but the three parts must appear as the primary content.

You are a research assistant helping to map the Urban Digital Twin (UDT) platform landscape for DTCC.

Apply the source policy from the required inputs for all final factual claims. Use the rubrics from the required inputs to score every platform on all twelve dimensions. Treat the platforms table from the required inputs as the complete, authoritative comparison scope.

**Platforms to compare:** Use the rows in `plan/rating/platforms.md`. Compare every platform in that file. Do not add comparison candidates beyond those rows unless the user explicitly asks you to expand scope. Treat the DTCC row as the reference platform for Part 3 landscape observations — DTCC MUST be present in `plan/rating/platforms.md`; if it is absent, stop and ask the user to add it before producing any output.

The `Layer` value from each row in `plan/rating/platforms.md` is the authoritative layer assignment — carry it into Part 1 unchanged. Do not reassess or revise Layer. Your task is to score all twelve dimensions with primary source research and produce authoritative scores and analysis.

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
- Numeric citations `[1]`, footnotes `[^1]`, AI-specific formats `【†source】` — this overrides your default citation format; use `[Description](https://...)` inline links instead

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

One row per platform in `plan/rating/platforms.md`, six dimension score columns, and six functional category score columns. The `Layer` column carries the value from the corresponding row in `plan/rating/platforms.md` unchanged — do not reassess or revise it.

| Name | Link | Layer | Arch | Open | City | Mature | Integ | Gov | Viz | DM | Sim | IoT | Std | Infra |
| ---- | ---- | ----- | ---- | ---- | ---- | ------ | ----- | --- | --- | -- | --- | --- | --- | ----- |

Use bare numbers (1–5) in score cells. Use `?` for unknown. Do not write `/5`.

**Column legend:**

| Abbreviation | Full name              | Description                                                                                                      |
| ------------ | ---------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Layer        | Ecosystem Layer        | Architectural role carried from discovery: `core-platform`, `backbone`, or `domain-module` — not reassessed here |
| Arch         | Technical Architecture | Core tech stack, data models, deployment model, scalability                                                      |
| Open         | Openness & Licensing   | Source availability, license type, contribution model                                                            |
| City         | City-Scale Capability  | Urban domains covered, geographic extent, multi-domain analytics                                                 |
| Mature       | Maturity & Adoption    | Development status, known city deployments, community activity                                                   |
| Integ        | Integration Posture    | Public APIs, plugin ecosystem, interoperability                                                                  |
| Gov          | Governance Model       | Who controls the roadmap, contribution and funding model                                                         |
| Viz          | Visualization          | 3D rendering, GIS viewers, scene composition                                                                     |
| DM           | Data Management        | Data ingestion, storage, twin models, semantic layers                                                            |
| Sim          | Simulation             | Urban simulation, physics, scenario modelling                                                                    |
| IoT          | IoT Sensing            | Real-time data, sensor integration, device management                                                            |
| Std          | Standards              | Open standards implementation, interoperability frameworks                                                       |
| Infra        | Infrastructure         | Built environment, BIM/GIS, infrastructure lifecycle                                                             |

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

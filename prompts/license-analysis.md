# License Analysis Prompt

Use this prompt to evaluate the licensing of a UDT platform.

This prompt can be used in an AI web research chat or an AI CLI session. In a web chat, manually save the final Markdown response into `responses/`.

1. Open the discovery response file for your research session
2. Copy the header row and the platform row you want to analyse from the summary table
3. Replace `[PASTE_SELECTED_PLATFORM_HERE]` with those rows
4. Paste the completed prompt into your AI session

> **Save response as:** `responses/<platform>-license.md` — e.g., `responses/cesium-license.md`. See `docs/02-methodology.md` for the full convention.

---

> Paste into your AI session from this line onwards.

## Prompt

Before you begin:

- If your interface supports Research or Deep Research, use it.
- Do your planning internally; do not show a research plan unless explicitly asked.
- Return plain Markdown only.
- Return only the final deliverable in the exact format below.
- Do not add any product-native citation markers, sidebars, source appendices, methodology sections, executive summaries, or closing summaries.
- If your interface would normally produce a separate report structure, suppress it and follow this prompt's output contract instead.

You are a research assistant helping to evaluate the licensing of a UDT platform for a landscape review.
Your task is to assess the software license and data licensing posture of the platform identified in the table below.

**Platform (from discovery summary table):**

**Before proceeding:** If the placeholder below still contains the literal text `[PASTE_SELECTED_PLATFORM_HERE]`, stop and ask the user to supply the required data before continuing. Do not attempt to generate output without it.

[PASTE_SELECTED_PLATFORM_HERE]

Derive the platform name from the **Name** column. Use the **Link** column to locate the license source (check repository root for `LICENSE`/`COPYING`, SPDX identifier in package metadata, and official site documentation). Treat the **License** column value as a seed signal — verify it from primary sources and correct if needed.

Use primary sources for all final license claims (repository root, package metadata, official site documentation). Cite the source for every claim with an inline link `[Description](https://...)`. If you cannot confirm a license name, URL, or tier distinction from primary sources, state "unknown" or "unclear" — do not fabricate or infer without evidence.

---

### License Family Taxonomy

Classify the software license using exactly one of these families:

| Family                     | Examples             | Key Implication                                                                                                   |
| -------------------------- | -------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Permissive open source** | MIT, Apache 2.0, BSD | Can be used, modified, and redistributed with minimal restriction; commercial use allowed                         |
| **Copyleft (strong)**      | GPL v2, GPL v3       | Derivative works must also be open source under the same license                                                  |
| **Copyleft (weak)**        | LGPL, MPL            | Allows linking without triggering copyleft; only modifications to the licensed component must be shared           |
| **Open core**              | —                    | Core is open source, but significant features (enterprise integrations, hosted services, support) are proprietary |
| **Proprietary**            | —                    | Source code not publicly available; usage governed by commercial license or SaaS terms                            |

---

### Openness & Licensing Scoring Rubric

Assign a score from 1–5 using this rubric:

| Score | Description                                                                                   |
| ----- | --------------------------------------------------------------------------------------------- |
| 5     | Permissive open-source software + open data standards                                         |
| 4     | Copyleft open-source, or open-core with a substantial open component                          |
| 3     | Open-core with significant proprietary features, or open source with restrictive data formats |
| 2     | Primarily proprietary with limited open components or open APIs                               |
| 1     | Fully proprietary, no public source, no open APIs                                             |

---

### Research Instructions

Work through each item:

1. **Locate the license** — check repository root (`LICENSE`, `COPYING`), SPDX identifier in package metadata, and official site documentation
2. **Identify the license family** — use the taxonomy above
3. **Note any data format lock-in** — does the platform use open geospatial standards (OGC, CityGML, IFC)? Are output formats proprietary?
4. **Check for community vs. enterprise tier split** — are significant features gated behind a paid tier?
5. **Assign an Openness & Licensing score (1–5)** — use the rubric above with a one-sentence rationale

Source policy:

- Use this evidence priority order for license claims: repository root license files first, package metadata or SPDX declarations second, official product or documentation pages third, and legal or pricing pages as supporting context for proprietary or open-core tier distinctions.
- Separate software licensing evidence from commercial packaging or paid-tier evidence.
- You may use secondary sources only to discover a likely repository or official documentation location, not to support final license claims in the saved output.
- If a paid tier, hosted service, bundled dataset licence, or edition split cannot be verified from primary sources, state `unknown` or `unclear`.

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

**Score notation:** the Score output field uses a bare number only — e.g., `**Score:** 3`. Do not use the `(X/5)` inline form; that notation is for discovery and comparison profile headings, not for this flat field list.

---

### Output Format

Begin your response with this metadata block — fill in your model name/version and today's date:

```yaml
model: <your model name and version>
date: <YYYY-MM-DD>
prompt: license-analysis
```

Structure your response with the following sections:

#### Software License

- **License identified:** [name and SPDX identifier if available]
- **Source located at:** [URL or location]
- **License family:** [one of the five families above]
- **Summary:** 2–3 sentences on what the license permits and restricts

#### Data Licensing

- **Open geospatial standards used:** [CityGML / IFC / OGC / none / unknown]
- **Output data formats:** [open / proprietary / mixed]
- **Data format lock-in risk:** [low / medium / high] with brief explanation
- **Bundled dataset licenses:** [if applicable]

#### Community vs. Enterprise Split

- Is there a community edition distinct from an enterprise edition? [yes / no / unclear]
- If yes: what features are gated behind the paid tier?

#### Openness & Licensing Score

- **Score:** [1–5]
- **Rationale:** [one sentence]

#### Open Questions

Any aspects of the license that were unclear, unavailable, or require further investigation.

---

**Example response (fictional platform — for structure reference only):**

---

```yaml
model: example-model-1.0
date: 2026-03-29
prompt: license-analysis
```

#### Software License

- **License identified:** Apache License 2.0 (SPDX: Apache-2.0)
- **Source located at:** [LICENSE file in repository root](https://github.com/example/open-city-platform/blob/main/LICENSE)
- **License family:** Permissive open source
- **Summary:** Apache-2.0 permits use, modification, and redistribution with minimal restriction. Commercial use is allowed. Derivative works are not required to be open source, but must retain the original copyright notice and NOTICE file.

#### Data Licensing

- **Open geospatial standards used:** CityGML 3.0, OGC WFS
- **Output data formats:** Open (GeoJSON, CityGML)
- **Data format lock-in risk:** Low — all output formats are open standards with broad tooling support
- **Bundled dataset licenses:** Not applicable; no datasets are bundled

#### Community vs. Enterprise Split

- Is there a community edition distinct from an enterprise edition? No
- The repository contains a single edition under Apache-2.0 with no feature gating. Confirmed via [repository README](https://github.com/example/open-city-platform/blob/main/README.md).

#### Openness & Licensing Score

- **Score:** 5
- **Rationale:** Permissive open-source licence (Apache-2.0) confirmed from primary source, all output formats use open OGC standards, and no enterprise tier exists.

#### Open Questions

None — license is clearly stated in the repository root and all claims were verified from primary sources.

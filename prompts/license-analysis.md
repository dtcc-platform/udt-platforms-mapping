# License Analysis Prompt

Use this prompt to evaluate the licensing of a UDT platform.

1. Open the discovery response file for your research session
2. Copy the header row and the platform row you want to analyse from the summary table
3. Replace `[PASTE_SELECTED_PLATFORM_HERE]` with those rows
4. Paste the completed prompt into your AI session

> **Source of truth for license taxonomy and scoring:** `docs/license-review.md`
> **Save response as:** `responses/<platform>-license.md` — e.g., `responses/cesium-license.md`. See `docs/methodology.md` for the full convention.

---

## Prompt

You are a research assistant helping to evaluate the licensing of a UDT platform for a landscape review.
Your task is to assess the software license and data licensing posture of the platform identified in the table below.

**Platform (from discovery summary table):**

[PASTE_SELECTED_PLATFORM_HERE]

Derive the platform name from the **Name** column. Use the **Link** column to locate the license source (check repository root for `LICENSE`/`COPYING`, SPDX identifier in package metadata, and official site documentation). Treat the **License** column value as a seed signal — verify it from primary sources and correct if needed.

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

### Review Checklist

Work through each item:

1. **Locate the license** — check repository root (`LICENSE`, `COPYING`), SPDX identifier in package metadata, and official site documentation
2. **Identify the license family** — use the taxonomy above
3. **Note any data format lock-in** — does the platform use open geospatial standards (OGC, CityGML, IFC)? Are output formats proprietary?
4. **Check for community vs. enterprise tier split** — are significant features gated behind a paid tier?
5. **Assign an Openness & Licensing score (1–5)** — use the rubric above with a one-sentence rationale

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

**Score notation:** in the Score field, bare number only (1–5). Do not write `/5`.

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

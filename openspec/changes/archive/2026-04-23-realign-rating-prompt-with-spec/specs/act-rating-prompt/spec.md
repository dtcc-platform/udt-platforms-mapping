## MODIFIED Requirements

### Requirement: Comparison prompt Part 1 scoring table includes functional category columns

The Part 1 scoring table SHALL include a `Layer` column and the six dimension columns and six functional category columns. It SHALL NOT include a `Relevance` column — Relevance is retired.

The `Layer` column SHALL appear immediately after `Link`. It SHALL carry the Layer value from the corresponding row in `plan/rating/platforms.md` unchanged. The comparison AI SHALL NOT reassess or revise the Layer assignment — Layer is owned by the discovery phase.

Each score column SHALL use the same 1–5 integer scoring format — bare integer, `?` for unknown, no `/5` suffix in table cells.

The prompt SHALL include a legend immediately below the Part 1 table instruction listing each abbreviated column header with its full name and one-line description.

#### Scenario: Researcher reads the Part 1 table

- **WHEN** an AI responds to the comparison prompt
- **THEN** the Part 1 table header contains exactly: `Name`, `Link`, `Layer`, `Arch`, `Open`, `City`, `Mature`, `Integ`, `Gov`, `Viz`, `DM`, `Sim`, `IoT`, `Std`, `Infra`

#### Scenario: Researcher compares functional strengths across platforms

- **WHEN** an AI responds to the comparison prompt
- **THEN** every platform row contains a numeric 1–5 score (or `?`) in every dimension and category column, and the Layer value from the discovery row

#### Scenario: Layer value is carried through unchanged

- **WHEN** `plan/rating/platforms.md` contains a platform row with `Layer=backbone`
- **THEN** the Part 1 table contains `backbone` in the Layer column for that platform; the comparison AI does not reassess or revise it

### Requirement: Comparison prompt enforces agent-agnostic output structure

The prompt template SHALL include a concrete example of the per-platform profile structure so any agent can reproduce the exact shape mechanically. The prompt SHALL comply with the shared Markdown contract defined in `prompt-markdown-format`.

In addition to that shared contract, the prompt SHALL specify:

- **Profile heading level:** every platform profile SHALL use `###` as the top-level heading so profiles nest consistently under part headings
- **Score notation:** dimension scores SHALL always be written as `X/5` (e.g., `4/5`) — no other formats (`★★★★☆`, `4 out of 5`, `80%`, bold numbers) are permitted
- **Score placement:** in profiles, scores SHALL appear inline with the dimension label as `**Dimension (X/5):**` — e.g., `**Technical Architecture (4/5):**`
- **Score in table:** in the scoring table, score cells SHALL contain only the numeric value (e.g., `4`) with `?` for unknown — no `/5` suffix in table cells
- **Research-mode suppression:** if the interface supports Research or Deep Research, the prompt SHALL instruct the model to do planning internally and return only the required three-part comparison output, with no generated research plan, executive summary, source appendix, methodology section, or provider-specific report wrapper

The prompt SHALL include a concrete example profile for one fictional platform demonstrating the exact heading levels, field labels, score notation, and sources section structure.

#### Scenario: Two agents respond to the same prompt

- **WHEN** a researcher runs the comparison prompt on ChatGPT and on Claude
- **THEN** both responses use identical heading levels, field labels, and score notation — the only difference is the content

#### Scenario: Response is opened in a standard Markdown viewer

- **WHEN** a researcher saves the response as a `.md` file and opens it in GitHub, VS Code, Obsidian, or Typora
- **THEN** all formatting renders correctly with no raw syntax visible, no broken elements, and no AI-specific artifacts

#### Scenario: Model uses AI-specific citation format

- **WHEN** an AI model would normally respond with numeric bracket citations or footnotes
- **THEN** the prompt instruction overrides this and the model uses `[Description](https://...)` inline links instead

#### Scenario: Research-mode interface would normally emit a report shell

- **WHEN** a researcher runs the comparison prompt in a Research or Deep Research web interface
- **THEN** the response omits any exposed research plan, executive summary, or provider-native report shell and contains only the required three parts in the required order

## MODIFIED Requirements

### Requirement: Comparison prompt requests a three-part structured output

The prompt template SHALL instruct the model to produce output in exactly three parts, in this order:

1. **Scoring table** — one row per platform, six dimension score columns, six functional category score columns, plus a link column
2. **Per-platform profiles** — one structured profile per platform with all six dimension analyses, sources, and scores
3. **Landscape observations** — four `####` subheadings, each followed by a bullet list: `#### Landscape Gaps`, `#### DTCC's Position`, `#### Comparable Platforms`, `#### Complementary Platforms`

#### Scenario: Researcher extracts summary data

- **WHEN** an AI responds to the comparison prompt
- **THEN** Part 1 contains a Markdown table with one row per platform, numeric dimension scores per dimension column, and numeric category scores per category column

#### Scenario: Researcher reads a platform profile

- **WHEN** a researcher reads Part 2 of the response
- **THEN** each platform has a self-contained profile with organization, link, license, type, dimension analyses with scores, and a sources section

#### Scenario: Researcher understands DTCC's position

- **WHEN** a researcher reads Part 3
- **THEN** the response contains exactly four `####` subheadings — `#### Landscape Gaps`, `#### DTCC's Position`, `#### Comparable Platforms`, `#### Complementary Platforms` — each followed by a bullet list

#### Scenario: Researcher scans Part 3 across two agent responses

- **WHEN** a researcher opens two comparison responses run on different AI agents
- **THEN** Part 3 has the same four subheadings in the same order in both responses

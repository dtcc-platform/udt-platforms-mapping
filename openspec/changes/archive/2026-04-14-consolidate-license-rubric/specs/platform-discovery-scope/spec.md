## MODIFIED Requirements

### Requirement: docs/01-scope.md contains all 13 scoring rubrics as the canonical source
`docs/01-scope.md` SHALL contain the Relevance rubric plus all 12 dimension and functional category rubrics (Arch, Open, City, Mature, Integ, Gov, Viz, DM, Sim, IoT, Std, Infra). This file is the single canonical source for all rubric definitions; the prompt files consume its content via the `[PASTE_SCOPE_HERE]` mechanism.

The **Openness & Licensing (`Open`)** rubric SHALL define the following criteria per level, with data format and copyleft terms made explicit:

| Score | Criteria |
| ----- | -------- |
| 5 | Permissive open-source (MIT/Apache/BSD) + open data formats (OGC standards, CityGML, IFC, or equivalent), no SaaS dependency |
| 4 | Copyleft open-source (strong: GPL — derivatives must be open; weak: LGPL/MPL — linking permitted without triggering copyleft), or open-core with substantial open component |
| 3 | Open-core with significant proprietary features, or open source with restrictive data formats (proprietary export formats with no open standard alternative) |
| 2 | Primarily proprietary with limited open components or open APIs |
| 1 | Fully proprietary, no public source, no open APIs |
| 0 | Not assessed |

#### Scenario: Researcher updates a rubric
- **WHEN** a researcher changes the criteria for a dimension score level
- **THEN** they edit `docs/01-scope.md` only; the prompts receive the updated rubric at run time via the paste step

#### Scenario: Scorer assesses a GPL-licensed platform
- **WHEN** a scorer encounters a platform under GPL v2 or v3
- **THEN** the rubric parenthetical at level 4 clarifies this is strong copyleft (derivatives must be open) and scores as 4, noting the integration implication in the rationale

#### Scenario: Scorer assesses an LGPL-licensed platform
- **WHEN** a scorer encounters a platform under LGPL or MPL
- **THEN** the rubric parenthetical at level 4 clarifies this is weak copyleft (linking permitted) and scores as 4

#### Scenario: Scorer assesses a platform with proprietary export formats
- **WHEN** a scorer encounters a platform that is open-source but only exports in proprietary binary formats with no OGC/CityGML/IFC alternative
- **THEN** the rubric at level 3 clarifies this counts as "restrictive data formats" and scores as 3, not 5

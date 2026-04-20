## MODIFIED Requirements

### Requirement: docs/01-scope.md contains all 13 scoring rubrics as the canonical source

`docs/01-scope.md` SHALL contain the Relevance rubric plus all 12 dimension and functional category rubrics (Arch, Open, City, Mature, Integ, Gov, Viz, DM, Sim, IoT, Std, Infra). This file is the single canonical source for all rubric definitions; the prompt files consume its content via the `[PASTE_SCOPE_HERE]` mechanism.

The **Openness & Licensing (`Open`)** rubric SHALL define the following criteria per level, with data format and copyleft terms made explicit:

| Score | Criteria                                                                                                                                                                    |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 5     | Permissive open-source (MIT/Apache/BSD) + open data formats (OGC standards, CityGML, IFC, or equivalent), no SaaS dependency                                                |
| 4     | Copyleft open-source (strong: GPL — derivatives must be open; weak: LGPL/MPL — linking permitted without triggering copyleft), or open-core with substantial open component |
| 3     | Open-core with significant proprietary features, or open source with restrictive data formats (proprietary export formats with no open standard alternative)                |
| 2     | Primarily proprietary with limited open components or open APIs                                                                                                             |
| 1     | Fully proprietary, no public source, no open APIs                                                                                                                           |
| 0     | Not assessed                                                                                                                                                                |

The file SHALL retain a brief prose section defining what a UDT platform is. This section's purpose is to frame discovery search queries — it SHALL describe what to look for (search boundary), not what to exclude. Exclusion decisions SHALL be delegated entirely to the Relevance rubric. The definition SHALL NOT contain explicit exclusion language such as "are out of scope" or "out of scope even if".

The definition SHALL name enabling-layer and infrastructure-twin platforms as positive examples of what falls within the search boundary, so that borderline candidates (e.g., device twin frameworks, infrastructure twin engines) surface during discovery and are evaluated by the rubric rather than filtered before scoring.

#### Scenario: Researcher reads scope before starting a discovery session

- **WHEN** a researcher opens `docs/01-scope.md` before running the discovery prompt
- **THEN** they find the Relevance 0–5 rubric, all 12 dimension/category rubrics, and a brief search-boundary definition of what a UDT platform is

#### Scenario: Discovery AI uses the definition to frame search queries

- **WHEN** a discovery AI reads the definition section
- **THEN** it uses the definition to anchor search queries toward urban/city-scale platforms, including enabling layers and infrastructure twins, without pre-filtering candidates before scoring

#### Scenario: Borderline platform reaches the rubric

- **WHEN** a platform (e.g., a device twin framework or BIM engine) is encountered during discovery
- **THEN** the definition does not exclude it; the platform is brought forward as a candidate and assessed against the Relevance rubric, which assigns score 1 if it is out of scope

#### Scenario: Researcher prepares a prompt session

- **WHEN** a researcher is about to run a discovery or comparison session
- **THEN** they paste the full content of `docs/01-scope.md` into the `[PASTE_SCOPE_HERE]` slot in the prompt

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

# Spec: relevance-score

## Purpose

TBD — Defines the Relevance 0–5 rubric used to score platform candidates in the UDT platform study. The rubric replaces the previous binary include/exclude gate and serves as the canonical scoring standard for the `Relevance` column in the platform inventory CSV.

## Requirements

### Requirement: Relevance rubric defined in docs/01-scope.md

> **RETIRED** — Relevance (0–5) is retired as a scored field. The Layer criteria table in `docs/01-discovery-scope.md` replaces the Relevance rubric as the inclusion and classification mechanism. Layer uses observable criteria (checkable against primary sources) rather than a scored rubric, making classification consistent across sessions without judgment-based scoring.
>
> Migration: Remove the Relevance column from the inventory CSV. Remove Relevance scoring from both prompts. Use the Layer criteria table in `docs/01-discovery-scope.md` for platform classification.

The repository SHALL define a Relevance 0–5 rubric in `docs/01-scope.md` that replaces the binary include/exclude gate previously defined as three named inclusion criteria and three named exclusion criteria. The rubric SHALL be the canonical reference for what belongs in the study and the scoring standard for the `Relevance` column in the platform inventory CSV.

#### Scenario: Researcher assesses whether a platform belongs in the study
- **WHEN** a researcher encounters a candidate platform and consults `docs/01-scope.md`
- **THEN** the rubric provides a 0–5 scale with criteria per level so they can assign a score rather than a binary yes/no

#### Scenario: Researcher assigns a Relevance score of 0
- **WHEN** a researcher scores a platform as Relevance 0
- **THEN** the rubric defines 0 as "out of scope / not assessed" — the platform does not appear as a meaningful row in comparisons but may remain in the CSV with all score columns set to 0

#### Scenario: Researcher assigns a Relevance score of 5
- **WHEN** a researcher scores a platform as Relevance 5
- **THEN** the rubric defines 5 as "Explicit UDT platform, purpose-built for city-scale urban digital twin use cases"

### Requirement: Relevance rubric covers the full 0–5 range with level descriptions

> **RETIRED** — Retired with Relevance. The 0–5 scale is replaced by the four-row Layer criteria table (`core-platform`, `backbone`, `domain-module`, `excluded`).
>
> Migration: No replacement. The Layer criteria table is the new classification system.

The Relevance rubric in `docs/01-scope.md` SHALL define criteria for all six levels (0 through 5). Each level SHALL include a one-line description sufficient to distinguish it from adjacent levels.

| Level | Meaning |
| ----- | ------- |
| 5 | Explicit UDT — platform presents itself as a city-scale urban digital twin |
| 4 | City-Scale Capabilities — strong multi-domain urban capabilities without explicit UDT framing |
| 3 | Adjacent Architecture — foundational building block commonly used in UDT systems |
| 2 | Marginal — tangential relevance; could be used in a UDT context but not designed for it |
| 1 | Out of scope candidate — assessed and found outside the study boundary |
| 0 | Not assessed |

#### Scenario: AI model scores a platform at discovery time
- **WHEN** an AI model applies the Relevance rubric during a discovery session
- **THEN** it assigns a score 0–5 per the level descriptions, not a binary include/exclude decision

#### Scenario: Researcher filters the inventory by relevance
- **WHEN** a researcher filters `docs/05-platform-inventory.csv` to Relevance >= 3
- **THEN** they get platforms that qualify under the previous inclusion criteria (Explicit UDT, City-Scale Capabilities, Adjacent Architecture or Governance)

### Requirement: docs/01-scope.md contains all 13 scoring rubrics as the canonical source

> **RETIRED** — `docs/01-scope.md` is retired. The 13 rubrics are split: `docs/01-discovery-scope.md` contains the Layer criteria table (replaces Relevance rubric); `docs/01-comparison-scope.md` contains the 12 dimension rubrics.
>
> Migration: See `platform-discovery-scope-file` and `platform-comparison-scope-file` specs.

`docs/01-scope.md` SHALL contain the Relevance rubric plus all 12 dimension and functional category rubrics (Arch, Open, City, Mature, Integ, Gov, Viz, DM, Sim, IoT, Std, Infra). This file is the single canonical source for all rubric definitions; the prompt files consume its content via the `[PASTE_SCOPE_HERE]` mechanism.

#### Scenario: Researcher updates a rubric
- **WHEN** a researcher changes the criteria for a dimension score level
- **THEN** they edit `docs/01-scope.md` only; the prompts receive the updated rubric at run time via the paste step

#### Scenario: AI session receives rubrics
- **WHEN** a researcher prepares a discovery or comparison session
- **THEN** they paste the content of `docs/01-scope.md` into the `[PASTE_SCOPE_HERE]` slot in the prompt, supplying all rubrics to the model in one step

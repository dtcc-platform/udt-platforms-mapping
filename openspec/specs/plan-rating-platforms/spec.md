# Spec: plan-rating-platforms

## Purpose

Defines the `plan/rating/platforms.md` file — the three-column (Name, Link, Layer) table holding the per-run platform selection for a rating cycle, which serves as the comparison-scope boundary and carries the DTCC inclusion requirement.

## Requirements

### Requirement: plan/rating/platforms.md file exists

The repository SHALL contain a file at `plan/rating/platforms.md` that defines the set of platforms selected for the current rating cycle run. The file is a declared input of `act/rating/prompt.md` and is resolved by the AI in CLI mode or inlined by the resolver in Web mode.

#### Scenario: Researcher prepares a rating session

- **WHEN** a researcher prepares to run the rating prompt
- **THEN** they find the platform selection at `plan/rating/platforms.md`

#### Scenario: Rating prompt is run without the file

- **WHEN** the rating prompt is run but `plan/rating/platforms.md` is missing
- **THEN** the AI CLI fails to resolve the Required Inputs and cannot proceed, surfacing a clear error naming the missing file

### Requirement: platforms.md uses a three-column GFM table

The file SHALL contain a Markdown pipe table with exactly three columns in this order: **Name**, **Link**, **Layer**. Each data row SHALL represent one platform to include in the current rating cycle. The table SHALL sit below a short header paragraph explaining the file's purpose.

The `Layer` value SHALL be carried from the relevant discovery response summary table unchanged. The rating model SHALL NOT reassess or revise the Layer assignment — Layer is owned by the discovery phase.

#### Scenario: Researcher curates the comparison set

- **WHEN** a researcher selects platforms from a discovery response for a rating cycle run
- **THEN** they copy the relevant `Name`, `Link`, and `Layer` cells into rows in `plan/rating/platforms.md`

#### Scenario: Rating output preserves Layer assignment

- **WHEN** the rating model produces its Part 1 scoring table
- **THEN** the `Layer` column for each platform matches the value in `plan/rating/platforms.md`, unchanged

### Requirement: platforms.md is the comparison-scope boundary

The rating prompt SHALL treat the rows in `plan/rating/platforms.md` as the complete and authoritative set of platforms to compare. The rating model SHALL NOT add platforms that are not listed in the file, and SHALL NOT drop platforms that are listed.

#### Scenario: Rating model runs in Web mode with deep research

- **WHEN** the rating prompt is resolved in Web mode and run in a deep research interface
- **THEN** the model limits its comparison to the rows in the resolved `plan/rating/platforms.md` content and does not introduce additional platforms

#### Scenario: Researcher expands the comparison

- **WHEN** a researcher wants to add a platform to the current rating cycle
- **THEN** they add a row to `plan/rating/platforms.md` and re-run the rating prompt — they do not edit `act/rating/prompt.md`

### Requirement: platforms.md must include the DTCC row

The file SHALL include a row for DTCC (Digital Twin Cities Centre) so the rating prompt's Part 3 landscape observations can orient around DTCC. The DTCC row SHALL use the same three-column shape as every other row.

#### Scenario: Researcher assembles a rating selection

- **WHEN** a researcher fills `plan/rating/platforms.md` for a cycle run
- **THEN** the DTCC row is present alongside the other selected platforms

#### Scenario: DTCC row is missing

- **WHEN** the rating prompt is run without the DTCC row present in `plan/rating/platforms.md`
- **THEN** Part 3 landscape observations cannot orient around DTCC; the rating prompt surfaces the missing DTCC row as a scope error before producing output

### Requirement: platforms.md is per-run data, not a slow-moving definition

`plan/rating/platforms.md` SHALL be treated as per-cycle-run data, distinct in nature from `plan/rating/rubrics.md` and `plan/rating/source-policy.md`, which SHALL be treated as slow-moving definitions shared across cycle runs.

The file's header paragraph SHALL state this distinction so readers understand that `platforms.md` iterates per run while its sibling files are comparatively stable. The git history of `plan/rating/platforms.md` SHALL serve as the authoritative record of which platforms were compared in each cycle run — reviewers SHALL consult `git log plan/rating/platforms.md` to answer "what did we compare in cycle N?" questions.

#### Scenario: Second rating cycle begins

- **WHEN** a researcher starts a new rating cycle run with a different platform selection
- **THEN** they update `plan/rating/platforms.md` for that run; `rubrics.md` and `source-policy.md` stay stable across runs

#### Scenario: Reviewer asks "what did we compare last cycle?"

- **WHEN** a reviewer wants to know the exact set of platforms compared in a previous rating cycle run
- **THEN** `git log plan/rating/platforms.md` and the diffs between runs are the authoritative answer

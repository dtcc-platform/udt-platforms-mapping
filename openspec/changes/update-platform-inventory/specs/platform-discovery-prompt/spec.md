## MODIFIED Requirements

### Requirement: Discovery prompt response begins with a required summary table

The prompt template SHALL instruct the model to output the summary table immediately after the metadata block and before any per-platform sections. The table is required and SHALL use the following columns:

**Name**, **Link**, **License**, **Type**, **Arch**, **Open**, **City**, **Mature**, **Integ**, **Gov**, **Criterion**

The `Criterion` column SHALL contain one of these exact values: the three inclusion criterion labels (`Explicit UDT`, `City-Scale Capabilities`, `Adjacent Architecture or Governance`) or one of the three exclusion criterion labels (`Spec or Standard`, `Single Domain`, `General Purpose`).

Score columns (Arch, Open, City, Mature, Integ, Gov) SHALL contain bare numbers (1–5) for included platforms, `-1` for excluded platforms, or `?` for unknown — no `/5` suffix.

Excluded platforms SHALL appear in the summary table with `-1` in all six score columns and their exclusion criterion label in the `Criterion` column.

#### Scenario: Researcher opens a discovery response to start a comparison

- **WHEN** a researcher opens a saved discovery response
- **THEN** the summary table appears at the top (after the metadata block), before any per-platform detail sections, with a `Criterion` column and any excluded platforms listed with `-1` scores

#### Scenario: Rows are pasted into the comparison prompt

- **WHEN** a researcher copies rows of included platforms from the summary table and pastes them into the comparison prompt
- **THEN** the comparison prompt receives platform names, license, type, and six seed scores as context

#### Scenario: Discovery session identifies platforms outside the inclusion boundary

- **WHEN** the model encounters platforms that do not meet any inclusion criterion
- **THEN** those platforms appear in the summary table with `-1` scores in all score columns and their exclusion criterion label in the `Criterion` column

#### Scenario: Excluded platforms have per-platform sections

- **WHEN** excluded platforms appear in the summary table
- **THEN** per-platform `##` sections for excluded platforms are NOT required — they MAY be omitted; included platforms always have per-platform sections

# Spec: plan-udt-platform-comparison-platforms

## Purpose

Defines the `plan/udt-platform-comparison-platforms.md` file — the two-column selection table holding the per-run `platform` subset for the comparison cycle.

## Requirements

### Requirement: platforms.md file exists

The repository SHALL contain a file at `plan/udt-platform-comparison-platforms.md`.

#### Scenario: Researcher finds comparison platform selection

- **WHEN** a researcher opens `plan/`
- **THEN** `plan/udt-platform-comparison-platforms.md` is available as the comparison platform selection file

### Requirement: platforms.md uses a two-column GFM table

The file SHALL contain a Markdown pipe table with exactly two columns in this order:

- `Name`
- `Link`

Each data row SHALL represent one selected row that already qualifies as `Type = platform` from the `udt-platforms` cycle.

#### Scenario: Researcher reviews platform selection table

- **WHEN** a researcher opens `plan/udt-platform-comparison-platforms.md`
- **THEN** the file contains a two-column GFM table with `Name` and `Link`
- **THEN** each data row represents a selected `Type = platform` row

### Requirement: platforms.md is the comparison-scope boundary

The comparison prompt SHALL treat the rows in `plan/udt-platform-comparison-platforms.md` as the complete and authoritative set of platforms to compare.

#### Scenario: Comparison prompt uses selected rows

- **WHEN** the comparison prompt runs
- **THEN** it treats `plan/udt-platform-comparison-platforms.md` as the authoritative comparison scope

### Requirement: platforms.md must include the DTCC row

The file SHALL include a row for DTCC so the comparison prompt's landscape observations can orient around DTCC.

#### Scenario: DTCC is present

- **WHEN** a researcher reviews `plan/udt-platform-comparison-platforms.md`
- **THEN** the file includes a row for DTCC

# Spec: observe-platform-comparison

## Purpose

Defines the observed output contract for this research action.

## Requirements

### Requirement: Platform comparison observations use the governed response contract

Saved platform comparison web responses SHALL use filenames matching `observe/platform-comparison-<model-short>.md`.

Each saved platform comparison response SHALL begin with a fenced YAML metadata block containing `model`, `date`, and `prompt: platform-comparison`.

Each saved platform comparison response SHALL contain exactly three parts:

- `Part 1 — Scoring Table`
- `Part 2 — Platform Profiles`
- `Part 3 — Landscape Observations`

The scoring table SHALL contain exactly these columns:

- `Name`
- `Link`
- `Arch`
- `Open`
- `City`
- `Mature`
- `Integ`
- `Gov`
- `Viz`
- `DM`
- `Sim`
- `IoT`
- `Std`
- `Infra`

Score cells SHALL use bare `1`-`5` values or `?` for unknown.

Each platform profile SHALL use a `###` heading and include organization, link, description, type, license, dimension analyses with inline scores, and a `#### Sources` section.

Landscape observations SHALL include exactly these subheadings in this order: `Landscape Gaps`, `DTCC's Position`, `Comparable Platforms`, and `Complementary Platforms`.

#### Scenario: Researcher saves platform comparison output

- **WHEN** a researcher saves a platform comparison web response
- **THEN** the response follows the metadata, scoring table, profile, and landscape observation contract

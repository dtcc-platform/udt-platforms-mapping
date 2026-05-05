# Spec: observe-platform-discovery

## Purpose

Defines the observed output contract for this research action.

## Requirements

### Requirement: Platform discovery observations use the governed response contract

Saved platform discovery web responses SHALL use filenames matching `observe/platform-discovery-<model-short>.md`.

Each saved platform discovery response SHALL begin with a fenced YAML metadata block containing `model`, `date`, and `prompt: platform-discovery`.

Each saved platform discovery response SHALL include a summary table with exactly these columns:

- `Name`
- `Link`
- `Type`
- `Reason`

Each platform discovery row SHALL assign exactly one `Type` value: `platform`, `framework`, `module`, or `excluded`.

`Reason` SHALL be blank for in-scope rows and SHALL contain a brief phrase for excluded rows.

Each saved platform discovery response SHALL include one `##` section per artifact with `Link`, `Type`, and `Reason` when excluded.

#### Scenario: Researcher saves platform discovery output

- **WHEN** a researcher saves a platform discovery web response
- **THEN** the response follows the metadata, table, Type, Reason, and section contract

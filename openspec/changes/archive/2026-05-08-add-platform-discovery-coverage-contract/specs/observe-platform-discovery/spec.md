## MODIFIED Requirements

### Requirement: Platform discovery observations use the governed response contract

Saved platform discovery web responses SHALL use filenames matching `observe/platform-discovery-<model-short>.md`.

Each saved platform discovery response SHALL begin with a fenced YAML metadata block containing `model`, `date`, and `prompt: platform-discovery`.

Each saved platform discovery response SHALL include a coverage statement before the summary table.

The coverage statement SHALL report total artifact count and counts by `Type`.

The coverage statement SHALL state whether platform discovery coverage targets were met.

When coverage targets were not met, the coverage statement SHALL identify the unmet targets and explain the search or evidence limitation.

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
- **THEN** the response follows the metadata, coverage statement, table, Type, Reason, and section contract

#### Scenario: Discovery output misses a coverage target

- **WHEN** a saved platform discovery response does not satisfy one or more coverage targets
- **THEN** the coverage statement names the unmet target
- **THEN** the coverage statement explains why the target was not met

## ADDED Requirements

### Requirement: Entity discovery observations use the governed response contract

Saved entity discovery web responses SHALL use filenames matching `observe/entity-discovery-<model-short>.md`.

Each saved entity discovery response SHALL begin with a fenced YAML metadata block containing `model`, `date`, and `prompt: entity-discovery`.

Each saved entity discovery response SHALL include a coverage statement before the summary table.

The coverage statement SHALL report total candidate count and counts by `Type`.

The coverage statement SHALL state whether discovery coverage targets were met.

When coverage targets were not met, the coverage statement SHALL identify the unmet targets and explain the search or evidence limitation.

Each saved entity discovery response SHALL include a summary table with exactly these columns in this order:

- `Name`
- `Type`
- `Link`

Each entity discovery row SHALL assign exactly one `Type` value: `platform`, `framework`, `module`, `initiative`, or `excluded`.

The summary table SHALL NOT include `Uses`, `Reason`, `Description`, `EntityKind`, or other detail columns.

Each saved entity discovery response SHALL include one `##` section per entity.

Each entity section SHALL include a concise paragraph describing what the entity is, why the assigned `Type` fits, and any uncertainty.

For initiative rows, the entity paragraph SHALL identify known technical substrate with `Uses: <artifact names>` when clear, or `Uses: ?` when unclear.

For excluded rows, the entity paragraph SHALL explain the exclusion reason.

#### Scenario: Researcher saves entity discovery output

- **WHEN** a researcher saves an entity discovery web response
- **THEN** the response follows the metadata, coverage statement, table, Type, and entity section contract

#### Scenario: Summary table is rendered

- **WHEN** an entity discovery response renders its summary table
- **THEN** the table columns are exactly `Name`, `Type`, and `Link`
- **THEN** `Link` is the final column
- **THEN** `Uses` and `Reason` are not table columns

#### Scenario: Initiative uses a known artifact

- **WHEN** an entity discovery response includes an initiative whose technical substrate is known
- **THEN** the initiative row uses `Type = initiative`
- **THEN** the initiative section records `Uses: <artifact names>` in prose

#### Scenario: Initiative substrate is unclear

- **WHEN** an entity discovery response includes an initiative whose technical substrate cannot be identified
- **THEN** the initiative row uses `Type = initiative`
- **THEN** the initiative section records `Uses: ?` in prose

#### Scenario: Excluded entity is reported

- **WHEN** an entity discovery response includes an excluded boundary candidate
- **THEN** the entity row uses `Type = excluded`
- **THEN** the entity section explains the exclusion reason in prose

## MODIFIED Requirements

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

Each saved entity discovery response SHALL include a `## Known Candidate Recall Check` section after the summary table.

The recall-check section SHALL include a table with exactly these columns in this order:

- `Name`
- `Link`
- `Expected Type`
- `Status`

Each recall-check row SHALL use exactly one `Status` value: `found`, `recall-miss`, `wording-miss`, `classification-miss`, `evidence-limited`, or `out-of-scope`.

The recall-check section SHALL include explanatory paragraphs below the recall-check table for any row whose `Status` is not `found`.

A `recall-miss` SHALL mean the known candidate is relevant but was not recovered during open discovery.

A `wording-miss` SHALL mean the candidate is likely relevant but was missed because its public framing does not use obvious Urban Digital Twin or digital twin terminology.

A `classification-miss` SHALL mean the candidate was found but assigned a different `Type` than the expected type.

An `evidence-limited` status SHALL mean the model could not verify enough evidence to include or classify the candidate confidently.

An `out-of-scope` status SHALL mean the candidate was checked and excluded under `plan-entity-definition`.

Each saved entity discovery response SHALL include one `##` section per entity.

Each entity section SHALL include a concise paragraph describing what the entity is, why the assigned `Type` fits, and any uncertainty.

For initiative rows, the entity paragraph SHALL identify known technical substrate with `Uses: <artifact names>` when clear, or `Uses: ?` when unclear.

For excluded rows, the entity paragraph SHALL explain the exclusion reason.

#### Scenario: Researcher saves entity discovery output

- **WHEN** a researcher saves an entity discovery web response
- **THEN** the response follows the metadata, coverage statement, table, Type, recall-check, and entity section contract

#### Scenario: Summary table is rendered

- **WHEN** an entity discovery response renders its summary table
- **THEN** the table columns are exactly `Name`, `Type`, and `Link`
- **THEN** `Link` is the final column
- **THEN** `Uses` and `Reason` are not table columns

#### Scenario: Recall check is rendered

- **WHEN** an entity discovery response renders the known candidate recall check
- **THEN** the recall-check table columns are exactly `Name`, `Link`, `Expected Type`, and `Status`
- **THEN** any non-`found` status is explained in a paragraph below the table

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

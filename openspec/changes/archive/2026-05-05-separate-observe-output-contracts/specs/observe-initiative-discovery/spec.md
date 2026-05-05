## ADDED Requirements

### Requirement: Initiative discovery observations use the governed response contract

Saved initiative discovery web responses SHALL use filenames matching `observe/initiative-discovery-<model-short>.md`.

Each saved initiative discovery response SHALL begin with a fenced YAML metadata block containing `model`, `date`, and `prompt: initiative-discovery`.

Each saved initiative discovery response SHALL include a summary table with exactly these columns:

- `Initiative`
- `Link`
- `Uses`
- `Reason`

`Uses` SHALL contain a comma-separated list of known platform discovery artifact names, or `?` when the technical substrate is unclear.

`Reason` SHALL be blank for in-scope rows and SHALL contain a brief phrase for excluded rows.

Each saved initiative discovery response SHALL include one `##` section per initiative with `Link`, `Uses`, `Description`, and `Reason` when excluded.

#### Scenario: Researcher saves initiative discovery output

- **WHEN** a researcher saves an initiative discovery web response
- **THEN** the response follows the metadata, table, Uses, Reason, and section contract

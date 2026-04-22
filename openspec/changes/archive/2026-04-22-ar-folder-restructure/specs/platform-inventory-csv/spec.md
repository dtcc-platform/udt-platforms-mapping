## MODIFIED Requirements

### Requirement: Inventory file is a CSV at reflect/discovery/reporting/ecosystem.csv

The repository SHALL contain a CSV file at `reflect/discovery/reporting/ecosystem.csv`. The file SHALL use standard comma-separated values format with a header row.

#### Scenario: Researcher opens the ecosystem CSV

- **WHEN** a researcher opens `reflect/discovery/reporting/ecosystem.csv`
- **THEN** the file opens as a table in any CSV viewer, spreadsheet tool, or plain text editor

#### Scenario: Old path no longer exists

- **WHEN** a researcher navigates to `docs/05-platform-inventory.csv`
- **THEN** the file does not exist; the canonical inventory is at `reflect/discovery/reporting/ecosystem.csv`

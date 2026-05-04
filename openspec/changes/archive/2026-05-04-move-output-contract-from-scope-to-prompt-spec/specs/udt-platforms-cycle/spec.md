## MODIFIED Requirements

### Requirement: UDT platforms thread maps technical artifacts through broad discovery

The `udt-platforms` thread SHALL classify technical artifacts only.
Its summary table SHALL use `Name`, `Link`, `Type`, and `Reason`.
`Type` SHALL be one of `platform`, `framework`, `module`, or `excluded`.
Only rows with `Type = platform` SHALL be eligible for `udt-platform-comparison`.
The thread SHALL be framed as broad global discovery that prioritizes recall and stable classification over strict source-policy filtering.

#### Scenario: UDT platforms output uses the governed schema

- **WHEN** a researcher or agent reviews a `udt-platforms` output
- **THEN** the summary table uses `Name`, `Link`, `Type`, and `Reason`
- **THEN** every row uses exactly one Type value from `platform`, `framework`, `module`, or `excluded`

#### Scenario: Platform comparison receives platform rows only

- **WHEN** `udt-platform-comparison` selects candidates from `udt-platforms`
- **THEN** only rows where `Type = platform` are eligible

### Requirement: UDT platforms thread owns the scope-table contract

The repository SHALL contain a file at `plan/udt-platforms/scope.md`.

That file SHALL contain exactly one classification table with these columns:

- `Type`
- `Definition`
- `Observable Criteria`

The rows SHALL be:

- `platform`
- `framework`
- `module`
- `excluded`

The file SHALL explain that initiatives and projects are tracked separately in `udt-initiatives`.
The file SHALL NOT contain output-format tables, output-format examples, output contract reminders, or comparison handoff rules.

#### Scenario: Scope file contains classification criteria only

- **WHEN** a researcher opens `plan/udt-platforms/scope.md`
- **THEN** the file contains the Type classification table
- **THEN** the file does not contain the `Name`, `Link`, `Type`, `Reason` output table
- **THEN** the file does not describe comparison eligibility

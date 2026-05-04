## ADDED Requirements

### Requirement: UDT platforms scope file exists

The repository SHALL contain a file at `plan/udt-platforms-scope.md`.

#### Scenario: Researcher finds UDT platforms scope

- **WHEN** a researcher opens `plan/`
- **THEN** `plan/udt-platforms-scope.md` is available as the `udt-platforms` scope input

### Requirement: UDT platforms scope defines Type classification criteria

`plan/udt-platforms-scope.md` SHALL define the technical-artifact classification used in the `udt-platforms` thread.
The file SHALL contain exactly one classification table with these columns:

- `Type`
- `Definition`
- `Observable Criteria`

The rows SHALL be:

- `platform`
- `framework`
- `module`
- `excluded`

#### Scenario: Scope file contains classification table

- **WHEN** a researcher opens `plan/udt-platforms-scope.md`
- **THEN** the file contains a `Type`, `Definition`, `Observable Criteria` table
- **THEN** the table includes rows for `platform`, `framework`, `module`, and `excluded`

### Requirement: UDT platforms scope stays separate from output format

`plan/udt-platforms-scope.md` SHALL explain that initiatives and projects are tracked separately in `udt-initiatives`.
The file SHALL NOT contain output-format tables, output-format examples, output contract reminders, or comparison handoff rules.

#### Scenario: Scope file omits output contract

- **WHEN** a researcher opens `plan/udt-platforms-scope.md`
- **THEN** the file does not contain the `Name`, `Link`, `Type`, `Reason` output table
- **THEN** the file does not describe comparison eligibility

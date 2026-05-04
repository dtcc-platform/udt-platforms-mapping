## ADDED Requirements

### Requirement: UDT initiatives scope file exists

The repository SHALL contain a file at `plan/udt-initiatives-scope.md`.

#### Scenario: Researcher finds UDT initiatives scope

- **WHEN** a researcher opens `plan/`
- **THEN** `plan/udt-initiatives-scope.md` is available as the `udt-initiatives` scope input

### Requirement: UDT initiatives scope defines initiative mapping contract

`plan/udt-initiatives-scope.md` SHALL define the initiative and project mapping contract used in the `udt-initiatives` thread.
The file SHALL describe `udt-initiatives` as a broad global discovery thread for UDT-related projects, programmes, deployments, and implementation efforts.
The file SHALL explain that technical artifacts belong in `udt-platforms`.

#### Scenario: Researcher reads initiative boundary

- **WHEN** a researcher opens `plan/udt-initiatives-scope.md`
- **THEN** the file describes initiative/project mapping
- **THEN** the file explains that technical artifacts belong in `udt-platforms`

### Requirement: UDT initiatives scope defines summary table fields

`plan/udt-initiatives-scope.md` SHALL define an initiative summary table with exactly these columns:

- `Initiative`
- `Link`
- `Uses`
- `Reason`

`Uses` SHALL contain a comma-separated list of artifact names from `udt-platforms`, or `?` if the technical substrate is unclear.
`Reason` SHALL be blank for in-scope rows and SHALL contain a brief phrase only when an initiative is excluded from the study boundary.

#### Scenario: Scope file contains initiative table contract

- **WHEN** a researcher opens `plan/udt-initiatives-scope.md`
- **THEN** the file defines `Initiative`, `Link`, `Uses`, and `Reason` columns
- **THEN** the file allows `Uses = ?` when the technical substrate is unclear

## MODIFIED Requirements

### Requirement: plan/ holds cycle inputs

`plan/udt-platforms/` SHALL contain `scope.md`.
`plan/udt-initiatives/` SHALL contain `scope.md`.
`plan/udt-platform-comparison/` SHALL contain `rubrics.md`, `source-policy.md`, and `platforms.md`.

#### Scenario: Researcher inspects canonical planning inputs
- **WHEN** a researcher opens the `plan/` tree
- **THEN** the discovery threads expose scope files while the comparison thread continues to expose the stricter source-policy input

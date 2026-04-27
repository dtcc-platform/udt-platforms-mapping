## MODIFIED Requirements

### Requirement: UDT initiatives cycle maps projects and deployments

The `udt-initiatives` cycle SHALL produce a summary table with:

- `Initiative`
- `Link`
- `Uses`
- `Reason`

`Uses` SHALL contain a comma-separated list of artifact names from `udt-platforms`, or `?` if unclear.

The cycle SHALL be governed by `plan/udt-initiatives/source-policy.md` for evidence prioritization, unacceptable sources, and contradiction handling.

#### Scenario: Researcher evaluates a candidate initiative
- **WHEN** a researcher or agent performs `udt-initiatives` mapping
- **THEN** the initiative inclusion and `Uses` judgment are constrained by the cycle’s explicit source-policy file

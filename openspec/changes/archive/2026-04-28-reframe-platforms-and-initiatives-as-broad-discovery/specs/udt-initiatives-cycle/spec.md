## MODIFIED Requirements

### Requirement: UDT initiatives cycle maps projects and deployments

The `udt-initiatives` cycle SHALL produce a summary table with:

- `Initiative`
- `Link`
- `Uses`
- `Reason`

`Uses` SHALL contain a comma-separated list of artifact names from `udt-platforms`, or `?` if unclear.

The cycle SHALL be treated as a broad global discovery thread oriented toward initiative and deployment recall rather than strict source-policy filtering.

#### Scenario: Researcher evaluates a candidate initiative
- **WHEN** a researcher or agent performs `udt-initiatives` discovery
- **THEN** the thread is allowed to retain incomplete but relevant initiative candidates, including `Uses = ?`, while preserving the canonical table contract

## MODIFIED Requirements

### Requirement: UDT platforms cycle maps technical artifacts

The `udt-platforms` cycle SHALL classify technical artifacts only.
Its summary table SHALL use `Name`, `Link`, `Type`, and `Reason`.
`Type` SHALL be one of `platform`, `framework`, `module`, or `excluded`.

The cycle SHALL be governed by `plan/udt-platforms/source-policy.md` for evidence prioritization, unacceptable sources, and contradiction handling.

#### Scenario: Researcher evaluates a candidate artifact
- **WHEN** a researcher or agent performs `udt-platforms` mapping
- **THEN** the classification is constrained by the cycle’s explicit source-policy file rather than ad hoc evidence selection

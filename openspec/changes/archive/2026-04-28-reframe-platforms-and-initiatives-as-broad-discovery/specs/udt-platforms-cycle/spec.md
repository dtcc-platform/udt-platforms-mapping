## MODIFIED Requirements

### Requirement: UDT platforms cycle maps technical artifacts

The `udt-platforms` cycle SHALL classify technical artifacts only.
Its summary table SHALL use `Name`, `Link`, `Type`, and `Reason`.
`Type` SHALL be one of `platform`, `framework`, `module`, or `excluded`.

The cycle SHALL be treated as a broad global discovery thread oriented toward candidate recall rather than strict source-policy filtering.

#### Scenario: Researcher evaluates a candidate artifact
- **WHEN** a researcher or agent performs `udt-platforms` discovery
- **THEN** the thread is allowed to cast a wide net across the ecosystem while still using the canonical `Type` output contract

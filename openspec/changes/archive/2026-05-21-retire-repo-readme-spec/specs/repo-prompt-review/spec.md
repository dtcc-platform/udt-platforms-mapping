## MODIFIED Requirements

### Requirement: README explains prompt interpretation review

The prompt interpretation review workflow SHALL have contributor-facing documentation in `README.md`.

The documentation SHALL describe prompt interpretation review as the method for using multiple agents to improve prompt/spec fidelity.

The documentation SHALL explain that accepted review feedback is captured through OpenSpec changes rather than calibration artifacts.

README placement and wording SHALL NOT be governed by a standalone README OpenSpec capability.

#### Scenario: Contributor reads the workflow overview

- **WHEN** a contributor reads `README.md`
- **THEN** they understand that multi-agent prompt review is sequential
- **THEN** they understand that OpenSpec history is the audit trail

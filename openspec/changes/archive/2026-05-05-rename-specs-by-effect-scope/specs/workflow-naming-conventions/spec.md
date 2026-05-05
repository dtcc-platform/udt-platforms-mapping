## ADDED Requirements

### Requirement: Spec capability names use effect-scope prefixes

OpenSpec capability names SHALL use the first hyphen-separated token to identify the spec's effect scope.

The supported effect-scope prefixes SHALL include:

- `repo` for repository-wide structure, conventions, and shared contracts
- `plan` for planning artifacts
- `act` for execution prompt artifacts
- `observe` for saved-output artifacts
- `reflect` for reflection, benchmarking, and reporting artifacts

#### Scenario: Contributor scans active specs

- **WHEN** a contributor reads the active spec list
- **THEN** the first token of each capability name identifies where the spec takes effect
- **THEN** repository-wide capabilities use the `repo` prefix

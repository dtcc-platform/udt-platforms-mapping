## MODIFIED Requirements

### Requirement: Workflow names are descriptive and stable

Workflow-facing names SHALL be descriptive enough to preserve meaning in git history and repository artifacts.

Where a governed naming pattern exists, agents and contributors SHALL use that pattern instead of ad hoc alternatives.

#### Scenario: Contributor creates a prompt review change

- **WHEN** a contributor captures accepted prompt-review feedback
- **THEN** the OpenSpec change name describes the prompt/spec improvement rather than the reviewing agent alone

### Requirement: OpenSpec change names are descriptive hyphenated identifiers

OpenSpec change names SHALL be lowercase, descriptive, and hyphen-separated.

They SHOULD describe the workflow or contract change rather than only the local edit mechanism.

#### Scenario: Contributor starts a governed workflow change

- **WHEN** a contributor creates an OpenSpec change
- **THEN** the change name is lowercase, descriptive, and hyphen-separated
- **THEN** the change name describes the intended contract or workflow change

## REMOVED Requirements

### Requirement: Isolated calibration branches use the agent name

**Reason**: The isolated calibration branch workflow is retired.

**Migration**: Use normal branch names appropriate to the OpenSpec change being made.

### Requirement: Calibration cycles use zero-padded sequence tokens

**Reason**: The `calibration/<spec-name>/<cycle>/<agent>/` artifact path is retired.

**Migration**: Use OpenSpec change names and archived change dates for traceability.

### Requirement: Calibration naming segments use governed identifiers

**Reason**: Calibration path segments are no longer part of the live repository contract.

**Migration**: Use descriptive OpenSpec change names.

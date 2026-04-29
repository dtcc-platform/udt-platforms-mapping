# Spec: workflow-naming-conventions

## Purpose

Defines repo-wide naming conventions that support workflow traceability across branches, commits, OpenSpec changes, and calibration history.

## Requirements

### Requirement: Workflow names are descriptive and stable

Workflow-facing names SHALL be descriptive enough to preserve meaning in git history and repository artifacts.

Where a governed naming pattern exists, agents and contributors SHALL use that pattern instead of ad hoc alternatives.

### Requirement: Commit messages use governed workflow patterns

Commit messages SHALL use one of the repository's governed naming patterns for workflow-relevant changes.

Supported patterns SHALL include:

- `<phase>(<thread>): <subject>`
- `<type>(<scope>): <subject>`

#### Scenario: Contributor commits a canonical research artifact

- **WHEN** a contributor commits a canonical phase artifact
- **THEN** the commit message uses the phase/thread pattern, such as `observe(udt-platforms): add claude response`

#### Scenario: Contributor commits a spec or workflow refactor

- **WHEN** a contributor commits a spec or workflow change
- **THEN** the commit message uses the type/scope pattern, such as `refactor(specs): rename cycles to udt-platforms`

### Requirement: Isolated calibration branches use the agent name

When calibration uses isolated agent branches before merge, the branch name SHALL be the agent name.

#### Scenario: Agent prepares an isolated calibration proposal

- **WHEN** an agent starts isolated proposal work after shared prompt generation
- **THEN** the branch name is the agent name, such as `codex`, `gemini`, or `claude`

### Requirement: Calibration cycles use zero-padded sequence tokens

Calibration cycle names SHALL use the zero-padded pattern `c01`, `c02`, and so on.

#### Scenario: Contributor starts a second calibration round for the same spec

- **WHEN** a second accepted-baseline calibration round is created
- **THEN** its cycle token is `c02` rather than `c2`

### Requirement: OpenSpec change names are descriptive hyphenated identifiers

OpenSpec change names SHALL be lowercase, descriptive, and hyphen-separated.

They SHOULD describe the workflow or contract change rather than only the local edit mechanism.

### Requirement: Calibration naming segments use governed identifiers

Calibration naming segments SHALL use:

- `<spec-name>` for the governed spec under calibration
- `<agent>` for the agent identity responsible for a generated prompt or isolated proposal branch

These naming expectations govern the identifiers used by structural specs but do not themselves define the full calibration path contract.

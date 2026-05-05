# Spec: repo-naming-conventions

## Purpose

Defines repo-wide naming conventions that support workflow traceability across branches, commits, OpenSpec changes, and archived change history.

## Requirements

### Requirement: Workflow names are descriptive and stable

Workflow-facing names SHALL be descriptive enough to preserve meaning in git history and repository artifacts.

Where a governed naming pattern exists, agents and contributors SHALL use that pattern instead of ad hoc alternatives.

#### Scenario: Contributor creates a prompt review change

- **WHEN** a contributor captures accepted prompt-review feedback
- **THEN** the OpenSpec change name describes the prompt/spec improvement rather than the reviewing agent alone

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

### Requirement: Phase artifact filenames encode thread and function

Canonical phase artifacts SHALL use direct filenames that encode thread, function, and artifact role when those distinctions are needed.

The filename pattern SHOULD be:

```text
<thread>-<function>-<artifact>.<ext>
```

The function segment MAY be omitted when the thread and artifact role are sufficient.

#### Scenario: Contributor adds a phase artifact

- **WHEN** a contributor adds a canonical artifact under `plan/`, `act/`, `observe/`, or `reflect/`
- **THEN** the artifact is a direct file in that phase folder
- **THEN** the filename identifies the thread and purpose without requiring a subfolder

### Requirement: OpenSpec change names are descriptive hyphenated identifiers

OpenSpec change names SHALL be lowercase, descriptive, and hyphen-separated.

They SHOULD describe the workflow or contract change rather than only the local edit mechanism.

#### Scenario: Contributor starts a governed workflow change

- **WHEN** a contributor creates an OpenSpec change
- **THEN** the change name is lowercase, descriptive, and hyphen-separated
- **THEN** the change name describes the intended contract or workflow change

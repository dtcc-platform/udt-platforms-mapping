## ADDED Requirements

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

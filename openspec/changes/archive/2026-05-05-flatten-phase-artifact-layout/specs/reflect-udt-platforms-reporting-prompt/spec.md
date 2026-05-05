## REMOVED Requirements

### Requirement: Prompt auto-scans observe/udt-platforms

**Reason**: The reporting prompt belongs to `act/` after phase flattening.

**Migration**: Use `act-udt-platforms-reporting-prompt`.

### Requirement: Prompt identifies qualifying files by udt-platforms YAML metadata

**Reason**: The reporting prompt contract belongs to `act/` after phase flattening.

**Migration**: Use `act-udt-platforms-reporting-prompt`.

### Requirement: Prompt extracts one consolidated Markdown table

**Reason**: The prompt behavior belongs to `act/`, while the output artifact belongs to `reflect/`, after phase flattening.

**Migration**: Use `act-udt-platforms-reporting-prompt` and `reflect-udt-platforms-ecosystem`.

## REMOVED Requirements

### Requirement: Comparison reporting prompt exists

**Reason**: The comparison reporting prompt belongs to `act/` after phase flattening.

**Migration**: Use `act-udt-platform-comparison-reporting-prompt`.

### Requirement: Comparison reporting workflow scans observe/udt-platform-comparison automatically

**Reason**: The prompt scan behavior belongs to the `act-udt-platform-comparison-reporting-prompt` capability after phase flattening.

**Migration**: Use `act-udt-platform-comparison-reporting-prompt`.

### Requirement: Comparison reporting identifies qualifying files by prompt metadata

**Reason**: The prompt qualification behavior belongs to the `act-udt-platform-comparison-reporting-prompt` capability after phase flattening.

**Migration**: Use `act-udt-platform-comparison-reporting-prompt`.

### Requirement: Comparison reporting writes ecosystem.csv and ecosystem-map.html

**Reason**: The synthesized comparison ecosystem artifacts are governed by a direct `reflect-*` output capability after phase flattening.

**Migration**: Use `reflect-udt-platform-comparison-ecosystem`.

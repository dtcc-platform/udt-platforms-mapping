## ADDED Requirements

### Requirement: Report platform discovery prompt synthesizes platform ecosystem

The repository SHALL contain `act/report-platform-discovery.md`.

The prompt SHALL scan `observe/platform-discovery-*.md` files without requiring manual path input.

The prompt SHALL treat as qualifying only files whose YAML block contains `prompt: platform-discovery`.

The prompt SHALL write its output to `reflect/platform-ecosystem.md`.

#### Scenario: Researcher runs platform discovery reporting

- **WHEN** a researcher runs `act/report-platform-discovery.md`
- **THEN** the prompt scans platform discovery observations
- **THEN** it writes the ecosystem summary under `reflect/`

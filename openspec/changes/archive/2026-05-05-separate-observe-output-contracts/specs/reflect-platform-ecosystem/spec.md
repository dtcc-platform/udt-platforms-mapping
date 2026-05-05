## MODIFIED Requirements

### Requirement: Platform ecosystem is the platform discovery synthesis

The repository SHALL contain `reflect/platform-ecosystem.md` as the synthesized ecosystem summary for platform discovery.

The platform ecosystem synthesis SHALL be a single Markdown table with exactly these columns:

- `Name`
- `Link`
- `Type`
- `Reason`

The synthesis SHALL be built from qualifying `observe/platform-discovery-*.md` files whose YAML metadata contains `prompt: platform-discovery`.

Rows SHALL be sorted deterministically by `Type`, then `Name`, then link URL, then `Reason`.

#### Scenario: Researcher opens reflect/

- **WHEN** a researcher opens `reflect/`
- **THEN** `platform-ecosystem.md` is available as a direct file
- **THEN** it follows the governed platform ecosystem table contract

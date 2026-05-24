## MODIFIED Requirements

### Requirement: Prompt review uses saved resolved prompt snapshots

Prompt review SHALL start from a saved resolved prompt snapshot generated from one governed `act/` manifest, its required OpenSpec contracts, and its required run inputs.

Resolved prompt snapshots SHALL be stored as direct files under `act/` using the pattern `act/<action>-resolved-<resolver-short>.md`.

The resolved prompt snapshot SHALL begin with the executable research query so the artifact remains runnable in web research tools.

The resolved prompt snapshot SHALL identify the source `act/` manifest, resolver, date, required contracts, and required run inputs after the executable research query.

The resolved prompt snapshot SHALL NOT replace the source `act/` manifest or any OpenSpec contract.

#### Scenario: Researcher saves a resolved prompt for review

- **WHEN** a researcher resolves `act/entity-discovery.md` for review using Codex
- **THEN** the resolved prompt snapshot is saved as `act/entity-discovery-resolved-codex.md`
- **THEN** the snapshot starts with the executable entity discovery research query
- **THEN** the snapshot identifies the manifest, resolver, date, required contracts, and required run inputs after the query
- **THEN** the source manifest and specs remain the canonical behavior source

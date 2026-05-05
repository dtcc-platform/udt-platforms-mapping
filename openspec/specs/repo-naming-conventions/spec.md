# Spec: repo-naming-conventions

## Purpose

Defines the researcher-facing naming contract for live repository artifacts.

## Requirements

### Requirement: Live artifact names use researcher-facing object/action/role language

Live repository artifact filenames SHALL use researcher-facing names that describe the artifact's research object, action, or role.

Live filenames SHALL NOT repeat the `udt-` prefix because the repository context supplies the Urban Digital Twin domain.

Live documentation and specs SHALL NOT describe canonical live artifacts as research threads. They SHALL use clearer terms such as research object, research action, artifact role, prompt, saved output, or synthesis.

#### Scenario: Contributor names a live artifact

- **WHEN** a contributor creates or renames a live canonical artifact
- **THEN** the filename uses object/action/role language
- **THEN** the filename does not begin with `udt-`
- **THEN** the governing docs avoid thread-centered language for the live workflow

### Requirement: Phase folders use phase-specific naming grammar

Plan artifacts SHALL use noun phrases such as `platform-definition.md`, `platform-dimensions-scoring.md`, `platform-comparison-set.md`, and `platform-discovery-benchmark.md`.

Act artifacts SHALL use verb phrases such as `discover-platforms.md`, `compare-platforms.md`, `benchmark-platform-discovery.md`, and `report-platform-discovery.md`.

Observe artifacts SHALL identify the research action and model or generated output, such as `platform-discovery-claude.md`, `platform-comparison-gemini.md`, and `platform-discovery-coverage.md`.

Reflect artifacts SHALL identify the research object and synthesis product, such as `platform-ecosystem.md` and `platform-comparison-ecosystem.csv`.

#### Scenario: Researcher scans phase folders

- **WHEN** a researcher opens `plan/`, `act/`, `observe/`, or `reflect/`
- **THEN** filenames communicate the artifact role without requiring knowledge of old thread identifiers

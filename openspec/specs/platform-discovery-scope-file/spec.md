# Spec: platform-discovery-scope-file

## Purpose

TBD — Defines the requirements for `docs/01-discovery-scope.md`, the scope reference file for discovery sessions. Researchers paste its full content into the `[PASTE_SCOPE_HERE]` slot in the discovery prompt before running a session.

## Requirements

### Requirement: docs/01-discovery-scope.md exists and contains the Layer criteria table

The repository SHALL contain a file at `docs/01-discovery-scope.md`. This file is the sole scope reference for discovery sessions — researchers paste its full content into the `[PASTE_SCOPE_HERE]` slot in the discovery prompt before running a session.

The file SHALL contain exactly one classification table with four rows and three columns: `Layer`, `Definition`, and `Criteria`. The rows SHALL be:

| Layer           | Definition                                    | Criteria                                                                                          |
| --------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `core-platform` | Full UDT platform                             | Official docs claim city-scale digital twin; owns data + simulation + visualisation as one system |
| `backbone`      | Enabling infrastructure layer                 | Designed to be composed into other systems; API/SDK is primary interface, not end-user UI         |
| `domain-module` | Domain-specific urban analytics or simulation | Covers one urban domain (mobility, energy, climate...); outputs consumed by a larger UDT stack    |
| `excluded`      | Outside the study boundary                    | None of the above apply; note reason in one sentence                                              |

The file SHALL NOT contain Relevance rubrics, dimension rubrics, seed lists, or target corpus size. Those belong in `docs/01-comparison-scope.md` or are retired.

The file SHALL include a brief header explaining its purpose: it defines the Layer classification system used in the discovery phase.

#### Scenario: Researcher prepares a discovery session

- **WHEN** a researcher is about to run a discovery session
- **THEN** they paste the full content of `docs/01-discovery-scope.md` into the `[PASTE_SCOPE_HERE]` slot in the discovery prompt — not the full `docs/01-scope.md`

#### Scenario: Discovery AI classifies a full UDT platform

- **WHEN** a discovery AI reads the criteria table and encounters a platform whose official docs claim city-scale digital twin and which owns data, simulation, and visualisation as one system
- **THEN** it assigns `Layer=core-platform`

#### Scenario: Discovery AI classifies a backbone component

- **WHEN** a discovery AI encounters a platform designed to be composed into other systems with an API/SDK as its primary interface
- **THEN** it assigns `Layer=backbone`

#### Scenario: Discovery AI classifies a domain-specific tool

- **WHEN** a discovery AI encounters a tool that covers one urban domain and produces outputs consumed by a larger UDT stack
- **THEN** it assigns `Layer=domain-module`

#### Scenario: Discovery AI encounters an out-of-scope platform

- **WHEN** a discovery AI encounters a platform that does not meet any of the three in-scope criteria
- **THEN** it assigns `Layer=excluded` and provides a one-sentence reason

#### Scenario: Researcher updates the Layer criteria

- **WHEN** a researcher needs to refine the criteria for a layer
- **THEN** they edit `docs/01-discovery-scope.md` only; the discovery prompt receives the updated table at run time via the paste step

### Requirement: docs/01-scope.md is retired

The file `docs/01-scope.md` SHALL be removed from the repository. It is replaced by `docs/01-discovery-scope.md` and `docs/01-comparison-scope.md`. Any references to `docs/01-scope.md` in prompt files SHALL be updated to reference the appropriate replacement file.

#### Scenario: Researcher looks for the old scope file

- **WHEN** a researcher navigates to `docs/01-scope.md`
- **THEN** the file does not exist; they find `docs/01-discovery-scope.md` and `docs/01-comparison-scope.md` instead

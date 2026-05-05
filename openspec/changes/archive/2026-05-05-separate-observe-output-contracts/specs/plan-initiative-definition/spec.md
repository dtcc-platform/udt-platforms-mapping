## MODIFIED Requirements

### Requirement: Initiative definition is the canonical initiative discovery planning contract

The repository SHALL contain `plan/initiative-definition.md` as the initiative and project discovery definition.

The file SHALL define initiative discovery scope for projects, programmes, deployments, and implementation efforts related to Urban Digital Twins.

The file SHALL explain that technical artifacts belong in platform discovery.

The file SHALL NOT define the exact saved response table or section output contract; that output contract is governed by `observe-initiative-discovery`.

#### Scenario: Researcher opens initiative definition

- **WHEN** a researcher opens `plan/initiative-definition.md`
- **THEN** they can find the initiative and project discovery scope
- **THEN** the file refers to platform discovery without using the old `udt-platforms` thread identifier
- **THEN** exact saved response formatting is left to the observe contract

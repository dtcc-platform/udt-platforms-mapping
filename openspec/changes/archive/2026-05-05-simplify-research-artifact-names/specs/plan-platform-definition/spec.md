## ADDED Requirements

### Requirement: Platform definition is the canonical platform discovery planning contract

The repository SHALL contain `plan/platform-definition.md` as the platform discovery definition and Type classification contract.

The file SHALL define the technical artifact categories used by platform discovery, including `platform`, `framework`, `module`, and `excluded`.

The file SHALL explain that initiative and project discovery is governed separately by `plan/initiative-definition.md`.

#### Scenario: Researcher opens platform definition

- **WHEN** a researcher opens `plan/platform-definition.md`
- **THEN** they can find the platform discovery scope and Type classification contract
- **THEN** the file refers to initiative discovery without using the old `udt-initiatives` thread identifier

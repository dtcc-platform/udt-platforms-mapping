## MODIFIED Requirements

### Requirement: Platform definition is the canonical platform discovery planning contract

The repository SHALL contain `plan/platform-definition.md` as the platform discovery definition and Type classification contract.

The file SHALL define the technical artifact categories used by platform discovery, including `platform`, `framework`, `module`, and `excluded`.

The file SHALL define interpretation rules for applying the `Type` criteria to borderline artifacts.

The interpretation rules SHALL require classification by observable presentation and role in the urban digital twin ecosystem.

The interpretation rules SHALL require exactly one `Type` per artifact.

The interpretation rules SHALL define tie-break guidance for artifacts that resemble multiple types.

The interpretation rules SHALL explain how to handle weak, ambiguous, or insufficient evidence.

The file SHALL explain that initiative and project discovery is governed separately by `plan/initiative-definition.md`.

#### Scenario: Researcher opens platform definition

- **WHEN** a researcher opens `plan/platform-definition.md`
- **THEN** they can find the platform discovery scope and Type classification contract
- **THEN** they can find interpretation rules for applying the Type criteria
- **THEN** they can find guidance for borderline and ambiguous artifacts
- **THEN** the file refers to initiative discovery without using the old `udt-initiatives` thread identifier

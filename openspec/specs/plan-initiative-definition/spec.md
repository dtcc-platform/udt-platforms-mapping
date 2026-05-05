# Spec: plan-initiative-definition

## Purpose

Defines this researcher-facing canonical artifact.

## Requirements

### Requirement: Initiative definition is the canonical initiative discovery planning contract

The repository SHALL contain `plan/initiative-definition.md` as the initiative and project discovery definition.

The file SHALL define the initiative summary table contract for projects, programmes, deployments, and implementation efforts related to Urban Digital Twins.

The file SHALL explain that technical artifacts belong in platform discovery.

#### Scenario: Researcher opens initiative definition

- **WHEN** a researcher opens `plan/initiative-definition.md`
- **THEN** they can find the initiative and project discovery contract
- **THEN** the file refers to platform discovery without using the old `udt-platforms` thread identifier

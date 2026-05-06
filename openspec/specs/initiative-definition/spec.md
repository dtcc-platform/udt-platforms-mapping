# Spec: initiative-definition

## Purpose

Defines initiative discovery behavior for Urban Digital Twin projects, programmes, deployments, and implementation efforts.

## Requirements

### Requirement: Initiative discovery identifies projects and deployments

Initiative discovery SHALL discover projects, programmes, deployments, implementation efforts, and institutional initiatives related to Urban Digital Twins.

Initiative discovery SHALL focus on real-world activity rather than classifying technical artifacts as primary rows.

#### Scenario: Initiative is discovered

- **WHEN** a project, programme, deployment, or implementation effort is related to Urban Digital Twins
- **THEN** initiative discovery may include it as an initiative

### Requirement: Initiative discovery separates initiatives from technical artifacts

Technical artifacts SHALL belong in platform discovery when they are the primary entity being classified.

Initiative discovery SHALL record the technical substrate separately when it is clear.

#### Scenario: Initiative uses a known platform

- **WHEN** an initiative clearly uses a known platform artifact
- **THEN** initiative discovery records that platform artifact as the initiative's technical substrate

### Requirement: Unknown technical substrate is explicit

Initiative discovery SHALL preserve uncertainty when an initiative's technical substrate is unclear.

When the technical substrate is unclear, initiative discovery SHALL use `Uses = ?`.

#### Scenario: Initiative substrate is unclear

- **WHEN** an initiative is relevant but its platform or technical artifact cannot be identified
- **THEN** initiative discovery records `Uses = ?`

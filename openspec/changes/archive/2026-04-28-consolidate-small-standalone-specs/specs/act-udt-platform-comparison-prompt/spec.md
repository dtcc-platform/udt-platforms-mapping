# Spec Delta: act-udt-platform-comparison-prompt

## Change Type

Modify capability

## Requirements

### Requirement: Comparison prompt owns rubric input contract

The comparison prompt capability SHALL own the requirement that the repository contains:

- `plan/udt-platform-comparison/rubrics.md`

That file SHALL contain the 12 dimension and functional-category rubrics used by `act/udt-platform-comparison/prompt.md`.

### Requirement: Comparison prompt owns platform-only handoff rule

Only rows from `udt-platforms` where `Type = platform` SHALL be eligible for `udt-platform-comparison`.

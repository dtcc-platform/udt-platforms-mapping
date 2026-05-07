# Spec: repo-act-prompt-manifest

## Purpose

Defines the shared manifest contract for governed prompt files under `act/`.

## Requirements

### Requirement: Governed act prompts are contract manifests

Governed prompt files under `act/` SHALL act as contract manifests rather than independent behavior definitions.

A governed act prompt manifest SHALL identify the contracts and run inputs that affect prompt execution.

A governed act prompt manifest SHALL NOT duplicate behavior that belongs to its required contracts.

#### Scenario: Researcher opens an act prompt

- **WHEN** a researcher opens a governed prompt file under `act/`
- **THEN** the file shows which contracts and inputs affect the action
- **THEN** the file does not act as a second source of behavior truth

### Requirement: Act prompt manifests explain contract purpose

A governed act prompt manifest SHALL include a `## Required Contracts` section when the action depends on OpenSpec contracts.

Each required contract entry SHALL include a short purpose comment explaining why that contract is included.

Purpose comments SHALL orient the researcher and resolver, but SHALL NOT add requirements, rules, scope, output shape, scoring behavior, evidence policy, or formatting behavior.

#### Scenario: Researcher reviews required contracts

- **WHEN** a researcher reads the `## Required Contracts` section
- **THEN** each listed contract has a concise purpose comment
- **THEN** the comment does not create behavior outside the referenced spec

### Requirement: Act prompt manifests distinguish run inputs

A governed act prompt manifest SHALL include a `## Required Run Inputs` section when the action depends on run-specific files or fixtures.

Each required run input entry SHALL include a short purpose comment explaining how the input is used.

Run input comments SHALL NOT define behavior beyond identifying the input's role.

#### Scenario: Researcher reviews run inputs

- **WHEN** a researcher reads the manifest for an action with run-specific inputs
- **THEN** required input files are distinguishable from contracts
- **THEN** each input has a concise purpose comment

### Requirement: Act prompt manifests limit resolver and execution glue

A governed act prompt manifest SHALL limit resolver or execution instructions to the instructions needed to produce or run the final prompt.

Allowed resolver and execution glue includes:

- instructions to inline required contracts
- instructions to inline required run inputs
- instructions to append a minimal prompt body
- instructions to output one copy-ready block
- instructions about whether the prompt is for a web model or an AI CLI with filesystem access
- save or write-location guidance when that location is already governed by a required output contract

Resolver and execution glue SHALL NOT restate the substantive behavior of the action.

#### Scenario: Resolver prepares a prompt

- **WHEN** a resolver processes a governed act prompt manifest
- **THEN** the manifest tells the resolver how to compose or run the prompt
- **THEN** substantive task behavior comes from required contracts and inputs

### Requirement: Act prompt bodies are minimal task invocations

The prompt body in a governed act prompt manifest SHALL be a minimal invocation of the action described by the inlined contracts.

The prompt body SHALL NOT duplicate contract-governed behavior such as:

- research scope
- evidence handling
- classification criteria
- scoring rules
- matching logic
- filesystem scanning rules
- output tables, fields, or sections
- Markdown formatting rules
- report aggregation logic

#### Scenario: Model receives a resolved prompt

- **WHEN** a model receives a prompt resolved from a governed act prompt manifest
- **THEN** the model gets substantive behavior from the inlined contracts
- **THEN** the manifest body only invokes the contracted action

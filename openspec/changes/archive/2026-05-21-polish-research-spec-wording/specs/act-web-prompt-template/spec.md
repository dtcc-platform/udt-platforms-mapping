## MODIFIED Requirements

### Requirement: Canonical web prompts declare contracts and run inputs separately

Canonical web prompt templates that conform to this contract SHALL distinguish required behavior/output contracts from required run inputs.

The prompt SHALL conform to `act-prompt-manifest`.

The prompt SHALL use a `## Required Contracts` section when it depends on OpenSpec behavior or output contracts.

The prompt SHALL use a `## Required Run Inputs` section when it depends on `plan/` files or other run-specific input artifacts.

#### Scenario: Researcher opens a canonical web prompt

- **WHEN** a researcher opens a conforming canonical web prompt
- **THEN** required OpenSpec contracts are distinguishable from run inputs
- **THEN** the prompt follows the act prompt manifest contract


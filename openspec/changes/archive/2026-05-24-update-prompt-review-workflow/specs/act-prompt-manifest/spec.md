## MODIFIED Requirements

### Requirement: Act prompt manifests limit resolver and execution glue

A governed act prompt manifest SHALL limit resolver or execution instructions to the instructions needed to produce or run the final prompt.

Allowed resolver and execution glue includes:

- instructions to inline required contracts
- instructions to inline required run inputs
- instructions to append a minimal prompt body
- instructions to output one copy-ready block
- instructions about whether the prompt is for a web model or an AI CLI with filesystem access
- save or write-location guidance when that location is already governed by a required output contract
- resolved-prompt save guidance when that location is governed by `research-prompt-review` or `research-workflow-structure`

Resolver and execution glue SHALL NOT restate the substantive behavior of the action.

#### Scenario: Resolver prepares a prompt

- **WHEN** a resolver processes a governed act prompt manifest
- **THEN** the manifest tells the resolver how to compose or run the prompt
- **THEN** substantive task behavior comes from required contracts and inputs

#### Scenario: Manifest includes resolved-prompt save guidance

- **WHEN** a governed act prompt manifest tells the resolver where to save a resolved prompt artifact
- **THEN** the save location is governed by `research-prompt-review` or `research-workflow-structure`
- **THEN** the manifest does not define a separate prompt-review storage convention

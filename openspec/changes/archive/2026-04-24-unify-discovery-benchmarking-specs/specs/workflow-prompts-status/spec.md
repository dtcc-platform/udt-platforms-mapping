## MODIFIED Requirements

### Requirement: Workflow prompt-status audit checks each prompt against governing files

For each live prompt file, the audit SHALL identify:
- its governing baseline prompt spec under `openspec/specs/`
- any shared baseline contract spec the prompt explicitly relies on
- any files declared under its `## Required Inputs` section, if present

The audit SHALL verify that:
- the prompt file exists
- each declared required-input file exists
- the prompt's declared input set is compatible with the governing spec
- the prompt's stated behavior does not directly contradict the governing spec

The audit mapping for live prompts SHALL use the current baseline set. In particular:
- `reflect/discovery/benchmarking/prompt.md` SHALL be checked against `openspec/specs/reflect-discovery-benchmarking/spec.md` without requiring a separate discovery benchmarking coverage shared-contract spec
- `reflect/discovery/reporting/prompt.md` SHALL be checked against `openspec/specs/reflect-discovery-reporting-prompt/spec.md` without requiring a separate discovery-reporting ecosystem shared-contract spec
- `reflect/rating/reporting/prompt.md` SHALL be checked against `openspec/specs/reflect-rating-reporting/spec.md`

#### Scenario: Prompt has a missing required input file
- **WHEN** a live prompt declares a required input path that does not exist
- **THEN** the audit marks that prompt as `invalid` and records the missing path in the report

#### Scenario: Prompt omits a required input required by spec
- **WHEN** a governing spec requires an input file declaration that the prompt does not include
- **THEN** the audit marks that prompt as `invalid` and records the mismatch in the report

#### Scenario: Discovery benchmarking no longer has a separate coverage shared contract
- **WHEN** the audit checks `reflect/discovery/benchmarking/prompt.md`
- **THEN** it does not require a separate discovery benchmarking coverage spec as a freshness dependency

#### Scenario: Discovery reporting no longer has a no-op shared contract
- **WHEN** the audit checks `reflect/discovery/reporting/prompt.md`
- **THEN** it does not require a separate discovery-reporting ecosystem shared-contract spec as a freshness dependency

#### Scenario: Rating reporting has a governing baseline spec
- **WHEN** the audit checks `reflect/rating/reporting/prompt.md`
- **THEN** it uses `openspec/specs/reflect-rating-reporting/spec.md` as the governing baseline spec rather than treating the prompt as unguided

## Why

The repository is moving toward a clearer boundary: OpenSpec specs define behavior contracts, `plan/` contains run inputs, and `act/` prompts operationalize contracts using those inputs.

Some current `plan/` files still contain behavior rules such as definitions, classification criteria, source policies, and scoring rubrics. Moving those behaviors into specs will make the source of truth clearer and make prompt review more direct.

## What Changes

- Move behavior-bearing platform and initiative definitions from `plan/` into behavior specs.
- Move platform comparison scoring and source-policy behavior from `plan/` into behavior specs.
- Keep `plan/` for run inputs such as comparison sets, benchmark fixtures, and optional run-specific scope material.
- Update canonical prompts to declare required behavior specs separately from required run inputs.
- Update repo structure and README contracts so `plan/` is documented as run-input storage, not the behavior-contract layer.
- Leave saved outputs, reflection artifacts, and output contracts unchanged.

## Capabilities

### New Capabilities

- `platform-definition`: Defines platform discovery classification behavior.
- `initiative-definition`: Defines initiative discovery scope and interpretation behavior.
- `platform-comparison-rubric`: Defines platform comparison dimensions and scoring behavior.
- `platform-source-policy`: Defines acceptable source and citation behavior for platform comparison.

### Modified Capabilities

- `repo-structure`: Reclassify `plan/` as run-input storage rather than the home for behavior definitions, policies, and rubrics.
- `repo-readme`: Align root README documentation with the spec/plan/prompt boundary.
- `act-discover-platforms-prompt`: Require the prompt to use `platform-definition` as a behavior contract and treat `plan/` only as run input when needed.
- `act-discover-initiatives-prompt`: Require the prompt to use `initiative-definition` as a behavior contract and treat `plan/` only as run input when needed.
- `act-compare-platforms-prompt`: Require the prompt to use `platform-comparison-rubric` and `platform-source-policy` as behavior contracts while keeping `plan/platform-comparison-set.md` as the selected run input.
- `plan-platform-definition`: Retire this plan artifact contract after behavior moves to `platform-definition`.
- `plan-initiative-definition`: Retire this plan artifact contract after behavior moves to `initiative-definition`.
- `plan-platform-dimensions-scoring`: Retire this plan artifact contract after behavior moves to `platform-comparison-rubric`.
- `plan-platform-source-policy`: Retire this plan artifact contract after behavior moves to `platform-source-policy`.

## Impact

- Affects `openspec/specs/` by adding behavior specs and retiring plan behavior specs.
- Affects `plan/` by removing or reducing files that currently carry behavior.
- Affects `act/discover-platforms.md`, `act/discover-initiatives.md`, and `act/compare-platforms.md`.
- Affects `README.md`, `plan/README.md`, and repo-wide structure/readme specs.
- Does not change `observe/` or `reflect/` output locations.

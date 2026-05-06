## 1. Behavior Specs

- [x] 1.1 Create baseline `platform-definition` behavior spec from platform classification rules.
- [x] 1.2 Create baseline `initiative-definition` behavior spec from initiative discovery rules.
- [x] 1.3 Create baseline `platform-comparison-rubric` behavior spec from comparison dimensions and scoring rules.
- [x] 1.4 Create baseline `platform-source-policy` behavior spec from comparison source and citation rules.
- [x] 1.5 Retire old `plan-*` behavior specs after migration.

## 2. Plan Inputs

- [x] 2.1 Remove stable behavior rules from `plan/platform-definition.md`, `plan/initiative-definition.md`, `plan/platform-dimensions-scoring.md`, and `plan/platform-source-policy.md`.
- [x] 2.2 Keep `plan/platform-comparison-set.md` and `plan/platform-discovery-benchmark.md` as run inputs.
- [x] 2.3 Update `plan/README.md` to describe `plan/` as run-input storage.

## 3. Prompts

- [x] 3.1 Update `act/discover-platforms.md` to use `platform-definition` as a required behavior contract.
- [x] 3.2 Update `act/discover-initiatives.md` to use `initiative-definition` as a required behavior contract.
- [x] 3.3 Update `act/compare-platforms.md` to use `platform-comparison-rubric` and `platform-source-policy` as behavior contracts and `plan/platform-comparison-set.md` as a run input.
- [x] 3.4 Keep output contracts and save-location instructions unchanged.

## 4. Documentation and Specs

- [x] 4.1 Update `README.md` to reflect specs as behavior contracts and `plan/` as run inputs.
- [x] 4.2 Update repo structure and README specs.
- [x] 4.3 Update prompt specs to distinguish behavior contracts from run inputs.

## 5. Validation

- [x] 5.1 Run `openspec validate move-planning-behavior-to-specs --strict`.
- [x] 5.2 Run `openspec validate --all --strict`.

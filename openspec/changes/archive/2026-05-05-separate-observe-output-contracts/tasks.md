## 1. Observe Contracts

- [x] 1.1 Add `observe-platform-discovery` spec for platform discovery web responses.
- [x] 1.2 Add `observe-initiative-discovery` spec for initiative discovery web responses.
- [x] 1.3 Add `observe-platform-comparison` spec for platform comparison web responses.
- [x] 1.4 Expand `observe-platform-discovery-coverage` spec with the coverage report output shape.

## 2. Act And Reflect Ownership

- [x] 2.1 Update discovery and comparison act specs to require output conformance to observe specs.
- [x] 2.2 Update benchmark/report act specs to require output conformance to observe or reflect specs.
- [x] 2.3 Expand reflect specs with platform ecosystem and platform comparison export schemas.

## 3. Plan Cleanup

- [x] 3.1 Remove exact initiative output table contract from `plan/initiative-definition.md`.
- [x] 3.2 Update `plan-initiative-definition` spec so it owns world definition only.

## 4. Prompt Alignment

- [x] 4.1 Add observe-contract references to the discover and compare prompt files.
- [x] 4.2 Add observe/reflect-contract references to benchmark and reporting prompt files.

## 5. Verification

- [x] 5.1 Validate the change with `openspec validate separate-observe-output-contracts --strict`.
- [x] 5.2 Validate all specs with `openspec validate --all --strict`.

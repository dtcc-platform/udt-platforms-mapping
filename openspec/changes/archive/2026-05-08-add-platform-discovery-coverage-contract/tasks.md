## 1. Specs

- [x] 1.1 Add `openspec/specs/platform-discovery-coverage/spec.md` with recall targets, type quotas, seed-list sampling rules, and early-stop prevention.
- [x] 1.2 Update `openspec/specs/act-discover-platforms-prompt/spec.md` so the canonical discovery prompt requires and renders `platform-discovery-coverage`.
- [x] 1.3 Update `openspec/specs/observe-platform-discovery/spec.md` so saved outputs include a coverage statement with counts, target status, and unmet-target explanations.

## 2. Manifest

- [x] 2.1 Update `act/discover-platforms.md` to declare `openspec/specs/platform-discovery-coverage/spec.md` as a required contract.
- [x] 2.2 Add a short purpose comment in the manifest explaining that `platform-discovery-coverage` prevents selected-example discovery runs.

## 3. Validation

- [x] 3.1 Run `openspec validate add-platform-discovery-coverage-contract --strict`.
- [x] 3.2 Resolve `act/discover-platforms.md` and verify the generated prompt includes candidate quotas, seed-list sampling, and coverage-statement instructions.

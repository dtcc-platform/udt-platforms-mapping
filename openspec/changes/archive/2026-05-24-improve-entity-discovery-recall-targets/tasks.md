## 1. Baseline Spec Update

- [x] 1.1 Update `openspec/specs/act-entity-discovery/spec.md` to use "candidate entities" instead of "candidate artifacts" for the broad recall floor.
- [x] 1.2 Raise the broad recall floor from 40 to 50 candidate entities when enough evidence is available.
- [x] 1.3 Add an explicit minimum target for `initiative` candidates.
- [x] 1.4 Add flexible remainder language for high-relevance entities of any allowed `Type`.
- [x] 1.5 Update the post-quota recall pass to include initiatives as well as platforms.
- [x] 1.6 Normalize adjacent seed-list wording from candidate artifacts to relevant candidates.

## 2. Verification

- [x] 2.1 Run `openspec validate improve-entity-discovery-recall-targets --strict`.
- [x] 2.2 Run `openspec validate --all --strict`.
- [x] 2.3 Review `act/entity-discovery.md` and related output contracts for consistency.

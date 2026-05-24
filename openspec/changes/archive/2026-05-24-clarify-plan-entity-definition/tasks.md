## 1. Baseline Spec Update

- [x] 1.1 Update `openspec/specs/plan-entity-definition/spec.md` so the first requirement centers on one output `Type` per candidate.
- [x] 1.2 Clarify that `artifact` is an internal parent concept for `platform`, `framework`, and `module`, not a required output table value.
- [x] 1.3 Replace example-specific exclusion wording with principle-based communication, presentation, and narrative mapping boundary language.
- [x] 1.4 Clarify that initiatives remain `Type = initiative` when they use, fund, deploy, or discuss technical artifacts, with substrate recorded separately when known.
- [x] 1.5 Clarify that weak evidence uses the best supported allowed `Type` and preserves uncertainty in explanatory fields rather than ad hoc output types.

## 2. Verification

- [x] 2.1 Run `openspec validate clarify-plan-entity-definition --strict`.
- [x] 2.2 Run `openspec validate --all --strict`.
- [x] 2.3 Review the baseline spec for duplicated or outdated wording introduced by the rewrite.

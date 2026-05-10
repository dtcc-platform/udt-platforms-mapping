## 1. Specs

- [x] 1.1 Update `openspec/specs/platform-discovery-coverage/spec.md` so quotas are minimum gates, not stopping conditions.
- [x] 1.2 Add a post-quota targeted recall requirement for regional, academic, open-source, and research-center UDT platforms.
- [x] 1.3 Add a DTCC Platform-style scenario requiring disambiguating searches such as `Digital Twin Cities Centre`, `Chalmers`, and `dtcc platform`.
- [x] 1.4 Update `openspec/specs/act-discover-platforms-prompt/spec.md` to require rendering quota-as-floor and post-quota targeted recall instructions.

## 2. Validation

- [x] 2.1 Run `openspec validate prevent-discovery-quota-stop --strict`.
- [x] 2.2 Resolve `act/discover-platforms.md` and verify the generated prompt includes quota-as-floor wording and regional/research-platform recall instructions.

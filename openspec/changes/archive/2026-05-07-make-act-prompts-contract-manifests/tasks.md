## 1. Cross Spec

- [x] 1.1 Add `repo-act-prompt-manifest` as the shared contract for governed `act/*.md` prompt files.
- [x] 1.2 Define manifest sections for required contracts and required run inputs.
- [x] 1.3 Allow short purpose comments for each required contract and input.
- [x] 1.4 Prohibit behavior duplication in manifest comments and prompt bodies.
- [x] 1.5 Allow resolver and execution glue in manifests.

## 2. Prompt Specs

- [x] 2.1 Update `act-discover-platforms-prompt` to require `repo-act-prompt-manifest`.
- [x] 2.2 Update `act-discover-initiatives-prompt` to require `repo-act-prompt-manifest`.
- [x] 2.3 Update `act-compare-platforms-prompt` to require `repo-act-prompt-manifest`.
- [x] 2.4 Update `act-benchmark-platform-discovery-prompt` to require `repo-act-prompt-manifest`.
- [x] 2.5 Update `act-benchmark-platform-comparison-prompt` to require `repo-act-prompt-manifest`.
- [x] 2.6 Update `act-report-platform-discovery-prompt` to require `repo-act-prompt-manifest`.
- [x] 2.7 Update `act-report-platform-comparison-prompt` to require `repo-act-prompt-manifest`.

## 3. Prompt Files

- [x] 3.1 Refactor `act/discover-platforms.md` into a manifest-style prompt.
- [x] 3.2 Refactor `act/discover-initiatives.md` into a manifest-style prompt.
- [x] 3.3 Refactor `act/compare-platforms.md` into a manifest-style prompt.
- [x] 3.4 Refactor `act/benchmark-platform-discovery.md` into a manifest-style prompt.
- [x] 3.5 Keep `act/benchmark-platform-comparison.md` as a manifest-style stub.
- [x] 3.6 Refactor `act/report-platform-discovery.md` into a manifest-style prompt.
- [x] 3.7 Refactor `act/report-platform-comparison.md` into a manifest-style prompt.
- [x] 3.8 Do not update untracked research case-study prompt files.

## 4. Validation

- [x] 4.1 Run `openspec validate make-act-prompts-contract-manifests --strict`.
- [x] 4.2 Run `openspec validate --all --strict`.

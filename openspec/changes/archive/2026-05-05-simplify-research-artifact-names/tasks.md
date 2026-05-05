## 1. Rename Planning Artifacts

- [x] 1.1 Rename `plan/udt-platforms-scope.md` to `plan/platform-definition.md` and update its internal wording from thread language to platform discovery language.
- [x] 1.2 Rename `plan/udt-initiatives-scope.md` to `plan/initiative-definition.md` and update its internal wording from thread language to initiative discovery language.
- [x] 1.3 Rename `plan/udt-platform-comparison-rubrics.md` to `plan/platform-dimensions-scoring.md`.
- [x] 1.4 Rename `plan/udt-platform-comparison-source-policy.md` to `plan/platform-source-policy.md`.
- [x] 1.5 Rename `plan/udt-platform-comparison-platforms.md` to `plan/platform-comparison-set.md` and update internal references.
- [x] 1.6 Rename `plan/udt-platforms-benchmark.md` to `plan/platform-discovery-benchmark.md` and update internal references.

## 2. Rename Prompt Artifacts

- [x] 2.1 Rename `act/udt-platforms.md` to `act/discover-platforms.md` and update required inputs, save-as path, and prompt identifier.
- [x] 2.2 Rename `act/udt-initiatives.md` to `act/discover-initiatives.md` and update required inputs, save-as path, and prompt identifier.
- [x] 2.3 Rename `act/udt-platform-comparison.md` to `act/compare-platforms.md` and update required inputs, save-as path, and prompt identifier.
- [x] 2.4 Rename `act/udt-platforms-benchmarking.md` to `act/benchmark-platform-discovery.md` and update fixture path, glob pattern, and coverage output path.
- [x] 2.5 Rename `act/udt-platforms-reporting.md` to `act/report-platform-discovery.md` and update glob pattern, prompt identifier, and reflection output path.
- [x] 2.6 Rename `act/udt-platform-comparison-benchmarking.md` to `act/benchmark-platform-comparison.md` and update stub wording.
- [x] 2.7 Rename `act/udt-platform-comparison-reporting.md` to `act/report-platform-comparison.md` and update glob pattern, prompt identifier, and reflection output paths.

## 3. Rename Output Artifacts

- [x] 3.1 Rename saved platform discovery observations from `observe/udt-platforms-web-*.md` to `observe/platform-discovery-*.md` and update YAML `prompt:` values to `platform-discovery`.
- [x] 3.2 Rename saved platform comparison observations from `observe/udt-platform-comparison-web-*.md` to `observe/platform-comparison-*.md` and update YAML `prompt:` values to `platform-comparison`.
- [x] 3.3 Rename `observe/udt-platforms-benchmarking-coverage.md` to `observe/platform-discovery-coverage.md` and update internal fixture references.
- [x] 3.4 Rename `reflect/udt-platforms-ecosystem.md` to `reflect/platform-ecosystem.md`.
- [x] 3.5 Rename `reflect/udt-platform-comparison-ecosystem.csv` and `reflect/udt-platform-comparison-ecosystem-map.html` to `reflect/platform-comparison-ecosystem.csv` and `reflect/platform-comparison-ecosystem-map.html`.

## 4. Update Documentation

- [x] 4.1 Update root `README.md` to use research object/action/role language and the new filenames.
- [x] 4.2 Update `plan/README.md`, `act/README.md`, `observe/README.md`, and `reflect/README.md` to use the new filenames and avoid thread-centered language.
- [x] 4.3 Add a short migration note explaining that archived OpenSpec history may still contain old `udt-*` names.

## 5. Update Specs

- [x] 5.1 Add baseline specs for all new researcher-facing capabilities from the accepted deltas.
- [x] 5.2 Remove old baseline specs whose capability names and file paths use retired `udt-*` artifact names.
- [x] 5.3 Update `repo-structure`, `repo-readme`, `repo-naming-conventions`, and `repo-prompt-markdown-format` baseline specs.
- [x] 5.4 Update any remaining prompt/spec references to old live paths, glob patterns, prompt IDs, or thread-centered language.

## 6. Verification

- [x] 6.1 Search live docs/specs/prompts for retired live path patterns such as `plan/udt-`, `act/udt-`, `observe/udt-`, and `reflect/udt-`.
- [x] 6.2 Validate the change with `openspec validate simplify-research-artifact-names --strict`.
- [x] 6.3 Validate all specs with `openspec validate --all --strict`.

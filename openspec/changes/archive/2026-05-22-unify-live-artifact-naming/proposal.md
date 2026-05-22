## Why

Live `act/` prompt filenames still use verb-first names while active OpenSpec capabilities use phase-object-role naming. Unifying live artifact naming removes the last naming exception and makes repository navigation match the current convention.

## What Changes

- Rename live `act/` prompt manifests from verb-first names to object-role names.
- Update specs, documentation, run inputs, and local skill references to the renamed live artifacts.
- Remove the live `act/` verb-first exception from the research workflow structure contract.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `research-workflow-structure`: require live research artifacts to use object/action/role naming without a verb-first `act/` exception.
- `act-entity-discovery`: rename the governed live prompt from `act/discover-entities.md` to `act/entity-discovery.md`.
- `act-platform-comparison`: rename the governed live prompt from `act/compare-platforms.md` to `act/platform-comparison.md`.
- `act-platform-discovery-benchmark`: rename the governed live prompt from `act/benchmark-platform-discovery.md` to `act/platform-discovery-benchmark.md`.
- `act-platform-discovery-report`: rename the governed live prompt from `act/report-platform-discovery.md` to `act/platform-discovery-report.md`.
- `act-platform-comparison-report`: rename the governed live prompt from `act/report-platform-comparison.md` to `act/platform-comparison-report.md`.
- `observe-markdown-output-format`: update examples of governed Markdown-producing prompts to the renamed live artifacts.
- `observe-platform-discovery-coverage`: update the governed source prompt path for the coverage output.

## Impact

- Renames five live files under `act/`.
- Updates README and phase README references.
- Updates `.codex/skills/udt-discover/SKILL.md` so the shortcut resolves the renamed entity discovery manifest.
- Does not change prompt behavior, output shape, scoring, source policy, or saved observation filenames.

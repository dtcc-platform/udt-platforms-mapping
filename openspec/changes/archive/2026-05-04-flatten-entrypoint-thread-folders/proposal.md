## Why

The current phase/thread folder layout is useful for output-heavy areas, but it adds avoidable nesting around low-volume entrypoint artifacts such as scope files and canonical act prompts. Flattening those entrypoints would make common workflow files faster to find while preserving thread grouping where artifact volume grows.

## What Changes

- Flatten `plan/` so thread planning inputs use descriptive top-level filenames instead of one folder per thread.
- Flatten canonical thread prompts in `act/` so each thread prompt is a direct file under `act/`.
- Keep `observe/` grouped by thread because saved model outputs multiply over time.
- Keep `reflect/` grouped by thread because benchmarking, reporting, and synthesis artifacts already form nested work areas.
- Update README guidance and prompt references to use the flattened `plan/` and `act/` entrypoint paths.
- **BREAKING**: Existing canonical paths under `plan/<thread>/` and `act/<thread>/prompt.md` are replaced by flattened paths.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `repository-structure`: Change the governed repository layout so `plan/` and canonical thread prompts under `act/` are flattened, while `observe/` and `reflect/` remain thread-grouped.
- `act-udt-platforms-prompt`: Update required input references and canonical prompt path for the flattened layout.
- `act-udt-initiatives-prompt`: Update required input references and canonical prompt path for the flattened layout.
- `act-udt-platform-comparison-prompt`: Update required input references and canonical prompt path for the flattened layout.

## Impact

- Affected workflow files: `README.md`, `plan/`, `act/`, and prompt templates that refer to planning inputs.
- Affected specs: repository structure plus the three canonical act prompt specs.
- Existing saved outputs under `observe/` and reporting artifacts under `reflect/` remain in place.
- Archived OpenSpec changes remain historical and are not rewritten.

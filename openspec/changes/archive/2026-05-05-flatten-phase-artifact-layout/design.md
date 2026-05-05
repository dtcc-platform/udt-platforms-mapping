# Design

## Layout Rule

Each phase folder SHALL contain direct files. File names encode thread, function, and artifact role:

```text
<phase>/<thread>-<function>-<artifact>.<ext>
```

The `function` segment is omitted when the thread and artifact role are enough, such as `act/udt-platforms.md`.

## Planned File Moves

Observed web outputs:

- `observe/udt-platforms/web-chatgpt.md` -> `observe/udt-platforms-web-chatgpt.md`
- `observe/udt-platforms/web-claude.md` -> `observe/udt-platforms-web-claude.md`
- `observe/udt-platforms/web-gemini.md` -> `observe/udt-platforms-web-gemini.md`
- `observe/udt-platform-comparison/web-chatgpt.md` -> `observe/udt-platform-comparison-web-chatgpt.md`
- `observe/udt-platform-comparison/web-claude.md` -> `observe/udt-platform-comparison-web-claude.md`
- `observe/udt-platform-comparison/web-gemini.md` -> `observe/udt-platform-comparison-web-gemini.md`

Benchmarking:

- `reflect/udt-platforms/benchmarking/benchmark.md` -> `plan/udt-platforms-benchmark.md`
- `reflect/udt-platforms/benchmarking/prompt.md` -> `act/udt-platforms-benchmarking.md`
- `reflect/udt-platforms/benchmarking/coverage.md` -> `observe/udt-platforms-benchmarking-coverage.md`

Reporting:

- `reflect/udt-platforms/reporting/prompt.md` -> `act/udt-platforms-reporting.md`
- `reflect/udt-platforms/reporting/ecosystem.md` -> `reflect/udt-platforms-ecosystem.md`
- `reflect/udt-platform-comparison/benchmarking/prompt.md` -> `act/udt-platform-comparison-benchmarking.md`
- `reflect/udt-platform-comparison/reporting/prompt.md` -> `act/udt-platform-comparison-reporting.md`
- `reflect/udt-platform-comparison/reporting/ecosystem.csv` -> `reflect/udt-platform-comparison-ecosystem.csv`
- `reflect/udt-platform-comparison/reporting/ecosystem-map.html` -> `reflect/udt-platform-comparison-ecosystem-map.html`

Empty nested folders and `.gitkeep` placeholders under `observe/` and `reflect/` are removed after their files move.

## Spec Shape

The old nested reflect specs are retired or narrowed:

- `reflect-udt-platforms-benchmarking` is retired and replaced by `plan-*`, `act-*`, and `observe-*` specs.
- `reflect-udt-platforms-reporting-prompt` is retired and replaced by an `act-*` prompt spec plus a `reflect-*` output spec.
- `reflect-udt-platform-comparison-reporting` is narrowed to synthesized outputs, with prompt behavior moved to an `act-*` spec.

## Tradeoffs

Flattening makes phase ownership clearer and makes the spec naming convention more consistent. The cost is longer filenames in `observe/` and `reflect/`, but the names become searchable and predictable.

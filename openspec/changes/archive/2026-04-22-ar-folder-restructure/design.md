## Context

The repository has grown organically with a flat folder layout (`docs/`, `prompts/`, `responses/`, `evals/`) that does not surface the action research methodology driving the work. Path references are scattered across prompts, eval scripts, and documentation. A restructure to explicit AR phase folders makes the loop visible and accommodates future cycles cleanly.

## Goals / Non-Goals

**Goals:**
- Four top-level folders matching AR phases: `plan/`, `act/`, `observe/`, `reflect/`
- Second level is always the cycle type: `discovery/`, `rating/`
- File names carry no cycle-type prefix (folder path provides that context)
- `rating/` cycle scaffolded across all four phases
- README replaces `methodology.md` as the process explanation
- All internal path references updated

**Non-Goals:**
- Changing any prompt content beyond path references
- Changing the benchmark, eval logic, or report format
- Introducing new research cycles beyond `discovery/` and `rating/`

## Decisions

### AR phase → cycle → content hierarchy

First level is the phase (`plan`, `act`, `observe`, `reflect`). Second level is always the cycle (`discovery`, `rating`). No shared files at phase root — each cycle is fully self-contained so a researcher can read the full loop for one cycle without jumping levels.

**Why:** `source-policy.md` could live at `plan/` root as shared, but discovery does not use it. Keeping each cycle self-contained avoids the question of which shared files apply where.

### Benchmarking and reporting both live in `reflect/`

`reflect/discovery/benchmarking/` holds the benchmark, eval prompt, and coverage report. `reflect/discovery/reporting/` holds the reporting prompt, CSV, and HTML. Both follow the same pattern: a `prompt.md` that drives the work, outputs alongside it at the same level.

**Why:** Benchmarking interprets raw responses (did models recall expected platforms?) — that is reflection, not observation. Observation is raw model output only.

### No `responses/` or `reports/` subfolder

Files in `observe/<cycle>/` sit directly in that folder. Files in `reflect/<cycle>/benchmarking/` and `reflect/<cycle>/reporting/` sit directly in those folders. No extra nesting.

**Why:** The folder path already provides full context. Extra subfolders add navigation cost with no disambiguation value.

### `run.md` renamed to `prompt.md` throughout

The eval runner and reporting script are both prompts. Naming them `prompt.md` makes the pattern consistent: every leaf folder in `act/` and `reflect/` contains a `prompt.md`.

### CSV and HTML move to `reflect/discovery/reporting/`

`ecosystem.csv` and `ecosystem-map.html` are synthesis outputs produced by running a prompt — they belong in reflect, not observe. Observe holds only raw model responses.

## Risks / Trade-offs

- **All existing path references break on rename** — every prompt usage header, the eval prompt, AGENTS.md, and README need updating. Mitigation: tasks checklist covers every known reference; git history preserves old paths.
- **`rating/` scaffolding is empty** — downstream tooling that globs `observe/rating/` or `reflect/rating/` will find nothing. Mitigation: `.gitkeep` files in empty dirs; expected state for a cycle not yet run.
- **`ecosystem.csv` filename is generic** — loses the `platform-inventory` identity from the old filename. Mitigation: folder path `reflect/discovery/reporting/` provides the context; README explains the naming convention.

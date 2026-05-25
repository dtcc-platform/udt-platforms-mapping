## Context

The repository moved from platform-only discovery to entity discovery, but the benchmark workflow still uses `platform-discovery` filenames and a `coverage` output name. The current output is a benchmark evaluation report: it compares saved discovery responses against a benchmark fixture and summarizes found, missing, wrong-type, and novel candidates.

## Goals / Non-Goals

**Goals:**

- Align benchmark artifact names with entity discovery.
- Make the observed output name communicate that it is a benchmark report.
- Preserve the current benchmark report content: recall table, novel finds, and summary.
- Retire obsolete platform-specific benchmark and coverage contracts.

**Non-Goals:**

- Redesign the benchmark fixture contents.
- Add an automated benchmark runner.
- Resolve current benchmark misses or change discovery outputs.

## Decisions

- Use `entity-discovery-benchmark` for the plan fixture and act prompt so the workflow is tied to the discovery action being evaluated.
- Use `entity-discovery-benchmark-report` for the observe artifact so coverage remains a report section instead of the artifact identity.
- Keep the report under `observe/` because it is generated from a run over saved model outputs.
- Keep the benchmark fixture under `plan/` because it is an input used to evaluate future discovery runs.

## Risks / Trade-offs

- Existing references to old filenames can break if missed. Mitigation: search and update all references during implementation.
- Old names may remain in archived history. Mitigation: archive the change with explicit retirement rationale.

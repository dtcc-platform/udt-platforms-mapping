## Context

The `reflect/discovery/benchmarking/` folder contains one coherent evaluation loop:
- `benchmark.md` defines the fixed reference set
- `prompt.md` runs the evaluation against discovery responses
- `coverage.md` is the generated output

The current baseline spec set splits that folder across four capabilities, including a separate alias-column rule. That is more granular than the folder structure and makes the spec set harder to scan.

## Goals / Non-Goals

**Goals:**
- Replace the four discovery-benchmarking baseline specs with one folder-level capability.
- Preserve the current live eval behavior, benchmark schema, alias semantics, and coverage output structure.
- Update the prompt-status audit mapping so it references the merged benchmarking capability.

**Non-Goals:**
- Change the live `reflect/discovery/benchmarking/prompt.md` workflow.
- Change the benchmark table columns or coverage report shape.
- Broaden the benchmark semantics beyond the current discovery-eval use case.

## Decisions

### Decision: Use one folder-level capability

The new capability will govern:
- the benchmark fixture file
- alias semantics inside that file
- the eval prompt behavior
- the coverage report structure

Why:
- This matches the folder structure directly.
- The user prefers fewer, more comprehensible contracts.

Alternative considered:
- Collapse into two specs: one workflow spec and one benchmark spec.
- Rejected because the user wants the strongest possible alignment with the folder structure and fewer top-level contracts.

### Decision: Update prompt-status audit mapping in the same change

The workflow audit will point `reflect/discovery/benchmarking/prompt.md` at the new unified spec and stop expecting a separate coverage shared-contract spec.

Why:
- Otherwise the merged baseline would immediately leave stale audit mappings.

## Risks / Trade-offs

- [The unified spec becomes denser] → Acceptable because density is traded for a much clearer one-folder/one-capability model.
- [Historical archived changes still mention the old capability names] → Leave archives unchanged; only the baseline set is simplified.
- [Future evolution could split fixture and report concerns again] → Re-split later only if they begin changing independently in practice.

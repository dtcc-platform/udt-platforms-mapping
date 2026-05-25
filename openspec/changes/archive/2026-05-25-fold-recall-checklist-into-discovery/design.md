## Context

The current benchmark is an external evaluation workflow: a separate prompt compares saved outputs against `plan/entity-discovery-benchmark.md`. The requested direction is different: known cases should be visible to the discovery model and treated as a planned recall checklist inside the discovery run.

## Goals / Non-Goals

**Goals:**

- Make known recall cases part of the discovery prompt contract.
- Preserve traceability by storing recall-check data in OpenSpec, not an ad hoc plan table.
- Require the model to classify each known case as found or as a specific miss category.
- Remove the standalone benchmark workflow and files.

**Non-Goals:**

- Preserve blind benchmark evaluation.
- Add CI automation.
- Re-run discovery outputs.

## Decisions

- Name the data contract `plan-entity-discovery-recall-checklist` because it is planned input for one action, not an independent benchmark workflow.
- Model each known entity as an individual requirement so future additions have explicit OpenSpec deltas and rationale.
- Add recall-check reporting to `observe-entity-discovery` so saved outputs carry both discovery results and known-case self-audit.
- Keep miss categories small: `found`, `recall-miss`, `wording-miss`, `classification-miss`, `evidence-limited`, and `out-of-scope`.
- Remove `act/entity-discovery-benchmark.md`, `plan/entity-discovery-benchmark.md`, `observe/entity-discovery-benchmark-report.md`, and their specs because they no longer define active workflow.

## Risks / Trade-offs

- The recall checklist is not a blind benchmark because the model sees the known candidates. This improves completeness and explanations, but it cannot measure unaided model recall.
- The model may overfit by including checklist entities without enough evidence. The discovery contract mitigates this by requiring classification, evidence handling, and miss explanations.

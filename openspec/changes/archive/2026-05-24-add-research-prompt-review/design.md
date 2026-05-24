## Context

The repository separates prompt manifests from behavior/output contracts. A resolver combines `act/` manifests, required specs, and run inputs into a concrete prompt. Different agents can independently review that resolved prompt to reveal missing contracts, invented behavior, ambiguous contract wording, or resolver mistakes.

The unresolved design question is storage. The manifest is source material under `act/`, while a resolved prompt is generated evidence for a review run. Review results are also observations. Only consolidated findings belong under `reflect/`.

## Goals / Non-Goals

**Goals:**

- Define prompt review as a cross-phase research governance capability.
- Store resolved prompt snapshots and per-agent prompt reviews in `observe/`.
- Store optional synthesized review findings in `reflect/`.
- Keep accepted fixes flowing through normal OpenSpec changes.
- Make README documentation and diagrams clear enough that contributors know where each artifact belongs.

**Non-Goals:**

- Add a resolver implementation.
- Require every prompt run to be reviewed.
- Treat reviewed resolved prompts as canonical source prompts.
- Replace `act/` manifests or OpenSpec behavior contracts.

## Decisions

1. Name the capability `research-prompt-review`.

   Rationale: the workflow crosses phases. It reviews `act/` manifests, `plan/` run inputs, behavior specs, output specs, resolved prompts, observed review findings, and optional reflection synthesis.

2. Store resolved prompt snapshots in `observe/`.

   Rationale: resolved prompts are generated artifacts. They are evidence of how a manifest and contracts were interpreted at a point in time, not the canonical source of behavior.

3. Store per-agent review outputs in `observe/`.

   Rationale: reviewer reports are observed outputs from agents. They should be preserved independently so interpretation differences are visible.

4. Store consolidated review synthesis in `reflect/`.

   Rationale: synthesis compares observed review outputs and identifies accepted ambiguities or improvements that should become OpenSpec changes.

5. Keep accepted fixes in OpenSpec changes.

   Rationale: review findings should not silently mutate prompts or specs. Accepted findings need proposal/spec/task history before baseline changes.

## Risks / Trade-offs

- More artifact types under `observe/` can make the folder busier -> use explicit filename patterns for resolved prompts and reviews.
- Review outputs could be mistaken for canonical prompt sources -> README and spec language must state that `act/` manifests and OpenSpec specs remain the source of truth.
- Multi-agent review may produce disagreement -> disagreement is useful evidence of ambiguity and should be handled through reflection and OpenSpec changes.

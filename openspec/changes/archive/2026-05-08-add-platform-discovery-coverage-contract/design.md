## Context

The current platform discovery prompt already asks for broad global discovery, adjacent search language, and seed-list use. However, it does not define minimum candidate volume, category quotas, seed-list extraction depth, or a coverage statement in the saved output. As a result, a model can return a small selected set while still appearing contract-compliant.

## Goals / Non-Goals

**Goals:**

- Add explicit recall coverage targets for platform discovery runs.
- Make seed-list use operational by requiring multiple seed-list families and candidate extraction from each.
- Preserve the existing `platform-definition` classification contract as the authority for assigning `Type`.
- Make output self-auditing by requiring a coverage statement before the summary table.

**Non-Goals:**

- Do not make platform discovery claim global completeness.
- Do not force weak or unsupported artifacts into the output only to satisfy quotas.
- Do not change the platform comparison contract, which remains limited to artifacts classified as `platform`.
- Do not replace the existing benchmark fixture or coverage evaluation workflow.

## Decisions

- Introduce `platform-discovery-coverage` as a separate contract instead of embedding quotas only in `act-discover-platforms-prompt`.
  - Rationale: coverage pressure is reusable research behavior, while the act prompt remains the manifest-level execution contract.
  - Alternative considered: add all quotas directly to `act-discover-platforms-prompt`; rejected because it would mix discovery coverage policy with prompt assembly behavior.

- Use target quotas with an evidence-based escape clause.
  - Rationale: the prompt should keep searching, but it should not fabricate or include unsupported rows to hit a number.
  - Alternative considered: absolute hard minimums without exception; rejected because web search can fail or evidence may be unavailable.

- Require a compact coverage statement in `observe-platform-discovery`.
  - Rationale: a researcher should be able to see whether a saved run met the intended coverage pressure before reading the artifact table.
  - Alternative considered: only enforce quotas in the prompt; rejected because saved outputs would not reveal incomplete runs clearly.

## Risks / Trade-offs

- Larger outputs may be harder to read in one web response. Mitigation: keep the output contract tabular and require concise artifact sections.
- Some models may still stop early. Mitigation: require the output to state unmet targets and search gaps explicitly.
- Quotas may bias discovery toward easy-to-find web GIS tools. Mitigation: keep type classification governed by `platform-definition` and require platform, framework, module, and boundary coverage.

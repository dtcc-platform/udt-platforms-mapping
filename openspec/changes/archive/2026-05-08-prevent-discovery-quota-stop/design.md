## Context

The existing coverage contract defines useful minimum quotas, but a model can still treat those quotas as a target to stop at. DTCC Platform shows the gap: a high-relevance regional, academic, open-source UDT platform can be missed when generic global candidates satisfy the counts first.

## Goals / Non-Goals

**Goals:**

- Make quotas explicitly operate as minimum quality gates, not stopping conditions.
- Add a post-quota recall pass for regional, academic, open-source, and research-center UDT platforms.
- Encourage replacement of weaker, less direct candidates with stronger technical artifacts when found.
- Add DTCC Platform as a named scenario to test targeted recall for ambiguous regional names.

**Non-Goals:**

- Do not make discovery claim global completeness.
- Do not add DTCC Platform as a hardcoded required row in every output.
- Do not change the `platform-definition` classification criteria.
- Do not change output table columns or the benchmark workflow.

## Decisions

- Strengthen `platform-discovery-coverage` instead of increasing numeric quotas.
  - Rationale: the issue is stopping behavior and recall diversity, not simply that 40 is too low.
  - Alternative considered: raise the minimum to 60 or 80; rejected because the same stopping-target behavior could recur at a higher count.

- Require a post-quota targeted recall pass.
  - Rationale: once generic candidates satisfy quotas, the model needs an explicit second pass for less search-visible but highly relevant research platforms.
  - Alternative considered: add regional search terms only to `act-discover-platforms-prompt`; rejected because quota interpretation belongs in the coverage contract.

- Use DTCC Platform as a scenario, not a mandatory fixture.
  - Rationale: scenarios make the expected behavior testable without turning the discovery contract into a static list of required artifacts.

## Risks / Trade-offs

- More recall passes can lengthen web runs. Mitigation: require at least one targeted pass rather than unbounded search.
- Candidate replacement may require judgment. Mitigation: replacement is based on stronger evidence and clearer fit to `platform-definition`.
- Named examples may overfit one case. Mitigation: DTCC Platform is framed as a scenario for a broader class of regional, academic, open-source, and research-center platforms.

## Context

The repository currently treats its research workflow as two cycles:

- `discovery`
- `rating`

That model was useful early on, but it is now too coarse for the workflow the repository is trying to make stable and trustworthy.

The paper `UDT_SLR_Chalmers_ComputersInIndustry.pdf` helped expose a better split:

- technical artifacts are not the same thing as initiatives/projects
- platform comparison is not the same thing as broad mapping

The repository should therefore stop using one overloaded first cycle and instead use:

- `udt-platforms`
- `udt-initiatives`
- `udt-platform-comparison`

## Goals / Non-Goals

**Goals:**

- Replace `discovery` with a more precise technical-artifact cycle
- Introduce a separate initiative/project cycle
- Replace `rating` with a paper-aligned comparison cycle name
- Define explicit output schemas for the first two cycles
- Make the comparison handoff rule unambiguous
- Realign folder, README, and calibration contracts around the new cycle model

**Non-Goals:**

- Fully redesign every prompt body in this proposal artifact
- Redesign the prompt-status workflow
- Remove the Action Research phase structure
- Remove the `calibration/` archive
- Expand calibration leaf folders beyond `prompt.md` and `result.md`

## Decisions

### Decision: Use `udt-platforms`, `udt-initiatives`, and `udt-platform-comparison` as the canonical cycle names

The repository will use three research-cycle names:

- `udt-platforms`
- `udt-initiatives`
- `udt-platform-comparison`

These names are more explicit than `discovery` and `rating`, and they better reflect the workflow's intended responsibilities.

Alternative considered:

- keep `discovery` and `rating`
  - Rejected because they hide the distinction between technical mapping, initiative mapping, and platform comparison.

### Decision: Merge literature-led artifact discovery and live ecosystem mapping into `udt-platforms`

The repository will not introduce a separate `slr` cycle in this change.

Instead, `udt-platforms` will absorb both:

- literature-grounded identification
- current ecosystem verification and extension

This keeps the workflow simpler while still allowing the methodology to be informed by the paper.

Alternative considered:

- separate `slr` and `mapping`
  - Rejected because it adds another top-level cycle before the current workflow has stabilized around the more important artifact-vs-initiative distinction.

### Decision: Treat initiatives as a separate cycle, not as a deployment column

`udt-initiatives` will be its own cycle rather than a column inside the technical-artifact mapping output.

This avoids mixing:

- ontology of technical artifacts
- deployment/project context

It also better matches the paper's use of initiatives/projects as meaningful first-phase outputs.

Alternative considered:

- keep initiatives as a `Deployment` column inside technical-artifact mapping
  - Rejected because it breaks down when initiatives are important even when the underlying technical substrate is unclear, mixed, or not cleanly classifiable.

### Decision: Use a technical-artifact table for `udt-platforms`

The `udt-platforms` summary table will use:

- `Name`
- `Link`
- `Type`
- `Reason`

`Type` will be one of:

- `platform`
- `framework`
- `module`
- `excluded`

This preserves a software-oriented classification that can be consumed by the comparison cycle.

Alternative considered:

- use paper categories directly as `framework`, `platform`, `initiative`
  - Rejected because initiatives are being split into their own cycle in this design.

### Decision: Use an initiative table for `udt-initiatives`

The `udt-initiatives` summary table will use:

- `Initiative`
- `Link`
- `Uses`
- `Reason`

`Uses` is a comma-separated list of artifact names from `udt-platforms`, or `?` if unclear.

This allows initiatives to remain meaningful even when they relate to multiple artifacts or when the technical substrate is only partially clear.

### Decision: Handoff into comparison is platform-only

`udt-platform-comparison` will only accept rows from `udt-platforms` where:

- `Type = platform`

This replaces the current softer handoff through discovery Layer values with a simpler and more explicit rule.

Alternative considered:

- allow frameworks or modules into comparison
  - Rejected because the comparison cycle is meant to benchmark selected UDT platforms side by side, not to compare every artifact class.

### Decision: Keep `calibration/` but update its path semantics to the new cycle names

The archive remains:

- `calibration/<research>/<cycle>/<agent>/`

But examples and expectations will use the new cycle names under `<research>`, such as:

- `calibration/udt-platforms/c1/agent-a/`
- `calibration/udt-initiatives/c1/agent-b/`
- `calibration/udt-platform-comparison/c1/agent-c/`

## Risks / Trade-offs

- [Large rename surface] → This change affects many paths and baseline assumptions; implementation should proceed in explicit, reviewable steps.
- [Old discovery/rating contracts are deeply embedded] → The change must clearly mark them as superseded and replace them with the new cycle model rather than mixing both indefinitely.
- [Initiatives may have uncertain `Uses` links] → Allow `?` and keep the initiative cycle valid even when the technical relation is unclear.
- [Merged literature/ecosystem mapping can still become broad] → Keep `udt-platforms` focused on technical artifacts rather than allowing it to drift back into initiative tracking.

## Migration Plan

1. Add cycle-level contracts for `udt-platforms`, `udt-initiatives`, and `udt-platform-comparison`.
2. Update `ar-folder-layout` to replace `discovery` and `rating` with the three new cycles.
3. Update `calibration-archive` examples to use the new research-cycle names.
4. Rewrite README to explain the new cycle model and the new handoff rules.
5. Replace or retire old discovery/rating capability specs and then implement the path changes in the live repository.

## Open Questions

- Whether `udt-platforms` should later split again into separate literature and live-ecosystem subcycles is intentionally deferred.
- Whether `udt-initiatives` should eventually gain its own benchmarking/reporting substructure beyond a summary table is intentionally deferred.

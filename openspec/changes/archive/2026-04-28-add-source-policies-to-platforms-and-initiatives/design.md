## Context

`udt-platform-comparison` already has an explicit source-policy input because scored claims need a governed evidence hierarchy. `udt-platforms` and `udt-initiatives` currently rely on implicit judgment even though they also use mixed evidence such as official documentation, repositories, academic literature, project pages, and vendor communications.

The paper this repository is increasingly using as a methodological reference separates source handling into two practical regimes:
- literature/database-driven review and screening
- broader platform characterization using official resources and secondary material, then validating weak spots through expert judgment

The repository does not yet have a separate expert-validation workflow for `udt-platforms` or `udt-initiatives`, so the immediate design goal is to make source-priority rules explicit at the planning layer.

## Goals / Non-Goals

**Goals:**
- Add a canonical source-policy file for `udt-platforms`
- Add a canonical source-policy file for `udt-initiatives`
- Make `udt-platforms` prompt execution explicitly depend on the new source policy
- Encode cycle-level requirements that source quality and prioritization are governed rather than ad hoc
- Keep the new policies distinct from the stricter comparison policy while following the paper’s mixed-source logic

**Non-Goals:**
- Redesign the `udt-platform-comparison` source policy in this change
- Add a new expert-validation cycle or Delphi-style workflow
- Introduce new output columns or change the summary-table contracts for `udt-platforms` or `udt-initiatives`
- Add a canonical `act/udt-initiatives/prompt.md` in this change

## Decisions

### Decision: source policy lives in `plan/` as a governed input, not inside prompt specs

Source policy is an execution input that researchers may refine over time without collapsing it into prompt prose. This keeps the method/input split intact:
- OpenSpec governs the existence and role of the file
- the `plan/` file carries the active policy text used by the cycle

Alternative considered:
- Inline all source-priority rules directly into prompt specs and prompt files
  - rejected because it makes source-policy edits look like prompt rewrites and reduces reuse across cycles

### Decision: `udt-platforms` and `udt-initiatives` get separate policies

The two cycles use overlapping but different evidence:
- `udt-platforms` centers on technical artifacts and should prioritize official docs, repositories, standards, and literature
- `udt-initiatives` centers on projects and deployments and should explicitly allow official initiative pages, programme documentation, and institutional reports

Alternative considered:
- one shared mapping policy for both cycles
  - rejected because initiative evidence is often project-centric rather than product-centric, and the repo should acknowledge that difference directly

### Decision: only `udt-platforms` prompt contract changes in this proposal

`udt-platforms` already has a canonical prompt, so the new policy must become one of its required inputs. `udt-initiatives` does not yet have an equivalent prompt contract, so its source policy is added at the cycle and folder-layout level only.

Alternative considered:
- delay both policy files until `udt-initiatives` has a full prompt
  - rejected because the cycle can still be governed at the plan/spec level now, and that governance will make later prompt creation cleaner

### Decision: comparison policy remains stricter and separate

This proposal does not unify all three policies. `udt-platform-comparison` already has a score-oriented source policy, and the new mapping policies should remain broader while still defining ranking, unacceptable sources, and contradiction handling.

Alternative considered:
- replace all three with one repo-wide source policy
  - rejected because the paper itself effectively uses different source regimes for mapping/review and for platform evaluation

## Risks / Trade-offs

- [Policy overlap across cycles] → Keep the new policies narrower in purpose and avoid rewriting the existing comparison policy in this change.
- [`udt-initiatives` remains partially governed without a canonical prompt] → Govern the planning input and cycle-level requirement now; add prompt-level enforcement later if that cycle becomes executable.
- [Researchers may assume source policy guarantees truth rather than evidence discipline] → Wording should emphasize prioritization, documentation, and contradiction handling rather than certainty.
- [README drift if source-policy files are added silently] → Only update documentation if implementation makes the new inputs part of the active walkthrough.

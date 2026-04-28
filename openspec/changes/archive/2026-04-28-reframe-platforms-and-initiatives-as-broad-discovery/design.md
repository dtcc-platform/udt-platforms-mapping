## Context

The repository recently added governed source-policy inputs for `udt-platforms` and `udt-initiatives`. That improved evidence discipline, but it also made the first two threads behave more like validated characterization stages than broad global discovery stages.

The current direction is different:
- `udt-platforms` should cast a wide net across technical artifacts
- `udt-initiatives` should cast a wide net across projects, programmes, and deployments
- `udt-platform-comparison` should remain the stage where stricter evidence expectations hold

This is not just a documentation preference. It changes the epistemic role of the first two threads from “high-confidence governed mapping” to “broad discovery with later tightening.”

## Goals / Non-Goals

**Goals:**
- Remove governed source-policy requirements from `udt-platforms`
- Remove governed source-policy requirements from `udt-initiatives`
- Reframe both threads as broad global discovery oriented toward recall
- Keep stricter evidence discipline for `udt-platform-comparison`
- Update prompt, cycle, and folder-layout contracts to reflect that role split

**Non-Goals:**
- Remove or weaken the comparison-cycle source policy
- Redesign the output tables for `udt-platforms` or `udt-initiatives`
- Introduce a new expert-validation thread in this change
- Eliminate all caution about evidence quality from discovery prompts; the change is about removing governed source-policy files, not encouraging careless claims

## Decisions

### Decision: discovery breadth is governed at the cycle level, not by per-thread source-policy files

`udt-platforms` and `udt-initiatives` should remain governed, but the governance should describe the role of the thread rather than require ranked source-policy inputs.

That means:
- thread purpose stays explicit
- broad recall becomes a design goal
- evidence quality tightening is deferred to later threads and reflection

Alternative considered:
- keep the source-policy files but soften their wording
  - rejected because their existence still frames the threads as policy-driven filtering stages

### Decision: remove only the first two source-policy capabilities

`udt-platform-comparison` keeps its source policy because comparison is where claims become evaluative and score-bearing.

Alternative considered:
- unify all three threads under the same looser discovery model
  - rejected because comparison needs stronger evidence discipline than candidate gathering

### Decision: the `udt-platforms` prompt should still express broad evidence guidance informally

Removing a governed source-policy file does not mean the prompt should be silent about evidence use. The prompt should still favor primary evidence where available and avoid overclaiming, but those rules no longer live as a separate governed plan input.

Alternative considered:
- delete all evidence guidance from the prompt
  - rejected because broad discovery still needs minimal restraint to avoid low-signal noise

## Risks / Trade-offs

- [Lower confidence in early-stage discovery outputs] → Make the role of the first two threads explicit: they optimize for recall, not final validation.
- [Users may misread discovery outputs as fully vetted] → Update README and cycle contracts to clarify that stricter evidence discipline belongs later, especially in comparison and reflection.
- [Recently added source-policy files become short-lived churn] → Treat this as a deliberate methodological correction and preserve the reasoning in archived change history.
- [Prompt behavior may become inconsistent without a governed policy file] → Keep lightweight evidence guidance in the live prompt even after removing the separate governed input.

## Migration Plan

1. Remove `source-policy.md` from `plan/udt-platforms/` and `plan/udt-initiatives/`
2. Retire the corresponding baseline source-policy specs
3. Update `act/udt-platforms/prompt.md` to remove the required input while keeping broad evidence guidance
4. Update thread and folder-layout specs to describe broad discovery semantics
5. Update README wording so the first two threads are understood as recall-oriented discovery and the comparison thread as higher-confidence evaluation

## Open Questions

- Should broad discovery be described as “recall-first,” “global discovery,” or “exploratory mapping” in the README?
- Should `udt-initiatives` eventually gain a canonical prompt before any further methodological tightening is attempted?

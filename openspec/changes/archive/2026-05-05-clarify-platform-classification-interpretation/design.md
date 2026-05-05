## Context

Platform discovery depends on a stable `Type` classification contract. The current prompt already says to use `plan/platform-definition.md` as authoritative, but the definition file mainly lists categories and observable criteria.

That leaves too much interpretation to each model when an artifact looks like both a platform and a framework, when evidence is weak, or when an item is primarily an initiative rather than a technical artifact.

## Goals / Non-Goals

**Goals:**

- Make platform classification more repeatable across model runs.
- Keep `plan/platform-definition.md` as the source of truth for classification logic.
- Require `act/discover-platforms.md` to render the interpretation rules into model-facing instructions.
- Preserve the existing `Type` values: `platform`, `framework`, `module`, and `excluded`.

**Non-Goals:**

- Do not change the platform discovery output format.
- Do not add a new `Type` value.
- Do not move initiative discovery into platform discovery.
- Do not make platform discovery exhaustive or evidence-perfect.

## Decisions

- Add interpretation rules to the planning contract rather than only the prompt.
  - Rationale: the contract should define how to classify; the prompt should operationalize it.
  - Alternative considered: patch only `act/discover-platforms.md`. That would improve the current prompt but leave the governing contract thin.

- Prefer classification by observable presentation and role.
  - Rationale: broad web discovery often lacks enough evidence for deeper architectural verification.
  - Alternative considered: require proof of deployment or technical architecture for every platform. That would reduce recall too much for discovery.

- Use tie-break rules for borderline cases.
  - Rationale: repeated runs need deterministic guidance when an artifact overlaps multiple categories.
  - Alternative considered: leave ambiguity to model judgment. That makes cross-agent comparison harder.

## Risks / Trade-offs

- Stricter interpretation rules may exclude some valid candidates -> Keep discovery broad and allow platform classification when an artifact is presented as usable for city-scale UDT work.
- Tie-break rules may oversimplify complex artifacts -> Require a short classification rationale in the artifact reason or details.
- The prompt could duplicate too much of the planning file -> Keep the full rules in `plan/platform-definition.md` and have the prompt inline the required input as it already does.

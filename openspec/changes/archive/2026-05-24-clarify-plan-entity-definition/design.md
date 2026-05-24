## Context

`plan-entity-definition` is the planning contract that tells agents how to classify UDT discovery candidates. The current spec mixes an internal grouping concept, `EntityKind`, with the output-facing `Type` field before explaining why both exist.

The output contract should remain simple because downstream discovery artifacts and human review rely on `Type` values such as `platform`, `framework`, `module`, `initiative`, and `excluded`. The internal `artifact` concept is still useful because it groups the three technical artifact types and prevents repeated wording across their definitions.

## Goals / Non-Goals

**Goals:**

- Make the first requirement understandable without changing the allowed output `Type` values.
- Document `artifact` as an internal parent concept for `platform`, `framework`, and `module`.
- Replace specific examples with durable boundary rules.
- Make initiative/artifact separation and uncertainty handling easier for agents to apply consistently.

**Non-Goals:**

- Add, remove, or rename discovery output columns.
- Add new allowed `Type` values.
- Reclassify existing research outputs.
- Change the broader research workflow or phase naming convention.

## Decisions

- Center the first requirement on output `Type` because this is what discovery tables expose and what reviewers see. `EntityKind` remains as explanatory internal structure rather than the first thing a reader must understand.
- Keep `artifact` because it removes duplication and helps distinguish technical UDT artifacts from initiatives and excluded candidates. Removing it would force `platform`, `framework`, and `module` to each restate the same technical-boundary rule.
- Replace named product-family examples with principle-based scenarios. The spec should describe why communication, presentation, and narrative mapping tools are excluded unless they satisfy UDT artifact or initiative criteria, rather than encoding one historical example.
- Treat uncertainty as explanation, not classification. Agents should select the best supported allowed `Type` and preserve uncertainty in reason/substrate/details instead of inventing types such as `unknown`, `tool`, or `system`.

## Risks / Trade-offs

- Readers may expect every concept in the spec to appear as an output column. Mitigation: state directly that `artifact` is internal and that output rows use `Type`.
- Generic exclusion language may feel less concrete than a named example. Mitigation: keep scenarios concrete enough to mention communication, presentation, and narrative publishing behavior.
- Tightening language may expose older artifacts that used looser terminology. Mitigation: this change clarifies forward-facing classification behavior and does not require retroactive research-output migration.

## Context

The phase folders now have clearer names: `plan/` defines inputs and world assumptions, `act/` contains executable prompts, `observe/` stores raw model outputs and generated observations, and `reflect/` stores synthesized outputs.

Output contracts should follow that same phase model. A prompt can render an output contract into instructions, but the contract itself belongs to the phase where the output is stored.

## Goals / Non-Goals

**Goals:**

- Put raw model output contracts under `observe-*` specs.
- Put synthesized/exported output contracts under `reflect-*` specs.
- Keep `act-*` specs as execution contracts that require conformance to observe/reflect contracts.
- Keep `plan-*` specs focused on definitions, selected inputs, scoring criteria, policies, and fixtures.

**Non-Goals:**

- Do not change the actual output formats in this change.
- Do not regenerate model outputs.
- Do not introduce new folders or frontmatter.

## Decisions

1. Use observe specs for raw web response contracts.

   Rationale: Saved model outputs live under `observe/`, so their shape should be governed there. This also lets multiple prompts or tools rely on the same output contract without duplicating it.

2. Keep act prompts operationally explicit.

   Rationale: A model still needs concrete instructions. The prompt may include the table and section format, but the act spec should say those instructions implement the observe contract.

3. Use reflect specs for synthesized/exported outputs.

   Rationale: Reporting prompts write reflection artifacts, so CSV/HTML/table output schemas belong to the corresponding `reflect-*` specs.

## Risks / Trade-offs

- More specs to maintain -> The ownership boundary is clearer and reduces drift between plan, act, observe, and reflect.
- Prompt text still contains output details -> This is necessary for execution, but the governing source of truth is now the observe/reflect spec.

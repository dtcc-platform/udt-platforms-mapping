## Context

The current repository has two overlapping layers for planning behavior. Some `plan/` files contain behavior rules, while OpenSpec specs govern those files. That makes review indirect: a reviewer asks whether a prompt implements a spec that says to use a plan file that contains the real behavior.

The desired model is simpler:

- specs define behavior contracts
- `plan/` contains run inputs
- prompts operationalize behavior contracts using run inputs

## Goals / Non-Goals

**Goals:**

- Move stable definitions, policies, and rubrics into behavior specs.
- Keep `plan/` for selected inputs, benchmark fixtures, and run-specific scope material.
- Make prompt review direct: reviewers compare prompts against behavior specs.
- Keep canonical output contracts and save locations unchanged.

**Non-Goals:**

- Do not remove the `plan/` folder.
- Do not change `observe/` or `reflect/` folder semantics.
- Do not rewrite all archived history.
- Do not change research outputs in this change.

## Decisions

- Introduce behavior specs without the `plan-` prefix for stable behavior.
  - Rationale: names such as `platform-definition` and `platform-comparison-rubric` describe the behavior scope directly.
  - Alternative considered: keep `plan-*` specs but change their meaning. That would preserve names but keep the old ambiguity.

- Retire plan behavior specs after migration.
  - Rationale: leaving both old and new behavior specs active would recreate duplication.
  - Alternative considered: keep old plan specs as redirects. That reduces breakage but increases long-term confusion.

- Keep `plan/platform-comparison-set.md` and `plan/platform-discovery-benchmark.md` as run-input artifacts.
  - Rationale: they contain concrete selected data for runs rather than stable behavior.
  - Alternative considered: model every input as a spec. That would overload OpenSpec with run data.

- Update prompts to distinguish required behavior contracts from required run inputs.
  - Rationale: prompts should show which parts are governed behavior and which parts are run-specific context.
  - Alternative considered: inline all specs and all inputs under one "Required Inputs" list. That hides the boundary this change is meant to clarify.

## Risks / Trade-offs

- Moving behavior out of `plan/` may make prompts more dependent on OpenSpec paths -> Use explicit "Required Contracts" sections in prompts.
- Retiring `plan-*` specs may break old mental models -> Update README, `plan/README.md`, repo-structure, and prompt specs together.
- Some current plan files mix behavior and examples -> During implementation, keep examples only when they are run input; move decision rules into specs.
- OpenSpec specs may become too verbose for prompt inlining -> Write behavior specs with researcher/model-facing rule text plus normative requirements.

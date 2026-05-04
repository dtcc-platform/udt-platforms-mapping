## Context

The `udt-platforms` workflow currently has three places that mention the same output contract:

- `openspec/specs/udt-platforms-cycle/spec.md`
- `openspec/specs/act-udt-platforms-prompt/spec.md`
- `plan/udt-platforms/scope.md`

The scope file is a required prompt input and should stay focused on classifying artifacts by `Type`. The prompt output shape is already governed by OpenSpec and implemented in `act/udt-platforms/prompt.md`, so keeping a separate output-format reminder in the scope file creates duplicated authority.

## Goals / Non-Goals

**Goals:**

- Make `plan/udt-platforms/scope.md` classification-only.
- Keep the normative output contract in OpenSpec.
- Make `act/udt-platforms/prompt.md` the operational owner of the concrete output-format instructions used in web runs.
- Preserve the existing output schema and comparison handoff rule.

**Non-Goals:**

- Change the `udt-platforms` table schema.
- Change the allowed `Type` values.
- Change saved observation file locations.
- Redesign the broader plan/act/observe/reflect workflow.

## Decisions

### Decision: Scope remains a required prompt input, but only for classification

`plan/udt-platforms/scope.md` will continue to be inlined into the resolved prompt because the model needs the Type criteria at runtime. It will no longer carry a summary table reminder or handoff text.

Alternative considered:

- Leave the reminder in scope.
  - Rejected because it duplicates the prompt and spec contracts and makes the plan file responsible for output formatting.

### Decision: The prompt spec owns the concrete output format

The `act-udt-platforms-prompt` spec will require the prompt template to include the summary table columns, Reason semantics, platform-only comparison eligibility, and per-artifact section template.

Alternative considered:

- Put the concrete output format only in the cycle spec.
  - Rejected because the cycle spec governs the thread, while the prompt spec governs the artifact that actually produces the web-model instructions.

### Decision: The cycle spec keeps the high-level thread contract

The `udt-platforms-cycle` spec will continue to state the thread-level output schema and Type set. It will also explicitly require the scope file to avoid output-format reminders.

Alternative considered:

- Remove all output-contract language from the cycle spec.
  - Rejected because downstream workflow rules, especially comparison eligibility, are cycle-level behavior.

## Risks / Trade-offs

- [Duplication still exists between cycle and prompt specs] -> Mitigation: keep cycle-level language high-level and prompt-level language concrete to match each spec's responsibility.
- [Existing readers may expect the reminder in scope] -> Mitigation: the prompt continues to contain the full output format, so no execution capability is lost.
- [The scope file may drift back into output instructions] -> Mitigation: add an explicit negative requirement in the cycle spec.

## Migration Plan

1. Update `plan/udt-platforms/scope.md` to remove `## Output Contract Reminder`.
2. Update `openspec/specs/udt-platforms-cycle/spec.md` through the delta to make the scope-file boundary explicit.
3. Update `openspec/specs/act-udt-platforms-prompt/spec.md` through the delta to make the prompt output-format ownership explicit.
4. Verify the prompt still includes the complete output format needed for web-model execution.

# Design: reframe-calibration-as-isolated-spec-review

## Summary

Replace default result-based calibration with a lighter and more credible prompt-interpretation calibration process.

## Current Model

The current baseline model in `calibration/` assumes:

- one prompt and one result per agent run
- prompt/result pairs are the main calibration evidence
- reflection happens after running prompts through web interfaces

This is expensive and noisy for the specific problem we actually care about first:
whether multiple agents interpret the same governing spec consistently.

## New Model

Calibration becomes a staged process:

### Stage 1: Shared Prompt Generation

All prompt-generation agents work from the same accepted governing spec.

The generated prompts are saved into shared calibration artifacts, for example:

- `calibration/act-udt-platforms-prompt/c01/codex/prompt.md`
- `calibration/act-udt-platforms-prompt/c01/gemini/prompt.md`
- `calibration/act-udt-platforms-prompt/c01/claude/prompt.md`

At this point, prompts are visible to all reviewers.

The `c01` segment matters because it preserves the accepted baseline identity for the round.
That makes it possible later to compare how each agent's generated prompt changed between `c01`, `c02`, and later accepted baselines.

### Stage 2: Isolated Review And Proposal Branches

After all prompts are available, create one branch per agent.

Each agent branch:

- reads the governing spec
- reads the shared generated prompts
- writes one independent OpenSpec change proposal

Crucially, agents on these branches do **not** see each other's proposals before merge.

### Stage 3: Calibration Branch Merge

Merge the agent branches into a dedicated calibration branch.

That branch contains:

- all generated prompts
- all isolated OpenSpec proposals

Only at this point can agents or humans compare proposals side by side.

### Stage 4: Synthesis During Implementation

Once the proposals are merged into the calibration branch, the merged OpenSpec deltas themselves become the review surface.

At this stage, one implementing agent or human reviewer can:

- inspect what is common across the proposals
- inspect where they differ
- decide what to keep in the accepted follow-up change

### Stage 5: Accepted Change

Human review selects what should become a real governed change.
That accepted subset becomes a normal OpenSpec change, which is then implemented and eventually merged back to `main`.

## Branching Rule

Branching should happen **after prompt generation**, not before.

Reason:

- the important shared context for review is the set of generated prompts
- agents should review the same visible prompt set
- isolation is needed for proposals, not for prompt generation itself

Recommended branch sequence:

1. accepted spec state on `main`
2. shared prompt artifacts written under `calibration/`
3. per-agent branches named only by agent, such as `codex`, `gemini`, and `claude`
4. merge into one calibration branch
5. accepted follow-up spec change back to `main`

## Why A Dedicated Calibration Branch Is Better Than `main`

Intermediate review artifacts and competing proposals are not accepted workflow state.
They should not go directly to `main`.

Using a dedicated calibration branch:

- preserves a clean acceptance boundary
- keeps isolated proposals out of the accepted baseline
- gives one place to synthesize before choosing what becomes a real spec change

## Artifact Model

The old leaf shape:

- `prompt.md`
- `result.md`

is no longer sufficient.

The new shared calibration area should at minimum support:

- `calibration/<spec-name>/c01/<agent>/prompt.md`

The isolated proposal work itself should use normal OpenSpec change directories on the per-agent branches.

The merged calibration branch does not require separate comparison-report artifacts.
The merged OpenSpec proposal deltas are the primary comparison surface.

## Result-Based Calibration

This proposal does not forbid result-based calibration.
It changes the default ordering.

Result-based calibration becomes a secondary, selective validation step used when needed after spec interpretation has already been tightened.

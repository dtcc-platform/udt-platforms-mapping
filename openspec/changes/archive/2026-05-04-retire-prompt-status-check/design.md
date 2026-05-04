# Design

## Overview

Remove the prompt-status maintenance workflow rather than preserving it as a dormant or archived live file. The active repository surface should contain the canonical research prompts and their governing specs, while validation remains handled by OpenSpec.

## Decisions

- Delete the live maintenance prompt and generated report from `act/`.
- Remove the `act-check-prompts-status` baseline spec because no active file or behavior remains to govern.
- Narrow the `repository-structure` spec so `act/` is described as the home of canonical thread prompts only.

## Alternatives Considered

- Keep only the report: rejected because a static report quickly becomes stale and gives a false signal.
- Keep only the prompt: rejected because maintaining a parallel prompt audit mapping duplicates OpenSpec validation and must be updated after every prompt/spec restructure.
- Move the files to a thread folder: rejected because the repository has already flattened entrypoints and the workflow itself is being retired.

# Design

## Overview

Replace calibration as a file-storage area with prompt interpretation review as a change-management workflow. The new workflow keeps the useful part of calibration, cross-agent scrutiny of prompt/spec alignment, but records decisions through OpenSpec deltas.

## Workflow

1. Start from an accepted governing spec.
2. Ask one agent to generate or update the operational prompt from that spec.
3. Ask another agent to review whether the prompt is a faithful interpretation of the spec and whether the spec can be made clearer.
4. If the reviewer finds a real improvement, capture it as an OpenSpec delta.
5. Regenerate the prompt from the updated contract.
6. Continue with the next reviewer, such as Gemini, using the current accepted change state.

## Decisions

- Sequential review replaces isolated review. Later agents may see earlier accepted deltas because the point is iterative improvement, not independent ambiguity detection.
- OpenSpec artifacts replace `calibration/` storage. Proposals, designs, delta specs, tasks, and archived changes become the audit trail.
- README keeps one primary diagram. The diagram should show the full spec-first loop rather than separate research and calibration flows.

## Risks

- Sequential review may hide independent disagreements because later reviewers see prior decisions. That is acceptable for this workflow because the goal is prompt/spec improvement, not blind comparison.
- Review comments can become vague unless the workflow requires concrete OpenSpec deltas for accepted improvements.

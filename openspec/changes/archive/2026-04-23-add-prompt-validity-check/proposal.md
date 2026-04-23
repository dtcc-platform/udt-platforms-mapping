## Why

The repository currently has no dedicated way to audit whether live prompt files are still consistent with the specs and reference files that govern them. Prompt drift is therefore discovered reactively, after a prompt or spec inconsistency is noticed by hand.

## What Changes

- Add a CLI-only audit prompt at `tools/prompt-validity/prompt.md` that checks live prompt files against their governing specs, declared required inputs, and selected shared contracts.
- Add a report file at `tools/prompt-validity/report.md` that records the audit results for each prompt with explicit status and findings.
- Define freshness rules that distinguish contract changes from per-run data changes so the audit does not incorrectly mark prompts stale when runtime input files change as expected.
- Make the audit capable of flagging three classes of result: valid, review-needed, and invalid.

## Capabilities

### New Capabilities
- `prompt-validity-audit-prompt`: CLI prompt that audits live prompt files for consistency and freshness against governing specs and related files
- `prompt-validity-audit-report`: Markdown report contract for the prompt-validity audit results

### Modified Capabilities
- None

## Impact

- Adds a new maintenance prompt and generated report under `tools/prompt-validity/`
- Introduces a formal audit workflow for prompt freshness and prompt/spec consistency
- Does not change the output contract of the existing discovery, rating, or reflect prompts

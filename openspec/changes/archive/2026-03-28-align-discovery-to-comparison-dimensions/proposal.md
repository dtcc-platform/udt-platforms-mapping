## Why

The discovery prompt captures nine bullet fields per platform, but only four of them map to the six comparison dimensions — Technical Architecture and Governance are completely absent, and the overlapping fields use different names and no scoring. This creates a disconnect: discovery responses cannot seed comparison sessions meaningfully, and researchers must re-derive information already collected. Aligning discovery to the comparison dimension vocabulary closes this gap and makes the two prompts a coherent research pipeline.

## What Changes

- Replace the nine-bullet per-platform field list in the discovery prompt with six fields mapped to the six comparison dimensions, each with a light 1–5 score using the same scale as comparison
- Add agent-agnostic output constraints to the discovery prompt matching the comparison prompt: score notation (`X/5` inline, bare number in table), heading level (`##` per platform), permitted/prohibited Markdown syntax, and a concrete example
- Update the summary table columns to include the six dimension scores so marked rows carry score context when pasted into the comparison prompt
- Update the discovery prompt spec to reflect the new field set, scoring requirement, and format constraints

## Capabilities

### New Capabilities

### Modified Capabilities
- `platform-discovery-prompt`: per-platform field set, scoring, summary table schema, and output format constraints all change

## Impact

- `prompts/platform-discovery.md` — per-platform section and summary table rewritten
- `openspec/specs/platform-discovery-prompt/spec.md` — structured output and format requirements updated

## Why

The "What Is a UDT Platform?" section in `docs/01-scope.md` currently lists explicit exclusions (generic IoT, general-purpose GIS), which causes the discovery AI to pre-filter candidates before scoring — dropping borderline platforms that the relevance rubric should evaluate and assign score 1–2. The definition should frame the search space, not act as a second exclusion gate.

## What Changes

- Rewrite the "What Is a UDT Platform?" definition to describe the search boundary (what to scan for) rather than what to exclude.
- Remove explicit exclusion language ("are out of scope") from the definition; leave all exclusion decisions to the relevance rubric (score 1 = out of scope).
- Clarify that the definition's purpose is to anchor discovery search queries, not to pre-filter candidates.

## Capabilities

### New Capabilities

_(none — this is a content edit, not a new capability)_

### Modified Capabilities

- `platform-discovery-scope`: The requirement for what the definition section must communicate changes — from "exclusion list" to "search boundary framing". The spec must reflect that the definition is permissive and discovery-oriented, with exclusion delegated entirely to the relevance rubric.

## Impact

- `docs/01-scope.md` — prose edit to the "What Is a UDT Platform?" section
- `openspec/specs/platform-discovery-scope/spec.md` — updated requirement for the definition's purpose
- No changes to prompts, rubrics, CSV, or other specs

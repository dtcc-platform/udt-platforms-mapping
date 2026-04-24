## Context

The repository separates discovery from rating. Discovery maps the ecosystem and assigns `Layer`; rating is intended to compare full UDT platforms. The current rating workflow still carries `Layer` into the rating selection and scoring/export artifacts, which weakens that distinction and invites non-core entries into a comparison phase that is supposed to stay platform-level.

## Goals / Non-Goals

**Goals:**
- Make rating explicitly core-platform-only
- Remove redundant `Layer` from the rating selection and scoring/export schemas
- Keep DTCC as a required reference platform in the comparison scope
- Clarify why aliases do not belong in the rating selection file

**Non-Goals:**
- Redesign the discovery workflow
- Change the twelve-dimension scoring rubrics
- Rebuild historical rating outputs from older broader-scope response files

## Decisions

### 1. Inclusion in `plan/rating/platforms.md` implies `core-platform`

The rating selection file will become a two-column canonical scope table: `Name`, `Link`.

Why:
- The file already represents a filtered handoff from discovery into rating
- If rating is only meaningful for full platforms, repeating `Layer=core-platform` on every row adds no information

Alternative considered:
- Keep `Layer` as a defensive validation field
Why not chosen:
- It preserves redundant state and weakens the semantic clarity of the phase boundary

### 2. Remove `Layer` from the rating Part 1 table

The live rating prompt and its contract will no longer include `Layer` in Part 1.

Why:
- Part 1 should focus on rating dimensions, not redisplay a discovery-owned classification
- The selection file already encodes the scope boundary

### 3. Keep rating reporting aligned with the act prompt

The rating reporting prompt will extract and export the same Part 1 schema produced by `act/rating/prompt.md`, without `Layer`.

Why:
- Downstream prompt expectations must match the upstream table shape
- This avoids a stale extractor contract

### 4. Clarify aliases as a discovery-benchmarking concern only

The rating selection file header will explicitly say aliases do not belong there.

Why:
- Rating compares exact selected rows
- Alias handling is only useful in discovery benchmarking where name matching across noisy responses is part of the task

## Risks / Trade-offs

- [Removing `Layer` removes a visible guard against non-core entries] → Mitigation: make the file contract explicit that only core-platform rows belong in rating
- [Existing generated rating exports still reflect older broader-scope runs] → Mitigation: treat them as stale until the rating reporting prompt is rerun on compliant rating responses
- [Researchers may still paste non-core platforms into the file] → Mitigation: the file header and prompt contract now make that misuse explicit rather than implicit

## Context

The eval prompt matches fixture platform names against discovery response summary tables using case-insensitive substring search. Models sometimes use variant names (e.g., "CityEnergyAnalyst" vs "City Energy Analyst", "CesiumJS" vs "Cesium / CesiumJS") that fail this match, producing false negatives. Currently there is no way for a researcher to record a known variant name without editing the eval prompt itself.

## Goals / Non-Goals

**Goals:**
- Give researchers a way to record known name variants directly in the fixture
- Make the eval consume those variants so false negatives from name variation are eliminated
- Keep the fixture as the single source of truth for all matching rules

**Non-Goals:**
- Fuzzy or similarity-based matching (aliases are explicit strings, not heuristics)
- Retroactive correction of past coverage reports
- Changing the coverage report output format

## Decisions

### Aliases column in the fixture table

Add an `Aliases` column as the last column in each gap-category table. The cell is a comma-separated list of variant names (e.g., `CityEnergyAnalyst, CEA`). Empty cells mean no aliases — the canonical `Name` is the only match target.

**Why a column, not a separate file:** Keeps variant names co-located with the platform entry. A researcher editing a fixture row sees the aliases immediately without cross-referencing another file.

**Why comma-separated, not a sub-table:** Alias lists are short (0–3 entries per platform in practice). Comma-separated values in a Markdown table cell are readable and require no parser changes beyond splitting on `,`.

### Matching logic in the eval prompt

Step 3 is extended: for each fixture platform, build a match set = `{Name} ∪ {each alias}`. A platform is "found" if any member of the match set appears as a case-insensitive substring in the response's `Name` column value.

**Why union, not replacement:** The canonical name should still match; aliases are additive.

## Risks / Trade-offs

- **Alias pollution** — overly broad aliases (e.g., "City") could cause false positives. Mitigation: aliases should be specific enough to identify the platform unambiguously; the eval is recall-only so a false positive here means an unexpected "found" for a platform that wasn't really found — researchers will notice.
- **Spec drift** — the `discovery-eval-prompt` and `discovery-fixtures-file` specs describe the old behaviour. Both need delta specs to stay accurate.

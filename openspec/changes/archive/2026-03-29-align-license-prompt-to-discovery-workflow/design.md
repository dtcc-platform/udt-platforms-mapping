## Context

The discovery prompt produces a summary table with columns: Name, Link, License, Type, Arch, Open, City, Mature, Integ, Gov, Inclusion Criterion. The comparison prompt already uses a `[PASTE_SELECTED_PLATFORMS_HERE]` token fed by rows from this table. The license analysis prompt sits outside this pattern — it uses two freeform tokens (`[PLATFORM_NAME]`, `[LICENSE_URL_OR_TEXT]`) that the researcher must fill in manually, even though the discovery table already contains the platform name, link, and a seed license value.

## Goals / Non-Goals

**Goals:**
- Replace the two freeform tokens with a single `[PASTE_SELECTED_PLATFORM_HERE]` token consistent with the comparison prompt pattern
- Allow the model to derive platform name and starting license signal from the pasted row
- Keep license analysis a per-platform operation (singular token, one row)
- Add license analysis as an optional step in the methodology workflow

**Non-Goals:**
- Changing the structure or content of the license analysis output sections
- Allowing multi-row input (license analysis is inherently per-platform)
- Removing the checklist or taxonomy from the prompt

## Decisions

**Singular token name: `[PASTE_SELECTED_PLATFORM_HERE]`** (not `[PASTE_SELECTED_PLATFORMS_HERE]`)
The comparison prompt uses plural because it accepts multiple rows. License analysis is a per-platform deep-dive; accepting multiple rows would blur the output. Singular token name signals this clearly.

**Model locates the license from the Link field, not from a provided URL**
The discovery table has the Link (platform homepage or repo) but not a direct license URL. The existing checklist already instructs the model to locate the license from the repo root or official site — so removing `[LICENSE_URL_OR_TEXT]` doesn't reduce capability, it just removes a manual step that the model handles itself. The seed `License` value from the discovery row serves as a first-pass signal the model can verify or correct.

**Methodology addition is optional, not sequential**
License analysis can be run independently (not only after discovery) and is not required before comparison. It is added to methodology as an optional parallel path, not inserted into the main sequence.

## Risks / Trade-offs

- **Loss of explicit license URL input** → Researchers who have a direct license URL can no longer pass it via the token. Mitigation: they can include it as a note in the pasted row or as a parenthetical after the token — but this is an edge case; the model's checklist already handles license location robustly.
- **Stale license field in discovery table** → The `License` column in the discovery table is a seed value from a quick first pass. It may be incomplete (e.g., "Proprietary" without further detail). The license analysis prompt's checklist instructs the model to verify from primary sources, so the seed is a hint, not a constraint.

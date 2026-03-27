## Context

`responses/` and `search_logs/` are both empty. The README mentions `search_logs/YYYY-MM-DD-<platform>.md` in passing but never defines it formally. `responses/` has no naming guidance at all. Without a convention, filenames will be ad hoc, making retrieval by platform or prompt type unreliable as the corpus grows.

## Goals / Non-Goals

**Goals:**
- Define canonical filename patterns for both `responses/` and `search_logs/`
- Document the convention in `docs/methodology.md` as the authoritative reference
- Surface the convention in the prompt usage headers so researchers see it at the point of use

**Non-Goals:**
- Encoding the session date in the filename — git history is the authoritative source for when a file was created or changed
- Enforcing naming via tooling or linting (out of scope for this change)
- Renaming any existing files (both directories are currently empty)
- Defining a convention for `sources/` or `notes/` (separate concern)

## Decisions

### Decision: `responses/` pattern — `<platform>-<prompt-type>.md`

Fields:
- `<platform>` — kebab-case platform name (e.g., `cesium`, `dtcc`, `3d-city-db`)
- `<prompt-type>` — one of `discovery`, `comparison`, `license`

Example: `cesium-license.md`

**Rationale:** Git already records when a file was created and how it changed over time — a date prefix would be redundant. The filename should identify *what* the file is, not *when* it was created. If a researcher re-runs the same prompt for the same platform, the new response overwrites the old one and git preserves the history.

**For comparison sessions** (two platforms): join names with `vs`, e.g., `cesium-vs-dtcc-comparison.md`. For more than two, use the first platform plus `et-al`: `cesium-et-al-comparison.md`.

**For broad discovery sessions** not tied to a single platform: use a kebab-case scope descriptor in place of a platform name, e.g., `european-platforms-discovery.md`.

### Decision: `search_logs/` pattern — `<platform>.md`

One log file per platform, overwritten as the research evolves. Git tracks the history. No prompt-type suffix because a session log covers one platform's full research session.

### Decision: Allowed characters — lowercase, digits, hyphens only

No spaces, no underscores, no uppercase. Consistent with kebab-case used throughout the project.

### Decision: Document in `docs/methodology.md`, reference from prompt headers

`docs/methodology.md` is the established home for research process rules. A brief note in each prompt's usage header points researchers there and shows a concrete filename example.

## Risks / Trade-offs

- **Overwrite risk** → Without dates, re-running a prompt overwrites the previous file. Mitigation: this is intentional — git preserves the history. Researchers who want to keep parallel runs can use a disambiguating suffix (e.g., `cesium-license-v2.md`), but this should be the exception.
- **Convention drift** → Researchers may not follow the convention. Mitigation: showing the expected filename in the prompt header at the moment of use is the strongest available nudge without tooling.

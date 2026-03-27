### Requirement: Response files follow a defined naming pattern
Files saved to `responses/` SHALL use the pattern `<platform>-<prompt-type>.md`, where:
- `<platform>` is the kebab-case platform name (e.g., `cesium`, `3d-city-db`)
- `<prompt-type>` is one of: `discovery`, `comparison`, `license`

For comparison sessions involving two platforms, both names SHALL be joined with `vs` (e.g., `cesium-vs-dtcc-comparison.md`). For more than two platforms, the first name plus `et-al` SHALL be used (e.g., `cesium-et-al-comparison.md`). For broad discovery sessions not tied to a single platform, a kebab-case scope descriptor MAY be used in place of a platform name (e.g., `european-platforms-discovery.md`).

All filename components SHALL use only lowercase letters, digits, and hyphens. No spaces, underscores, or uppercase letters are permitted.

If a session is re-run for the same platform and prompt type, the file SHALL be overwritten. Git history preserves previous versions.

#### Scenario: Researcher saves a license analysis response for Cesium
- **WHEN** a researcher completes a license analysis session for Cesium
- **THEN** the file is saved as `responses/cesium-license.md`

#### Scenario: Researcher saves a comparison response for two platforms
- **WHEN** a researcher completes a comparison session for Cesium and DTCC
- **THEN** the file is saved as `responses/cesium-vs-dtcc-comparison.md`

#### Scenario: Researcher saves a broad discovery response
- **WHEN** a researcher completes a discovery session scoped to "European city-scale platforms"
- **THEN** the file is saved using a scope descriptor such as `responses/european-platforms-discovery.md`

#### Scenario: Researcher re-runs a prompt for the same platform
- **WHEN** a researcher runs the license prompt for Cesium a second time
- **THEN** `responses/cesium-license.md` is overwritten and git history preserves the previous version

### Requirement: Session log files follow a defined naming pattern
Files saved to `search_logs/` SHALL use the pattern `<platform>.md`, where `<platform>` is the kebab-case platform name. All filename components SHALL use only lowercase letters, digits, and hyphens.

#### Scenario: Researcher saves a session log for Cesium
- **WHEN** a researcher completes a research session for Cesium
- **THEN** the session log is saved as `search_logs/cesium.md`

### Requirement: Naming convention is documented in methodology
The file naming convention for both `responses/` and `search_logs/` SHALL be documented in `docs/methodology.md` under a **File Naming** section, serving as the authoritative reference.

#### Scenario: Researcher looks up the naming convention
- **WHEN** a researcher needs to know how to name an output file
- **THEN** `docs/methodology.md` contains the pattern, field definitions, and examples for both directories

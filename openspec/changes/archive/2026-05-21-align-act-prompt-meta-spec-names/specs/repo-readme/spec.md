## MODIFIED Requirements

### Requirement: Act README explains prompt manifests

`act/README.md` SHALL explain that `act/` contains contract manifests used to resolve or run governed research, benchmarking, and reporting workflows.

It SHALL explain the live manifest filenames, including `discover-entities.md`, `compare-platforms.md`, `benchmark-platform-discovery.md`, `report-platform-discovery.md`, `benchmark-platform-comparison.md`, and `report-platform-comparison.md`.

It SHALL explain that manifest behavior is governed by OpenSpec prompt specs and `act-prompt-manifest`.

It SHALL explain that manifest and prompt behavior changes should go through OpenSpec.

#### Scenario: Researcher opens act/

- **WHEN** a researcher reads `act/README.md`
- **THEN** they understand which files are action manifests
- **THEN** they understand that prompt contracts and manifest structure are governed by OpenSpec

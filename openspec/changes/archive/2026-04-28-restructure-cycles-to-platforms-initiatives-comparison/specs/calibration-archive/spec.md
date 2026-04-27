## MODIFIED Requirements

### Requirement: Calibration archive uses research, cycle, and agent path segments

Calibration artifacts SHALL use the path pattern `calibration/<research>/<cycle>/<agent>/`.

`<research>` SHALL identify one of the canonical research cycles:

- `udt-platforms`
- `udt-initiatives`
- `udt-platform-comparison`

`<cycle>` SHALL identify the accepted iteration baseline, such as `c1` or `c2`.

`<agent>` SHALL identify the agent or branch responsible for the calibration run.

#### Scenario: Technical-artifact calibration run is archived

- **WHEN** a researcher saves a `udt-platforms` calibration run for agent `agent-a` from cycle `c1`
- **THEN** the artifacts live under `calibration/udt-platforms/c1/agent-a/`

#### Scenario: Initiative calibration run is archived

- **WHEN** a researcher saves a `udt-initiatives` calibration run for agent `agent-b` from cycle `c1`
- **THEN** the artifacts live under `calibration/udt-initiatives/c1/agent-b/`

#### Scenario: Platform-comparison calibration run is archived

- **WHEN** a researcher saves a `udt-platform-comparison` calibration run for agent `agent-c` from cycle `c2`
- **THEN** the artifacts live under `calibration/udt-platform-comparison/c2/agent-c/`

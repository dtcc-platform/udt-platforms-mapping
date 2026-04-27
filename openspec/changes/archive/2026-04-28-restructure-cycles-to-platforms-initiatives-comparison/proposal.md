## Why

The repository's current cycle names, `discovery` and `rating`, are too generic for the workflow it is trying to stabilize.

Recent exploration around `UDT_SLR_Chalmers_ComputersInIndustry.pdf` clarified a better model:

- one cycle should map technical UDT artifacts
- one cycle should map UDT initiatives and projects
- one cycle should compare selected platforms side by side

The current `discovery` cycle also conflates two different things:

- software or technical artifacts such as platforms, frameworks, and modules
- real-world initiatives or projects

That makes the handoff into the comparison cycle less explicit than it should be.

The workflow should instead make three things clear:

- what technical artifacts exist
- what initiatives or projects exist
- which technical artifacts are eligible for platform comparison

## What Changes

- Replace the generic `discovery` cycle with `udt-platforms`.
- Replace the generic `rating` cycle with `udt-platform-comparison`.
- Add a separate `udt-initiatives` cycle.
- Define the `udt-platforms` output contract around a technical-artifact table:
  - `Name`
  - `Link`
  - `Type`
  - `Reason`
- Define the `udt-initiatives` output contract around an initiative table:
  - `Initiative`
  - `Link`
  - `Uses`
  - `Reason`
- Define the comparison handoff rule explicitly:
  - only `Type = platform` entries from `udt-platforms` are eligible for `udt-platform-comparison`
- Update the folder-layout contract and calibration-path examples to use the new cycle names.
- Update README and prompt/spec contracts so the repository explains and enforces the new cycle model consistently.

## Capabilities

### New Capabilities

- `udt-platforms-cycle`: Governs the technical-artifact mapping cycle and its output contract.
- `udt-initiatives-cycle`: Governs the initiative/project mapping cycle and its output contract.
- `udt-platform-comparison-cycle`: Governs the platform-only comparison cycle and its handoff rules.

### Modified Capabilities

- `ar-folder-layout`: Replaces `discovery` and `rating` with `udt-platforms`, `udt-initiatives`, and `udt-platform-comparison`.
- `calibration-archive`: Keeps the same archival structure but uses the new research-cycle names in its path examples.

### Retired / Superseded Capabilities

- `plan-discovery-scope`
- `act-discovery-prompt`
- `act-rating-prompt`
- `plan-rating-platforms`

These older capability names are tied to the outgoing cycle model and will be replaced by the new cycle-specific contracts in this change.

## Impact

- Affects top-level cycle naming across `plan/`, `act/`, `observe/`, `reflect/`, and `calibration/`.
- Introduces a separate initiative/project cycle instead of overloading technical-artifact mapping.
- Changes the first-cycle output contract from Layer-based discovery toward a technical-artifact classification centered on `platform`, `framework`, `module`, and `excluded`.
- Makes the comparison-cycle input rule explicit and platform-only.
- Requires README and spec realignment before implementation can be considered complete.

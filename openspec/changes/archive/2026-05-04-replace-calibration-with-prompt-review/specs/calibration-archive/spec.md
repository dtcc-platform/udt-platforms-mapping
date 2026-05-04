## REMOVED Requirements

### Requirement: Calibration archive exists as a top-level archival area

**Reason**: The repository no longer uses `calibration/` as a live archival area for generated prompt artifacts.

**Migration**: Use `prompt-interpretation-review` and OpenSpec change artifacts for prompt/spec review evidence.

### Requirement: Calibration archive uses spec-name, cycle, and agent path segments

**Reason**: The `calibration/<spec-name>/<cycle>/<agent>/` path contract is retired with the calibration folder.

**Migration**: Use descriptive OpenSpec change names and archived change history.

### Requirement: Calibration archive stores generated prompts before branching

**Reason**: Sequential prompt review no longer stores generated prompts in a shared calibration tree before branch creation.

**Migration**: Capture generated prompt changes and review outcomes in the relevant OpenSpec change.

### Requirement: Calibration proposal context is isolated before merge

**Reason**: The replacement workflow is sequential and intentionally lets later reviewers see earlier accepted deltas.

**Migration**: Ask each reviewer to assess the current prompt against the current governing spec/change state.

### Requirement: Calibration branch review happens after isolated proposal generation

**Reason**: The replacement workflow does not require a dedicated calibration branch or merged independent proposals.

**Migration**: Use normal OpenSpec proposal, implementation, archive, and git review flow.

### Requirement: Calibration archive is archival rather than canonical

**Reason**: No live calibration archive remains.

**Migration**: Treat archived OpenSpec changes as the audit trail for prompt-review decisions.

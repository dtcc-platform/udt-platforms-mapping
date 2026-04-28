## REMOVED Requirements

### Requirement: UDT initiatives source policy file exists
**Reason**: `udt-initiatives` is being reframed as a broad global discovery thread rather than a governed source-policy filtering stage.
**Migration**: Remove `plan/udt-initiatives/source-policy.md` from the live workflow and keep only lightweight evidence guidance in documentation if needed.

### Requirement: UDT initiatives source policy defines ranked evidence for initiative mapping
**Reason**: Broad initiative discovery should optimize for recall and tolerate uneven documentation without requiring a separate governed ranking file.
**Migration**: Keep initiative-scoping semantics in the thread contract and defer stricter evidence discipline to later stages when needed.

### Requirement: UDT initiatives source policy allows unknown technical substrate without inventing one
**Reason**: This behavior belongs to the broad-discovery thread contract itself rather than a separate governed policy file.
**Migration**: Preserve `Uses = ?` behavior in the cycle contract after removing the source-policy capability.

### Requirement: UDT initiatives source policy defines contradiction handling
**Reason**: Strict contradiction handling no longer needs its own governed capability for this broad discovery thread.
**Migration**: Let later reflection or downstream comparison workflows resolve higher-confidence judgments when necessary.

## REMOVED Requirements

### Requirement: UDT platforms source policy file exists
**Reason**: `udt-platforms` is being reframed as a broad global discovery thread rather than a governed source-policy filtering stage.
**Migration**: Remove `plan/udt-platforms/source-policy.md` from the live workflow and keep only lightweight evidence guidance inside the prompt or README as needed.

### Requirement: UDT platforms source policy defines ranked evidence for technical-artifact mapping
**Reason**: Broad discovery for `udt-platforms` should optimize for recall rather than require a separate governed ranking file.
**Migration**: Preserve any minimal evidence caution in `act/udt-platforms/prompt.md` instead of a dedicated plan input.

### Requirement: UDT platforms source policy rejects unreliable evidence classes
**Reason**: This guidance no longer needs to live as a separate governed capability for the discovery thread.
**Migration**: Fold only the minimal practical caution that remains necessary into prompt wording or documentation.

### Requirement: UDT platforms source policy defines contradiction handling
**Reason**: Strict contradiction handling is being moved out of a dedicated governed discovery policy and left to later reflection or comparison stages.
**Migration**: Use thread-level discovery wording and later reflection to tighten interpretation when needed.

## REMOVED Requirements

### Requirement: Workflow presentation area exists
**Reason**: The repository no longer treats workflow presentation as an active governed subsystem. The README is the primary explanation artifact.
**Migration**: Use `README.md` as the maintained workflow explanation unless a future change reintroduces a presentation capability.

### Requirement: Workflow presentation prompt exists as a CLI generator prompt
**Reason**: The dedicated generator prompt is no longer part of the intended active repository model.
**Migration**: No direct replacement in this change. Keep workflow explanation in `README.md`.

### Requirement: Workflow presentation deck is Pandoc-ready Markdown
**Reason**: The deck is no longer part of the active model.
**Migration**: No direct replacement in this change.

### Requirement: Workflow presentation teaches the repository workflow as a tutorial
**Reason**: The tutorial responsibility moves back to README and canonical documentation.
**Migration**: Keep the workflow explanation in `README.md`.

### Requirement: Workflow presentation stays aligned with live repository behavior
**Reason**: Removing the capability removes the need for a governed presentation refresh workflow.
**Migration**: Keep the live workflow explanation in `README.md` and current baseline specs.

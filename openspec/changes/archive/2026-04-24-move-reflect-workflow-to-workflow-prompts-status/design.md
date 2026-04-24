## Context

The repository currently stores prompt-validity audit artifacts under `reflect-workflow/prompt-validity/`. That path was introduced to separate workflow-level reflection from discovery and rating reflection, but the agreed direction is broader: introduce a top-level `workflow/` root and begin with a concrete `workflow/prompts-status/` area.

This change is mostly a governed path migration. The capability stays the same: a CLI audit prompt checks live prompts under `act/` and `reflect/` and writes a status report. The main work is to move the live artifacts and update the repository contracts that name their location.

## Goals / Non-Goals

**Goals:**
- Replace `reflect-workflow/prompt-validity/` with `workflow/prompts-status/` as the live path.
- Update governed prompt and report specs so the new path is authoritative.
- Update the folder-layout contract so a top-level `workflow/` root is explicitly allowed.
- Keep the workflow-audit capability unchanged apart from its location and naming.

**Non-Goals:**
- Introduce `workflow/docs/` or `workflow/presentation/`.
- Change the audit logic, statuses, or report structure.
- Expand the audit scope beyond the current live prompts.

## Decisions

### Decision: Introduce `workflow/` through one concrete subfolder first

The change will prepare the broader `workflow/` root by adding only `workflow/prompts-status/` now.

Why:
- It matches the current user decision to start with prompt status only.
- It avoids speculative structure for docs or presentation before those artifacts exist.

Alternative considered:
- Rename directly from `reflect-workflow/` to another standalone root such as `prompts-status/`.
- Rejected because it would not prepare the broader `workflow/` umbrella that the user wants.

### Decision: Treat this as a path-contract migration, not a capability redesign

The prompt-validity audit behavior stays stable. Only the governed location changes.

Why:
- The existing audit capability is already implemented and in use.
- Keeping behavior stable reduces migration risk and makes the change easy to review.

Alternative considered:
- Use the rename to also redesign the audit logic or report contents.
- Rejected because it would mix naming/structure work with behavior changes.

### Decision: Update the folder-layout spec alongside the prompt-validity specs

The folder-layout contract must explicitly allow the additional top-level `workflow/` root and must name `workflow/prompts-status/` as the owner of the prompt-status artifacts.

Why:
- Otherwise the repo would contain a live folder structure not described by the baseline layout spec.
- The change is structural, not only local to the prompt-validity capability.

Alternative considered:
- Change only the prompt-validity specs and leave folder-layout for later.
- Rejected because it would leave an immediate baseline inconsistency.

## Risks / Trade-offs

- [Older docs or prompts may still mention `reflect-workflow/`] → Search and update live references during implementation; leave historical archive references unchanged.
- [The broader `workflow/` root may remain underused for a time] → Keep the current change narrow and allow later additions only when new workflow artifacts are ready.
- [Users may confuse `workflow/prompts-status/` with ordinary research-cycle reflection] → Use explicit naming in specs and README updates when those are introduced later.

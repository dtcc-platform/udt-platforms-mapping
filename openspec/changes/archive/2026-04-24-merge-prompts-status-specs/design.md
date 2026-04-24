## Context

The live prompt-status workflow is small and tightly coupled: one CLI prompt audits live repository prompts and writes one Markdown report. The current baseline splits that into two capabilities, one for the prompt and one for the report, even though the report is just the required output of the prompt workflow.

The change is a spec simplification, not a behavior change. The live paths, audit logic, statuses, and report format remain the same. The main work is to collapse the contracts into one capability and remove the extra baseline spec.

## Goals / Non-Goals

**Goals:**
- Replace the two prompt-status baseline specs with one `workflow-prompts-status` spec.
- Preserve the current live behavior and output contract while reducing spec overhead.
- Make it clearer that the report is part of the audit workflow, not a separate capability.

**Non-Goals:**
- Change the live `workflow/prompts-status/` paths.
- Redesign the audit logic or report shape.
- Broaden prompt-status into a larger workflow system.

## Decisions

### Decision: Treat the report as part of the workflow contract

The single capability will govern both the audit behavior and the report structure.

Why:
- The report has no independent execution path.
- The user wants one simpler capability rather than two closely coupled ones.

Alternative considered:
- Keep separate prompt and report specs for maximal behavioral/output separation.
- Rejected because this capability is too small for that separation to pay for itself.

### Decision: Replace rather than alias the old capabilities

The old prompt-validity capability names will be removed from baseline specs instead of kept as wrappers.

Why:
- The goal is to reduce spec count, not introduce another layer of naming.
- No current live prompt references depend on those baseline spec names.

Alternative considered:
- Keep the old specs as thin forwarding or deprecated compatibility stubs.
- Rejected because that would preserve the cognitive overhead the change is meant to remove.

## Risks / Trade-offs

- [Historical OpenSpec archives still use the old capability names] → Leave archives unchanged; only baseline capabilities are simplified.
- [A future expansion of prompt-status might want separate output specs again] → Re-split later only if behavior and output begin to evolve independently.
- [Reviewers may expect one capability per generated artifact] → Make the merged spec explicit that the report is a required output of the workflow, not a standalone capability.

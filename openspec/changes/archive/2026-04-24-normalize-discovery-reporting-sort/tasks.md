## 1. Update the discovery reporting contract

- [x] 1.1 Update `reflect/discovery/reporting/prompt.md` to describe aggregation-first sorting
- [x] 1.2 Update the normalized URL ordering instructions to use host/domain grouping with leading-`www.` normalization
- [x] 1.3 Add deterministic tie-breaker wording after normalized host grouping

## 2. Validate the revised ordering rule

- [x] 2.1 Regenerate `reflect/discovery/reporting/ecosystem.md` using the revised sort rule
- [x] 2.2 Confirm related host variants such as DTCC rows group together in the final output
- [x] 2.3 Re-run any relevant prompt-validity or consistency checks after implementation

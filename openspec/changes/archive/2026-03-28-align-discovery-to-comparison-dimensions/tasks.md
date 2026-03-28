## 1. Update the discovery prompt

- [x] 1.1 Replace the nine-bullet per-platform section in `prompts/platform-discovery.md` with the two-block structure: identification (Organization, Link, License, Type, Inclusion criterion) + six scored dimension fields (Technical Architecture, Openness & Licensing, City-Scale Capability, Maturity & Adoption, Integration Posture, Governance), each with `**Dimension (X/5):**` notation and a one-sentence rationale
- [x] 1.2 Update the summary table to use the new columns: Name, Link, License, Type, Arch, Open, City, Mature, Integ, Gov, Inclusion Criterion, Select
- [x] 1.3 Add an agent-agnostic output constraints section matching the comparison prompt: permitted syntax, prohibited syntax, whitespace rules, `##` heading level for platforms, score notation rules, and a concrete example section for one fictional platform

## 2. Update the live spec

- [x] 2.1 Apply the delta spec to `openspec/specs/platform-discovery-prompt/spec.md` — replace the structured output and summary table requirements with the new two-block field set, aligned summary table columns, and format constraint requirement

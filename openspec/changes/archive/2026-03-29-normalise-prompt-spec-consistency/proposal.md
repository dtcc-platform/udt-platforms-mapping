## Why

Exploration across all three prompts, their specs, and methodology surfaced six concrete inconsistencies: stale language, duplicate spec requirements, missing requirements, and divergent naming for equivalent sections. Fixing them together makes the system coherent enough to reason about as a whole.

## What Changes

- **Fix stale language** in the comparison prompt body: "rows marked for selection from the discovery summary table" still references the selection-marking concept that was removed
- **Remove duplicate portable-Markdown requirements** from the discovery and comparison specs — each carries both an "agent-agnostic output structure" requirement and a "portable Markdown syntax" requirement that overlap heavily; the portable-Markdown requirement is merged into the agent-agnostic one and removed as a separate entry
- **Merge duplicate usage-header requirements** in the license spec — "follows the discovery-to-prompt pattern" and "includes save-as filename instruction" overlap; consolidate into one
- **Add uncertainty handling requirements** to discovery and license specs — this behaviour exists in the prompts but is only formally required in the comparison spec
- **Add primary sources requirements** to discovery and license specs — same gap
- **Rename the "what to do" section** in all three prompts to `### Research Instructions` — currently "Research Instructions" (discovery), "Rules" (comparison), "Review Checklist" (license); same concept, three names; discovery's name becomes the canonical form

## Capabilities

### New Capabilities

_None._

### Modified Capabilities

- `platform-discovery-prompt`: remove duplicate portable-Markdown requirement; add uncertainty handling requirement; add primary sources requirement; spec already uses "Research Instructions" — no rename needed
- `platform-comparison-prompt`: fix stale "marked for selection" language (prompt body); remove duplicate portable-Markdown requirement; rename `### Rules` to `### Research Instructions` in prompt
- `license-analysis-prompt`: merge duplicate usage-header requirements; add uncertainty handling requirement; add primary sources requirement; rename `### Review Checklist` to `### Research Instructions` in prompt

## Impact

- `prompts/platform-comparison.md` — stale language fix; section rename
- `prompts/license-analysis.md` — section rename
- `openspec/specs/platform-discovery-prompt/spec.md` — remove portable-Markdown requirement; add uncertainty handling and primary sources requirements
- `openspec/specs/platform-comparison-prompt/spec.md` — remove portable-Markdown requirement
- `openspec/specs/license-analysis-prompt/spec.md` — merge usage-header requirements; add uncertainty handling and primary sources requirements

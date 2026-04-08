## Why

The three prompt specs each repeat the same core Markdown portability rules: allowed syntax, inline-link citation style, prohibited syntax, and whitespace rules. That duplication makes the spec set harder to maintain and increases drift risk when the shared rules need to change.

The repository already treats other cross-cutting prompt conventions, such as placeholder guards and cut-lines, as their own platform-level contracts. The common Markdown portability rules should be governed the same way, while prompt-specific heading and score rules remain local to each prompt capability.

## What Changes

- Add a new shared spec capability, `prompt-markdown-format`, that defines the common portable Markdown contract used by prompt templates
- Modify the discovery, comparison, and license prompt specs so they reference the shared contract instead of restating the common Markdown rule set inline
- Keep prompt-specific formatting requirements local to each prompt spec, including heading levels, score notation, and any prompt-specific citation notes

## Capabilities

### New Capabilities

- `prompt-markdown-format`: A shared portable Markdown contract for AI prompt templates, covering permitted syntax, inline-link citations, prohibited syntax, and whitespace rules

### Modified Capabilities

- `platform-discovery-prompt`: References the shared Markdown contract and retains discovery-specific output-format rules
- `platform-comparison-prompt`: References the shared Markdown contract and retains comparison-specific output-format rules
- `license-analysis-prompt`: References the shared Markdown contract and retains license-specific score-format rules

## Impact

- `openspec/specs/prompt-markdown-format/spec.md` — new shared spec
- `openspec/specs/platform-discovery-prompt/spec.md` — Markdown requirement narrowed to discovery-specific deltas
- `openspec/specs/platform-comparison-prompt/spec.md` — Markdown requirement narrowed to comparison-specific deltas
- `openspec/specs/license-analysis-prompt/spec.md` — Markdown requirement narrowed to license-specific deltas
- `prompts/platform-discovery.md`, `prompts/platform-comparison.md`, `prompts/license-analysis.md` — wording may be normalised during implementation so the prompt files clearly match the refactored spec structure

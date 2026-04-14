## Why

The discovery prompt currently filters silently — only platforms with Relevance ≥ 3 appear in the output. Platforms considered and rejected are dropped without record, meaning future sessions waste time re-researching and re-rejecting the same candidates. The Relevance 0–5 rubric was designed to express gradations, not act as a gate.

## What Changes

- **`prompts/platform-discovery.md`**: Remove the "Relevance ≥ 3" filter. Include all discovered platforms in the summary table regardless of score. Produce brief per-platform sections for Relevance 1–2 (one-line reason sufficient) in addition to full sections for Relevance 3–5. Update the Research Instructions accordingly.

## Capabilities

### New Capabilities

_(none)_

### Modified Capabilities

- `platform-discovery-prompt`: Discovery output changes from filtered (Relevance ≥ 3 only) to comprehensive (all discovered platforms, Relevance 1–5, with brief sections for out-of-scope entries)

## Impact

- `prompts/platform-discovery.md` — output scope and section instructions updated
- `docs/05-platform-inventory.csv` — will receive Relevance 1–2 rows from future discovery sessions (existing rows unaffected)

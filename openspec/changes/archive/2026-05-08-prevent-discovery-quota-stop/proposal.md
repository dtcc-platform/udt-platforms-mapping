## Why

The new discovery quota improved result volume, but a recent run treated the quota as a stopping target and missed a high-relevance regional research platform, DTCC Platform. The coverage contract needs to state that quotas are minimum gates and require an extra recall pass for regional, academic, open-source, and research-center UDT platforms.

## What Changes

- Clarify that platform discovery quotas are minimum quality gates, not stopping conditions.
- Require at least one post-quota recall pass for regional, academic, open-source, and research-center UDT platforms.
- Require discovery to prefer replacing weaker candidates with stronger, better-evidenced candidates rather than merely satisfying quotas.
- Add DTCC Platform as an explicit recall scenario for ambiguous or regional platform names that require targeted terms such as `Digital Twin Cities Centre`, `Chalmers`, and `dtcc platform`.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `platform-discovery-coverage`: Strengthen coverage behavior so quotas do not become a stopping condition and add a post-quota targeted recall pass.
- `act-discover-platforms-prompt`: Require the canonical prompt to render the strengthened quota interpretation and regional/research-platform recall behavior.

## Impact

- Affects resolved `act/discover-platforms.md` prompts through existing required contracts.
- Updates baseline specs after apply/archive.
- No runtime code or dependency changes.

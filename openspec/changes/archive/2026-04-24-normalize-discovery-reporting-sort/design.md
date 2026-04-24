## Context

Discovery reporting already aggregates rows from all qualifying `observe/discovery/` responses into one Markdown table. The ambiguity is in the ordering rule: the current spec says to order by the URL portion of `Link`, but does not define whether that means the raw URL string or a normalized host-based sort key. In practice, raw string sorting splits closely related rows across `platform.`, `www.`, and bare-host variants.

## Goals / Non-Goals

**Goals:**
- Make the aggregation-first behavior explicit
- Define a deterministic normalized URL sort key that groups related host variants together
- Preserve stable tie-breaking after normalization

**Non-Goals:**
- Deduplicate rows across discovery responses
- Change which rows qualify for discovery reporting
- Redesign the discovery reporting output format

## Decisions

### 1. Sorting happens after aggregation

The prompt contract will explicitly state that all qualifying rows are gathered first, then sorted once across the complete combined row set.

Why:
- This matches the intended semantics of a consolidated report
- It prevents implementations from sorting per file and appending later

Alternative considered:
- Keep the current wording and rely on interpretation
Why not chosen:
- It is too easy to implement incorrectly and still appear compliant

### 2. Normalize the host for the primary sort key

The primary sort key will be derived from the URL target by:
- extracting the URL from the Markdown link
- lowercasing it
- using the host/domain as the main grouping key
- stripping a leading `www.` when present

Why:
- It groups obvious host variants together
- It fixes the DTCC-style case directly
- It remains simple enough to express in prompt form

Alternative considered:
- Sort by the full raw URL target
Why not chosen:
- It creates misleading separation for closely related domain variants

### 3. Keep deterministic tie-breakers after normalized host grouping

After normalized-host ordering, implementations should break ties using the full URL target, then `Name`, then `Layer`, then `Reason`.

Why:
- It preserves determinism
- It avoids unstable ordering within a host group

## Risks / Trade-offs

- [Different subdomains may still represent distinct products] → Mitigation: use normalized host only as the primary grouping key, then preserve the full URL as the next tie-breaker
- [Prompt implementations may normalize too aggressively] → Mitigation: keep normalization narrow to lowercasing and removing only a leading `www.`
- [Existing generated files will reorder] → Mitigation: treat this as the intended behavior change and regenerate discovery reporting outputs after implementation

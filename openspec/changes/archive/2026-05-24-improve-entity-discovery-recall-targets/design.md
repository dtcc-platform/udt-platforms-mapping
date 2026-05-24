## Context

Entity discovery now covers all allowed entity `Type` values from `plan-entity-definition`: `platform`, `framework`, `module`, `initiative`, and `excluded`. The existing broad recall requirement still uses artifact-oriented wording and sets quotas for platform, framework, module, and excluded candidates only.

The improved target should encourage broader coverage without making agents pad results with weak evidence.

## Goals / Non-Goals

**Goals:**

- Align recall wording with unified entity discovery.
- Add initiative coverage to the minimum recall targets.
- Raise the recall floor enough to reduce shallow outputs while retaining evidence quality.
- Preserve anti-padding and anti-early-stop behavior.

**Non-Goals:**

- Change the entity discovery output table shape.
- Add new allowed `Type` values.
- Require exactly 50 entities.
- Require weak candidates when evidence is unavailable.

## Decisions

- Use "candidate entities" instead of "candidate artifacts" because entity discovery includes technical artifacts, initiatives, and excluded boundary cases.
- Set the minimum at 50 candidate entities. This creates a stronger breadth expectation than 40 without making the quota so high that agents are likely to fabricate or over-include weak candidates.
- Keep explicit minimums for `platform`, `framework`, `module`, `initiative`, and `excluded`, and require the remaining candidates to be high-relevance entities of any allowed `Type`. This keeps the distribution flexible while guaranteeing initiative coverage.
- Preserve the existing rule that quotas are quality gates, not stopping conditions. Strong outputs should continue beyond the floor when more well-evidenced candidates are discoverable.

## Risks / Trade-offs

- A higher minimum may increase pressure to include weak candidates. Mitigation: keep the existing no-fabrication rule and require unmet targets to be explained when evidence is insufficient.
- A flexible remainder may produce uneven distribution. Mitigation: fixed minimums still preserve coverage for every allowed `Type`.

# Design: product-native source handle ban

## Approach

Update only the shared Markdown formatting contract.

The contract already governs portable Markdown output and is inlined by the active web prompt manifests. Strengthening this one spec keeps the behavior central and avoids repeating formatting rules in each prompt or observe contract.

## Contract Detail

The updated contract will:

- keep the general ban on AI-product-specific citation artifacts
- add explicit examples for current observed failure modes:
  - `cite...`
  - `url...`
  - `turn8search14`, `turn11view6`, and similar opaque result IDs
  - source handles that are not resolvable URLs
- require links to be emitted as `[label](https://...)` or another real URL scheme when a link is required

## Non-Goals

This change does not edit existing model outputs. Existing outputs may remain non-conforming until rerun or manually repaired.

This change does not tighten output shape for a specific observe contract.

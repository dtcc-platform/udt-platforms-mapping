## Why

The repository now uses phase folders as semantic boundaries, but output contracts are still split across plan files, act prompts, and underspecified specs. Observed model response shapes should be governed by `observe-*` specs so `act-*` prompts can implement those contracts without owning them.

## What Changes

- Add observe output specs for platform discovery, initiative discovery, and platform comparison web responses.
- Move initiative response table ownership out of `plan/initiative-definition.md`.
- Make discovery and comparison act prompt specs require prompts to produce outputs conforming to the matching observe specs.
- Make benchmark coverage remain an observe contract and expand it with the coverage report shape.
- Make reflection/export specs own synthesized output contracts for platform ecosystem and platform comparison CSV/HTML outputs.
- Keep act prompt specs focused on execution, required inputs, save paths, and conformance to observe/reflect contracts.

## Capabilities

### New Capabilities

- `observe-platform-discovery`: Governs saved platform discovery web response output shape.
- `observe-initiative-discovery`: Governs saved initiative discovery web response output shape.
- `observe-platform-comparison`: Governs saved platform comparison web response output shape.

### Modified Capabilities

- `plan-initiative-definition`: Remove exact response-table ownership from the planning definition.
- `act-discover-platforms-prompt`: Require conformance to `observe-platform-discovery`.
- `act-discover-initiatives-prompt`: Require conformance to `observe-initiative-discovery`.
- `act-compare-platforms-prompt`: Require conformance to `observe-platform-comparison`.
- `act-benchmark-platform-discovery-prompt`: Require conformance to `observe-platform-discovery-coverage`.
- `act-report-platform-discovery-prompt`: Require conformance to `reflect-platform-ecosystem`.
- `act-report-platform-comparison-prompt`: Require conformance to `reflect-platform-comparison-ecosystem`.
- `observe-platform-discovery-coverage`: Define the benchmark coverage output shape.
- `reflect-platform-ecosystem`: Define the synthesized platform ecosystem output shape.
- `reflect-platform-comparison-ecosystem`: Define the platform comparison CSV/HTML output shape.
- `repo-structure`: Add canonical initiative discovery observation pattern.

## Impact

- Affected specs: `plan-*`, `act-*`, `observe-*`, `reflect-*`, and `repo-structure`.
- Affected live files: `plan/initiative-definition.md`, `act/discover-platforms.md`, `act/discover-initiatives.md`, `act/compare-platforms.md`, benchmark/report prompts.
- No dependency or tooling changes.

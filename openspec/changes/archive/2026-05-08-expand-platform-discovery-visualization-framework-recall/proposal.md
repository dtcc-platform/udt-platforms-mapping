# Proposal: expand platform discovery recall for geospatial visualization frameworks

## Summary

Expand platform discovery recall so broad discovery includes adjacent geospatial visualization frameworks, 3D web viewing libraries, and browser-based 2D/3D geospatial frameworks that may not use explicit "urban digital twin platform" language.

Giro3D is the motivating example from GitHub issue #3. It presents itself as an open-source JavaScript framework and web viewing library for geospatial 2D, 2.5D, and 3D data. Under the existing `platform-definition`, it should be included and classified as `framework`.

## Motivation

The discovery prompt now includes adjacent module recall language, but it does not explicitly cover enabling visualization frameworks that are likely to matter in the UDT ecosystem.

This can under-represent technical frameworks that present themselves as:

- geospatial visualization frameworks
- 3D web viewing libraries
- 3D geospatial JavaScript frameworks
- browser-based geospatial visualization tools
- 3D Tiles or point-cloud viewers
- terrain and raster/vector visualization frameworks
- three.js or OpenLayers-based geospatial frameworks

The issue is recall, not classification. The current `framework` definition already covers reusable enabling frameworks and visualization layers.

## Scope

In scope:

- update `act-discover-platforms-prompt` to require adjacent geospatial visualization framework recall language
- add a Giro3D-style scenario showing such tools should be surfaced and classified via `platform-definition`
- reference GitHub issue #3 in the change rationale

Out of scope:

- changing `platform-definition`
- changing allowed `Type` values
- changing observe output shape
- editing observed model outputs

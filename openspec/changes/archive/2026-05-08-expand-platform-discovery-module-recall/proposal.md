# Proposal: expand platform discovery recall for urban analytics modules

## Summary

Expand platform discovery recall so broad discovery includes adjacent technical urban analytics, resilience, infrastructure-risk, simulation, and visualization modules that may not use explicit "urban digital twin platform" language.

GeoDatalytics is the motivating example from GitHub issue #2. It presents itself as an urban visualization and data analysis toolkit, so it can be missed by searches focused only on obvious UDT platform terms. Under the existing `platform-definition`, it should be included and classified as `module`.

## Motivation

The platform discovery prompt currently emphasizes broad recall, but it does not name the adjacent module-language search space. This can under-represent technical UDT ecosystem components that present themselves as:

- urban analytics toolkits
- geospatial risk analysis tools
- climate resilience visualization tools
- infrastructure risk modeling tools
- urban simulation or data analysis toolkits
- PostGIS-based urban analytics systems
- city model visualization toolkits

The issue is recall, not classification. The current `module` definition already covers bounded analytical functions, data pipelines, visualization components, simulators, and integration components.

## Scope

In scope:

- update `act-discover-platforms-prompt` to require adjacent technical module search language during broad discovery
- add a GeoDatalytics-style scenario showing such tools should be surfaced and classified via `platform-definition`
- reference GitHub issue #2 in the change rationale

Out of scope:

- changing `platform-definition`
- changing allowed `Type` values
- changing observe output shape
- editing observed model outputs

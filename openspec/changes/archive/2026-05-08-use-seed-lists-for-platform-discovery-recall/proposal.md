# Proposal: use seed lists for platform discovery recall

## Summary

Update platform discovery behavior so broad discovery uses adjacent ecosystem seed lists as recall aids for UDT-enabling frameworks and modules.

The motivating example is `joewdavies/awesome-frontend-gis`, tracked in GitHub issue #4. It is not a UDT platform list, but it contains many frontend GIS, geospatial visualization, LiDAR, web mapping, spatial data processing, and geospatial analytics projects that may classify as `framework`, `module`, or useful `excluded` boundary examples under `platform-definition`.

## Motivation

Recent recall gaps show that relevant UDT-enabling artifacts are easy to miss when discovery relies mostly on explicit UDT platform wording:

- GeoDatalytics-style urban analytics modules
- Giro3D-style geospatial visualization frameworks
- frontend GIS frameworks and point-cloud viewers from curated seed lists

The current prompt now includes some adjacent term families, but it does not explicitly require consulting curated ecosystem seed lists. Seed lists can improve breadth while still preserving the platform-definition boundary.

## Scope

In scope:

- update `act-discover-platforms-prompt` to require use of adjacent ecosystem seed lists as recall aids
- include seed-list domains such as frontend GIS, geospatial visualization, 3D Tiles, point-cloud, web mapping, spatial data processing, and spatial analytics
- require seed-list candidates to be classified through `platform-definition`
- add an `awesome-frontend-gis`-style scenario

Out of scope:

- changing `platform-definition`
- promoting all seed-list entries into platform discovery automatically
- changing observe output shape
- adding a new frontend GIS discovery workflow
- editing observed model outputs
